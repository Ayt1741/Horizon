---
layout: post
title: "Выпуск 2026-06-28 (RU)"
date: 2026-06-28 09:00:00 +0000
lang: ru
---

# Выпуск 2026-06-28


## [r/LocalLLaMA] Locally running mode turns an Image into a Cute Controllable Character you can Play as

_Reddit r/LocalLLaMA · 2026-06-28 · score 0.825_

This is a sequel to my last post here !! It meant a lot to have such positive feedback last time. This is the 800M version of the previous model. It still has a LOT of issues but the promise is the same. Working comfortably on consumer GPUs The context is increased to 12 latent frames. The wierd flashes of last time are gone. Stability is much better although consistency is horrible. I'm hoping to fix that in next iteration. the 500M model gets over 60 fps on a RTX 5090 now. The architecture is still the same , I mostly just fattened the MLP. Again the de noiser is trained from scratch with di...


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1uicq8x/locally_running_mode_turns_an_image_into_a_cute/)

<!-- url_hash:1bfbfcc488ca31432206f0c7230cf7d6efb36a1d30db0e1c63408de56e8db6c3 -->


## [r/artificial] The Government Built the Internet. Why Didn’t It Build AI?

_Reddit r/artificial · 2026-06-28 · score 0.825_

Hey guys, I just red an article from the CEO of Microsoft who said: *“It will cost 'hundreds of billions' to keep up with frontier AI in the next decade.”* The article made sent me in a rabbit hole and made me think how other life changing events in our history kick-started. And every single time - the government played a big role in making it possible.


[Источник](https://www.reddit.com/r/artificial/comments/1uhxhsq/the_government_built_the_internet_why_didnt_it/)

<!-- url_hash:78e308e267f8cc18f4d08d2d3de29d0a2dc5648ec56c5467c917a327939db0d4 -->


## [r/LocalLLaMA] A barebones CPU-only inference engine for Qwen 3, written from scratch in pure C

_Reddit r/LocalLLaMA · 2026-06-28 · score 0.825_

TL;DR: The (very messy) code and writeups can be found at https://github.com/jakint0sh/qwen3-engine Read the README for instructions on how to get started. And for those who just want a bulleted list: - Inference engine for Qwen 3 sizes 4B and below - Written from scratch in pure C - No dependencies except libc, libm, and cJSON (and OpenMP if compiled with parallelization) - Loads directly from HF safetensors, does 4-bit affine quant on the fly - Does KV caching - Built-in chat interface - Very slow, but the code is readable and tractable, and would be good to learn from And now for the blab-fest...


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1uht9rf/a_barebones_cpuonly_inference_engine_for_qwen_3/)

<!-- url_hash:051e5a132c7cbec6bb0066f337a8c7b3105cabc51c1a0a3bb31d62e821f4026a -->


## [r/LocalLLaMA] Hypothetically speaking...

_Reddit r/LocalLLaMA · 2026-06-28 · score 0.8_

Would it not be possible to create crowd sourced, truly open sourced distilled LLMs with a simple wrapper around command line based AI services that exist today? I'm imagining a layer that goes around whatever application people currently use for coding/AI boyfriend that collects your inputs and associates them with your outputs.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1uhzhf6/hypothetically_speaking/)

<!-- url_hash:6542c7a7a1fa8594adcb93964e6577ab28a81836350ce1f81c1fafd57c0bbdc7 -->


## [r/LocalLLaMA] Qwen3.6 27B local vs Opus 4.8, voxel engine in raw C with zero frameworks

_Reddit r/LocalLLaMA · 2026-06-28 · score 0.8_

Sunday experiment. Same prompt to both. Build a voxel world in plain C. No engine, no game library, no framework, just the compiler. The model does its own chunk meshing, render loop and memory management by hand. Left is Claude Code on Opus 4.8. Right is Qwen3.6 27B local on vLLM, the new NVFP4 quant, 256k context. Runs around 130 TPS on an RTX 6000 Blackwell 96GB through my own [coding agent](https://github.com/codehamr/codehamr). Opus clearly understands voxel physics. Terrain holds, chunks line up, collision works. The 27B compiles and renders, then tears itself apart on screen. The qualit...


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1uhv3wc/qwen36_27b_local_vs_opus_48_voxel_engine_in_raw_c/)

<!-- url_hash:7dfcee2d9c5c7787bae727254663a8a7ca4e0f9fd84f1ce4b60100af355f7df2 -->


## [r/LocalLLaMA] How many of you do use Q1 or Q2 of Big models(100-250B)? How's it?

_Reddit r/LocalLLaMA · 2026-06-28 · score 0.8_

Sharing popular(also recent) models for reference: **151-250B** : * DeepSeek-V4-Flash * Step-3.X-Flash * Command-a-plus-05-2026 * Laguna-M.1 * MiniMax-M2.X * Qwen3-235B-A22B **100-150B** : * GLM-4.5-Air * Qwen3.5-122B-A10B * NVIDIA-Nemotron-3-Super-120B-A12B * Mistral-Small-4-119B-2603 * Devstral-2-123B-Instruct-2512 * Mistral-Medium-3.5-128B * Llama-4-Scout-17B-16E-Instruct (Yay! got your attention) **<100B** : * Llama-3.3-70B-Instruct * Qwen3-Coder-Next * Qwen3-Next-80B-A3B I see that some people do use Q3(even up to IQ3\_XXS) whenever they couldn't run Q4 on their rig.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1uhummm/how_many_of_you_do_use_q1_or_q2_of_big/)

