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