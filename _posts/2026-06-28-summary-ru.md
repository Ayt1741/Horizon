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


## [r/OpenAI] Consumer Ai Models is Dumped?!

_Reddit r/OpenAI · 2026-06-28 · score 0.825_

IMPORTANT: Friends, please share your own experience in the comments. I do not believe I am the only one who has noticed this. My honest impression ⚠️ I am not claiming I know exactly what is happening internally. But after regulators in the US started putting more pressure on companies like Anthropic and OpenAI, it really feels like public-facing models may be getting increasingly: restricted; over-filtered; behaviorally “flattened”; less decisive; less capable of following a long technical chain without drifting. Maybe it is safety tuning. Maybe cost optimization. Maybe routing. Maybe model ...


[Источник](https://www.reddit.com/r/OpenAI/comments/1uhtssy/consumer_ai_models_is_dumped/)

<!-- url_hash:cc78c8ebd3056a021df2befe5671d786e6d1421213755f979fb8bc7237122dd7 -->


## [r/OpenAI] What happens when you give an AI a budget?

_Reddit r/OpenAI · 2026-06-28 · score 0.8_

Over the past few weeks, I've been exploring whether LLMs can work with execution budgets. We've seen models produce meaningful artifacts with projects like Caveman and Ponytail, but what happens when you give models limited Budget.


[Источник](https://www.reddit.com/r/OpenAI/comments/1ui4stw/what_happens_when_you_give_an_ai_a_budget/)

<!-- url_hash:2c7e1ee3ddd7e22415e343fba1dfa154916920d7cb5fda2382db59b33603b401 -->


## [r/OpenAI] Where’s OpenAI’s designing agent? What’s the alternative to Claude Design?

_Reddit r/OpenAI · 2026-06-28 · score 0.8_

I guess GPT 5.5 even with high thinking cannot design even at par with Claude Design. I used it to design some components (like a chain of events to show on home page) for my application and it sticked to the 90s old fashioned textboxes style design.


[Источник](https://www.reddit.com/r/OpenAI/comments/1ui29be/wheres_openais_designing_agent_whats_the/)

<!-- url_hash:7e6c6e555500a294df0d9a876762c33ff5fb07abb215c80f527db33f176e949c -->


## [r/OpenAI] Question from outside the US: should I just commit to Chinese/Other models now?

_Reddit r/OpenAI · 2026-06-28 · score 0.8_

Watching the last two weeks, it feels like we just saw a new system get built in real time. Commerce pulled Fable and Mythos, then partially gave Mythos back to around 100 US institutions, and now OpenAI's GPT-5.6 is going out to "trusted partners approved with the US government" first WTF?.


[Источник](https://www.reddit.com/r/OpenAI/comments/1uhvioq/question_from_outside_the_us_should_i_just_commit/)

<!-- url_hash:3ad22039730b9cf9508ec0e601aaede0ba17efba219d5a2d9d671d6d2e6d6ef3 -->


## [r/OpenAI] Help me AI, needing advice

_Reddit r/OpenAI · 2026-06-28 · score 0.8_

Hi guys so I use ChatGPT pro pretty much everyday. I use it for all sorts of things. But mainly my health/skin stuff, mental health and general conversation However, I’m finding lately I’m having to check it all the time! It’s super frustrating! Like it’ll fuck up, I’ll pull it up on why it’s fucked up “you’re right to catch that out! I apologise” blah blah blah. Like I know it’s AI but mine can’t even follow a normal conversation most of the time, and I don’t know if the facts it’s gives me are correct as I’ve caught it saying incorrect stuff lots of time. Anyway, I’ve obviously given this ch...


[Источник](https://www.reddit.com/r/OpenAI/comments/1uhpj17/help_me_ai_needing_advice/)

<!-- url_hash:1a4ecefc1dca0c304b6fcfe909a3b7c691731f1d9fc3c5b0d52f891655754480 -->


## [r/OpenAI] Why does openai-whisper re-download the model every few transcriptions?

_Reddit r/OpenAI · 2026-06-28 · score 0.775_

I've been running openai-whisper installed via pipx for some while now, using it to transcribe voice notes taken via a digital recorder, and while I'm generally very happy with the results I'm confused about one aspect of its behavior. I run a bash script to recurse through an import directory to transcribe any new notes that are present, invoking whisper from the cli.


[Источник](https://www.reddit.com/r/OpenAI/comments/1ui93rd/why_does_openaiwhisper_redownload_the_model_every/)

<!-- url_hash:be2242ee9c4169954f09a5c2ef2a756a09770af41fabb7941a0c534d97b099ec -->


## [r/OpenAI] What does "production-ready" actually mean for AI agents?

_Reddit r/OpenAI · 2026-06-28 · score 0.775_

Everywhere I look, I see announcements for folks who’ve just built an AI agent but seldom do I find conversations about what happens after the demo. For “traditional” software, the requirements for a production-ready system are pretty well-defined: - Monitoring.


[Источник](https://www.reddit.com/r/OpenAI/comments/1ui566i/what_does_productionready_actually_mean_for_ai/)

<!-- url_hash:f90bbea57f716e3e8f1bda31253f172806a66cf60328e0ac6771c8efe6ede486 -->


## [r/OpenAI] What AI workflow became part of your daily routine without you realizing it?

_Reddit r/OpenAI · 2026-06-28 · score 0.775_

One year ago, I only opened ChatGPT when I had a precise question in mind. Now I find myself leveraging AI for a number of miniature operations each and every day on an almost automatic level.


[Источник](https://www.reddit.com/r/OpenAI/comments/1ui50r7/what_ai_workflow_became_part_of_your_daily/)

<!-- url_hash:90d067903c43e3e7c8a5b65e19bf35c82565bc7ffe75127879107883af21607b -->


## [r/OpenAI] AI-assisted Skyrim Modding

_Reddit r/OpenAI · 2026-06-28 · score 0.775_

I am unfortunately one of those modders who always tried to learn as little as possible and just accomplish everything, even when others told me to stop, through the normal mod manager install process. I avoided using any other tools or learning even minimal modding myself.


[Источник](https://www.reddit.com/r/OpenAI/comments/1uhxj17/aiassisted_skyrim_modding/)

<!-- url_hash:812fdf3c5aa2992ef5df0c01dfd1b4c285004fe913f47b89ec0a44a5b9e7c405 -->


## [r/OpenAI] Why is every AI lab suddenly trying to build their own chips?

_Reddit r/OpenAI · 2026-06-28 · score 0.775_

Just saw that OpenAI is dropping their own custom chip - Jalapeño, later this year, and Anthropic is apparently trying to do the exact same thing. I get that compute is scarce right now and there's certain benefits in designing chips based on own requirements.


[Источник](https://www.reddit.com/r/OpenAI/comments/1uhn4y9/why_is_every_ai_lab_suddenly_trying_to_build/)

<!-- url_hash:7fd32c519403d77810ea873feb8f155ecf1ea244286ea03ff668b6928ad0ef09 -->


## [r/OpenAI] chatgpt image generation dimensions inconsistent

_Reddit r/OpenAI · 2026-06-28 · score 0.775_

https://preview.redd.it/r47cgi0e7x9h1.png?width=2746&format=png&auto=webp&s=1f96b498cd6ee412d7b118727899f619b8a42fbf I had chatgpt generate this image for me. It's close to what I want, but the house isn't properly centered on the x-axis like I need it.


[Источник](https://www.reddit.com/r/OpenAI/comments/1uhj2h9/chatgpt_image_generation_dimensions_inconsistent/)

<!-- url_hash:c940ca2a9950e3e124db5df116f8f8cdb84f85e0466546de925f65a523c06519 -->
