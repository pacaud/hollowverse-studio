# Logs — Chat Center

Logs are **condensed memory** for the Chat Center.

They are not raw chat transcripts.
They are short summaries, checkpoints, and extracted decisions that prevent “where were we?”

## Boot rule (read this first)
When starting a new chat session:
1) Run Room Clear
2) Then read logs in this order:
   - newest in `session_summaries/`
   - newest in `checkpoints/`
   - newest in `exports/` (if anything changed)
3) Return to `CURRENT.md` and do `next_action`

## Folders
- `session_summaries/` — short “what happened” summaries (aim 5–20 lines)
- `checkpoints/` — “chapter breaks” (where we paused + what’s next)
- `decisions/` — only decisions that became canon files/bundles
- `exports/` — exported bundles + why

## Log style rules
- Prefer **small and scannable** over complete.
- If a log grows too big:
  - keep a short summary here
  - move details into the relevant bundle (core/world/chat_center) or a dedicated archive later

## Canon reminder
Conversation is draft.
If it matters, it must be written into files and bundled.

## Latest
- session summary: `session_summaries/2026-02-07__pointers_mirrors_repo_visibility.md`
- decision: `decisions/2026-02-07__decision__no_converter_use_source_txt_mirrors.md`

