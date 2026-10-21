---
layout: post
title: "Выпуск 2026-06-14 (RU)"
date: 2026-06-14 09:00:00 +0000
lang: ru
---

# Выпуск 2026-06-14


## [r/LocalLLaMA] Can we stop dunking on DiffusionGemma and hack it instead?

_Reddit r/LocalLLaMA · 2026-06-14 · score 0.825_

Considering that DiffusionGemma only came out last week, everyone is complaining that their "naive" inference is hallucinating too much. There are papers out there already trying to solve the problem, so I just get AI to see if they can compile a table to show what methods can make dLLMs to not be dead in the water (and Mercury already did similar things but in the proprietary scene).


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1u5duqe/can_we_stop_dunking_on_diffusiongemma_and_hack_it/)

<!-- url_hash:64e348b3bac3363995d9858adef659f00e53e89dc0b16e04a47583e7c2a2896c -->


## [r/LocalLLaMA] Looking for blunt feedback on a local LLM benchmark tool

_Reddit r/LocalLLaMA · 2026-06-14 · score 0.8_

I’m working on a small open-source benchmark tool for local MLX inference engines on Apple Silicon, and I’m looking for blunt feedback on the methodology and usefulness of it. The goal is not to say “model X is better than model Y” or “engine X wins, period”.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1u5gekl/looking_for_blunt_feedback_on_a_local_llm/)

<!-- url_hash:c2c05a023f05f18de83eb257e9aeb9b161ae180bcfa072f28e2e55577f205892 -->


## [r/LocalLLaMA] Build for local LLM with 2 separate GPUs

_Reddit r/LocalLLaMA · 2026-06-14 · score 0.8_

I want to build a headless compute machine to run a RTX Ada 4000 (20GB) with a RTX Pro 5000 (48GB) **or** RTX PRO 4500 (32GB) in parallel for inference. The goal is not running one large model using 2x GPUs, but rather running separate models on each GPU.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1u5fhqj/build_for_local_llm_with_2_separate_gpus/)

<!-- url_hash:5e892c5173623326626415f9be5f4092df5fc66ce4a22c430ee0e7ea8abc0f16 -->


## [r/LocalLLaMA] Tuning a local multi-agent developer environment: Custom PM2 orchestration, Libuv/V8 heap overrides, and GPU telemetry

_Reddit r/LocalLLaMA · 2026-06-14 · score 0.8_

Hey everyone, I wanted to share my local developer environment configurations and discuss some performance bottlenecks I hit while running local multi-agent LLM pipelines, vector databases, and background RAG indexers simultaneously on my workstation (Alienware, 16 Cores/24 Threads, RTX 4080). *Full disclosure: I packaged these configurations into a free, open-source MIT-licensed blueprint called Kinetix IDE on GitHub.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1u59fv6/tuning_a_local_multiagent_developer_environment/)

<!-- url_hash:31e9d8e95df4be603986a4f202059654951d4b861f1b70bd2fa9ee683a60e681 -->


## [r/MachineLearning] I built an open-source Knowledge Graph pipeline with hybrid retrieval to improve LLM multi-hop reasoning [P]

_Reddit r/MachineLearning · 2026-06-14 · score 0.775_

Hey everyone, I built an open-source full-stack pipeline (Django + React) that constructs a Knowledge Graph from raw text, detects thematic communities, and uses hybrid search to solve the "lost in the middle" problem in standard vector retrieval. **The Pipeline:** 1.


[Источник](https://www.reddit.com/r/MachineLearning/comments/1u5yyyl/i_built_an_opensource_knowledge_graph_pipeline/)

<!-- url_hash:b6d62cbf923aeaa06777f365be660476cc0aa441fc234208db8a10f40c585f2f -->


## [r/LocalLLaMA] How are you handling memory provenance in persistent agents — verified vs. inferred facts?

_Reddit r/LocalLLaMA · 2026-06-14 · score 0.775_

Hitting a wall that isn’t recall accuracy — it’s that my agent’s memory can’t distinguish what it actually verified from what it inferred once and now treats as fact several sessions later. Old inferences get promoted to facts; superseded info comes back as current; and I can’t cleanly audit why it believed something when it acts on it.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1u5v8st/how_are_you_handling_memory_provenance_in/)

<!-- url_hash:b1d54141b63c39066df791c7a2e060cf5aa09737874ccd0c1001d6e967513fdd -->


## [r/LocalLLaMA] Help with resources for using LLMs as fictional characters

_Reddit r/LocalLLaMA · 2026-06-14 · score 0.775_

Hey ya'll, I'm an ex-cognitive scientist turned NLP Data Scientist by day, and science fiction author by night. I want to bring fictional characters in my prose to life with Local LLMs, and **I'm looking for the best resources out there for doing this kind of work (datasets, models, libraries, common patterns, etc.).


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1u5tdlh/help_with_resources_for_using_llms_as_fictional/)

<!-- url_hash:3fe4387f30337b1d59dc3522b7ea54d5f3ff9059fe365888fe3332ba0aeb7fbe -->


## [r/LocalLLaMA] Aionforge Memory - Long Term Agent Memory

