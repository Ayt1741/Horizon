---
layout: post
title: "Выпуск 2026-06-06 (RU)"
date: 2026-06-06 09:00:00 +0000
lang: ru
---

# Выпуск 2026-06-06


## [r/LocalLLaMA] dvlt.cu: inference engine written from scratch in CUDA/C++ for NVIDIA's DVLT 3D transformer model

_Reddit r/LocalLLaMA · 2026-06-06 · score 0.825_

Im into both HPC and 3D reconstruction, so I built this as a side project. [`dvlt.cu`](http://dvlt.cu) `is a single 5MB binary:` \- No python, torch, TF, ONNX, llama.cpp, vLLM, or huggingface runtime \- Nearly no dependencies: only cuBLASLt (shipped with libcuda ) + cuTLASS ( header only lib ) \- mmap'd bf16 weights, one bulk GPU upload, static dims, one-shot arena, deterministic \- Weights (117M Params) are NVIDIA's (non-commercial), fetched separately at setup.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1tyu79c/dvltcu_inference_engine_written_from_scratch_in/)

<!-- url_hash:460202925a34e7f51618329fe4f07d2d8ddb92758367d2fd6d9ec4c33e010d8f -->


## [r/LocalLLaMA] Built a local-first roleplay client where third-party MCP servers expose lore as canon-equivalent retrieval

_Reddit r/LocalLLaMA · 2026-06-06 · score 0.8_

I've been building [Chronicler](https://github.com/yantrikos/chronicler) — a local-first roleplay/character-chat client. Self-hosted (docker compose up), works with any OpenAI-compat endpoint (Ollama, llama.cpp server, vLLM, OpenRouter, nano-gpt), all data stays on your machine.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1tyrmfd/built_a_localfirst_roleplay_client_where/)

<!-- url_hash:12e009a48d8833d11426f554fa364ad175695b413a2c6bdd00be88076f9751f6 -->


## [r/LocalLLaMA] 120 tok/s on 12GB VRAM with Gemma 4 12B QAT MTP

_Reddit r/LocalLLaMA · 2026-06-06 · score 0.8_

Google just released the QAT (Quantization-Aware Training) variant of their Gemma 4 models, including 12B, so it was only natural for me to benchmark it on my 12GB GPU since it fits entirely in VRAM. I was pleasantly surprised of the result!


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1typjmc/120_toks_on_12gb_vram_with_gemma_4_12b_qat_mtp/)

<!-- url_hash:d4337ae0a3c3efab8d3eb55e44e556cc897d22edf5d20b9e48c2f1062ea4d33c -->
