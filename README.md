# Presentation skills

A portable skill for planning, writing, assembling, and reviewing analytical presentations. It covers argument, explanatory writing, layout selection, evidence, and adaptation to the audience and delivery setting.

## Package

The skill lives at [skills/build-analytical-presentations/SKILL.md](skills/build-analytical-presentations/SKILL.md). Its seven supporting references provide detailed guidance and fictional worked examples. The core has no required connector, API key, model version, font, or slide-authoring library.

Use your current organisation's approved template and authorised evidence. Keep confidential task material in its appropriate workspace.

## Install once, use from both hosts

Clone this repository after publication and choose the revision you reviewed. For repeatable use, check out a full commit hash rather than following an unreviewed branch update.

Both hosts can read the same canonical skill folder through separate directory symlinks. Check your installed client's documented discovery location first. Current Codex documentation uses `~/.agents/skills`; older installations may use `~/.codex/skills`. Claude Code uses `~/.claude/skills`. Avoid installing the same named skill in multiple discovery locations for one host.

From the repository root, the following commands create links only if those link names do not already exist:

```sh
skill_path="$PWD/skills/build-analytical-presentations"
mkdir -p "$HOME/.claude/skills" "$HOME/.agents/skills"
ln -s "$skill_path" "$HOME/.claude/skills/build-analytical-presentations"
ln -s "$skill_path" "$HOME/.agents/skills/build-analytical-presentations"
```

If your installed Codex uses the legacy directory, use that directory instead of adding another copy. Do not overwrite an existing skill. Inspect and reconcile it deliberately. These commands do not install a renderer or grant permission to publish task material.

Project-only installation is also possible: link the skill under `.agents/skills` for Codex and `.claude/skills` for Claude Code within the intended project. Confirm the host discovers the package before relying on it.

## Invoke

Codex:

```text
Use $build-analytical-presentations to build a six-slide decision briefing from this evidence. The audience knows the background. Follow the attached company template, keep the proposal distinct from measured results, and deliver an editable presentation.
```

Claude Code:

```text
/build-analytical-presentations
Turn this material into a technical review for independent reading. Explain the mechanism, show results against the supplied acceptance criteria, and close with the next decision.
```

The description also supports automatic selection for substantial presentation work. Pure spelling fixes, conversions, and cosmetic edits should use their narrower workflows.

Other environments can read the complete `SKILL.md` and its relevant references as task instructions. Reading one file does not implement a host's automatic skill discovery, permissions, or rendering capability. Ordinary chat products may require a supported skill upload or plugin mechanism; a GitHub URL alone does not install a skill. Behaviour should be checked in each intended host.

## Validate

```sh
python3 scripts/validate_package.py
```

This checks the package structure, frontmatter, reference links, plain ASCII text, and fixture integrity. It does not prove narrative quality or cross-host behaviour. Use the [evaluation cases](tests/cases.json) and [evaluation guidance](tests/README.md) for behavioural checks.

## Design and compatibility

The package follows the [Agent Skills specification](https://agentskills.io/specification). The core contains the workflow and loads detailed references selectively. Product-specific UI metadata stays in `agents/openai.yaml`.

Authoring and installation guidance was checked against [OpenAI skills documentation](https://developers.openai.com/codex/skills/), [Claude Code skills documentation](https://code.claude.com/docs/en/skills), and [Anthropic skill-authoring guidance](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) on 20 October 2026. Discovery paths and host features can change. Check the installed version before changing configuration.

## Licence

MIT. See [LICENSE](LICENSE). Fictional examples illustrate the method and do not substantiate real-world claims.
