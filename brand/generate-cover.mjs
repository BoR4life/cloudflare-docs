#!/usr/bin/env node
/**
 * Bundle of Rays — procedural cover generator.
 *
 * Influence: someform (Matthias Winckelmann, Helge Kiehl) — identity built from logic,
 * with tooling handed over so assets can be generated without a designer in the loop.
 * Rendered in this brand's own vocabulary (ink, paper, flat colour, riso offset) rather
 * than in someform's simulated-photographic surface, which would fight the Jullien mark.
 *
 * Deterministic: the same seed always yields the same artwork, so module BOR-114 has one
 * cover for its whole life and nobody has to store it as a decision.
 *
 * Usage:
 *   node brand/generate-cover.mjs BOR-114
 *   node brand/generate-cover.mjs BOR-114 --ratio social --out build/
 *   node brand/generate-cover.mjs --batch BOR-101 BOR-114 "Deteriorating Patient"
 */

// ---- palette, mirrored from tokens.json ----
export const INK = "#14110f";
export const PAPER = "#f6f1e7";
export const FLATS = [
	{ name: "ray", hex: "#e8a33c" },
	{ name: "pulse", hex: "#e24e38" },
	{ name: "breath", hex: "#3f8f5b" },
	{ name: "deep", hex: "#2b47c8" },
];

/**
 * Flats for a reversed (ink) ground. These are the dark-ground values from
 * tokens.css, not tints — Deep in particular is only 2.54:1 against Ink and
 * has to lift before it can sit on it.
 */
export const FLATS_REVERSED = [
	{ name: "ray", hex: "#e8a33c" },
	{ name: "pulse", hex: "#f0705c" },
	{ name: "breath", hex: "#5fb37c" },
	{ name: "deep", hex: "#8fa3f0" },
];

export const RATIOS = {
	cover: [1200, 1600],
	social: [1200, 630],
	square: [1200, 1200],
	scene: [1920, 1080],
};

// ---- deterministic PRNG (xmur3 hash -> mulberry32) ----
function hash(str) {
	let h = 1779033703 ^ str.length;
	for (let i = 0; i < str.length; i++) {
		h = Math.imul(h ^ str.charCodeAt(i), 3432918353);
		h = (h << 13) | (h >>> 19);
	}
	return () => {
		h = Math.imul(h ^ (h >>> 16), 2246822507);
		h = Math.imul(h ^ (h >>> 13), 3266489909);
		return (h ^= h >>> 16) >>> 0;
	};
}
function rng(seed) {
	let a = hash(String(seed))();
	return () => {
		a |= 0;
		a = (a + 0x6d2b79f5) | 0;
		let t = Math.imul(a ^ (a >>> 15), 1 | a);
		t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
		return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
	};
}

// ---- shape vocabulary, all derived from the mark ----

/** The arch: rounded top, flat base. The lung/face form from the mark. */
function arch(x, y, w, h, fill) {
	const r = w / 2;
	return `<path d="M${x} ${y + h} L${x} ${y + r} A${r} ${r} 0 0 1 ${x + w} ${y + r} L${x + w} ${y + h} Z" fill="${fill}"/>`;
}

/** A bundle of tapering rays from a point. The "rays" in the name. */
function rays(cx, cy, count, len, spread, rot, fill) {
	let out = "";
	for (let i = 0; i < count; i++) {
		const t = count === 1 ? 0.5 : i / (count - 1);
		const a = rot + (t - 0.5) * spread;
		const w = len * 0.055;
		const x2 = cx + Math.cos(a) * len;
		const y2 = cy + Math.sin(a) * len;
		const nx = -Math.sin(a) * w;
		const ny = Math.cos(a) * w;
		out += `<path d="M${cx} ${cy} L${(x2 + nx).toFixed(1)} ${(y2 + ny).toFixed(1)} L${(x2 - nx).toFixed(1)} ${(y2 - ny).toFixed(1)} Z" fill="${fill}"/>`;
	}
	return out;
}

