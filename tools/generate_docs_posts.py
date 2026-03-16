from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path


@dataclass(frozen=True)
class PostSpec:
    source_md: Path
    rel_source_md: str
    date: date
    slug: str
    title: str
    subtitle: str


def _slugify(value: str) -> str:
    value = value.strip().lower()
    value = value.replace("\\", "/")
    value = re.sub(r"[^a-z0-9/._-]+", "-", value)
    value = value.replace("/", "-")
    value = value.replace(".", "-")
    value = re.sub(r"-+", "-", value)
    value = value.strip("-")
    if not value:
        return "doc"
    return value[:180]


def _extract_title(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            title = line.lstrip("#").strip()
            if title:
                return title
        break
    return fallback


def _extract_excerpt(md_text: str, max_lines: int = 18) -> str:
    lines: list[str] = []
    in_code = False
    for raw in md_text.splitlines():
        line = raw.rstrip()
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if line.strip().startswith("#"):
            continue
        if not line.strip():
            if lines:
                break
            continue
        lines.append(line)
        if len(lines) >= max_lines:
            break
    if not lines:
        return "Documento de referencia dentro de `core/docs`."
    return "\n".join(lines)


def _build_post(spec: PostSpec, md_text: str) -> str:
    excerpt = _extract_excerpt(md_text)
    cover = "/assets/img/open_code.png"
    thumb = "/assets/img/kaos-daavid-2.png"

    lines: list[str] = []
    lines.append("---")
    lines.append("layout: post")
    lines.append(f'title: "{spec.title.replace("\"", "\\\"")}"')
    lines.append(f'subtitle: "{spec.subtitle.replace("\"", "\\\"")}"')
    lines.append(f"cover-img: {cover}")
    lines.append(f"thumbnail-img: {thumb}")
    lines.append(f"share-img: {cover}")
    lines.append(
        f"tags: [post, ka0s, docs, source, {spec.slug.split('-')[0]}]"
    )
    lines.append("author: Ka0s")
    lines.append("---")
    lines.append("")
    lines.append(excerpt)
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"Fuente: `{spec.rel_source_md}`")
    lines.append("")
    return "\n".join(lines) + "\n"


def _iter_docs(docs_root: Path) -> list[Path]:
    files = [p for p in docs_root.rglob("*.md") if p.is_file()]
    files.sort(key=lambda p: p.as_posix().lower())
    return files


def _build_specs(
    docs_root: Path,
    posts_root: Path,
    start_date: date,
    start_index: int,
) -> list[PostSpec]:
    docs = _iter_docs(docs_root)
    specs: list[PostSpec] = []
    for idx, src in enumerate(docs, start=start_index):
        rel = src.relative_to(docs_root).as_posix()
        d = start_date + timedelta(days=(idx - start_index))
        slug = _slugify(rel)
        fallback_title = f"{docs_root.name}/{rel}"
        md_text = src.read_text(encoding="utf-8", errors="ignore")
        title = _extract_title(md_text, fallback=fallback_title)
        subtitle = f"Documento: core/docs/{rel}"
        specs.append(
            PostSpec(
                source_md=src,
                rel_source_md=f"core/docs/{rel}",
                date=d,
                slug=slug,
                title=title,
                subtitle=subtitle,
            )
        )
    return specs


def generate(
    docs_root: Path,
    posts_root: Path,
    start_date: date,
    start_index: int = 0,
    dry_run: bool = False,
) -> dict[str, int]:
    docs_root = docs_root.resolve()
    posts_root = posts_root.resolve()
    posts_root.mkdir(parents=True, exist_ok=True)

    created = 0
    skipped = 0

    specs = _build_specs(
        docs_root=docs_root,
        posts_root=posts_root,
        start_date=start_date,
        start_index=start_index,
    )
    for spec in specs:
        filename = f"{spec.date.isoformat()}-doc-{spec.slug}.md"
        dest = posts_root / filename
        if dest.exists():
            skipped += 1
            continue
        md_text = spec.source_md.read_text(encoding="utf-8", errors="ignore")
        content = _build_post(spec, md_text)
        if not dry_run:
            dest.write_text(content, encoding="utf-8")
        created += 1

    return {"created": created, "skipped": skipped, "total_docs": len(specs)}


def _find_repo_roots() -> tuple[Path, Path]:
    here = Path(__file__).resolve()
    ka0s_github_io = here.parents[1]
    ka0s = (ka0s_github_io / ".." / "ka0s").resolve()
    return ka0s, ka0s_github_io


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--docs",
        default=None,
        help="Ruta al directorio core/docs del repo ka0s",
    )
    parser.add_argument(
        "--posts",
        default=None,
        help="Ruta al directorio _posts del repo ka0s.github.io",
    )
    parser.add_argument("--start-date", default="2026-06-01")
    parser.add_argument("--start-index", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    ka0s_root, ka0s_github_io_root = _find_repo_roots()

    docs_root = Path(args.docs) if args.docs else (ka0s_root / "core" / "docs")
    posts_root = Path(args.posts) if args.posts else (ka0s_github_io_root / "_posts")

    y, m, d = (int(x) for x in args.start_date.split("-"))
    result = generate(
        docs_root=docs_root,
        posts_root=posts_root,
        start_date=date(y, m, d),
        start_index=args.start_index,
        dry_run=args.dry_run,
    )

    print(result)


if __name__ == "__main__":
    main()

