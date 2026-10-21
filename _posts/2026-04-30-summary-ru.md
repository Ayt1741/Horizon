---
layout: post
title: "Выпуск 2026-04-30 (RU)"
date: 2026-04-30 09:00:00 +0000
lang: ru
---

# Выпуск 2026-04-30


## [r/MachineLearning] Applying Karpathy's autoresearch to a 33M-token public transit dataset (14% improvement, replication notes) [P]

_Reddit r/MachineLearning · 2026-04-30 · score 0.85_

Hello r/MachineLearning! I work in the US transit industry and I went all-in on learning AI & ML a few months ago. When I heard about Andrej Karpathy's autoresearch framework, I thought it was really cool. I decided to use the same transit dataset from an earlier GPT-2 XL fine-tuning project to train a small 80M model from scratch. Autoresearch is designed for from-scratch pretraining (not fine-tuning) so I started a new project rather than retrofitting the GPT-2 XL one. I would love to hear from you … 1. Where did I mess up? 2. What’s interesting here? 3. What should I focus on learning? What...


[Источник](https://www.reddit.com/r/MachineLearning/comments/1t04rrz/applying_karpathys_autoresearch_to_a_33mtoken/)

<!-- url_hash:9595f577e18029658d00e3424a9ba28a8dda6b4a45f45ac8e7387eba3c262a5e -->


## [r/artificial] Anthropic mass shipped 9 connectors and accidentally leaked their entire creative industry strategy

_Reddit r/artificial · 2026-04-30 · score 0.85_

The announcement yesterday was genuinely significant and i don't think most people outside the creative industry understand why. Anthropic released 9 connectors that let claude directly control professional creative software through mcp which means actually execute actions inside them the full list contains adobe creative cloud (50+ apps including photoshop, premiere, illustrator), blender (full python api access for 3d modeling), autodesk fusion , ableton, splice , affinity by canva , sketchup , resolume (), and claude design.


[Источник](https://www.reddit.com/r/artificial/comments/1szoe78/anthropic_mass_shipped_9_connectors_and/)

<!-- url_hash:bd15ab654810848046efb1be462d70d109e178bbbea23bdab111e3f5f2e41470 -->


## [r/LocalLLaMA] Cuda + ROCm simultaneously with -DGGML_BACKEND_DL=ON !

_Reddit r/LocalLLaMA · 2026-04-30 · score 0.825_

I invested quite a bit of time and it wasn't easy but finally I can run models like Minimax 2.7 Q4 using Cuda+ROCm at the same time bypassing Vulkan. load\_tensors: offloaded 63/63 layers to GPU load\_tensors: CUDA0 model buffer size = 83650.42 MiB load\_tensors: CUDA\_Host model buffer size = 622.76 MiB load\_tensors: ROCm0 model buffer size = 40314.35 MiB the main advantage is the prefill.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1t0bkaf/cuda_rocm_simultaneously_with_dggml_backend_dlon/)

<!-- url_hash:da2c485e8334b20d09d9010dacc929c9ceb097dc2a0cb2a6800f76a6a22bdbc2 -->


## [r/LocalLLaMA] Final Monster: 32x AMD MI50 32GB at 9.7 t/s (TG) & 264 t/s (PP) with Kimi K2.6

_Reddit r/LocalLLaMA · 2026-04-30 · score 0.825_

[32 MI50 32GB setup](https://preview.redd.it/8186petvjeyg1.jpg?width=600&format=pjpg&auto=webp&s=ad67f085d0a1df0a207f4750ed688958378cf178) **moonshotai/Kimi-K2.6 int4 @ 9.7 tok/s** (output of 136 tok) and **263 tok/s** (input of 14564 tok) on **vllm-gfx906-mobydick** **Github link of vllm fork**: [https://github.com/ai-infos/vllm-gfx906-mobydick](https://github.com/ai-infos/vllm-gfx906-mobydick) **Power draw**: \~640W (idle) / \~4800W (peak inference) **Is it worth ? No, unless you’ve got solar panels or free energy…** **Setup details:** **That’s just 2 nodes of 16 GPU that i plugged together with 10G cable ethernet.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1t0b0ie/final_monster_32x_amd_mi50_32gb_at_97_ts_tg_264/)

<!-- url_hash:0cb51b079c1ee57c99911895c91cda63b9f685de24efeb6e7348c831ecdc1aab -->


## [r/OpenAI] I pitted different LLMs against each other in Pokemon Showdown

_Reddit r/OpenAI · 2026-04-30 · score 0.825_

I wanted to see if LLMs could reason through complex game states, so I built a system where they can play Pokémon Showdown battles autonomously. They get the battle state every turn and use tool calls to attack or switch.


[Источник](https://www.reddit.com/r/OpenAI/comments/1t094tj/i_pitted_different_llms_against_each_other_in/)

<!-- url_hash:0fe0ef3281b37b0b72ea2673660002cbfa35af38386ea3a5a64389645ba34561 -->


## [r/MachineLearning] I finally sat down and did the math on my Cloud LLM bills… and I’m moving almost everything to a 4090. [R]

_Reddit r/MachineLearning · 2026-04-30 · score 0.825_

I used to be all-in on cloud APIs. For any side project, I’d just grab an OpenAI or Anthropic key and not think twice. It was convenient. No worrying about VRAM, super fast responses, and I could spin something up in minutes. But that “pay-as-you-go” comfort slowly turned into real pain. Last month one of my small RAG tools that I built for a few friends racked up $120 in API costs. Then an experimental agent I left running in a loop hit $450. That was the moment I opened a spreadsheet and realized I was basically burning money every time someone used my stuff. The numbers that really shocked ...


[Источник](https://www.reddit.com/r/MachineLearning/comments/1szqz1o/i_finally_sat_down_and_did_the_math_on_my_cloud/)

<!-- url_hash:7b04f3dbe90b9c53bc5195e17d73494f6bb37c5c5edad92b577a04ea61f91a38 -->


## [r/LocalLLaMA] Best RTX Pro 6000 vllm settings?

_Reddit r/LocalLLaMA · 2026-04-30 · score 0.8_

Just got myself (for my company) a RTX Pro 6000 Blackwell Workstation card. Managed to get really good TPS on qwen3 27b fp8. Using it for many agents that specialize on one specific task at a time. Trying to get the best possible Speed + Concurrency running on vllm 0.20.1 nightly cuda 13.1. Engine 000: Avg prompt throughput: 763.5 tokens/s, Avg generation throughput: 1320.2 tokens/s, Running: 28 reqs, Waiting: 0 reqs, GPU KV cache usage: 50.4%, Prefix cache hit rate: 1.3%, MM cache hit rate: 0.0% (APIServer pid=00000) INFO 04-30 19:20:02 \[metrics.py:101\] SpecDecoding metrics: Mean acceptance...


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1t0blfg/best_rtx_pro_6000_vllm_settings/)

<!-- url_hash:79dee1bfe539cd703732022b3c3b974c28eec51d98d0ffa0d9ebc019098cd413 -->


## [r/OpenAI] 49 years ago Asimov wrote a story about a matchmaking AI. Can I finally expect this?

_Reddit r/OpenAI · 2026-04-30 · score 0.8_

Seriously, if any AI company wanted my money, they would release an agent to handle my dating life (something I've proven deeply inept at). Thinking about the programing requirements (something I'm pretty good at), this seems doable.


[Источник](https://www.reddit.com/r/OpenAI/comments/1t09qcq/49_years_ago_asimov_wrote_a_story_about_a/)

<!-- url_hash:118bfc2edefa93fada1909650663f8e9865b9779f1343aecae08d4c5d73d34c2 -->


## [r/LocalLLaMA] Stateless LLM agents cause ~20% double-refunds in payment flows — here's a structural fix (benchmark)

_Reddit r/LocalLLaMA · 2026-04-30 · score 0.8_

Hey r/LocalLLaMA, I've been working on \*\*llm-nano-vm\*\* — not just another agent helper, but an \*execution model\* for LLM pipelines. Just released v0.5.0.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1t060qf/stateless_llm_agents_cause_20_doublerefunds_in/)

<!-- url_hash:a8072f729c04b093e554ed002ebf3b51b402a71ed1eb5de47ed6ce4662c6b6db -->


## [r/LocalLLaMA] Terminal Bench score for Mistral 3.5 Medium

_Reddit r/LocalLLaMA · 2026-04-30 · score 0.8_

So... there were a couple promising benchmark scores reported by mistralai in the model card for Mistral 3.5 Medium, BUT there wasn't the one that I usually care about the most, which is TerminalBench 2.0.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1t00fkh/terminal_bench_score_for_mistral_35_medium/)

<!-- url_hash:21a8334128c7e3737418d0242c611212da84e0d8ebecbdc896c8f55a7783f2fe -->


## [r/artificial] Why v2 of my trading system strips the LLM of its execution rights (Blueprint & Architecture)

_Reddit r/artificial · 2026-04-30 · score 0.8_

Thanks to the incredible feedback on my last post, I’m officially moving away from the "distributed veto" system (where 8 LLM agents argue until they agree to trade). For v2, I am implementing a strict State Machine using a deterministic runtime (llm-nano-vm).


[Источник](https://www.reddit.com/r/artificial/comments/1szs9vh/why_v2_of_my_trading_system_strips_the_llm_of_its/)

<!-- url_hash:94eac603785e05411930145aa5a323522de0ef3ff3dcb0f35586ba3407578a24 -->
