#!/usr/bin/env python3
"""Dependency-free package validation; behavioural quality needs separate review."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/build-analytical-presentations'

def validate(root=ROOT, skill=SKILL):
    errors = []
    path = skill / 'SKILL.md'
    if not path.is_file():
        return ['Missing SKILL.md']
    text = path.read_text(encoding='utf-8')
    parts = text.split('---', 2)
    if len(parts) != 3 or parts[0].strip():
        errors.append('Frontmatter must be delimited at the start')
        front = {}
    else:
        front = dict(re.findall(r'^([a-z-]+):\s*(.+)$', parts[1], re.M))
    name = front.get('name', '')
    if name != skill.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name)>64:
        errors.append('Skill name must match its folder and the standard')
    description = front.get('description', '')
    if not 1 <= len(description) <= 1024:
        errors.append('Description length must be 1-1024 characters')
    if len(text.splitlines()) >= 500:
        errors.append('Core instructions must stay below 500 lines')
    for f in root.rglob('*'):
        if not f.is_file() or '.git' in f.relative_to(root).parts:
            continue
        if f.suffix in {'.md','.py','.json','.yaml','.yml'} or f.name in {'LICENSE','.gitignore'}:
            value = f.read_text(encoding='utf-8')
            if not value.isascii():
                errors.append(f'Non-ASCII text: {f.relative_to(root)}')
            if f.suffix == '.md':
                for target in re.findall(r'\]\(([^)]+)\)',value):
                    if re.match(r'[a-z]+://|#',target):
                        continue
                    target=target.split('#')[0]
                    if not (f.parent/target).is_file():
                        errors.append(f'Broken link in {f.relative_to(root)}: {target}')
    cases = json.loads((root/'tests/cases.json').read_text())
    ids = [case['id'] for case in cases]
    if len(ids) != len(set(ids)):
        errors.append('Duplicate evaluation case IDs')
    if not all(isinstance(c.get('should_trigger'),bool) and c.get('request') for c in cases):
        errors.append('Each case needs request and boolean should_trigger')
    if not (any(c['should_trigger'] for c in cases) and any(not c['should_trigger'] for c in cases)):
        errors.append('Evaluation set needs positive and negative cases')
    for f in (skill/'references').glob('*.md'):
        if f'references/{f.name}' not in text:
            errors.append(f'Undiscoverable reference: {f.name}')
    return errors

if __name__ == '__main__':
    errors = validate()
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        sys.exit(1)
    print('PASS: structure, metadata, links, ASCII, references and fixtures')
