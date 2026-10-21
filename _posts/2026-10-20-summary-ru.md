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
