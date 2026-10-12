#!/usr/bin/env python3
"""Write manifest.json: the list of photos / songs in each media folder.

The page reads this file so it also works where folders can't be listed (e.g. GitHub Pages).
Run it again after adding or removing photos:  python3 make_manifest.py
"""
import json, os
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
MEDIA = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.mp3', '.m4a', '.wav', '.ogg', '.aac', '.flac')
FOLDERS = ['photos/life/1_baby/', 'photos/life/2_kid/', 'photos/life/3_student/', 'photos/life/4_now/',
           'photos/pile/', 'music/cds/']

manifest = {}
for folder in FOLDERS:
    path = os.path.join(HERE, folder)
    names = sorted(n for n in os.listdir(path) if n.lower().endswith(MEDIA)) if os.path.isdir(path) else []
    manifest[folder] = [quote(n) for n in names]          # URL-encoded, like a folder listing's links

with open(os.path.join(HERE, 'manifest.json'), 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
print('manifest.json:', {k: len(v) for k, v in manifest.items()})
