"""Pre-render the site to plain HTML for static hosting.

Every route here is read-only — no forms, no database, no sessions — so the
Flask app is only ever assembling the same pages from the same data. Running a
server to do that on every request buys nothing, and on a free tier it costs
the visitor a ~20 second wait while the service wakes up.

This renders each route once and writes the result to `dist/`, which can be
hosted as static files: no server, no cold start, no monthly instance hours.

Usage:  python freeze.py
Then:   wrangler pages deploy dist --project-name=tpa-honey-website
"""

import shutil
import sys
from pathlib import Path

from app import PRODUCTS, app

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"

# route -> file written. Directory-style paths get /index.html so the URL keeps
# working without a trailing-slash redirect.
PAGES = {
    "/": "index.html",
    "/products": "products/index.html",
    "/contact": "contact/index.html",
    "/about": "about/index.html",
    "/health-products": "health-products/index.html",
    "/skincare": "skincare/index.html",
    "/gallery": "gallery/index.html",
}

# One page per product category, built from the same data the app uses, so a
# new product appears here automatically rather than needing this list edited.
for category in PRODUCTS:
    PAGES[f"/products/{category}"] = f"products/{category}/index.html"


def main() -> int:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    failures = []
    with app.test_client() as client:
        for route, out in PAGES.items():
            response = client.get(route)
            if response.status_code != 200:
                failures.append(f"{route} -> HTTP {response.status_code}")
                continue
            target = DIST / out
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(response.data)
            print(f"  {route:34s} -> dist/{out}  ({len(response.data):,} bytes)")

    # The images and CSS ship as they are.
    shutil.copytree(ROOT / "static", DIST / "static")
    static_count = sum(1 for _ in (DIST / "static").rglob("*") if _.is_file())
    print(f"  copied {static_count} files from static/")

    if failures:
        print("\nFAILED:")
        for f in failures:
            print("  " + f)
        return 1

    total = sum(f.stat().st_size for f in DIST.rglob("*") if f.is_file())
    print(f"\n{len(PAGES)} pages + {static_count} assets, {total / 1_048_576:.1f} MB in dist/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