/** The pair of eyes. Used sparingly — it is the most recognisable part of the mark. */
function eyes(cx, cy, r, gap, fill) {
	return (
		`<circle cx="${cx - gap / 2}" cy="${cy}" r="${r}" fill="${fill}"/>` +
		`<circle cx="${cx + gap / 2}" cy="${cy}" r="${r}" fill="${fill}"/>`
	);
}

/** A horizon band. */
function band(y, h, w, fill) {
	return `<rect x="0" y="${y}" width="${w}" height="${h}" fill="${fill}"/>`;
}

/**
 * A headset visor, placed where the mark's eyes sit — that substitution is the
 * whole idea: these are our people, and they are in headsets.
 *
 * Deliberately not a television. A CRT with antennae in military dress is a
 * specific existing character (Prince Robot IV, Saga); a visor band is the
 * generic form and reads as this business rather than someone else's comic.
 */
function visor(x, y, w, fill, glint) {
	const vy = y + w * 0.34; // tied to width, so it stays on the head however long the body runs
	const vh = w * 0.26;
	const vw = w * 0.8;
	const vx = x + (w - vw) / 2;
	const strapH = w * 0.075;
	// The strap has to stop at the silhouette. The arch's dome is a semicircle of
	// radius r, so solve its half-width at the strap's height instead of running
	// the full head width, which juts out into open paper and reads as a mistake.
	const r = w / 2;
	const d = vy + vh / 2 - y;
	const half = d < r ? Math.sqrt(Math.max(0, r * r - (r - d) * (r - d))) : r;
	const sx = x + r - half;
	const sw = half * 2;
	const g =
		glint === null
			? ""
			: `<path d="M${(vx + vw * 0.1).toFixed(1)} ${(vy + vh * 0.72).toFixed(1)} L${(vx + vw * 0.26).toFixed(1)} ${(vy + vh * 0.18).toFixed(1)} L${(vx + vw * 0.38).toFixed(1)} ${(vy + vh * 0.18).toFixed(1)} L${(vx + vw * 0.22).toFixed(1)} ${(vy + vh * 0.72).toFixed(1)} Z" fill="${glint}"/>`;
	return (
		`<rect x="${sx.toFixed(1)}" y="${(vy + vh / 2 - strapH / 2).toFixed(1)}" width="${sw.toFixed(1)}" height="${strapH.toFixed(1)}" fill="${fill}"/>` +
		`<rect x="${vx.toFixed(1)}" y="${vy.toFixed(1)}" width="${vw.toFixed(1)}" height="${vh.toFixed(1)}" rx="${(vh / 2).toFixed(1)}" fill="${fill}"/>` +
		g
	);
}

/** One figure: the mark's arch form, wearing either eyes or a headset. */
function figure(x, base, w, h, opts) {
	const { ink, ground, flat, headset, off } = opts;
	const y = base - h;
	const body = arch(x + off, y + off, w, h, flat) + arch(x, y, w, h, ink);
	const face = headset
		? visor(x, y, w, flat, ground)
		: eyes(x + w / 2, y + w * 0.4, w * 0.1, w * 0.36, ground);
	return body + face;
}

// ---- composed archetypes; the seed picks one ----
/**
 * Adding to or reordering this list reshuffles every existing seed, because the
 * archetype is the first draw. Lock it before covers go into production.
 */
const ARCHETYPES = [
	"arch-and-rays",
	"the-pair",
	"corner-rays",
	"horizon",
	"crew",
];

