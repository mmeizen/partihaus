#!/usr/bin/env python3
"""
migrate_products.py
-------------------
Rewrites content/products/*/index.md files to use clean front matter
compatible with layouts/products/single.html

- For pantone-mug: fully populated from existing content
- For all others: pre-filled with known data (name, material, image)
  and stubbed fields for you to fill in

Run from your site root:
    python3 migrate_products.py

A backup of each original file is saved as index.md.bak before overwriting.
"""

import os
import shutil

PRODUCTS_DIR = "content/products"

# ---------------------------------------------------------------------------
# Product data
# All known products. Fill in story/why/designer/origin/made_for as you go.
# ---------------------------------------------------------------------------
PRODUCTS = [
    {
        "folder": "pantone-mug",
        "title": "Pantone Mug",
        "material": "color-matched ceramic",
        "image": "/images/products/pantone-mug.jpg",
        "story": [
            "The **Pantone** mug is a piece of graphic design history made functional. Each mug is glazed in an exact Pantone color match and labeled with the corresponding chip number — the same system that designers, printers, and manufacturers worldwide use as their shared language of color.",
            "It's a rare object that works as a gift regardless of whether the recipient is a designer or not. For designers, it's a knowing reference. For everyone else, it's simply a beautifully colored ceramic mug with an interesting number on it. The box alone earns it a place under a tree.",
        ],
        "why": "selected because it's the most giftable object in the collection — instantly understood, immediately personal, endlessly collectible.",
        "designer": "Pantone LLC",
        "materials": "glazed ceramic",
        "origin": "Various",
        "made_for": "daily use, gifting, collecting",
        "affiliate_url": "AFFILIATE_URL",
        "affiliate_text": "find it here →",
    },
    {
        "folder": "kontra fruit bowl",
        "title": "Kontra Fruit Bowl",
        "material": "wood and stainless steel",
        "image": "/images/products/kontra-bowl.jpg",
        "story": [
            "ADD STORY PARAGRAPH 1 HERE.",
            "ADD STORY PARAGRAPH 2 HERE.",
        ],
        "why": "ADD WHY SELECTED QUOTE HERE.",
        "designer": "ADD DESIGNER",
        "materials": "wood and stainless steel",
        "origin": "ADD ORIGIN",
        "made_for": "ADD MADE FOR",
        "affiliate_url": "AFFILIATE_URL",
        "affiliate_text": "find it here →",
    },
    {
        "folder": "kaiser-idell-lamp",
        "title": "Kaiser Idell Table Lamp",
        "material": "bauhaus steel, high-gloss finish",
        "image": "/images/products/kaiser-lamp.jpg",
        "story": [
            "ADD STORY PARAGRAPH 1 HERE.",
            "ADD STORY PARAGRAPH 2 HERE.",
        ],
        "why": "ADD WHY SELECTED QUOTE HERE.",
        "designer": "Christian Dell",
        "materials": "bauhaus steel, high-gloss finish",
        "origin": "ADD ORIGIN",
        "made_for": "ADD MADE FOR",
        "affiliate_url": "AFFILIATE_URL",
        "affiliate_text": "find it here →",
    },
    {
        "folder": "kubus-candleholder",
        "title": "Kubus Candleholder",
        "material": "architectural steel design",
        "image": "/images/products/kubus-candleholder.jpg",
        "story": [
            "ADD STORY PARAGRAPH 1 HERE.",
            "ADD STORY PARAGRAPH 2 HERE.",
        ],
        "why": "ADD WHY SELECTED QUOTE HERE.",
        "designer": "ADD DESIGNER",
        "materials": "steel",
        "origin": "ADD ORIGIN",
        "made_for": "ADD MADE FOR",
        "affiliate_url": "AFFILIATE_URL",
        "affiliate_text": "find it here →",
    },
    {
        "folder": "emma-french-press",
        "title": "Emma French Press",
        "material": "steel with beechwood handle",
        "image": "/images/products/emma-french-press.jpg",
        "story": [
            "ADD STORY PARAGRAPH 1 HERE.",
            "ADD STORY PARAGRAPH 2 HERE.",
        ],
        "why": "ADD WHY SELECTED QUOTE HERE.",
        "designer": "Stelton",
        "materials": "steel, beechwood",
        "origin": "ADD ORIGIN",
        "made_for": "ADD MADE FOR",
        "affiliate_url": "AFFILIATE_URL",
        "affiliate_text": "find it here →",
    },
    {
        "folder": "barbry-salt-pepper-mills",
        "title": "Barbry Salt & Pepper Mills",
        "material": "polished stainless steel",
        "image": "/images/products/barbry-salt-pepper.jpg",
        "story": [
            "ADD STORY PARAGRAPH 1 HERE.",
            "ADD STORY PARAGRAPH 2 HERE.",
        ],
        "why": "ADD WHY SELECTED QUOTE HERE.",
        "designer": "ADD DESIGNER",
        "materials": "polished stainless steel",
        "origin": "ADD ORIGIN",
        "made_for": "ADD MADE FOR",
        "affiliate_url": "AFFILIATE_URL",
        "affiliate_text": "find it here →",
    },
    {
        "folder": "blomus-alpha-carafe",
        "title": "Blomus Alpha Decanting Carafe",
        "material": "minimal curved glass",
        "image": "/images/products/blomus-decantor.jpg",
        "story": [
            "ADD STORY PARAGRAPH 1 HERE.",
            "ADD STORY PARAGRAPH 2 HERE.",
        ],
        "why": "ADD WHY SELECTED QUOTE HERE.",
        "designer": "blomus",
        "materials": "glass",
        "origin": "ADD ORIGIN",
        "made_for": "ADD MADE FOR",
        "affiliate_url": "AFFILIATE_URL",
        "affiliate_text": "find it here →",
    },
    {
        "folder": "iittala-kartio-tumbler",
        "title": "iittala Kartio Tumbler",
        "material": "clear medium glass (set of 8)",
        "image": "/images/products/iittala-Kartio-Tumbler.jpg",
        "story": [
            "ADD STORY PARAGRAPH 1 HERE.",
            "ADD STORY PARAGRAPH 2 HERE.",
        ],
        "why": "ADD WHY SELECTED QUOTE HERE.",
        "designer": "Kaj Franck",
        "materials": "glass",
        "origin": "Finland",
        "made_for": "ADD MADE FOR",
        "affiliate_url": "AFFILIATE_URL",
        "affiliate_text": "find it here →",
    },
    {
        "folder": "turning-tray",
        "title": "Turning Tray",
        "material": "dual-tone laminated wood",
        "image": "/images/products/turning-tray.jpg",
        "story": [
            "ADD STORY PARAGRAPH 1 HERE.",
            "ADD STORY PARAGRAPH 2 HERE.",
        ],
        "why": "ADD WHY SELECTED QUOTE HERE.",
        "designer": "Finn Juhl",
        "materials": "laminated wood",
        "origin": "Denmark",
        "made_for": "ADD MADE FOR",
        "affiliate_url": "AFFILIATE_URL",
        "affiliate_text": "find it here →",
    },
]


