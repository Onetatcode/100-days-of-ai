# Day 01 — Environment Setup + First Tool-Calling Agent

## Goal
Get your OpenRouter connection working and build the smallest possible
agent: one that can call a single tool (a calculator) when it decides it
needs to, using raw API calls — no framework.

## Why this matters
Every agent framework (LangGraph, CrewAI, etc.) is built on this exact
loop: send messages + tool definitions → model responds with either text
or a tool call → you execute the tool → you feed the result back → repeat.
Understanding this by hand means frameworks won't feel like magic later.

## Tasks
1. Copy `.env.example` to `.env` in the repo root and add your OpenRouter
   API key (free tier: https://openrouter.ai/).
2. Run `agent.py` and confirm you get a response.
3. Ask it a question that requires math (e.g. "what is 4821 * 17?") and
   watch it call the `calculator` tool instead of guessing.
4. Read through `agent.py` line by line — make sure you understand:
   - how the tool is *described* to the model (the JSON schema)
   - how the model's tool-call response is parsed
   - how the tool result is sent back as a new message
5. **Extend it**: add a second tool of your own (e.g. `word_count`,
   `reverse_string`, or a simple `whois_lookup` stub). This is the real
   exercise — don't skip it.

## Notes
Write your own notes/observations here as you go:

- What surprised you about how tool calling works?
- Where did the model choose *not* to use a tool when you expected it to?

## Done when
- [ ] `.env` configured and agent runs
- [ ] Agent successfully calls the calculator tool
- [ ] You've added a second custom tool
- [ ] Notes above filled in
