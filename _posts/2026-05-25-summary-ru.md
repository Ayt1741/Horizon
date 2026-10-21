---
layout: post
title: "Выпуск 2026-05-25 (RU)"
date: 2026-05-25 09:00:00 +0000
lang: ru
---

# Выпуск 2026-05-25


## DiSC: Resolution-Scalable Acceleration of Diffusion Models by Exploiting Sparsity and Cached Token Reuse with Hash-based Distribution

_arXiv · 2026-05-25 · score 0.85_

Transformer-based diffusion models offer superior scalability and performance but suffer from high computational overhead due to the iterative nature and quadratic complexity of self-attention at high resolutions. In this paper, we propose DiSC, a resolution-scalable, sparsity-aware hardware accelerator.


[Источник](https://arxiv.org/abs/2605.25798)

<!-- url_hash:eb36469ec955d876d64c428cb53c53ee355930db77e44575a34d0c12e6286321 -->


## A Comprehensive Dataset for Human vs. AI Generated Text Detection

_arXiv · 2026-05-25 · score 0.825_

The rapid advancement of large language models (LLMs) has led to increasingly human-like AI-generated text, raising concerns about content authenticity, misinformation, and trustworthiness. Addressing the challenge of reliably detecting AI-generated text and attributing it to specific models requires large-scale, diverse, and well-annotated datasets.


[Источник](https://arxiv.org/abs/2510.22874)

<!-- url_hash:0ffb34529b303afd13246725493dba37821f6321f316f39ecd66948629158ce3 -->


## DisagFusion: Asynchronous Pipeline Parallelism and Elastic Scheduling for Disaggregated Diffusion Serving

_arXiv · 2026-05-25 · score 0.825_

Diffusion-based generation is increasingly powering production content pipelines; however, deploying these models at scale remains a significant challenge. Model weights frequently exceed the memory capacity of commodity GPUs, while the encoder, diffusion transformer (DiT), and decoder stages exhibit highly imbalanced computational and memory footprints.


[Источник](https://arxiv.org/abs/2605.25550)

<!-- url_hash:555613eedf209884e17f048c443f8bbb20dd9f01caf5af6931916ca0bf39716b -->


## TIE: Time Interval Encoding for Video Generation over Events

_arXiv · 2026-05-25 · score 0.825_

Director-style prompting, robotic action prediction, and interactive video agents demand temporal grounding over concurrent events -- a regime in which 68% of general clips and over 99% of robotics/gameplay clips contain overlapping events, yet existing multi-event generators rest on a single-active-prompt assumption. However, modern video generators, such as Diffusion Transformers (DiT), represent time as discrete points through point-wise positional encodings.


[Источник](https://arxiv.org/abs/2605.10543)

<!-- url_hash:afcbf677e3781c5074627065258547363c9e72298ef1c83e15167f82865605ee -->


## SONAR-LLM: Autoregressive Transformer that Thinks in Sentence Embeddings and Speaks in Tokens

_arXiv · 2026-05-25 · score 0.825_

The recently proposed Large Concept Model (LCM) generates text by predicting a sequence of sentence-level embeddings and training with either mean-squared error or diffusion objectives. We present SONAR-LLM, a decoder-only transformer that "thinks" in the same continuous SONAR embedding space, yet is supervised through token-level cross-entropy propagated via the frozen SONAR decoder.


[Источник](https://arxiv.org/abs/2508.05305)

<!-- url_hash:c202f2286ed335c3e0455eea14f710787730da33e6ec0647a953e28e27acfee6 -->


## Benchmarking and Learning Real-World Customer Service Dialogue

_arXiv · 2026-05-25 · score 0.8_

Existing benchmarks and training pipelines for industrial intelligent customer service (ICS) remain misaligned with real-world dialogue requirements, overemphasizing verifiable task success while under-measuring subjective service quality and realistic failure modes, leaving a gap between offline gains and deployable dialogue behavior. We close this gap with a benchmark-to-optimization loop: we first introduce OlaBench, an ICS benchmark spanning retrieval-augmented generation, workflow-based systems, and agentic settings, which evaluates service capability, safety, and latency sensitivity; moreover, motivated by OlaBench results showing state-of-the-art LLMs still fall short, we propose OlaM


[Источник](https://arxiv.org/abs/2510.22143)

<!-- url_hash:5cd90b741418a67661771ab97b56cb6bbe73e1de66fb96ce2918d3f38348849f -->


## MEMTIER: Tiered Memory Architecture and Retrieval Bottleneck Analysis for Long-Running Autonomous AI Agents

_arXiv · 2026-05-25 · score 0.8_

Long-running autonomous AI agents suffer from a well-documented memory coherence problem: tool-execution success rates degrade 14 percentage points over 72-hour operation windows due to four compounding failure modes in existing flat-file memory systems. We present MEMTIER, a tripartite memory architecture for the OpenClaw agent runtime that introduces a structured episodic JSONL store, a five-signal weighted retrieval engine, an attention-attributed cognitive weight update loop, an asynchronous consolidation daemon promoting episodic facts to a semantic tier, and a PPO-based policy framework for adapting retrieval weights (infrastructure validated; performance gains pending camera-ready).


[Источник](https://arxiv.org/abs/2605.03675)

<!-- url_hash:2319d97409906edaa78779ec96a03ed342fbf96e947f009e854d3e09410bdc57 -->


## BacktestBench: Benchmarking Large Language Models for Automated Quantitative Strategy Backtesting

_arXiv · 2026-05-25 · score 0.8_

Quantitative backtesting is essential for evaluating trading strategies but remains hampered by high technical barriers and limited scalability. While Large Language Models (LLMs) offer a transformative path to automate this complex, interdisciplinary workflow through advanced code generation, tool usage, and agentic planning, the practical realization is significantly challenged by the current lack of a large-scale benchmark dedicated to automated quantitative backtesting, which hinders progress in this field.


[Источник](https://arxiv.org/abs/2605.17937)

<!-- url_hash:89bcaacfa3fdf493e28d33a9db2648e2f2c6d9d1989922ce601de3d1a7b104a6 -->


## Findings of the Counter Turing Test: AI-Generated Text Detection

_arXiv · 2026-05-25 · score 0.8_

The growing capability of large language models to produce fluent, contextually coherent text has created mounting pressure on the systems and institutions responsible for ensuring the authenticity of digital content. Advanced generative models such as GPT-4, Claude 3.5, and Llama can produce highly coherent and human-like text, making it increasingly difficult to differentiate between human-written and AI-generated content.


[Источник](https://arxiv.org/abs/2605.20761)

<!-- url_hash:799ebd20bcf94d0e9e3a7b5f896af7fe01cc215362a39c40d0eeef6e52454c54 -->


## Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving

_arXiv · 2026-05-25 · score 0.8_

End-to-end autonomous driving via Vision-Language-Action (VLA) models demands a precarious balance between high-fidelity trajectory planning and efficient inference. Existing paradigms typically fall short: autoregressive (AR) VLAs are memory-bandwidth-bound on edge hardware and prone to exposure-bias drift, while full-sequence diffusion models preclude KV-cache reuse and suffer from "logical leakage" that violates the fundamental perceive-then-plan causality.


[Источник](https://arxiv.org/abs/2605.23163)

<!-- url_hash:d2083769e34589b10c252c9e24c30da06bba94507f419af08442b7743e033228 -->


## Evo-Attacker: Memory-Augmented Reinforcement Learning for Long-Horizon Tool Attacks on LLM-MAS

_arXiv · 2026-05-25 · score 0.8_

While Large Language Model-based Multi-Agent Systems (LLM-MAS) demonstrate remarkable capabilities in solving complex tasks by orchestrating specialized agents and external tools, the implicit trust in tool outputs creates a critical attack surface. Existing tool attacks are limited by domain specificity or fixed and static templates.


[Источник](https://arxiv.org/abs/2605.25389)

<!-- url_hash:4407d48a99ffd89374545145a2dee60d526874e2f0befa9b677998be036169f9 -->


## Security of OpenClaw Agents: Fundamentals, Attacks, and Countermeasures

_arXiv · 2026-05-25 · score 0.8_

The rapid evolution of large language model (LLM)-driven autonomous agents has given rise to OpenClaw, a new class of open-source agent frameworks that operate as continuously running, skill-augmented systems with persistent memory, multi-channel interaction, and high degrees of autonomy. Such capabilities enable OpenClaw agents to autonomously execute complex, multi-step tasks and interact seamlessly with external applications, but simultaneously introduce a substantially enlarged attack surface.


[Источник](https://arxiv.org/abs/2605.25435)

<!-- url_hash:555507780c6930f7eff9c1061175f2306d453f7d34006f7a228c3d7ad9c4c2e6 -->


## Enhancing Single-Image Facial Demorphing using Multimodal Large Language Models

_arXiv · 2026-05-25 · score 0.8_

Face recognition systems are increasingly vulnerable to morphing attacks, where a composite image is crafted to match multiple identities, enabling unauthorized access and identity fraud. Existing detection methods identify morphed images but cannot recover constituent images or identities, limiting their forensic utility.


[Источник](https://arxiv.org/abs/2605.25442)

<!-- url_hash:b00d285b03b5f3160a00081fa8c473604868735d5cc783048d23c9e70161a724 -->


## AI Content Moderation in Therapy Conversations

_arXiv · 2026-05-25 · score 0.8_

Large language models (LLMs) are increasingly being used for emotional support. They are also being developed for formal therapy purposes. However, LLMs like ChaptGPT or Llama are often developed with content moderation guardrails that prevent them from discussing sensitive subjects with users for both liability and safety purposes, and this inability to broach these subjects may affect their capacity as therapists. In this study, we perform an algorithm audit on three state-of-the-art moderation systems (OpenAI's moderation endpoint, Meta's Llama Guard, and Google's Shield Gemma) to investiga...


[Источник](https://arxiv.org/abs/2605.25454)

<!-- url_hash:46bd2ccb4e90813647d52ea73779565e1b4d604b850ea0d110f3d771e341a84e -->


## RepSAM: Bridging Foundation Models to Robotic Vision via Representation-Guided Adaptation

_arXiv · 2026-05-25 · score 0.8_

Robotic perception in unstructured environments remains challenging despite the zero-shot capabilities of foundation models such as SAM. This work attributes performance degradation to non-uniform representation shifts across transformer layers: shallow layers exhibit substantial domain gaps (CKA 0.7).


[Источник](https://arxiv.org/abs/2605.25495)

<!-- url_hash:bc319b5a1bf4e170db0deddd1f25f313a898ab9bd92479a695f1562a86efb351 -->


## DriveGen3D: Boosting Feed-Forward Driving Scene Generation with Efficient Video Diffusion

_arXiv · 2026-05-25 · score 0.8_

We present DriveGen3D, a novel framework for generating high-quality and highly controllable dynamic 3D driving scenes that addresses critical limitations in existing methodologies. Current approaches to driving scene synthesis either suffer from prohibitive computational demands for extended temporal generation, focus exclusively on prolonged video synthesis without 3D representation, or restrict themselves to static single-scene reconstruction.


[Источник](https://arxiv.org/abs/2510.15264)

<!-- url_hash:cdf55519707e5239dfddadb0f52a6b636644540665fe9edb425700b2cca1f723 -->


## Findings of the Counter Turing Test: AI-Generated Image Detection

_arXiv · 2026-05-25 · score 0.8_

The rapid advancements in generative AI technologies, such as Stable Diffusion, DALL-E, and Midjourney, have significantly transformed the creation of synthetic visual content. While these models enable innovation across industries, they also pose serious challenges, including misinformation, disinformation, and biased content generation.


[Источник](https://arxiv.org/abs/2605.20787)

<!-- url_hash:5658af8782152dc13907c1050ff89d15d31c5b4820cd78baf901b756e9720b15 -->


## Therm-FM: Foundation Model is ALL YOU NEED for 3D-ICs Thermal Simulation

_arXiv · 2026-05-25 · score 0.8_

Data-driven thermal predictors for 3D-ICs are often trained from scratch for each chip design using many high-fidelity finite-element simulations, leading to high data-generation cost and costly cross-design reuse. We propose Therm-FM, a neural operator framework that adapts a pretrained partial differential equation (PDE) foundation model to steady-state and transient 3D-IC thermal simulation.


[Источник](https://arxiv.org/abs/2605.22663)

<!-- url_hash:8559bb856c1ccd7377479c6fde4909be885065583a97f8e51f11530d17ce702b -->


## Bandwidth-Aware LLM Inference on Heterogeneous Many-Core Supercomputers

_arXiv · 2026-05-25 · score 0.8_

Large language model (LLM) inference is limited by high computational cost and memory bandwidth demands, making deployment on heterogeneous many-core processors challenging. Taking the MT-3000 processor used in the Tianhe supercomputer as an example, its limited main-memory bandwidth and distributed memory hierarchy exemplify these bottlenecks, making it difficult to directly migrate existing GPU-based inference frameworks.


[Источник](https://arxiv.org/abs/2605.25655)

<!-- url_hash:6fa14ac19100d4077af830276cd270a0bc917873381b0567a858171b6ce46767 -->


## Profiling-Driven Adaptive Distributed Transformer Inference on Embedded Edge Deployment

_arXiv · 2026-05-25 · score 0.8_

Distributing Transformer inference across embedded edge devices can alleviate individual memory and compute constraints, yet practical benefits on real hardware remain unclear: prior work relies largely on simulations that overlook hardware-specific communication overheads. We present a hardware prototype study on NVIDIA Jetson Orin Nano devices connected over WiFi.


[Источник](https://arxiv.org/abs/2605.25682)

<!-- url_hash:ca80874eb0adaafccc3a968a523182c42029ab3f34150c5c881753ffe7f5f905 -->


## Agent-Centric Social Trajectory Prediction: A Free Energy Principle Perspective

_arXiv · 2026-05-25 · score 0.8_

Trajectory prediction methods have demonstrated remarkable capabilities in capturing complex motion patterns. However, existing methods rely on global state assumptions, suffer from insufficient belief inference under partial observability, and lack cognitive behavioral constraints in prediction.


[Источник](https://arxiv.org/abs/2605.25748)

<!-- url_hash:358014fc037f9ed59419e0129ad1cfe395dafb4c7e1fc543b1d76b733ffbcde8 -->


## Where Concept Erasure Should Occur: Concept-Layer Alignment in Text-to-Video Diffusion Models

_arXiv · 2026-05-25 · score 0.8_

Text-to-video diffusion transformers encode semantic information unevenly across model depth, which constrains effective concept erasure. We identify a representational bottleneck, termed concept-layer topological alignment, under which target concepts exhibit higher separability at certain representational depths.


[Источник](https://arxiv.org/abs/2605.25941)

<!-- url_hash:30c36f4cec5489d24c7ca7b23678810c9ac8d33f838c16507792598833db0dfa -->


## Triplet-Block Diffusion RWKV

_arXiv · 2026-05-25 · score 0.8_

Causal Transformer language models suffer from strictly sequential decoding and a quadratic per-step attention cost. While linear-time causal models and discrete diffusion models each address these weaknesses, their integration remains inherently inconsistent: diffusion requires bidirectional attention, while causal models are unidirectional.


[Источник](https://arxiv.org/abs/2605.25969)

<!-- url_hash:039fbba03c3d96c57814726f2f6d8fa254ffeb282a2331dbb96e48980dec06b0 -->


## What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA

_arXiv · 2026-05-25 · score 0.8_

Medical RAG needs evidence-grounded claims, so plugging a claim-level NLI checker into retrieval-augmented RL is intuitive. \textbf{We find that the checker's \emph{output distribution} during training, not its held-out accuracy, decides whether it provides trainable gradient.} We compare four NLI checker back-ends as process rewards inside a GRPO-trained medical RAG agent (Qwen2.5-7B, replicated on Qwen3-4B and Llama-3.1-8B) across four held-out medical QA benchmarks.


[Источник](https://arxiv.org/abs/2605.25988)

<!-- url_hash:5d22d1ee890b496b5cdd380e5ffe49bbb73c4737d0ae58418db2a7d2e315f8da -->


## Trustworthy Software Project Generation : a Case Study with an Interactive Theorem Prover

_arXiv · 2026-05-25 · score 0.8_

Generating code from natural-language requirements has become a primary route for LLM-assisted software development. Although LLMs can successfully complete small programming tasks, generating an entire complex project remains unreliable because subtle errors may survive compilation and testing.


[Источник](https://arxiv.org/abs/2605.26017)

<!-- url_hash:f22e5584918b56eb7bb7b4e4e99912a633165a930989113e8a0c27fe98a9952c -->


## Looped Diffusion Language Models

_arXiv · 2026-05-25 · score 0.8_

Masked diffusion models (MDMs) have emerged as a promising alternative to autoregressive models for language modeling, yet the effective design of transformer architectures for MDMs remains underexplored. In this paper, we show that selectively looping the early-middle transformer layers significantly improves both training efficiency and model performance in MDMs.


[Источник](https://arxiv.org/abs/2605.26106)

<!-- url_hash:488679448013b8a4123f11c2287bcbcedb926b993a157a831141f2db61d45235 -->


## Squeezing Capacity from Multimodal Large Language Models for Subject-driven Generation

_arXiv · 2026-05-25 · score 0.8_

Subject-driven image generation aims to synthesize new images that preserve the identity of the given subject while following textual instructions. Existing approaches often encode text and reference images separately.


[Источник](https://arxiv.org/abs/2605.26111)

<!-- url_hash:af350ba0d68bcfb76ee59dcf3553790ae7e1dbb0194f52c824e3c05692d7685b -->


## From Model Scaling to System Scaling: Scaling the Harness in Agentic AI

_arXiv · 2026-05-25 · score 0.8_

This paper studies the next major bottleneck in agentic AI as system scaling, not only model scaling: the design of auditable, persistent, modular, and verifiable architectures around foundation models. We refer to this shift as scaling the harness: treating the structured execution layer around a foundation model as a first-class object of design, evaluation, and optimization.


[Источник](https://arxiv.org/abs/2605.26112)

<!-- url_hash:80b4d5d598a4182215d903dfcf0b2f6b9feec61ff81b10d63416c5d17314ea5b -->


## AnyScene: Towards Highly Controllable Driving Scene Generation at Anywhere and Beyond

_arXiv · 2026-05-25 · score 0.8_

Generating high-fidelity and controllable synthetic data is critical for advancing end-to-end autonomous driving, particularly for addressing the long tail of rare safety-critical scenarios. Existing occupancy-guided methods typically rely on shallow conditioning mechanisms and reference-frame-dependent video synthesis, which limits fine-grained controllability from arbitrary BEV layouts and restricts their applicability for scalable simulation.


[Источник](https://arxiv.org/abs/2605.26113)

<!-- url_hash:ae3933074d2087e466889952bad1b2f8ffc61de6cc1686c8511d314b6684df63 -->


## AgentSociety: Incentivizing Agentic Social Intelligence

_arXiv · 2026-05-25 · score 0.8_

The success of deployed agents relies on their ability to handle open-ended user requests using their inherent capabilities, not only in solving requests directly but also in effectively leveraging inter-agent communication channels and feedback signals over time. This requires a multi-agent environment where agents can operate autonomously, strategically communicate, behave collaboratively and be driven by economic incentives, much like humans in society.


[Источник](https://arxiv.org/abs/2605.26203)

<!-- url_hash:d7aba9fc6b1cb74c4b278d8a7fd4d561f348a78c866cd12c98dc18bd9b41470b -->


## AgentSecBench: Measuring Prompt Injection, Privacy Leakage, and Tool-Use Integrity in LLM Agents

_arXiv · 2026-05-25 · score 0.8_

LLM agents process trusted instructions, retrieved records, and tool observations through a common generative channel. This conflates data flow with authority: an untrusted string can affect a secret-bearing response or an action proposal even when no application policy authorizes that influence.


[Источник](https://arxiv.org/abs/2605.26269)

<!-- url_hash:3d1c9a7c645ddb9564b48fd7217b568b3ad7fca42bc047872904f249aa4eebdd -->
