#!/usr/bin/env python3
"""Guard against theme files that Zed loads without error but renders unstyled.

Zed's ThemeContent accepts only `name`, `appearance` and `style`; syntax styles
live at `style.syntax`. A `syntax` object placed anywhere else is silently
dropped by serde, leaving every buffer painted in `editor.foreground` while the
UI colors still look correct -- so this failure mode survives JSON validation.
"""

import glob
import json
import sys

ALLOWED_THEME_KEYS = {"name", "appearance", "style"}

errors = []

for path in sorted(glob.glob("themes/*.json")):
    with open(path) as f:
        doc = json.load(f)

    for theme in doc.get("themes", []):
        label = f"{path}: {theme.get('name', '<unnamed>')}"

        stray = set(theme) - ALLOWED_THEME_KEYS
        if stray:
            errors.append(f"{label}: keys ignored by Zed: {sorted(stray)}")

        syntax = theme.get("style", {}).get("syntax")
        if not syntax:
            errors.append(f"{label}: style.syntax is missing or empty")
            continue

        for token, style in syntax.items():
            if not style.get("color"):
                errors.append(f"{label}: syntax token '{token}' has no color")

for error in errors:
    print(f"error: {error}", file=sys.stderr)

sys.exit(1 if errors else 0)