function compose(name, r, W, H, flat, ink, ground) {
	const pick = (lo, hi) => lo + r() * (hi - lo);
	const off = 2 * (W / 1200); // riso offset, scaled from the 2px spec
	// riso: the flat sits offset behind the ink shape, never the other way round
	const riso = (shapeFn) => shapeFn(off, off, flat) + shapeFn(0, 0, ink);

	switch (name) {
		case "arch-and-rays": {
			const w = pick(W * 0.42, W * 0.6);
			const h = pick(H * 0.34, H * 0.46);
			const x = (W - w) / 2 + pick(-W * 0.06, W * 0.06);
			const y = H - h;
			const cx = x + w / 2;
			const cy = y - pick(H * 0.02, H * 0.07);
			return (
				rays(
					cx,
					cy,
					Math.round(pick(5, 9)),
					pick(H * 0.3, H * 0.44),
					1.5,
					-Math.PI / 2,
					flat,
				) + riso((dx, dy, f) => arch(x + dx, y + dy, w, h, f))
			);
		}
		case "the-pair": {
			// Jullien's pairs are never rigidly symmetrical — one form leads.
			const w = pick(W * 0.2, W * 0.32);
			const w2 = w * pick(0.78, 1.14);
			const h = pick(H * 0.34, H * 0.56);
			const h2 = h * pick(0.72, 1.2);
			const gap = pick(W * 0.015, W * 0.09);
			const x = (W - (w + w2 + gap)) / 2 + pick(-W * 0.05, W * 0.05);
			const base = H - pick(0, H * 0.16);
			const x2 = x + w + gap;
			const withEyes = r() < 0.72;
			const headset = r() < 0.5;
			const behind = r() < 0.3;
			const er = Math.min(w, w2) * pick(0.085, 0.125);
			return (
				(behind
					? rays(
							W / 2,
							base - Math.max(h, h2) - H * 0.03,
							Math.round(pick(6, 10)),
							H * 0.3,
							1.7,
							-Math.PI / 2,
							flat,
						)
					: "") +
				riso((dx, dy, f) => arch(x + dx, base - h + dy, w, h, f)) +
				riso((dx, dy, f) => arch(x2 + dx, base - h2 + dy, w2, h2, f)) +
				(withEyes
					? eyes(
							x + w / 2,
							base - h + h * pick(0.2, 0.32),
							er,
							w * pick(0.3, 0.42),
							ground,
						) +
						eyes(
							x2 + w2 / 2,
							base - h2 + h2 * pick(0.2, 0.32),
							er,
							w2 * pick(0.3, 0.42),
							ground,
						)
					: "")
			);
		}
		case "corner-rays": {
			const corner = Math.floor(r() * 4);
			const pts = [
				[0, 0, 0.25],
				[W, 0, 0.75],
				[W, H, 1.25],
				[0, H, 1.75],
			][corner];
			const w = pick(W * 0.3, W * 0.44);
			const h = pick(H * 0.2, H * 0.3);
			return (
				rays(
					pts[0],
					pts[1],
					Math.round(pick(7, 12)),
					pick(W * 0.7, W * 1.05),
					1.1,
					pts[2] * Math.PI,
					flat,
				) + riso((dx, dy, f) => arch((W - w) / 2 + dx, H - h + dy, w, h, f))
			);
		}
		case "crew": {
			const n = Math.round(pick(3, 5));
			const base = H - pick(H * 0.04, H * 0.16);
			const unit = W / (n + 1.1);
			const w = unit * pick(0.62, 0.84);
			const gap = (W - w * n) / (n + 1);
			let out = "";
			// one figure keeps the eyes, so the mark's own face stays in the family
			const eyed = Math.floor(r() * n);
			for (let i = 0; i < n; i++) {
				const h = w * pick(1.5, 2.7);
				const x = gap + i * (w + gap);
				out += figure(x, base, w, h, {
					ink,
					ground,
					flat,
					headset: i !== eyed,
					off,
				});
			}
			if (r() < 0.4) {
				out =
					rays(
						W / 2,
						base - w * 2.9,
						Math.round(pick(6, 10)),
						H * 0.26,
						1.8,
						-Math.PI / 2,
						flat,
					) + out;
			}
			return out;
		}
		case "horizon":
		default: {
			const by = pick(H * 0.42, H * 0.72);
			const w = pick(W * 0.26, W * 0.52);
			const h = pick(H * 0.3, H * 0.5);
			const x = pick(W * 0.04, W * 0.96 - w);
			const withEyes = r() < 0.45;
			const er = w * 0.1;
			return (
				band(by, H - by, W, flat) +
				riso((dx, dy, f) => arch(x + dx, by - h + dy, w, h, f)) +
				(withEyes
					? eyes(x + w / 2, by - h + h * 0.26, er, w * 0.34, ground)
					: "")
			);
		}
	}
}

