---
layout: post
title: "Выпуск 2026-06-17 (RU)"
date: 2026-06-17 09:00:00 +0000
lang: ru
---

# Выпуск 2026-06-17


## Spotlight: Synergizing Seed Exploration and Spot GPUs for DiT RL Post-Training

_arXiv · 2026-06-17 · score 0.85_

Reinforcement learning (RL) post-training of Diffusion Transformers (DiTs) is prohibitively expensive, requiring thousands of high-end GPUs. Existing works explore two directions to reduce cost: seed exploration improves training convergence by selecting high-contrast samples, yet adds compute to the critical path; spot GPUs offer 69--77\% lower cost, yet sit idle during training because DiT rollouts finish nearly simultaneously, which prevents LLM-style pipelining of rollout with training.


[Источник](https://arxiv.org/abs/2606.19004)

<!-- url_hash:1ea6577f4393a70880fe414760209961b00444af5aad8638f03e9e919ea15eb6 -->


## The Gate Is Only as Honest as Its Contracts: ContractGuard for the Contract Layer of Risk-Aware Causal Gating

_arXiv · 2026-06-17 · score 0.825_

Risk-Aware Causal Gating (RACG) defends tool-augmented LLM agents against indirect prompt injection by removing dangerous tools from the agent's visible action space, so that even a fully injection-compliant agent cannot call a tool it cannot see. We make three points.


[Источник](https://arxiv.org/abs/2606.18550)

<!-- url_hash:bb5ffca7dd0583675731bceed73a731233b6716ffb30e40e8a4c4d20e4ad319b -->


## MoVerse: Real-Time Video World Modeling with Panoramic Gaussian Scaffold

_arXiv · 2026-06-17 · score 0.825_

We present MoVerse, a real-time video world model that creates an interactively navigable scene from a single narrow-field-of-view image. This setting is challenging because the input observes only a small fraction of the environment, while interactive roaming requires a complete surrounding world, persistent geometry, controllable camera motion, and temporally coherent high-fidelity observations.


[Источник](https://arxiv.org/abs/2606.13376)

<!-- url_hash:9fe75b477331c7d1d53a9a694362963093cc7a215f3919120b15c6c3af414dff -->


## CAPRA: Scaling Feedback on Software Architecture Deliverables with a Multi-Agent LLM System

_arXiv · 2026-06-17 · score 0.825_

Automated assessment in software engineering education has advanced significantly for code grading and essay scoring. However, reviewing software architecture deliverables, which requires analyzing structural completeness and requirements traceability, has not yet been fully automated.


[Источник](https://arxiv.org/abs/2606.18976)

<!-- url_hash:3171a8c895cb63a8c70d6f9eeecf61a03dd7e0a7df4014785157686702431c01 -->


## Pulse: Training Acceleration for Large Diffusion Models with Automatic Pipeline Parallelism

_arXiv · 2026-06-17 · score 0.825_

Diffusion models are now a dominant approach for high-fidelity image and video generation, yet scaling their training across GPU clusters remains challenging. Unlike transformer-only architectures, diffusion backbones commonly adopt UNet-style encoder-decoder structures with heterogeneous layers and long-range skip connections.


[Источник](https://arxiv.org/abs/2606.19163)

<!-- url_hash:7a9b4a611eb3f8444a7ac142969f075cac6dd442a7a73d24cbcba83fd4bc136f -->


## FloatDoor: Platform-Triggered Backdoors in LLMs

_arXiv · 2026-06-17 · score 0.825_

Large language models (LLMs) are increasingly deployed in sensitive settings such as software engineering, where their outputs directly shape downstream artifacts. Recent work has shown that an identical model can produce measurably different outputs depending on the deployment platform, a consequence of non-associative floating-point arithmetic and divergent kernel implementations.


[Источник](https://arxiv.org/abs/2606.19535)

<!-- url_hash:a903ca4540f67cfccfdb9e1c36c11cf431bd28d8a8c4bd53f7596a6ae8e16729 -->


## Code-Augur: Agentic Vulnerability Detection via Specification Inference

_arXiv · 2026-06-17 · score 0.8_

The advent of agentic vulnerability detection is already becoming a watershed moment for software security. Audits conducted entirely by autonomous LLM agents are uncovering critical vulnerabilities in fundamental software underpinning digital society.


[Источник](https://arxiv.org/abs/2606.18619)

<!-- url_hash:df2e8d03165ffbb88c0104c644989e903c2db7502aad52302953f0bf0a9be5b4 -->


## Epipolar Geometry Improves Video Generation Models

_arXiv · 2026-06-17 · score 0.8_

Video generation models have advanced significantly through the latent diffusion transformers trained with rectified flow techniques. Yet these models still struggle with geometric inconsistencies, unstable motion, and visual artifacts that break the illusion of realistic 3D scenes.


[Источник](https://arxiv.org/abs/2510.21615)

<!-- url_hash:d3c4a8778917d7dc4dd2181b83281a942f744677c67c11e45007b4bdae467b27 -->


## Scaling up FHE-based Privacy-Preserving ML: Higher Throughput, Longer Inputs for LLama-3-8B

_arXiv · 2026-06-17 · score 0.8_

As large language models (LLMs) become ubiquitous, privacy concerns pertaining to inference keep growing. Fully homomorphic encryption (FHE) has emerged as a primary cryptographic solution for non-interactive confidential LLM inference.


[Источник](https://arxiv.org/abs/2601.18511)

<!-- url_hash:55345fc3bd630dfe6643dd9b14b111b87e6e408ce30077999d756922a025e6dc -->


## DSB: Dynamic Sliding Block Scheduling for Diffusion LLMs

_arXiv · 2026-06-17 · score 0.8_

Diffusion large language models (dLLMs) have emerged as a promising alternative for text generation, distinguished by their native support for parallel decoding. In practice, block inference is crucial for avoiding order misalignment in global bidirectional decoding and improving output quality.


[Источник](https://arxiv.org/abs/2602.05992)

<!-- url_hash:1791b58f6fb40504192b4735c27135ee6adcf9e05c8dfeb86ff79c5cd704fb3c -->


## InfoPO: Information-Driven Policy Optimization for User-Centric Agents

_arXiv · 2026-06-17 · score 0.8_

Real-world user requests to LLM agents are often underspecified. Agents must interact to acquire missing information and make correct downstream decisions.


[Источник](https://arxiv.org/abs/2603.00656)

<!-- url_hash:e2fcc1b3d7ddd944e621ec1878572867b37e3fef1f49b39d06f4076dafb3691b -->


## LivePI: More Realistic Benchmarking of Agents Against Indirect Prompt Injection

_arXiv · 2026-06-17 · score 0.8_

AI agents such as OpenClaw are increasingly deployed in local workflows with access to external tools. This creates indirect prompt-injection (IPI) risk: an agent may execute harmful instructions embedded in untrusted inputs such as email, downloaded files, webpages, repositories, or group-chat messages.


[Источник](https://arxiv.org/abs/2605.17986)

<!-- url_hash:b9c4edec8c71f1b0c543fa005c304e369307ec4148415e549921f809a4523308 -->


## iTryOn: Mastering Interactive Video Virtual Try-On with Spatial-Semantic Guidance

_arXiv · 2026-06-17 · score 0.8_

Video Virtual Try-On (VVT) aims to seamlessly replace a garment on a person in a video with a new one. While existing methods have made significant strides in maintaining temporal consistency, they are predominantly confined to non-interactive scenarios where models merely showcase garments.


[Источник](https://arxiv.org/abs/2605.21431)

<!-- url_hash:8b519f52f7fbaf093997fbeff4b2c635cd3bf0db5485bc5a39b4c3873f78cc4d -->


## Trust Region On-Policy Distillation

_arXiv · 2026-06-17 · score 0.8_

On-Policy Distillation (OPD) is a fundamental technique for efficient post-training of large language models (LLMs), with broad applications in agent learning, multi-task enhancement, and model compression. However, OPD training becomes unstable when the teacher and student distributions differ substantially, as teacher supervision on student-generated tokens may yield unreliable policy gradients and even cause optimization failure.


[Источник](https://arxiv.org/abs/2606.01249)

<!-- url_hash:2408d6f113f3a28f773d96189031d337880cb4d9c2089f2ad04276620a8aad34 -->


## HANSEL: Extracting Breadcrumbs from Web Agent Trajectories for Interactive Verification

_arXiv · 2026-06-17 · score 0.8_

AI web agents can perform complex, multi-step tasks such as searching for products, comparing options, and making purchases on behalf of users. However, verifying the correctness of an agent's output remains difficult.


[Источник](https://arxiv.org/abs/2606.18671)

<!-- url_hash:ff05e2caef174cf1f1ab8c17497dd3448b66a23fb6e6d3cd00e1426c0f04773c -->


## Image Prompt Reconstruction Attacks on Distributed MLLM Inference Frameworks

_arXiv · 2026-06-17 · score 0.8_

Distributed large language model (LLM) inference frameworks connect isolated consumer-grade devices for large-scale model inference, substantially reducing hardware constraints. However, recent studies show that intermediate embeddings transmitted among participants can leak private prompts.


[Источник](https://arxiv.org/abs/2606.18710)

<!-- url_hash:30543072037c82b935a32dc1646ebc3aa5a7cdf951da9929b5f7271ff9331588 -->


## SAMA: Semantic Anchor-aligned Augmentation for Unified Low-Resource Multimodal Information Extraction

_arXiv · 2026-06-17 · score 0.8_

Multimodal Information Extraction (MIE)-covering tasks such as Multimodal Named Entity Recognition (MNER), Relation Extraction (MRE), and Event Extraction (MEE)-is essential for understanding multimedia content but remains constrained by severe data scarcity. Although data augmentation is a promising remedy, existing approaches are impeded by coarse cross-modal alignment and fragmented, task-specific designs that fail to exploit shared semantic knowledge.


[Источник](https://arxiv.org/abs/2606.18780)

<!-- url_hash:d09e8d50eb402e23991f474abd10a6021beba730eda584e329a649b6bba2609a -->


## PowerAgentBench-SS: A Benchmark for Agentic AI in Power System Steady-State Studies

_arXiv · 2026-06-17 · score 0.8_

Power system benchmarks usually evaluate numerical solvers, prediction models, or sequential controllers. These benchmarks are necessary, but they do not directly test whether a Large Language Model (LLM) agent can execute an engineering workflow: inspect a grid case, select tools, call simulators, screen contingencies, propose admissible mitigations, validate results, and produce an auditable evidence trail.


[Источник](https://arxiv.org/abs/2606.18789)

<!-- url_hash:7112b798460444956ac670b1b532161658545e9e3c0fb09635812ae6aaf1cd6f -->


## Generative-Model Predictive Planning for Navigation in Partially Observable Environments

_arXiv · 2026-06-17 · score 0.8_

Navigation in partially observable environments presents a significant challenge for autonomous agents, requiring effective decision-making with limited sensory information in unknown environments. Belief-based methods, particularly those using neural networks to approximate the belief space, often fail to capture the inherent multimodality of belief spaces, especially in high-dimensional cases with perceptual aliasing.


[Источник](https://arxiv.org/abs/2606.18888)

<!-- url_hash:7b9f7e606dad789011dc9f8b9ae38ca5074cd022d693a3b0062e4210c928be85 -->


## A performance portable fast Ewald summation for Stokes flow

_arXiv · 2026-06-17 · score 0.8_

We present GPU algorithms for Ewald summation methods for accelerating N-body Stokes flow problems in periodic domains. Like most N-body codes, Ewald sums use a near-field/far-field decomposition.


[Источник](https://arxiv.org/abs/2606.19059)

<!-- url_hash:5f55201082b6d054b02dfd76da3775b2bfc885df4a79ea3f8119c225d6dcd466 -->


## TurboServe: Serving Streaming Video Generation Efficiently and Economically

_arXiv · 2026-06-17 · score 0.8_

Streaming video generation is emerging as a new serving workload in which users interact with long-lived sessions that generate video progressively, chunk by chunk. Unlike offline video generation or typical LLM serving, streaming video generation must preserve session state across active and idle periods, repeatedly schedule ongoing sessions, and deliver each chunk under a tight latency target.


[Источник](https://arxiv.org/abs/2606.19271)

<!-- url_hash:7c1b8741545533c2895a409907c9f1c7213dc91a85340d2d0fda7be688b6c771 -->


## Random-matrix reduction in projective quantum mechanics: Numerical simulations

_arXiv · 2026-06-17 · score 0.8_

We present numerical simulations supporting the random-matrix state-reduction framework developed in the companion theoretical paper. The simulations test the main derived features of the model: isotropic diffusion generated by Gaussian Unitary Ensemble Hamiltonians in projective state space, the restriction of this diffusion to Brownian motion on the classical submanifold, Born-rule frequencies for detector-defined outcome classes, and stroboscopic Newtonian motion for macroscopic systems under repeated environmental monitoring.


[Источник](https://arxiv.org/abs/2606.19273)

<!-- url_hash:8be465bc0f10b45ec55cdc38798d953a8b7e70f4feb6e9de282b68b36e530316 -->


## Diffusion-Proof: Recipe for Formal Theorem Proving Beyond Auto-Regressive Generation

_arXiv · 2026-06-17 · score 0.8_

Enhancing the formal math reasoning capabilities of Large Language Models (LLMs) has become a key focus in both mathematical and computer science communities in recent years. While significant progress has been made in using state-of-the-art Auto-Regressive (AR) LLMs for formal theorem proving, these models suffer from inherent limitations.


[Источник](https://arxiv.org/abs/2606.19315)

<!-- url_hash:2058a421dad0c77f26f0c254e8089e5e3879124ae6c9fb720949601abe023333 -->


## S2D2: Fast Decoding for Diffusion LLMs via Training-Free Self-Speculation

_arXiv · 2026-06-17 · score 0.8_

Block-diffusion language models offer a promising path toward faster-than-autoregressive generation by combining block-wise autoregressive decoding with within-block parallel denoising. However, in the few-step regime needed for practical acceleration, standard confidence-thresholded decoding is often brittle: aggressive thresholds hurt quality, while conservative thresholds require unnecessary denoising steps.


[Источник](https://arxiv.org/abs/2603.25702)

<!-- url_hash:ae1e8f975ea0f193395a2841caed490527fe1b63b6ac604ec98b179bf289b8e5 -->


## Target-Side Paraphrase Augmentation for Sign Language Translation with Large Language Models

_arXiv · 2026-06-17 · score 0.8_

Sign language translation (SLT) remains constrained by the limited availability of paired sign-video/text corpora and by the heavy-tailed vocabularies typical of real-world datasets. We study a target-side augmentation strategy in which a large language model (LLM) generates controlled paraphrase variants of the reference spoken-language sentence while the sign input remains unchanged.


[Источник](https://arxiv.org/abs/2605.31393)

<!-- url_hash:80c93b5610e5fa57d403ea7c900e0bb4e405024d2ad6448acfb73e3a67edb630 -->


## MonaVec: A Training-Free Embedded Vector Search Kernel for Edge and Offline AI Systems

_arXiv · 2026-06-17 · score 0.8_

We present MonaVec, a deterministic, embedded vector-search kernel for edge and offline AI -- settings where server infrastructure, network connectivity, and training data are all unavailable. Existing vector-search systems assume a persistent server, gigabytes of RAM, or a training pass over the corpus; MonaVec instead targets the deployment profile of SQLite: one file, one function call, runs anywhere.


[Источник](https://arxiv.org/abs/2606.19458)

<!-- url_hash:df4f80c65ebf5a809b6802624e07f198bbfc9f8560621c8f7a410b7afdfcbc8e -->


## PerceptionDLM: Parallel Region Perception with Multimodal Diffusion Language Models

_arXiv · 2026-06-17 · score 0.8_

Multimodal large language models (MLLMs) have achieved remarkable progress in visual understanding tasks. However, most existing MLLMs rely on autoregressive generation, which limits their efficiency for perception tasks that require captioning multiple regions.


[Источник](https://arxiv.org/abs/2606.19534)

<!-- url_hash:a994ba7e0b19daa76898fe4b0801b7b41183c263f3e94b72660068bec94684a1 -->


## Uncertainty Decomposition for Clarification Seeking in LLM Agents

_arXiv · 2026-06-17 · score 0.8_

Recent position papers argue that the classical aleatoric/epistemic uncertainty framework is insufficient for interactive large language model (LLM) agents and call for underspecification-aware, decomposed, and communicable uncertainty representations that can unlock new agent capabilities such as proactive clarification seeking and shared mental-model building. Practical deployment constraints -- black-box APIs, interactive latency budgets, and the absence of labeled trajectories -- rule out logprob-based, multi-sampling, and training-based methods, leaving prompt-based estimation as the most viable family for surfacing such signals at deployment time.


[Источник](https://arxiv.org/abs/2606.19559)

<!-- url_hash:58cfe7564e27b13c7e3634eeebda8a7d9ca0f0b049bc7fc42709d05bd7327929 -->


## IHBench: Evaluating Post-Interruption Recovery in Voice Agents with Structured Workflows

_arXiv · 2026-06-17 · score 0.8_

Voice agents deployed in structured workflows (customer service, healthcare scheduling, account management) must handle frequent user interruptions while maintaining progress through multi-step procedures. Existing benchmarks for speech-capable models focus on the timing of interruptions: barge-in detection, endpointing, and turn-taking dynamics.


[Источник](https://arxiv.org/abs/2606.19595)

<!-- url_hash:598bfad7b3beedc4337c80743d103fbee96bebcda78e467576cb0afe3e306a1e -->


## From 50K to 8.2 Million in 24 Hours: Vozinha's Algorithmic Consecration and the Multilingual Making of World Cup Visibility

_arXiv · 2026-06-17 · score 0.8_

We present a multilingual computational discourse analysis of how language constructed the algorithmic consecration of Vozinha, the 40-year-old Cape Verde goalkeeper, after Spain 0-0 Cape Verde at the 2026 FIFA World Cup. The study contributes a multilingual corpus in Portuguese, Spanish, English, and French; a nine-frame narrative taxonomy with cue-based frame annotation; a reproducible annotation pipeline combining LLM-assisted suggestion with human validation; and an analysis of cross-lingual narrative diffusion across discourse phases.


[Источник](https://arxiv.org/abs/2606.19647)

<!-- url_hash:4e439727a3c6b0a646b19205e37af32651c4947838e4389682a0a85af18359e4 -->


## DF-ExpEnse: Diffusion Filtered Exploration for Sample Efficient Finetuning

_arXiv · 2026-06-17 · score 0.8_

A natural recipe for intelligent robotic decision-making is initializing from pretrained generative control policies, which have summarized offline experience, and adapting them to self-collected online experience. We present DF-ExpEnse, an exploration technique that improves the quality of online experience collection, thus increasing finetuning sample-efficiency.


[Источник](https://arxiv.org/abs/2606.19656)

<!-- url_hash:dcca92e0fe9e39a6e2890c2b6ccdbe2334035086f922037184909ef4aca64216 -->