<!-- url_hash:12f130b2e31f75a48cb7476b21e63cce7c1373fb338f9497a67be39ef367e556 -->


## [r/LocalLLaMA] NPC Engine Using Local Models

_Reddit r/LocalLLaMA · 2026-06-28 · score 0.775_

I’ve been working on a game-agnostic NPC engine/backend based pretty heavily on SillyTavern-style architecture, and with smaller local models getting better and better, I honestly think this kind of thing could be the future of RPGs. Right now I’m using NVIDIA Parakeet 0.6 for STT, Gemma 4 26B A4B for the LLM, and Qwen3-TTS for voice, and I’m getting super fast response times with pretty decent quality.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1uibt9o/npc_engine_using_local_models/)

<!-- url_hash:2cae42fe512a974815b9f569e430fe2488b883a7622e40f98df716c5fa13b25d -->


## [r/artificial] Building Mini CompanyOS AI with Hindsight Memory and cascadeflow Routing

_Reddit r/artificial · 2026-06-28 · score 0.775_

Most AI agents forget everything after each conversation. I wanted to see what happens if AI behaves more like an organization instead. So I built a multi-agent executive system where: • Sales agents provide market and customer recommendations. • Finance agents evaluate cost, risk, and ROI. • HR agents consider hiring and operational impact. • A CEO agent synthesizes all recommendations into a final decision. The interesting part was memory. Using Hindsight, agents could reference previous discussions and decisions instead of starting from zero every time. Some observations after building it: ...


[Источник](https://www.reddit.com/r/artificial/comments/1ui2l62/building_mini_companyos_ai_with_hindsight_memory/)

<!-- url_hash:aeacf7e73349742e050b4cc52086bb41ea1e00a7b750fa32cee0fd2344879273 -->


## [r/LocalLLaMA] Script to monitor llama cpp and analyze memory usage

_Reddit r/LocalLLaMA · 2026-06-28 · score 0.775_

My goal has always been to be productive with commodity hardware. So far my workhorses have been the MoE editions of gemma 4 and Qwen 3.6 on an old desktop with a single 9060XT with 16GB ram.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1ui0u4v/script_to_monitor_llama_cpp_and_analyze_memory/)

<!-- url_hash:aef131b5c5a1c2f3a1bdb0ac6592618505bf7e4f692da1cd6fb41fdfd9506748 -->


## [r/LocalLLaMA] Best case for dual RTX 3090 (250W each) on Crosshair VIII Hero?

_Reddit r/LocalLLaMA · 2026-06-28 · score 0.775_

I'm building a local LLM workstation and would appreciate some advice from people already running 2×3090s. Current hardware: * ASUS Crosshair VIII Hero (X570) * One Gainward Phoenix RTX 3090 * Looking for a second used 3090 (not necessarily the same model) * Both GPUs will be power-limited to \~250W I'm trying to keep the case budget under 200 euros SEK (including any extra fans), but might stretch if neccesary...


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1uhv2hi/best_case_for_dual_rtx_3090_250w_each_on/)

<!-- url_hash:a0a6d3436a0433a75beec8455c38877e9ee22061d3e7ee7c351735d3455ed101 -->


## [r/artificial] Analysis: AI is entering a dark age

_Reddit r/artificial · 2026-06-28 · score 0.775_

[https://eigenwise.io/writing/the-ai-dark-age-government-switch](https://eigenwise.io/writing/the-ai-dark-age-government-switch) What started as me thinking this was all payback for Anthropic refusing to cooperate with the DoD has kind of fallen apart on me... because then GPT-5.6 got gatekept too, like two weeks later.


[Источник](https://www.reddit.com/r/artificial/comments/1uhrtvf/analysis_ai_is_entering_a_dark_age/)

<!-- url_hash:1e4af0e101bb8dfbfa370fb490d9a8ee45fb7147a6b391efd23a32e853f68b64 -->


## [r/LocalLLaMA] Reverse engineered DeepSeek Chat into an OpenAI compatible API (V4 & R1 models, no API key, no bills)

_Reddit r/LocalLLaMA · 2026-06-28 · score 0.775_

DeepSeek already has an official OpenAI compatible API, but it's paid. The consumer web chat, on the other hand, is free. So I built a local proxy that logs into your DeepSeek account once, stores the session, and exposes an OpenAI compatible endpoint at `http://localhost:8000/v1`. That means existing OpenAI compatible tools (Open WebUI, agents, CLI tools, SDKs, etc.) can talk to DeepSeek Chat without changing any code. Features: * OpenAI compatible `/v1` endpoint * Streaming responses * Multi-turn conversations * Drop-in replacement for most OpenAI SDKs and clients I originally built it for l...


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1uhqrnb/reverse_engineered_deepseek_chat_into_an_openai/)

<!-- url_hash:57ecce8516c51080452c97ce731a26ae3fa18099f87c0a0f137d137cdc83812a -->