_Reddit r/LocalLLaMA · 2026-06-14 · score 0.775_

TLDR -> Aionforge Memory is a Rust memory layer for agent systems. It stores episodes, facts, notes, skills, bad patterns, work items, core memory, and audit events in selene-db, then retrieves relevant context with lexical anchors, vector search, graph traversal, recency, importance, and trust signals.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1u5oyzl/aionforge_memory_long_term_agent_memory/)

<!-- url_hash:4677a951c2dec58e9876364c2360ffb372b3e03cb54b40f5218d5d431da27eb3 -->


## [r/LocalLLaMA] I built a local coding agent harness app to actually understand how local LLMs work under the hood here's what I learned and what I made

_Reddit r/LocalLLaMA · 2026-06-14 · score 0.775_

I started this project because I didn't really get how local LLMs worked at the wire level. How does llama.cpp actually serve requests? How does streaming tool calling even work? What's happening when a model uses \`reasoning\_content\`? So I figured, why not try to make one? After a couple months, Sulfur is what I made. **What it is:** A PyQt6 desktop coding agent harness for Windows that runs entirely locally. You point it at your workspace files, and the AI can read, write, edit, and search them. Sessions are saved, history persists, and nothing ever leaves your computer. And its open sourc...


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1u5ox2u/i_built_a_local_coding_agent_harness_app_to/)

<!-- url_hash:20d16ad30eb7cf347975489f240a59ad47fff37b1a63352601f38b6700038398 -->


## [r/LocalLLaMA] Open-source agent that investigates AWS incidents for you (read-only, bring-your-own-LLM) — feedback wanted

_Reddit r/LocalLLaMA · 2026-06-14 · score 0.775_

Disclosure: I’m the author of an open-source tool that automates parts of incident investigation. I’m not here to push it — I’m trying to validate whether the problem I’m solving actually matches how real AWS/Azure on-call works.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1u5msrx/opensource_agent_that_investigates_aws_incidents/)

<!-- url_hash:6afa2e9a8edaeb45f35e2074528c15e414edf0f5ac5861c837a2fbe16e23a8d5 -->


## [r/LocalLLaMA] Dual DGX Sparks- 40tk/s single 1M ; 350 tk/s agg. - Deepseek V4 Flash (vs RTX Pro 6000 vs Mac M2 Ultra 192)

_Reddit r/LocalLLaMA · 2026-06-14 · score 0.775_

First of all shout out to Aiden/Antirez & geniuses at the Nvidia community threads. I'm merely claude-vibing off of their works. That a said, i thought i'd share recipes & learnings & benchmarks so far on running big MOE models on two dgx sparks at a reasonable speed for agent use: [https://github.com/elsung/dgx-spark-deepseek-v4-flash](https://github.com/elsung/dgx-spark-deepseek-v4-flash) The kicker here is that you need **2 DGX sparks** to really get the speed we need, and you have to spend the **$180** on that single cable for 200G/s over connectx7 in order to get this speed. BUT, being ab...


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1u5g9pr/dual_dgx_sparks_40tks_single_1m_350_tks_agg/)

<!-- url_hash:0545deec56bb2cbcc9b739afd6a29d38567ea5a6b3de057d57fb204113da57f0 -->


## [r/artificial] Can an AI agent complete a task and still fail?

_Reddit r/artificial · 2026-06-14 · score 0.775_

A lot of AI-agent discussions focus on whether the agent completed the task. But I think there is a missing category: the agent may complete the task, but do it in an unsafe or policy-violating way.


[Источник](https://www.reddit.com/r/artificial/comments/1u58qwi/can_an_ai_agent_complete_a_task_and_still_fail/)

<!-- url_hash:52e25dd371ff1d8375bf451dedf624330105c94808e28e373b6462bf7622862f -->


## [r/MachineLearning] The Verifier Tax: Horizon-Dependent Safety–Success Tradeoffs in Tool-Using LLM Agents [R]

_Reddit r/MachineLearning · 2026-06-14 · score 0.775_

We recently presented a paper at ACM CAIS 2026 on safety evaluation for tool-using LLM agents. The core issue is that task completion alone can be misleading: an agent may complete a task while violating a safety or policy constraint.


[Источник](https://www.reddit.com/r/MachineLearning/comments/1u58mkq/the_verifier_tax_horizondependent_safetysuccess/)

<!-- url_hash:08c741444a7b689a295adb34c6db790935f97ac778c198bffa78bdb97fd69b62 -->


## [r/LocalLLaMA] How do you actually know your LLM setup didn't get worse after you change something?

_Reddit r/LocalLLaMA · 2026-06-14 · score 0.775_

Something I keep running into, and I’m curious how others handle it: I’ll tweak a prompt, swap a model, or change a retrieval step — and then I have no real idea whether I actually improved things or quietly broke something else. Usually I just run a few examples by hand, the outputs *look* fine, and I ship it.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1u568pn/how_do_you_actually_know_your_llm_setup_didnt_get/)

<!-- url_hash:4de3dfe6b760749e605e0ab6714cf4d51094bc59d7bf3e9fa0abb9c3d9ee9da6 -->