def build_frontmatter(p):
    """Build a clean YAML front matter + empty body for a product."""

    def esc(s):
        """Escape double quotes in a string for YAML."""
        return s.replace('"', '\\"')

    lines = ["---"]
    lines.append(f'title: "{esc(p["title"])}"')
    lines.append(f'material: "{esc(p["material"])}"')
    lines.append(f'image: "{p["image"]}"')
    lines.append("story:")
    for para in p["story"]:
        # Use block scalar for paragraphs to handle special chars safely
        lines.append(f'  - "{esc(para)}"')
    lines.append(f'why: "{esc(p["why"])}"')
    lines.append(f'designer: "{esc(p["designer"])}"')
    lines.append(f'materials: "{esc(p["materials"])}"')
    lines.append(f'origin: "{esc(p["origin"])}"')
    lines.append(f'made_for: "{esc(p["made_for"])}"')
    lines.append(f'affiliate_url: "{p["affiliate_url"]}"')
    lines.append(f'affiliate_text: "{esc(p["affiliate_text"])}"')
    lines.append("---")
    lines.append("")  # empty body — layout handles everything
    return "\n".join(lines)


def migrate():
    skipped = []
    migrated = []

    for p in PRODUCTS:
        folder = os.path.join(PRODUCTS_DIR, p["folder"])
        index_path = os.path.join(folder, "index.md")

        if not os.path.isdir(folder):
            print(f"  [SKIP] Folder not found: {folder}")
            skipped.append(p["folder"])
            continue

        # Backup original
        backup_path = index_path + ".bak"
        if os.path.exists(index_path):
            shutil.copy2(index_path, backup_path)
            print(f"  [BAK]  {index_path} → {backup_path}")

        # Write new clean front matter
        new_content = build_frontmatter(p)
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"  [OK]   {index_path}")
        migrated.append(p["folder"])

    print()
    print(f"Done. {len(migrated)} migrated, {len(skipped)} skipped.")
    if skipped:
        print(f"Skipped (folder not found): {skipped}")


if __name__ == "__main__":
    migrate()
