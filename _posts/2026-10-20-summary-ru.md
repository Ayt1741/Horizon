---
layout: default
title: "Horizon Summary: 2026-10-20 (RU)"
date: 2026-10-20
lang: ru
---

> From 69 items, 4 important content pieces were selected

---

**Бесплатные ИИ**
1. [HermesConsole и VoiceManager: бесплатный локальный стек голосового ИИ с MIT-лицензией](#item-free-ai-1) ⭐️ 9.0/10
2. [DeepSeek открыл исходный код движка вывода DeepInfer](#item-free-ai-2) ⭐️ 8.0/10
3. [MPS in PyTorch 2.15](#item-free-ai-3) ⭐️ 8.0/10
4. [Tess-4.5-27B: бесплатная Qwen-дообучка с 25% меньше токенов](#item-free-ai-4) ⭐️ 8.0/10

---

## Бесплатные ИИ

<a id="item-free-ai-1"></a>
### [HermesConsole и VoiceManager: бесплатный локальный стек голосового ИИ с MIT-лицензией](https://www.reddit.com/r/LocalLLaMA/comments/1xag5bj/hermesconsole_a_demo_showing_off_voicemanager_my/) ⭐️ 9.0/10

VoiceManager — это полностью открытый \(MIT\) локальный сервер потокового STT/TTS с поддержкой wake-word \(«hey computer»\), barge-in \(перебивание ответа голосом\), вызовов инструментов и рендеринга markdown/изображений. Работает на устройстве без облачных API, ключей или лимитов использования. По умолчанию использует audio.cpp с моделями Nemotron и Breeze TTS 2. Есть Python-клиент для интеграции в агентов и Kotlin-референс \(HermesConsole\). Репозитории: github.com/TacoTakumi/VoiceManager и github.com/TacoTakumi/HermesConsole. Документация: tacotakumi.github.io/VoiceManager. Никаких регистраций, карт или квот — просто клонируйте и запускайте.

reddit · r/LocalLLaMA · /u/HockeyDadNinja · Oct 20, 02:18

**「Контекст проекта」** Автор разрабатывал VoiceManager с марта 2026 года для поддержки игрового концепта и собственных ИИ-ассистентов. HermesConsole — это демонстрационное LCARS-приложение на Kotlin, служащее референс-клиентом. Архитектура передаёт аудио и команды через один WebSocket, сохраняя контекст сессии между репликами и историю прошлых сессий. Barge-in отключён по умолчанию из-за сложностей с эхо-отменой; на планшете автора сломался аппаратный AEC, поэтому добавлен переключатель.

**「Что это даёт разработчику」** Можно добавить полноценный голосовой интерфейс к локальному агенту без расходов на API и без отправки аудио в облако. Первым делом стоит попробовать Python-клиент: подключить к своему LLM-агенту и проверить wake-word + стриминг TTS предложение за предложением. Следить за настройкой эхо-отмены при включении barge-in — на некоторых устройствах может требоваться программная AEC.

**Tags**: `#free-local-voice`, `#open-source-stt-tts`, `#python-client`, `#kotlin-reference`, `#wake-word-streaming`

---

<a id="item-free-ai-2"></a>
### [DeepSeek открыл исходный код движка вывода DeepInfer](https://github.com/deepseek-ai/DeepInfer) ⭐️ 8.0/10

DeepSeek опубликовал на GitHub исходный код DeepInfer — бесплатного движка для высокопроизводительного вывода LLM, поддерживающего разные аппаратные платформы, включая NPU Huawei Ascend. Репозиторий доступен сразу без регистрации и ключей: github.com/deepseek-ai/DeepInfer. Движок используется в продакшене для модели DeepSeek-V4.1-Flash, обеспечивая, по данным компании, 155 триллионов токенов в день на кластере. Ограничения: документация пока на китайском, поддержка железа вне NVIDIA/Huawei не детализирована, готовые бинарники не предоставлены — нужно собирать самостоятельно.

hackernews · ggcr · Oct 20, 09:08 · [Discussion](https://news.ycombinator.com/item?id=50163277)

**「Контекст」** DeepInfer — это движок вывода, который DeepSeek использует для обслуживания своей модели DeepSeek-V4.1-Flash, запущенной ранее в 2026 году с нативной мультимодальной поддержкой и контекстным окном в 1 млн токенов. Ранее DeepSeek публиковал только лёгкие демо-версии для FP8/BF16 вывода и обеспечивал поддержку через SGLang, но сам высокопроизводительный стек оставался закрытым. Открытие DeepInfer делает доступным тот же фреймворк, который обеспечивает пропускную способность 155 трлн токенов в день на кластере и поддержку аппаратных ускорителей, включая Huawei Ascend NPU.

**「Влияние на бесплатный ИИ」** DeepInfer даёт разработчикам готовый, бесплатный движок для развёртывания LLM на собственном железе без привязки к API-провайдерам и плате за токены. Поддержка Huawei Ascend NPU и других не-NVIDIA ускорителей снижает порог входа для лабораторий без доступа к GPU NVIDIA. Функция batch-invariant inference \(только NVIDIA\) гарантирует детерминированные результаты при разных батчах — важно для продакшн-сценарриев. Первым делом стоит попробовать запустить DeepSeek-V4.1-Flash или совместимую модель на имеющемся оборудовании, проверив пропускную способность. Риск: экосистема пока ориентирована на стек DeepSeek, поддержка сторонних моделей и долгосрочная поддержка драйверов для альтернативных NPU требуют проверки на практике.

**「Обсуждение」** Комментаторы называют релиз стратегическим ударом по вендорной привязке к NVIDIA: открытая поддержка Ascend 950 позволяет малым лабораториям разворачивать вывод на китайском железе без API-плат. Упоминается удержание KV-кеша более 72 часов и доход $38/карта/час в непик, но участники спорят, достаточно ли этого для реальной конкуренции с CUDA-экосистемой.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/DeepSeek-V3">GitHub - deepseek -ai/ DeepSeek -V3 · GitHub</a></li>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">Introducing DeepSeek -V4.1-Flash: smarter, faster, more efficient.</a></li>
<li><a href="https://github.com/deepseek-ai/DeepInfer">GitHub - deepseek- ai / DeepInfer : DeepInfer : High-performance...</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#inference-engine`, `#free-software`, `#hardware-acceleration`, `#deepseek`

---

<a id="item-free-ai-3"></a>
### [MPS in PyTorch 2.15](https://huggingface.co/blog/mps-pytorch-2-15) ⭐️ 8.0/10

PyTorch 2.15 brings FP8 support and 5–6.5× faster MoE inference to Mac via MPS, enabling free local LLM runs on Apple Silicon.

rss · HuggingFace Blog · Oct 20, 00:00

**Tags**: `#mps`, `#pytorch`, `#mac`, `#local-inference`, `#free-compute`

---

<a id="item-free-ai-4"></a>
### [Tess-4.5-27B: бесплатная Qwen-дообучка с 25% меньше токенов](https://www.reddit.com/r/LocalLLaMA/comments/1xadfm7/migtisseratess4527b_qwen_finetune/) ⭐️ 8.0/10

Tess-4.5-27B — открытая дообучка Qwen3.8-27B от автора Synthia, доступная бесплатно на Hugging Face в формате GGUF для локального запуска. Модель выдаёт те же результаты на 150 сценариях BenchLocal, используя на 25% меньше токенов: 262K против 349K у базовой модели. На CLI-40 экономия 32%, на извлечении данных — 43%. Меньше токенов означает быстрее ответы, меньше контекста на рассуждения и более длинные сессии. Для запуска нужен только собственный GPU; регистрации, карт или квот нет.

reddit · r/LocalLLaMA · /u/jacek2023 · Oct 20, 00:09

**「Контекст: Qwen3.8-27B и BenchLocal」** Tess-4.5-27B — это дообученная версия модели Qwen3.8-27B, выпущенной исследователями Qwen в августе 2026 года и протестированной в формате FP8 на GPU RTX PRO 6000 Blackwell \(tool-2-1\). Качество сравнивается через набор BenchLocal — локальный бенчмарк из 150 сценариев, охватывающих CLI, извлечение данных, поиск ошибок и другие задачи \(tool-2-3\). Автор модели, migtissera, ранее выпускал серию Synthia.

**「Влияние」** Для локального инференса это даёт конкретный выигрыш: те же качественные ответы при меньшей нагрузке на контекст и ускоренной генерации за счёт драфт-головы. Стоит попробовать на задачах с длинным контекстом \(CLI, извлечение данных\), где экономия токенов максимальна. Риск: модель новая, долгосрочная стабильность и поддержка не проверены сообществом.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.veladan.org/2026/08/14/qwen3-8-27b-fp8-benchmarks.html">Qwen3.8-27B-FP8: First Benchmarks on RTX PRO 6000 Blackwell</a></li>
<li><a href="https://gist.github.com/everson/261fdef8a3d35298b36a07f436e407f6">Tess localbench. GitHub Gist: instantly share code, notes, and snippets.</a></li>

</ul>
</details>

**Tags**: `#open-model`, `#local-inference`, `#qwen-finetune`, `#efficiency`, `#free-llm`

---


## [r/MachineLearning] Building and Pre-training a GPT-2 LLM from Scratch [P]

_Reddit r/MachineLearning · 2026-10-20 · score 0.85_

A couple of months ago, I started a small side project to understand how Large Language Models (LLMs) are pre-trained by actually building and training one from scratch. I chose GPT-2 (124M parameters).


[Источник](https://www.reddit.com/r/MachineLearning/comments/1xaq9s8/building_and_pretraining_a_gpt2_llm_from_scratch_p/)

<!-- url_hash:c056334086efad2a6651ec99bc96510662159acd9ce080640c8ff4b4599bfa14 -->


## [r/LocalLLaMA] Qwen 3.8-27B-pi on 3080+3060

_Reddit r/LocalLLaMA · 2026-10-20 · score 0.825_

Hey, for some time now I play with various setup for local LLM hosting on my old gaming rig, starting from Qwen-2.5-7B on Ollama to llama.cpp and buying second-hand 3060 to get more VRAM. Right now what I have is: 3080 10gb vram 3060 12gb vram 32gb DDR5 4800 As you can see, I am running a budget option and I do not plan any expensive expansions, rather small incremental steps.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1xaxbp3/qwen_3827bpi_on_30803060/)

<!-- url_hash:dbb4c3d4c7af99af0322fcd9a80bfbc87d59ac886f93a525577770c7d293a5e9 -->


## [r/LocalLLaMA] Geezuz kernel: Qwen3.8-27B at 190 tok/s (620~ tok/s at 8 requests) on two 3090s

_Reddit r/LocalLLaMA · 2026-10-20 · score 0.825_

**Geezuz, its fast!** Qwen3.8-27B, two RTX 3090s power-limited to 280 W, plain PCIe, no NVLink, at 0 Context: (tests showing results with context are found on the next table) |Requests|Q4\_K\_M|Q8\_0| |:-|:-|:-| |1 request|**190 tok/s**|143 tok/s| |8 requests at once (total)|**622 tok/s**|610 tok/s| llama.cpp's fastest two-GPU setup did about 100 tok/s on the same prompts. This did 164 on average and 214 on code, at the same output quality (KL divergence against llama.cpp).


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1xaslfk/geezuz_kernel_qwen3827b_at_190_toks_620_toks_at_8/)

<!-- url_hash:764f8bc9c31cf9ea41b1906a7e50d4019d262ba6f53713fea36e73548fb56b54 -->


## [r/artificial] Research shows AI agents reject sponsored listings 97% of the time. Nobody is building the advertising infrastructure for what comes next.

_Reddit r/artificial · 2026-10-20 · score 0.825_

Two recent papers caught my attention and I think they point to a massive blind spot in how we're thinking about AI agents in commerce. Wadi & Ma (McGill, Sep 2026) tested what happens when you tell an LLM "you work for the traveler" vs "you work for the booking platform." The consumer-deployed agent chose sponsored listings only 2.8% of the time — a 97.2% rejection rate.


[Источник](https://www.reddit.com/r/artificial/comments/1xadsk6/research_shows_ai_agents_reject_sponsored/)

<!-- url_hash:48587bf65af6d215927b06f1d4548a632b52fdc7a4824008af31383b765e75ac -->


## [r/LocalLLaMA] Fast-swap available v0.3.0 (Berth) - Testing needed

_Reddit r/LocalLLaMA · 2026-10-20 · score 0.8_

Berth v0.3 is out, and I need testers with big RAM and more than one GPU v0.3 parks engines in system RAM instead of unloading them. A switch back to a parked engine skips the reload from disk.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1xb783i/fastswap_available_v030_berth_testing_needed/)

<!-- url_hash:3c5ad62269d16da7cc43e1bc9c42f96caad7c601ad075f6eb6cc1c3fe57846c9 -->


## [r/LocalLLaMA] ChatGPT, but self-hosted

_Reddit r/LocalLLaMA · 2026-10-20 · score 0.8_

Happy ~~taco~~ slopo Tuesday friends, OWUI is bloated. It tries to do too many things and doesn't get the basics right. A polished interface is what most of us actually want. Not everyone needs knowledge bases and a RAG pipeline. Some people just want a clean, polished place to chat and code with their local models. That's what I've been building for the past few months. ChatGPT, but self-hosted. Because that's what ChatGPT actually is now. A really good chat experience, with Codex sitting in it for when you want to code. **What you get:** * Built-in voice: local TTS + STT + live voice2voice, ...


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1xb70r1/chatgpt_but_selfhosted/)

<!-- url_hash:624500d8f8c9b61a513c60cd3c5831d452f0e47eb0b6fe8b10a122d87b6c1098 -->


## [r/LocalLLaMA] VectorDash update: now written in Rust, with full clipboard management, LOCAL reverse image search, web search, and AI chat (with computer and browser use), (mostly) powered by EmbeddingGemma 2!

_Reddit r/LocalLLaMA · 2026-10-20 · score 0.8_

Thanks to everyone who tried VectorDash and shared feedback. A recurring request was to move from Python to Rust and build something that could replace more of what people use [Everything ](https://www.voidtools.com/support/everything/searching/)and Windows search for.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1xb41jt/vectordash_update_now_written_in_rust_with_full/)

<!-- url_hash:c8a623bf0698041513fd20897433d996d857fd8e143bfbd5ec9dbd2233b209b6 -->


## [r/LocalLLaMA] Kokon 0.10: the Qwen-Image 2.1 text encoder now writes your prompts too (no extra model), plus your own LoRAs (beta)

_Reddit r/LocalLLaMA · 2026-10-20 · score 0.8_

![video](vr0duj9mynwh1 "Kokon 0.10: Prompt+ and your own LoRAs") A week ago I [posted Kokon here](https://www.reddit.com/r/StableDiffusion/comments/1x5tmlp/), a no-settings desktop editor for Qwen-Image 2.1. 0.10 is out with the two things people asked for most.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1xazqxz/kokon_010_the_qwenimage_21_text_encoder_now/)

<!-- url_hash:a2ad6349937737d5900c0f599b8ec546079fd456d3a4b250f7abfacd98362983 -->


## [r/LocalLLaMA] Running 35B MoE models on a Tesla K80 (2014) at ~21 tok/s, in plain C

_Reddit r/LocalLLaMA · 2026-10-20 · score 0.8_

I've spent about a year on an inference engine that doesn't need modern hardware. It's called **Pantheon** (LLM engine) on top of **Foundry** (ML library), both in C with no outside libraries.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1xaz06x/running_35b_moe_models_on_a_tesla_k80_2014_at_21/)

<!-- url_hash:7b998503aef9115441d838894f5ceec4366bd4ae4ee085648732c030534d170b -->


## [r/LocalLLaMA] Character cards are untrusted input. Notes from a security pass on my local RP frontend

_Reddit r/LocalLLaMA · 2026-10-20 · score 0.8_

I make Vellium, a free open-source app for roleplay and story writing with local models. Windows, macOS and Linux. The last release was only security fixes, and one of the bugs is worth knowing about even if you never use my app. When you imported a character card, Vellium saved the card's avatar field as the path to the avatar file. When you later changed that character's picture, it deleted the old file at that path. So a card with ../../ and some path in that field could make the app delete a file the card author picked, the moment you swapped the avatar. If the field held a web link instea...


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1xaqrpg/character_cards_are_untrusted_input_notes_from_a/)

<!-- url_hash:70340e196d6015df5abee9657d4819a317907e26f13056e938169bea1a8afeb3 -->


## [r/LocalLLaMA] amd ryzen ai halo

_Reddit r/LocalLLaMA · 2026-10-20 · score 0.8_

https://i.redd.it/y8nox8d3blwh1.png [*link to techpowerup's original article*](https://www.techpowerup.com/review/amd-ryzen-ai-max-395-strix-halo-mini-pc/) **TL;DR:** priced at $4k, amd's ryzen ai halo mini-pc features the ryzen ai max+ 395 cpu and 128gb of unified memory, letting power users run large local ai models that standard 32gb gpus can't handle. although nvidia's rival dgx spark offers faster time-to-first-token performance, cuda integration, and fp8/fp4 support, it costs much more ($7k for 128gb).


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1xangcv/amd_ryzen_ai_halo/)

<!-- url_hash:81fddb4a6b7b94ef9c8a010e837fcbdfe935e9883ee1782bbc0a0b50cafa8837 -->


## [r/LocalLLaMA] I run llama-swap, Ollama, ComfyUI, Strata and a game on one card. Here is what keeps it alive

_Reddit r/LocalLLaMA · 2026-10-20 · score 0.8_

Berth is one Go binary that leases your GPU to whatever asks for it. You start your engines with \`berth run\` instead of the engine's own command.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1xag1yv/i_run_llamaswap_ollama_comfyui_strata_and_a_game/)

<!-- url_hash:13dda9e665045c84b7f9ea679c5f9e39c79367103db152e98469c367887a4504 -->


## OPTIMA: Optimal One-shot Pruning for LLMs via Quadratic Programming Reconstruction

_arXiv · 2026-10-20 · score 0.85_

Post-training pruning cuts the inference cost of large language models, yet it faces a trade-off: simple heuristics that zero weights are fast but degrade accuracy, while principled joint optimization methods recover accuracy but are computationally infeasible at modern scale. One-shot methods such as SparseGPT sit in between and apply efficient but approximate weight updates.


[Источник](https://arxiv.org/abs/2512.13886)

<!-- url_hash:63c5182066c3123913bedb614b2ad2e81e2cc84ea77ad1e2cc9737bde9c7bd3d -->


## TTS-Q: Speaker-Aware Post-Training Quantization of Text-to-Speech Diffusion Transformers

_arXiv · 2026-10-20 · score 0.825_

Zero-shot text-to-speech (TTS) can clone a voice from seconds of audio. Yet the quality comes from billion-parameter diffusion transformers whose size and multi-step sampling put them out of reach of the on-device, assistive, and real-time applications that need them most.


[Источник](https://arxiv.org/abs/2610.12474)

<!-- url_hash:d0a83417a85757e69c786fd5ae749bab1e0be6c83aec0e9370ba79729d191158 -->


## Toward Agentic AI for the 6G Physical Layer: From Algorithm Discovery to Verified Baseband Silicon

_arXiv · 2026-10-20 · score 0.825_

6G will be designed faster than it can be built: AI-driven search already proposes physical-layer algorithms at machine speed, while carrying a single one onto embedded baseband silicon remains specialist work. That silicon imposes hard memory and numeric limits, but also exposes cost structures a GPU lacks, and a design flow that never runs on the target sees neither.


[Источник](https://arxiv.org/abs/2610.27797)

<!-- url_hash:b51157cfd910bdf8c3af9cd06d70fa6330794625dee7fb69f2f771e050b29a65 -->


## FiTv2: Scalable and Improved Flexible Vision Transformer for Diffusion Model

_arXiv · 2026-10-20 · score 0.8_

\textit{Nature is infinitely resolution-free}. In the context of this reality, existing diffusion models, such as Diffusion Transformers, often face challenges when processing image resolutions outside of their trained domain.


[Источник](https://arxiv.org/abs/2410.13925)

<!-- url_hash:54be8cdf5a2bb32c2cbb90febfa763839c43858618e63bebf64c60ddf0af71a3 -->


## DIFFLET: A Fast Inference Engine for Diffusion Transformer Models on AWS Trainium

_arXiv · 2026-10-20 · score 0.8_

On AWS Trainium2, every component of a diffusion model runs as a program compiled ahead of time for fixed shapes, while pipelines differ across models, prompt lengths across requests, and caching decisions across denoising steps. We present Difflet, a serving engine in which five model pipelines share one compilation backend, joint attention is split across cores by attention head, and a host controller decides at each denoising step whether to run the denoiser or reuse its earlier output.


[Источник](https://arxiv.org/abs/2610.23047)

<!-- url_hash:6978b90b4bc501c2fc068025cdc5247ee47783d12b13385dfb4fc60c1417d8e8 -->


## Recoverability and Verifier Strength: Two Measured Preconditions for Unattended Agent Self-Improvement

_arXiv · 2026-10-20 · score 0.8_

Agent platforms are starting to improve their own agents: they read a deployed agent's execution traces, derive a change, have an automated verifier approve it, and release it with no human author. How much of this loop can safely run without a human?


[Источник](https://arxiv.org/abs/2610.27465)

<!-- url_hash:825130cf8cb2d52ff72a0d11158a685bc7aa0d3d60d3d32cc9501bab6d985068 -->


## The Show-Up Attack: When Subagents Win Over Their Supervisor

_arXiv · 2026-10-20 · score 0.8_

Multi-agent systems are increasingly deployed to coordinate multiple large language model (LLM) agents. However, this also creates new attack surfaces: malicious agents may have chances to exploit the coordination.


[Источник](https://arxiv.org/abs/2610.27574)

<!-- url_hash:f996f95d4c064835c43b09b9bbc10b5033e93f7c6f414dc37eff219433ab6516 -->


## TeCoP: Accelerating Diffusion Large Language Model Decoding via Tentative Context Pipelining

_arXiv · 2026-10-20 · score 0.8_

Diffusion large language models (dLLMs) predict multiple token positions per forward pass, yet block-wise decoders serialize generation and repeatedly recompute stable predictions. We attribute this inefficiency to coupling a prediction's readiness for irreversible commitment with its utility as context.


[Источник](https://arxiv.org/abs/2610.27583)

<!-- url_hash:6d48116db08648aabdd1cea0302cf082bf8c3e6bebed835f75c7b89b4717b5cb -->


## Quantum Mechanics as a Reversible Diffusion Theory

_arXiv · 2026-10-20 · score 0.8_

This paper proposes an interpretation of quantum mechanics, relying on the time-symmetric stochastic dynamics of quantum particles and on non-classical probability theory. Our main purpose is to demonstrate that the wave function and its complex conjugate can be interpreted as complex probability distributions in two complex diffusion equations related to non-real forward and backward in time stochastic motions respectively.


[Источник](https://arxiv.org/abs/2502.10523)

<!-- url_hash:59bb96663d2734c7dc9717ab50d8004bed0682b880920ef172b0131499c3814a -->


## PISA: Piecewise Sparse Attention Is Wiser for Efficient Diffusion Transformers

_arXiv · 2026-10-20 · score 0.8_

Diffusion Transformers are fundamental for video and image generation, but their efficiency is bottlenecked by the quadratic complexity of attention. While block sparse attention accelerates computation by attending only critical key-value blocks, it suffers from degradation at high sparsity by discarding context.


[Источник](https://arxiv.org/abs/2602.01077)

<!-- url_hash:8b6e97eed2f98c707339d5f21fd455b8f14842caae9bdafd91d02e9a207a111e -->


## LSGQuant: Layer-Sensitivity Guided Quantization for One-Step Diffusion Real-World Video Super-Resolution

_arXiv · 2026-10-20 · score 0.8_

One-Step Diffusion Models have demonstrated promising capability and fast inference in video super-resolution (VSR) for real-world. Nevertheless, the substantial model size and high computational cost of Diffusion Transformers (DiTs) limit downstream applications.


[Источник](https://arxiv.org/abs/2602.03182)

<!-- url_hash:6834505886efa99ec818d650db9c8c281e7b72938ef69c82617d27ea9a0e3f64 -->


## SARES-DEIM: Sparse Mixture-of-Experts Meets DETR for Clutter-Aware SAR Ship Detection

_arXiv · 2026-10-20 · score 0.8_

Ship detection in Synthetic Aperture Radar (SAR) imagery is challenged by coherent speckle noise, complex coastal clutter, and the prevalence of small-scale targets. Conventional detectors, primarily designed for optical imagery, often exhibit limited adaptability to SAR-specific degradation and suffer from the loss of fine-grained ship signatures during spatial downsampling.


[Источник](https://arxiv.org/abs/2604.04127)

<!-- url_hash:b9d0f1fef7a086d3f92cecae3c11078e5842dc2aef72ea0132901d119a4e3e09 -->


## Rethinking Cross-Layer Information Routing in Diffusion Transformers

_arXiv · 2026-10-20 · score 0.8_

Diffusion Transformers (DiTs) have become a de facto backbone of modern visual generation, and nearly every major axis of their design -- tokenization, attention, conditioning, objectives, and latent autoencoders -- has been extensively revisited. The residual stream that governs how information accumulates across layers, however, has been directly inherited from the original Transformer.


[Источник](https://arxiv.org/abs/2605.20708)

<!-- url_hash:75f5a7d6b73f759b2ae5b53657d639cbfd8b72df7ed3f573657c76a7e2d385d7 -->


## NVIDIA Spectrum-X: Hardware-Accelerated Multiplane Networking for Large-Scale AI Training

_arXiv · 2026-10-20 · score 0.8_

As distributed model training scales to span hundreds of thousands of GPUs, scale-out networks face unprecedented performance and efficiency demands. NVIDIA Spectrum-X Ethernet has been designed from the ground up to achieve predictable and stable network performance with high utilization and low latency.


[Источник](https://arxiv.org/abs/2605.21187)

<!-- url_hash:f2d084abe7f5217bf36e0a7f2d7d9dfab979e5440680d6200f7088d9ea016c6f -->


## Global Sobolev Convergence of Howard Iteration for Finite-Horizon Controlled Diffusions

_arXiv · 2026-10-20 · score 0.8_

We study Howard policy iteration for finite-horizon stochastic control problems in which the control enters the diffusion coefficient. Each iteration selects a policy by maximizing the Hamiltonian and evaluates it through a linear parabolic equation.


[Источник](https://arxiv.org/abs/2609.15607)

<!-- url_hash:00208f6953d7045d3ad8a1502ebe8559ae430a6bb0f6d1a8d500647fec7a605c -->


## EMERGE: Resolution-Agnostic Point Cloud Generation with Equivariant Graph-Based Diffusion

_arXiv · 2026-10-20 · score 0.8_

Point cloud generation has emerged as a crucial task for accurately capturing and reproducing the complexity of the physical world. However, existing generative approaches, predominantly relying on Transformers and Variational Autoencoders (VAEs), frequently ignore the continuous, non-grid topologies inherent to 3D spaces.


[Источник](https://arxiv.org/abs/2609.26039)

<!-- url_hash:d25e9f616925706316cc46d033e750d3fcedd41aae419289354316afa1a57746 -->


## QwenGyre: An Elastic Reinforcement Learning Framework for Training xLong-Horizon Agents

_arXiv · 2026-10-20 · score 0.8_

Large language model (LLM) agents increasingly undertake extreme-long (xlong) horizon tasks, where a single execution can span hours, hundreds of model--environment interactions, and nearly 1M tokens per rollout. Applying online reinforcement learning (RL) to such executions poses two fundamental challenges: (1) severe execution variance and prolonged rollout delays cause massive GPU idling; and (2) complex non-linear branching generates massive trajectory redundancy, crippling training efficiency.


[Источник](https://arxiv.org/abs/2609.33848)

<!-- url_hash:94ca26797d74be615df666f1994769d5afadae2c8f2b88188199abfa4dfd9f59 -->


## Exploring More, Reasoning Better: Stepwise Risk-Sensitive GRPO for Diffusion Language Models

_arXiv · 2026-10-20 · score 0.8_

Diffusion large language models (dLLMs) generate text by denoising a sequence or successive blocks, allowing several tokens to be revealed in parallel. Reinforcement learning with verifiable rewards (RLVR) reuses terminal feedback across these decisions, even as their conditioning context changes.


[Источник](https://arxiv.org/abs/2610.00661)

<!-- url_hash:f39fbf886dac265cab49441559cf7077cc31913ce7b4a386866ca04306a2e1db -->


## Backend-Agnostic Sparse Attention for Fast High-Resolution Visual Generation

_arXiv · 2026-10-20 · score 0.8_

Diffusion Transformers (DiTs) have achieved strong performance in image and video generation, but the quadratic complexity of full attention makes high-resolution generation computationally expensive. Window attention offers an efficient alternative, yet existing methods face a practical trade-off: partitioned window attention typically achieves computational efficiency consistent with its theoretical complexity.


[Источник](https://arxiv.org/abs/2610.08772)

<!-- url_hash:73153cc74cbbf131787d9708efb81d6644fb5957c73ec20815f3f0b47551fe80 -->


## SAFE-Mem: Secure Agentic Memory with Fine-Grained Authority and Governance-Aware Retrieval

_arXiv · 2026-10-20 · score 0.8_

Large language model (LLM) agents increasingly rely on persistent memory to support long-term reasoning and personalized interactions. However, information collected from external sources can introduce security risks when untrusted claims (i.e., atomic statements) are later treated as authorized preferences, policies, or permissions.


[Источник](https://arxiv.org/abs/2610.22959)

<!-- url_hash:f3bf282b1623b9184ddc428897f619e2e594edc882fdf0184c4173d2299860c2 -->


## TamedFlow: Trajectory-Aware Distillation for Teacher-Assisted Diffusion Sampling

_arXiv · 2026-10-20 · score 0.8_

Diffusion Transformers (DiTs) deliver high-fidelity image and video generation, but inference requires many sequential model evaluations. Two acceleration strategies are increasingly important: model compression makes each evaluation cheaper, while adaptive inference avoids selected teacher computation through reuse, forecasting, or speculative execution.


[Источник](https://arxiv.org/abs/2610.26025)

<!-- url_hash:8a61b631202cef9016b99f28e772d5c5fa7767b60714c2daadbcd27e02981dff -->


## HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs

_arXiv · 2026-10-20 · score 0.8_

Harness development plays a crucial role in building capable AI agents. Recent approaches improve harnesses through recursive self-improvement (RSI), but their performance gains often come with higher execution costs.


[Источник](https://arxiv.org/abs/2610.26770)

<!-- url_hash:2870028c1b5185065816cc991a2cb0282bf516fe403747d763c842110a5cec5b -->


## Beyond Experience: Knowledge-Guided Evolution for NPU Kernel Generation

_arXiv · 2026-10-20 · score 0.8_

LLM agents have become capable kernel engineers on mainstream GPU stacks, but they struggle on emerging accelerators such as Ascend NPUs, whose programming model is barely represented in pretraining data. Recent NPU agents address this gap largely through experience: they accumulate memory from their own generation and optimization trials and reuse it on later tasks.


[Источник](https://arxiv.org/abs/2610.27588)

<!-- url_hash:0d5e72a763fbb4b0f5defe96ce259f1c3c789e8de69a12a07ec3d04dfa5953a6 -->


## WaveSpec: Multi-Spectral Iris Presentation Attack Detection via Wavelength-Conditioned Spectral Coherence Adaptation

_arXiv · 2026-10-20 · score 0.8_

Multispectral iris presentation attack detection benefits from observing the same iris across multiple near-infrared wavelengths, but existing methods often use wavelength information mainly for conditioning or fusion. This can limit their ability to explicitly model whether the spectral response of a sample is coherent across bands.


[Источник](https://arxiv.org/abs/2610.27608)

<!-- url_hash:e985fc0d10aa7a9409c140bc3074c95a1c62bea46e163a423a54177e752c51ba -->


## Standards-Guided and Dependency-Aware Code-Level Documentation Generation

_arXiv · 2026-10-20 · score 0.8_

Automatically generating high-quality documentation for software repositories remains challenging: existing approaches largely treat documentation as unconstrained text generation, lacking explicit quality specifications, depending heavily on long-context prompts over raw code, and offering limited support for reproducible evaluation. We argue that code-level documentation generation should instead be a standards-guided software engineering task, in which documentation is generated and assessed against explicit, reusable quality requirements derived from authoritative standards.


[Источник](https://arxiv.org/abs/2610.27634)

<!-- url_hash:cb30d2361a3a91b74246733a0024b8bb1f0910a6f8ee76f1890c21bb56fa1ff4 -->


## RSI Control: Can AI Models Perform Covert Sabotage in the Self-Improvement Process?

_arXiv · 2026-10-20 · score 0.8_

Recursive self-improvement, in which frontier AI models work on training the next generation, is quickly becoming a reality. However, the safety of this process has received far less attention than it should.


[Источник](https://arxiv.org/abs/2610.27735)

<!-- url_hash:1a1408327520a27be5d4bcf6adefa8db2b3c82dd10feb7a60f0b278c35347f09 -->


## PixelSR: Pixel-Space Orthogonal Flow Decoupling for Real-World Image Super-Resolution

_arXiv · 2026-10-20 · score 0.8_

Latent diffusion models have recently achieved remarkable progress in Real-world Image Super-Resolution (Real-SR). However, existing methods consistently exhibit a persistent seesaw effect: enhancing perceptual realism compromises structural fidelity.


[Источник](https://arxiv.org/abs/2610.27759)

<!-- url_hash:3950f239bbbb80f071c2ac77a1cb02d6a50b35726cc177daa5f78bb63bbdb9d1 -->


## Frontier LLMs Enter the World of Robotics: A Cross-Model Evaluation on RoboColiseum

_arXiv · 2026-10-20 · score 0.8_

Recent studies have explored the potential of multimodal large language models for robot control, yet the models' embodied capabilities remain insufficiently characterized across models, tasks, and execution settings. We conduct a multidimensional comparative evaluation on RoboColiseum across four tracks: Instruction Following, Spatial Reasoning, General Manipulation, and Robustness.


[Источник](https://arxiv.org/abs/2610.27865)

<!-- url_hash:0eb7a3aa83372f3fd390b7edcfdb7ce63c7fcb6777e24114ac32e880c53a87d0 -->


## How Developers Configure LLM Inference: A Large-Scale Study of Real-World Practices

_arXiv · 2026-10-20 · score 0.8_

LLMs are increasingly integrated into software systems, making deployment and inference configuration a recurring software engineering task. Inference backends expose many options that affect model loading, generation, serving, and request processing.


[Источник](https://arxiv.org/abs/2610.27945)

<!-- url_hash:96fd12dff486dbf9fe0b6ed089dfab184c616fa1c9caa5634151649fc746c0df -->


## Recast the Past: Stable Long Video Generation with Full Context Memory

_arXiv · 2026-10-20 · score 0.8_

Long-horizon video generation requires retaining an ever-expanding history, but conditioning on its growing token sequence is costly. Existing methods restrict or compress historical context, potentially losing information needed for future generation.


[Источник](https://arxiv.org/abs/2610.27986)

<!-- url_hash:ef620805445528ac9d27121d687b653478d9d8e45fac98371f0ae4a2e38e65d0 -->


## Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds

_arXiv · 2026-10-20 · score 0.8_

Moving from controllable videos to genuinely playable worlds requires persistent world state, executable game rules, and low-latency interaction. We outline a roadmap for the next generation of Matrix-Game that separates game execution from visual generation through an executable game harness, and introduce Matrix-Game 4.0 as the first system built on this design.


[Источник](https://arxiv.org/abs/2610.27999)

<!-- url_hash:a91b664b17af96a7115b1aa449a098c5c3b9654897b8906f8facf90a3c2f5a33 -->


## RANGER: Retrieval Agent for Navigating Graphs with Semantic Evaluation Rewards

_arXiv · 2026-10-20 · score 0.8_

The integration of Large Language Models and Reinforcement Learning offers a promising direction for complex sequential decision-making tasks, such as multi-hop question answering over knowledge graphs. While LLMs provide strong semantic understanding and reasoning capabilities, they often struggle with precise, multi-step navigation in structured environments.


[Источник](https://arxiv.org/abs/2610.28010)

<!-- url_hash:f5fb54f0bcdf38f5597aca9305f8beeebdec3fe292d5df8656e416c5e65e7dad -->


## MoDDiT: Simple Token Routing in Diffusion Transformers

_arXiv · 2026-10-20 · score 0.8_

Real-time video generation, interactive world models, and on-device image synthesis are almost a reality. Diffusion Transformers (DiT) achieve excellent sample quality, shifting the bottleneck to the throughput of the models themselves.


[Источник](https://arxiv.org/abs/2610.28086)

<!-- url_hash:28f4e146d4d036749847a4319039bea63ebfe72f107698b59ea6ff84163b9ae1 -->