/**
 * Build one cover as an SVG string.
 * @param {string} seed        any stable string — a module code works well
 * @param {object} [opts]
 * @param {keyof RATIOS} [opts.ratio="cover"]
 * @param {number} [opts.grain=0.045]  paper grain opacity, per the texture spec
 */
export function coverSVG(seed, opts = {}) {
	const { ratio = "cover", grain = 0.045 } = opts;
	const [W, H] = RATIOS[ratio] || RATIOS.cover;
	const r = rng(seed);
	// consume in a fixed order so archetype, ground and flat stay stable per seed
	const archetype = ARCHETYPES[Math.floor(r() * ARCHETYPES.length)];
	const reversed = r() < 0.28;
	const flatIdx = Math.floor(r() * FLATS.length);
	const flat = reversed ? FLATS_REVERSED[flatIdx] : FLATS[flatIdx];
	const ground = reversed ? INK : PAPER;
	const ink = reversed ? PAPER : INK;
	const body = compose(archetype, r, W, H, flat.hex, ink, ground);
	const gid = "g" + Math.abs(hash(String(seed))() % 100000);

	return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="Bundle of Rays cover for ${escapeXml(String(seed))}">
	<title>${escapeXml(String(seed))} — ${archetype} / ${flat.name}${reversed ? " / reversed" : ""}</title>
	<defs>
		<filter id="${gid}" x="0" y="0" width="100%" height="100%">
			<feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="4" stitchTiles="stitch"/>
		</filter>
	</defs>
	<rect width="${W}" height="${H}" fill="${ground}"/>
	${body}
	<rect width="${W}" height="${H}" filter="url(#${gid})" opacity="${grain}"/>
</svg>`;
}

function escapeXml(s) {
	return s.replace(
		/[<>&"']/g,
		(c) =>
			({
				"<": "&lt;",
				">": "&gt;",
				"&": "&amp;",
				'"': "&quot;",
				"'": "&apos;",
			})[c],
	);
}

/** Which archetype and flat a seed resolves to, without rendering. */
export function describe(seed) {
	const r = rng(seed);
	const archetype = ARCHETYPES[Math.floor(r() * ARCHETYPES.length)];
	const reversed = r() < 0.28;
	const flat = FLATS[Math.floor(r() * FLATS.length)].name;
	return { archetype, flat, reversed };
}

// ---- CLI ----
const isMain =
	process.argv[1] && import.meta.url.endsWith(process.argv[1].split("/").pop());
if (isMain) {
	const { writeFileSync, mkdirSync } = await import("node:fs");
	const argv = process.argv.slice(2);
	let ratio = "cover";
	let out = ".";
	const seeds = [];
	for (let i = 0; i < argv.length; i++) {
		if (argv[i] === "--ratio") ratio = argv[++i];
		else if (argv[i] === "--out") out = argv[++i];
		else if (argv[i] === "--batch") continue;
		else seeds.push(argv[i]);
	}
	if (!seeds.length) {
		console.error(
			"usage: node brand/generate-cover.mjs <seed...> [--ratio cover|social|square|scene] [--out dir]",
		);
		process.exit(1);
	}
	if (!RATIOS[ratio]) {
		console.error(
			`unknown ratio "${ratio}" — pick one of: ${Object.keys(RATIOS).join(", ")}`,
		);
		process.exit(1);
	}
	mkdirSync(out, { recursive: true });
	for (const seed of seeds) {
		const file = `${out}/${String(seed)
			.replace(/[^a-z0-9]+/gi, "-")
			.toLowerCase()}-${ratio}.svg`;
		writeFileSync(file, coverSVG(seed, { ratio }));
		const d = describe(seed);
		console.log(`${file}  ${d.archetype} / ${d.flat}`);
	}
}
