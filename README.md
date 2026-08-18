# 100 Days of Agentic AI — Red Team Edition

A 100-day daily practice log building agentic AI skills, progressing from
fundamentals to a full autonomous recon/pentest assistant. Built with free
tools only: OpenRouter free tier (Llama 3.3 70B), Ollama for local models,
LangGraph, SQLite, and HTB/Vulnhub as live targets.

## Phases

| Phase | Days | Focus |
|---|---|---|
| 1 | 1–25 | Agentic AI fundamentals — tool calling, ReAct, memory, LangGraph basics |
| 2 | 26–50 | Multi-agent patterns, RAG, tool design |
| 3 | 51–75 | Agentic recon/enumeration tooling against real targets |
| 4 | 76–100 | Full agentic pentest assistant + live dashboard |

## Stack

- **LLM**: OpenRouter (free tier, Llama 3.3 70B) + Ollama (local fallback)
- **Framework**: raw API calls (days 1–20) → LangGraph (days 21+)
- **Memory**: SQLite
- **Targets**: HTB retired/active boxes, Vulnhub, local Docker vuln apps (DVWA, Juice Shop, WebGoat)
- **Dashboard (Phase 4)**: Flask + SocketIO

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r shared/requirements.txt
cp .env.example .env   # add your OPENROUTER_API_KEY
```

## Progress Tracker

| Day | Topic | Status |
|---|---|---|
| 01 | Environment setup + first raw tool-calling agent | ⬜ |
| 02 | ReAct loop from scratch | ⬜ |
| 03 | Structured output / JSON mode | ⬜ |
| 04 | Prompt engineering for tool use | ⬜ |
| 05 | Short-term memory (context window mgmt) | ⬜ |
| 06 | Long-term memory with SQLite | ⬜ |
| 07 | Building a safe shell-exec tool | ⬜ |
| 08 | Building a file-read/write tool | ⬜ |
| 09 | Error handling & retries in agent loops | ⬜ |
| 10 | Mini project: file-organizing agent | ⬜ |
| 11 | Intro to LangGraph: nodes & edges | ⬜ |
| 12 | LangGraph conditional routing | ⬜ |
| 13 | LangGraph state management | ⬜ |
| 14 | LangGraph + tool calling | ⬜ |
| 15 | Streaming agent output | ⬜ |
| 16 | Rate limiting & cost tracking | ⬜ |
| 17 | Local models with Ollama | ⬜ |
| 18 | Comparing model outputs (OpenRouter vs Ollama) | ⬜ |
| 19 | Logging & observability for agents | ⬜ |
| 20 | Mini project: CLI research agent | ⬜ |
| 21 | Planner/executor pattern | ⬜ |
| 22 | Critic/reviewer agent pattern | ⬜ |
| 23 | Multi-agent handoffs | ⬜ |
| 24 | Shared state across agents | ⬜ |
| 25 | Phase 1 review + writeup | ⬜ |
| 26 | RAG basics: chunking & embeddings | ⬜ |
| 27 | Local vector store (Chroma/FAISS) | ⬜ |
| 28 | Indexing your own HTB notes | ⬜ |
| 29 | RAG-augmented agent queries | ⬜ |
| 30 | Tool design principles for agents | ⬜ |
| 31 | Wrapping a CLI tool as an agent tool | ⬜ |
| 32 | Structured tool outputs & parsing | ⬜ |
| 33 | Tool result validation | ⬜ |
| 34 | Scope-checking guardrails | ⬜ |
| 35 | Human-in-the-loop approval gates | ⬜ |
| 36 | Agent action logging to SQLite | ⬜ |
| 37 | Building a report-generator tool | ⬜ |
| 38 | Multi-agent: planner + recon executor | ⬜ |
| 39 | Multi-agent: adding a critic | ⬜ |
| 40 | Mini project: note-taking research agent | ⬜ |
| 41 | Agent cost/token budget management | ⬜ |
| 42 | Prompt caching strategies | ⬜ |
| 43 | Few-shot examples for tool use | ⬜ |
| 44 | Testing agents (eval basics) | ⬜ |
| 45 | Building an eval harness | ⬜ |
| 46 | Failure mode analysis | ⬜ |
| 47 | Agent self-correction loops | ⬜ |
| 48 | Combining RAG + tools | ⬜ |
| 49 | Mini project: doc-QA agent over HTB writeups | ⬜ |
| 50 | Phase 2 review + writeup | ⬜ |
| 51 | Wrapping nmap as an agent tool | ⬜ |
| 52 | Parsing nmap output for agent consumption | ⬜ |
| 53 | Wrapping gobuster/ffuf | ⬜ |
| 54 | Wrapping subfinder/amass | ⬜ |
| 55 | Wrapping whatweb/wappalyzer | ⬜ |
| 56 | Agent decides next enum step from prior output | ⬜ |
| 57 | Building a recon state machine | ⬜ |
| 58 | Rate limiting active scans | ⬜ |
| 59 | Scope enforcement (target allowlists) | ⬜ |
| 60 | Mini project: passive recon agent | ⬜ |
| 61 | Mini project: active recon agent (HTB box) | ⬜ |
| 62 | Logging recon decisions to SQLite | ⬜ |
| 63 | Building a findings summarizer | ⬜ |
| 64 | Vuln-pattern matching from enum data | ⬜ |
| 65 | CVE lookup tool integration | ⬜ |
| 66 | Agent-assisted service fingerprinting | ⬜ |
| 67 | Web app recon agent (dirs, params, tech stack) | ⬜ |
| 68 | Agent-driven wordlist selection | ⬜ |
| 69 | Combining multiple recon tools in one flow | ⬜ |
| 70 | Full autonomous recon run on HTB box #1 | ⬜ |
| 71 | Full autonomous recon run on HTB box #2 | ⬜ |
| 72 | Reviewing & tuning false positives | ⬜ |
| 73 | Adding human checkpoints before exploitation | ⬜ |
| 74 | Recon agent writeup/report output | ⬜ |
| 75 | Phase 3 review + writeup | ⬜ |
| 76 | Exploit-suggestion agent (advisory only) | ⬜ |
| 77 | Chaining recon → suggestion pipeline | ⬜ |
| 78 | Critic agent reviews exploit suggestions | ⬜ |
| 79 | Report-drafting agent | ⬜ |
| 80 | CVSS scoring assistant | ⬜ |
| 81 | Remediation-guidance generator | ⬜ |
| 82 | Flask backend skeleton | ⬜ |
| 83 | SocketIO live event streaming | ⬜ |
| 84 | Dashboard: live agent reasoning view | ⬜ |
| 85 | Dashboard: findings panel | ⬜ |
| 86 | Dashboard: approval-gate UI | ⬜ |
| 87 | End-to-end run: recon → report on HTB box | ⬜ |
| 88 | End-to-end run: second target | ⬜ |
| 89 | Hardening guardrails & scope checks | ⬜ |
| 90 | Error handling polish | ⬜ |
| 91 | Performance/cost optimization pass | ⬜ |
| 92 | Documentation pass | ⬜ |
| 93 | Demo video/script prep | ⬜ |
| 94 | Final bug fixes | ⬜ |
| 95 | Code cleanup & refactor | ⬜ |
| 96 | Writing the project README/writeup | ⬜ |
| 97 | Publishing writeup (blog/HTB forum style) | ⬜ |
| 98 | Final full demo run | ⬜ |
| 99 | Retrospective: what worked, what didn't | ⬜ |
| 100 | Ship it — public release | ⬜ |

Status legend: ⬜ not started · 🟨 in progress · ✅ done

## Structure

```
100-days-agentic-ai/
  day-01/ ... day-100/    each day: README.md (notes) + code
  shared/                 reusable agent/tool modules + requirements.txt
  targets/                local docker-compose for vuln apps
  docs/                   writeups, longer notes
```
