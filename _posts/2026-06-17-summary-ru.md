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


## Experimental asymmetric relativistic zero-knowledge proofs with unconditional security

_arXiv · 2026-06-17 · score 0.775_

Zero-knowledge proofs (ZKPs) are widely applied in digital economies, such as cryptocurrencies and smart contracts, for establishing trust and privacy between untrusted parties. Classical ZKPs rely on computational assumptions and are vulnerable to quantum attacks.


[Источник](https://arxiv.org/abs/2501.18176)

<!-- url_hash:a0da3d9cdc5364bf364e8c26be3bfd6f6adefb35cdd4008feb8c06053dfa6053 -->


## Bootstrapping mirror pairs: The beginning of the end

_arXiv · 2026-06-17 · score 0.775_

Three-dimensional supersymmetric gauge theories with eight supercharges possess a unique duality known as 3D mirror symmetry. Under this correspondence, the Coulomb branch of one theory is equivalent to the Higgs branch of its mirror dual, and vice versa.


[Источник](https://arxiv.org/abs/2510.14489)

<!-- url_hash:de33dcf4d682acd82c036c7244beb88f529d611121147f9ea77f561e0718bcc4 -->


## GrowthHacker: Automated Off-Policy Evaluation Optimization Using Code-Modifying LLM Agents

_arXiv · 2026-06-17 · score 0.775_

With data-driven development now widely adopted, online A/B testing is an established method for measuring the effects of new technologies. However, deploying online experiments demands resources for design, implementation, and deployment, and may negatively impact users (e.g., unsafe or unethical outcomes) while requiring weeks of data collection.


[Источник](https://arxiv.org/abs/2511.00802)

<!-- url_hash:065346d728b1eca4361da067cec217ffc52f16b7818d96556d2a56f156dba5cf -->


## Posterior Continuation with Noise-Conditioned Frequency Exposure for Diffusion Inverse Problems

_arXiv · 2026-06-17 · score 0.775_

Diffusion posterior sampling solves inverse problems by combining a pretrained diffusion prior with measurement-consistency guidance. However, full-band guidance can be unreliable at high noise levels, where clean estimates contain score-induced errors and high-frequency measurement directions are weakly identifiable.


[Источник](https://arxiv.org/abs/2602.00176)

<!-- url_hash:b6bce96b94792002a002519f0623e8e12310787ab972d82c13086b42564cb309 -->


## Outrunning LLM Cutoffs: A Live Kernel Crash Resolution Benchmark for All

_arXiv · 2026-06-17 · score 0.775_

Repairing system crashes discovered by kernel fuzzers like Syzkaller is a critical yet underexplored challenge in software engineering. While recent works have introduced Large Language Model (LLM) based agents for Linux kernel crash-resolution, their evaluation benchmarks are usually static and thus, do not capture the evolving nature of the Linux kernel, and suffer from potential data contamination due to LLM knowledge cutoffs.


[Источник](https://arxiv.org/abs/2602.02690)

<!-- url_hash:e8baec9a20aa2d24830c6ac29137ce752e66e9385df5cfac2b52a0db7a668b45 -->


## Forged Calamity: Benchmark for Cross-Domain Synthetic Disaster Detection in the Age of Diffusion

_arXiv · 2026-06-17 · score 0.775_

The rapid advancement of text-to-image diffusion models has enabled the creation of highly photorealistic synthetic images that closely resemble real photographs, making it increasingly difficult to distinguish authentic content from AI-generated fabrications. This poses challenges for cybersecurity, digital forensics, and disaster response, where fake imagery of floods, fires, or earthquakes can spread misinformation or disrupt emergency operations.


[Источник](https://arxiv.org/abs/2606.18554)

<!-- url_hash:9e9d5e1e9311403613c7eec7f02ed1abe83f67eead342f1a090cebd50f5d700a -->


## Rethinking Text-to-Image as Semantic-Aware Data Augmentation for Indoor Scene Recognition

_arXiv · 2026-06-17 · score 0.775_

In the realm of computer vision, indoor image recognition presents challenges due to the intricate interplay of lighting conditions, occlusions, and diverse object arrangements within confined spaces. To address the lacks of training indoor images, we introduce a novel approach leveraging Stable Diffusion (SD) for the generation of synthetic images, which serve as a powerful data augmentation tool.


[Источник](https://arxiv.org/abs/2606.18555)

<!-- url_hash:73827ed693b88d457c119d430c53d738a3e2de3d3be187684940352a5e0d93a5 -->


## Bridging Creative Intent and Visual Quality: Creator-Driven Recurrent Video Generation with Agentic Feedback Loops

_arXiv · 2026-06-17 · score 0.775_

Generative AI has made content creation increasingly accessible, but many AI-generated videos lack narrative coherence and creative direction, issues that become more substantial at longer durations. Unlike coding, where AI generation benefits from reliable feedback and techniques such as recurrent self-improvement, video generation requires subjective feedback about plot, scenes, and narrative, which naturally motivates approaches that incorporate human creative direction.


[Источник](https://arxiv.org/abs/2606.18591)

<!-- url_hash:af7c38d20d0ed4f9e01acb04925784bc613d45bad86dc6bd4a365845f0861beb -->


## ShuntServe: Cost-Efficient LLM Serving on Heterogeneous Spot GPU Clusters

_arXiv · 2026-06-17 · score 0.775_

As large language model (LLM) services become widely adopted, the cost of GPU resources for serving these models in cloud environments has emerged as a critical concern. Spot instances offer up to 90% cost savings over on-demand instances, but their frequent interruptions and limited availability pose significant challenges for continuous LLM serving.


[Источник](https://arxiv.org/abs/2606.18600)

<!-- url_hash:582ffbad785f38b3619b056e6bbbd218dc132fbace6560405ae45dd20f2dc400 -->


## Hallmark Signatures of Electronic Pairing in Two-Photon Two-Electron Coincidence Angle-Resolved Photoemission Spectroscopy

_arXiv · 2026-06-17 · score 0.775_

Understanding strongly correlated quantum materials remains a central challenge in condensed matter physics and materials science. While angle-resolved photoemission spectroscopy (ARPES) has become an indispensable probe of single-quasiparticle excitations, it accesses electronic correlations only indirectly.


[Источник](https://arxiv.org/abs/2606.18616)

<!-- url_hash:553f807cbd61fac0c055afd93da6b1bf7afb2ff7ea4d4d959c2b39884b87db25 -->


## PersonalPlan: Planning Multi-Agent Systems for Personalized Programming Learning

_arXiv · 2026-06-17 · score 0.775_

Effective programming education requires personalized instruction adapted to diverse learner backgrounds. However, while LLM-based multi-agent systems (MAS) excel at complex planning, existing planners often lack profile-grounding and pedagogical scaffolding, thereby undermining personalized programming learning.


[Источник](https://arxiv.org/abs/2606.18633)

<!-- url_hash:ed10218318b994e48cec0ebccc6d83e40f5511f673c82ea4b781a66ee193345e -->


## PEC-Home: Interpretation of Progressively Elliptical Commands in Smart Homes

_arXiv · 2026-06-17 · score 0.775_

Recent advancements in Large Language Models (LLMs) have empowered home assistants with natural language interaction capabilities. However, current assistants overlook the progressive omission that occurs in human dialogue as shared context accumulates, leading to more elliptical expressions for efficient communication.


[Источник](https://arxiv.org/abs/2606.18636)

<!-- url_hash:d44c3e27d35982d858b21930ce30560baa3e6d9b839e55694a880aa82df60f31 -->


## VGGHeads: 3D Multi Head Alignment with a Large-Scale Synthetic Dataset

_arXiv · 2026-06-17 · score 0.775_

Human head detection, keypoint estimation, and 3D head model fitting are essential tasks with many applications. However, traditional real-world datasets often suffer from bias, privacy, and ethical concerns, and they have been recorded in laboratory environments, which makes it difficult for trained models to generalize.


[Источник](https://arxiv.org/abs/2407.18245)

<!-- url_hash:9960a577c3d0f1712084b4f7bc1dd9100afbade4d91043ec9bb2972825c0d366 -->


## SuperCarver: Texture-Consistent 3D Geometry Super-Resolution for High-Fidelity Surface Detail Generation

_arXiv · 2026-06-17 · score 0.775_

Conventional production workflow of high-precision mesh assets necessitates a cumbersome and laborious process of manual sculpting by specialized 3D artists/modelers. The recent years have witnessed remarkable advances in AI-empowered 3D content creation for generating plausible structures and intricate appearances from images or text prompts.


[Источник](https://arxiv.org/abs/2503.09439)

<!-- url_hash:62ec78602b181f1fb8f3b40b053bcf98acdca27dbc6049d90a8b7400f29b6b5b -->


## Efficient Hallucination Detection for LLMs Using Uncertainty-Aware Attention Heads

_arXiv · 2026-06-17 · score 0.775_

While large language models (LLMs) have become highly capable, they remain prone to factual inaccuracies, commonly referred to as "hallucinations." Uncertainty quantification (UQ) offers a promising way to mitigate this issue, but most existing methods are computationally intensive and/or require supervision. In this work, we propose Recurrent Attention-based Uncertainty Quantification (RAUQ), an unsupervised and efficient framework for identifying hallucinations.


[Источник](https://arxiv.org/abs/2505.20045)

<!-- url_hash:53bac8b6ce77c4811f1583ba668fe5a9dcfa9b305089132abfa3a51da48422ed -->


## ASyMOB: Algebraic Symbolic Mathematical Operations Benchmark

_arXiv · 2026-06-17 · score 0.775_

Large language models (LLMs) are increasingly applied to symbolic mathematics, yet existing evaluations often conflate pattern memorization with genuine reasoning. To address this gap, we present ASyMOB, a high-resolution dataset of 35,368 validated symbolic math problems spanning integration, limits, differential equations, series, and hypergeometrics.


[Источник](https://arxiv.org/abs/2505.23851)

<!-- url_hash:d6fd9de392201262223d2b9f50086263b8d76c0ec22e7a9fb361480ac90402b7 -->


## ToolGrad: Efficient Tool-use Dataset Generation with Textual "Gradients"

_arXiv · 2026-06-17 · score 0.775_

Prior work synthesizes tool-use LLM datasets by first generating a user query, followed by complex tool-use annotations like depth-first search (DFS). This leads to inevitable annotation failures and low efficiency in data generation.


[Источник](https://arxiv.org/abs/2508.04086)

<!-- url_hash:54abf5ff919c912aab9b4cf29dea13d41368d60fe1ff2861898d083ddabe4a0c -->


## Efficient Image-to-Image Schrödinger Bridge for CT Field of View Extension

_arXiv · 2026-06-17 · score 0.775_

Computed tomography (CT) is a cornerstone imaging modality for non-invasive, high-resolution visualization of internal anatomical structures. However, when the scanned object exceeds the scanner's field of view (FOV), projection data are truncated, resulting in incomplete reconstructions and pronounced artifacts near FOV boundaries.


[Источник](https://arxiv.org/abs/2508.11211)

<!-- url_hash:9342337a0e307aed750ee6e958862c18790d2230c821693de836284569fcf28c -->


## DiFlow-TTS: Compact and Low-Latency Zero-Shot Text-to-Speech with Discrete Flow Matching

_arXiv · 2026-06-17 · score 0.775_

Zero-shot text-to-speech (TTS) has made significant progress in replicating unseen voices, yet balancing generation quality and inference efficiency remains challenging. Autoregressive models suffer from high latency, while diffusion-based approaches are constrained by training-time configurations.


[Источник](https://arxiv.org/abs/2509.09631)

<!-- url_hash:d154edc15398168135cf79cafb35dbf8b73a28239ae83227d2ccf9717e430b5f -->


## UniECG: Understanding and Generating ECG in One Unified Model

_arXiv · 2026-06-17 · score 0.775_

Electrocardiogram (ECG) interpretation is a fundamental skill in medical education, yet students often need more than static examples to connect waveform evidence with diagnostic reasoning. This paper presents UniECG as a step toward interactive ECG education.


[Источник](https://arxiv.org/abs/2509.18588)

<!-- url_hash:7a2a89eeaa2600077c9adc8f090e12fcc62bed0dfe7f6e272c4fde198dfe180a -->


## ParaToric 1.0: Continuous-time quantum Monte Carlo for the toric code in a parallel field

_arXiv · 2026-06-17 · score 0.775_

We introduce ParaToric, a C++ package for simulating the toric code in a parallel field (i.e., $X$- and $Z$-fields) at finite temperature. We implement and extend the continuous-time quantum Monte Carlo algorithm of Wu, Deng, and Prokof'ev on the square, triangular, honeycomb, and cubic lattices with either periodic or smooth open boundaries.


[Источник](https://arxiv.org/abs/2510.14781)

<!-- url_hash:5ec1c941095a041d79a050f182bf893d935c046ae8cbb046bbb3a73d11077982 -->


## Evolution of Conditional Entropy for Diffusion Dynamics on Graphs

_arXiv · 2026-06-17 · score 0.775_

The modeling of diffusion processes on graphs is the basis for many network science and machine learning approaches. Entropic measures of network-based diffusion have recently been employed to investigate the reversibility of these processes and the diversity of the modeled systems.


[Источник](https://arxiv.org/abs/2510.19441)

<!-- url_hash:5289894500732bbd7c976b96898039f57d3205ebd4913e253f3a1ef0536257ca -->


## S3OD: Towards Generalizable Salient Object Detection with Synthetic Data

_arXiv · 2026-06-17 · score 0.775_

Salient object detection exemplifies data-bounded tasks where expensive pixel-precise annotations force separate model training for related subtasks like DIS and HR-SOD. We present a method that dramatically improves generalization through large-scale synthetic data generation and ambiguity-aware architecture.


[Источник](https://arxiv.org/abs/2510.21605)

<!-- url_hash:ba9d74ba792585c0a8c7732409562bd5cd140d0949d7ade0ead2a5ba55b46767 -->


## Learning Patient-Specific Disease Dynamics with Latent Flow Matching for Longitudinal Imaging Generation

_arXiv · 2026-06-17 · score 0.775_

Understanding disease progression is a central clinical challenge with direct implications for early diagnosis and personalized treatment. While recent generative approaches have attempted to model progression, key mismatches remain: disease dynamics are inherently continuous and monotonic, yet latent representations are often scattered, lacking semantic structure, and diffusion-based models disrupt continuity with random denoising process.


[Источник](https://arxiv.org/abs/2512.09185)

<!-- url_hash:9e6f8bdb8f718e26301120e6bb5a9e009c7b120035ff125bc203e56ca0805030 -->


## Confinement and finite-range effects in a quasi-two-dimensional gas of fermionic dimers

_arXiv · 2026-06-17 · score 0.775_

We investigate the ground-state properties of ultracold two-component Fermi gases in the presence of a transverse harmonic potential, focusing on the strongly interacting regime in which pairs of fermions form tightly bound molecules. Using the fixed-node diffusion Monte Carlo method, we calculate the equation of state and density profiles for the full fermionic system, which allows us to address the importance of finite-range corrections arising from the internal fermionic structure of the dimers.


[Источник](https://arxiv.org/abs/2512.09753)

<!-- url_hash:3cfb7bb942a84330ef990c2b95bf8568de9db50ee13d4d4ced3f7bf462a6edbe -->


## DeepInflation: an AI agent for research and model discovery of inflation

_arXiv · 2026-06-17 · score 0.775_

We present DeepInflation, an AI agent designed for research and model discovery in inflationary cosmology. Built upon a multi-agent architecture, DeepInflation integrates Large Language Models (LLMs) with a symbolic regression (SR) engine and a retrieval-augmented generation (RAG) knowledge base.


[Источник](https://arxiv.org/abs/2601.14288)

<!-- url_hash:5b1ca02a0c8283665a751c0869e68a08e27bdf87c8c848bfa1c26e8cf6cea962 -->


## Private Iris Recognition with High-Performance FHE

_arXiv · 2026-06-17 · score 0.775_

Among biometric verification systems, irises stand out because they offer high accuracy even in large-scale databases. For example, the World ID project aims to provide authentication to all humans via iris recognition, with millions already registered.


[Источник](https://arxiv.org/abs/2601.17561)

<!-- url_hash:0275eecebfe697ad0bd09452f31011bbd98780dfd230b8ca29ac988974e7ab5d -->


## Global Well-Posedness and Numerical Approximation of a Coupled Darcy-Convection-Diffusion System with Exponential Nonlinearity

_arXiv · 2026-06-17 · score 0.775_

This paper investigates density driven flow in porous media, focusing on the roles of viscosity contrast, density contrast, and linear adsorption. In this setup, the fluid on top is heavier and more viscous than the fluid below.


[Источник](https://arxiv.org/abs/2601.17968)

<!-- url_hash:3acc30f109523a0ead5b8d710f1c4213ae90b2de1b2253325ace6aa6072564ab -->


## HeRo-Q: A General Framework for Stable Low Bit Quantization via Hessian Conditioning

_arXiv · 2026-06-17 · score 0.775_

Post Training Quantization (PTQ), a mainstream model compression technique, often leads to the paradoxical 'low error, high loss' phenomenon because it focuses solely on minimizing quantization error. The root cause lies in the Hessian matrix of the LLM loss landscape: a few high curvature directions are extremely sensitive to perturbations.


[Источник](https://arxiv.org/abs/2601.21626)

<!-- url_hash:c8d982e55148ab98535ec3cd3450f04e66e0cebf83cf09510ed8eb6d5d5dfa19 -->


## MUFASA: A Multi-Layer Framework for Slot Attention

_arXiv · 2026-06-17 · score 0.775_

Unsupervised object-centric learning (OCL) decomposes visual scenes into distinct entities. Slot attention is a popular approach that represents individual objects as latent vectors, called slots.


[Источник](https://arxiv.org/abs/2602.07544)

<!-- url_hash:d8ba31821748963ca6ddbccd5b10a7315577bd7917f48478d9c5d26bf853e085 -->


## E-VAds: An E-commerce Short Videos Understanding Benchmark for MLLMs

_arXiv · 2026-06-17 · score 0.775_

E-commerce short videos represent a high-revenue segment of the online video industry characterized by a goal-driven format and dense multi-modal signals. Current models often struggle with these videos because existing benchmarks focus primarily on general-purpose tasks and neglect the reasoning of commercial intent.


[Источник](https://arxiv.org/abs/2602.08355)

<!-- url_hash:13f0a4c82dbb832100c139e2b00bbc25ef38ccd5f8eb474964a484e2cc9417d6 -->


## ActMem: Bridging the Gap Between Memory Retrieval and Reasoning in LLM Agents

_arXiv · 2026-06-17 · score 0.775_

Memory management is essential for LLM agents in long-term interactions. Current memory frameworks typically treat agents as passive ``recorders'' and retrieve information without understanding its deeper implications.


[Источник](https://arxiv.org/abs/2603.00026)

<!-- url_hash:5d26184d6fdcc3deae893564c5879827619ee1460cbb22c2b72505effc3992df -->


## Bidirectional Cross-Attention Fusion of High-Resolution RGB and Low-Resolution Hyperspectral Inputs for Multimodal Semantic Segmentation

_arXiv · 2026-06-17 · score 0.775_

Multimodal semantic segmentation with heterogeneous sensors must reconcile complementary information across modalities that differ in spatial resolution and channel dimensionality. In particular, high-resolution RGB imaging provides detailed spatial structure but often fails to distinguish visually similar materials, whereas hyperspectral imaging (HSI) provides discriminative spectral signatures but at lower spatial resolution.


[Источник](https://arxiv.org/abs/2603.13941)

<!-- url_hash:e750fe702c2e91e355298f66bcb9a1c6f4b90ad7f5e0cc666bff07a48980980e -->


## MemRerank: Preference Memory for Personalized Product Reranking

_arXiv · 2026-06-17 · score 0.775_

LLM-based shopping agents increasingly rely on long purchase histories and multi-turn interactions for personalization, yet naively appending raw history to prompts is often ineffective due to noise, length, and relevance mismatch. We propose MemRerank, a preference memory framework that distills user purchase history into concise, query-independent signals for personalized product reranking.


[Источник](https://arxiv.org/abs/2603.29247)

<!-- url_hash:c664bfdfc3d8eea8c6c8311f908a025d242cea0326c87ec8c8ffa6ad256050d4 -->


## IPSL-AID: Generative Diffusion Models for Climate Downscaling from Global to Regional Scales

_arXiv · 2026-06-17 · score 0.775_

Effective adaptation and mitigation strategies for climate change require high-resolution projections to inform strategic decision-making. Conventional global climate models, which typically operate at resolutions of 150 to 200 kilometers, lack the capacity to represent essential regional processes.


[Источник](https://arxiv.org/abs/2604.03275)

<!-- url_hash:9a6e041af2c3e3fdc83bae76ba2ab469e7db13fa3918ba7a8c18301db62e7d6c -->


## DiffVQE: Hybrid Diffusion Voice Quality Enhancement Under Acoustic Echo and Noise

_arXiv · 2026-06-17 · score 0.775_

Acoustic echo and background noise pose challenges on speech enhancement in hands-free systems and speakerphones. Discriminatively trained end-to-end methods represent a powerful solution for joint acoustic echo control (AEC) and denoising.


[Источник](https://arxiv.org/abs/2605.08189)

<!-- url_hash:08bcb3f819715f5e569f6accebfbf66278cc951f0bf0b205c1399bfe91521ea9 -->


## Wave packet landscape in open quantum systems

_arXiv · 2026-06-17 · score 0.775_

We formulate a landscape theory for the long-time wave packet spreading of free and harmonically trapped particles with quantum fluctuations and its related dissipation. We show that the diffusion, localization, and collapse of wave packets arise from symmetry structures of an underlying landscape in covariance space.


[Источник](https://arxiv.org/abs/2605.15658)

<!-- url_hash:e8633a12ac2c539e221c92c6f9b16ee623571dc7323d274f4b34d16b3c621ea0 -->


## Notation Matters: A Benchmark Study of Token-Optimized Formats in Agentic AI Systems

_arXiv · 2026-06-17 · score 0.775_

Large language models in Agentic AI systems consume tool schemas and execution results and emit tool invocations as structured data. The default language for that exchange, JSON, was designed for application-to-application interchange rather than token efficiency, so its structural elements impose substantial token overhead.


[Источник](https://arxiv.org/abs/2605.29676)

<!-- url_hash:2b69648dde8a935e418be507f0e61f89cfcee0689a5a23985f5fdbdaac4ba6f6 -->


## Geometry-Aware Dataset Condensation for Diffusion Model Training

_arXiv · 2026-06-17 · score 0.775_

Dataset condensation aims to construct compact datasets from real data via synthesis or selection. However, existing approaches are ill-suited for diffusion model training: synthetic data generation often yields low-fidelity samples unsuitable for authentic modeling, while real subset selection typically fails to preserve the distributional geometry required by diffusion likelihood objectives.


[Источник](https://arxiv.org/abs/2606.05883)

<!-- url_hash:3d9b9e5ca698244377174a0f0f1d9e42202eaa9e366fc77b330024725105051e -->


## Physics in 2-Steps: Locking Motion Priors Before Visual Refinement Erases Them

_arXiv · 2026-06-17 · score 0.775_

Image-to-Video diffusion models leverage input images to generate visually stunning content, yet frequently produce motion that violates physical laws. We reveal a surprising finding: a 2-step generation often exhibits better physical consistency than a 50-step output from the same model.


[Источник](https://arxiv.org/abs/2606.06361)

<!-- url_hash:febcdaf0cb87596062d5d7c68522704c49d74c0502dfc48528b9e9bab3c7782e -->


## From Privacy to Workflow Integrity: Communication-Graph Metadata in Autonomous Agent Interoperability

_arXiv · 2026-06-17 · score 0.775_

Agent-interoperability protocols such as A2A and MCP standardize what agents say to one another but assume address-based transport. Whether over HTTP(S) or a content-protecting binding such as MLS-based SLIM, these transports protect message content yet leave the communication graph exposed: which agent contacts which, when, and how often.


[Источник](https://arxiv.org/abs/2606.07150)

<!-- url_hash:c96b30a5e53b40ed31f57233c5180f0a80d7363692eb4a085ea4edf90f2a68c0 -->


## Refined anti-proton and anti-deuteron fluxes from weak-scale Dark Matter

_arXiv · 2026-06-17 · score 0.775_

We provide the cosmic-ray (CR) fluxes of antiprotons and antideuterons produced by the Galactic annihilation or decay of weak-scale dark matter (DM) particles of masses in the range from a few GeV to 100 TeV. We estimate these fluxes based on the updated models for the propagation of charged particles in the Galaxy and using the improved $\bar{p}$ and $\bar{d}$ spectra provided by $\texttt{CosmiXs}$.


[Источник](https://arxiv.org/abs/2606.10017)

<!-- url_hash:1161b8aca454f0507b2bb89650fd9ef5d096109f00eba8757add0d4fcbb79330 -->


## Sparsity-Driven Source Localization in Tomographic Sensing Applications

_arXiv · 2026-06-17 · score 0.775_

Hyperspectral standoff detection systems such as Focal Plane Array (FPA) Fourier Transform Infrared (FTIR) spectrometers provide high spatial resolution in detecting airborne chemical contaminants that are invisible to the human eye but potentially hazardous. When two such systems are operated simultaneously with a suitable opening angle, they enable tomographic reconstruction of contaminant plumes with improved spatial and temporal accuracy.


[Источник](https://arxiv.org/abs/2606.11840)

<!-- url_hash:dc859aaa274f08682cdea2de15817b3600821225cc9bc23e0fe724ce125e395a -->


## EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments

_arXiv · 2026-06-17 · score 0.775_

Large language model (LLM) agents have achieved strong performance on a wide range of benchmarks, yet most evaluations assume static environments. In contrast, real-world deployment is inherently dynamic, requiring agents to continually align their knowledge, skills, and behavior with changing environments and updated task conditions.


[Источник](https://arxiv.org/abs/2606.13681)

<!-- url_hash:b96ee01b81d456ac4e29410b7d04c56a23045a224059f9c8b0b9d6ef0dabc9e4 -->


## DiPOD: Diffusion Policy Optimization without Drifting Apart

_arXiv · 2026-06-17 · score 0.775_

RL post-training has become increasingly pivotal for improving diffusion policies, but existing diffusion policy-gradient methods are often unstable and cannot achieve reliable policy improvement. We identify the cause as the double-drift phenomenon: optimizing a variational surrogate can let the ELBO separate from the true log-likelihood, which then makes the resulting proxy policy gradient misaligned with the true policy gradient of expected return.


[Источник](https://arxiv.org/abs/2606.13795)

<!-- url_hash:2d69fbe5ed9f7dd6ea0791ed475663d9cef2bba203d24f33537b0491772c844b -->


## Quasi-Monte Carlo finite element approximation for singularly perturbed convection-diffusion problems with random velocity

_arXiv · 2026-06-17 · score 0.775_

This paper studies the numerical approximation of a singularly perturbed convection-diffusion problem over a bounded polygonal domain in $\mathbb{R}^d$ ($d=2,3$), where the velocity field is modeled by a log-uniform random field, a setting typical in uncertainty quantification. We introduce a novel numerical framework for computing the expected value of the linear functionals of the solution.


[Источник](https://arxiv.org/abs/2606.18678)

<!-- url_hash:62b5ce2a5a5ea19172253a252856526a1997ed69936159c03db8b9276c917e56 -->


## Attention as Frustrated Synchronization

_arXiv · 2026-06-17 · score 0.775_

A network of oscillators that synchronizes perfectly computes nothing further, so an attention architecture built from synchronization must locate its computation in structured departures from agreement. We introduce the Frustrated Synchronization Network (FSN), whose token states are phases on a torus and whose entire value pathway is one learned complex coupling kernel over harmonics and a one-step delay.


[Источник](https://arxiv.org/abs/2606.18694)

<!-- url_hash:d64be5d7169bdb005182ee6ffaa4cdd8405c118f1e55d2db5c3080d85eec02e7 -->


## UniTemp: Unlocking Video Generation in Any Temporal Order via Bidirectional Distillation

_arXiv · 2026-06-17 · score 0.775_

Autoregressive video diffusion models have emerged as a promising approach for long video generation, achieving strong performance in streaming settings. However, existing methods are restricted to forward temporal generation, whereas practical video creation often requires flexible generation order, e.g., conditioning on future context to extend backward, or on both past and future context for inbetween generation.


[Источник](https://arxiv.org/abs/2606.18702)

<!-- url_hash:9ac3ef4eff8ba5f5df60ab3c0fcc0ffd1dcd185de319fcddfe04ae00f92f9f64 -->


## Integration of diamond nanobeams with SnVs on Al2O3 waveguides for scalable quantum photonic chip application

_arXiv · 2026-06-17 · score 0.775_

Tin vacancy (SnV) centers in diamond are promising solid state qubits for integrated quantum photonics. Here, we fabricate and characterize a diamond on Al2O3 dual taper waveguide structure containing SnV centers, demonstrating optical coupling between the diamond nanobeam and the underlying Al2O3 waveguide.


[Источник](https://arxiv.org/abs/2606.18711)

<!-- url_hash:7ce8341722ffca67591fc4834d09d9c01828b3b9f52dafa4e502953935a3bb50 -->


## Generating Natural and Expressive Robot Gestures through Iterative Reinforcement Learning with Human Feedback using LLMs

_arXiv · 2026-06-17 · score 0.775_

Expressive gestures are essential for natural and effective communication, complementing speech when verbal cues alone are insufficient (e.g., pointing). For social robots such as the humanoid Pepper, producing natural and expressive movements is critical for improving human-robot interaction (HRI) and long-term acceptance.


[Источник](https://arxiv.org/abs/2606.18747)

<!-- url_hash:80b4e6a73cc3352ea8aa62f6b508b468438e62d504c963ad91c4a381f67c06cf -->


## SMART: A Flexible, Interpretable, and Scalable Spatio-temporal Brain Atlas from High-Resolution Imaging Data

_arXiv · 2026-06-17 · score 0.775_

We introduce SMART, a framework for learning a flexible, interpretable, and scalable spatio-temporal brain atlas from longitudinal high-resolution 3D medical images. Existing approaches to spatio-temporal atlas construction rely on black-box generative models that lack flexibility, limit interpretability, and struggle to scale to high-dimensional data.


[Источник](https://arxiv.org/abs/2606.18753)

<!-- url_hash:2f32086615b04e638b2b23332d727d642f93d8b2eda1db1c40d63b59a6ea1a6e -->


## Universal photon blockade via two-photon light-matter interaction at chiral exceptional points

_arXiv · 2026-06-17 · score 0.775_

The photon blockade (PB) effect is a hallmark non-classical phenomenon in quantum optics and finds important applications for building quantum sources, while the control of PB by the non-Hermitian exceptional points remains largely unexplored. In this work, we theoretically investigate universal photon blockade in a microcavity harboring chiral exceptional points (CEPs) for building multiplexing quantum sources with nonreciprocal photon statistics.


[Источник](https://arxiv.org/abs/2606.18756)

<!-- url_hash:073f4dbfb1ced895c84cb23551b0897afca245c339d08d62c08235f79f642f52 -->


## SpectralDiT: Timestep-Conditioned Spectral Residual Correction for Flow-Matching DiTs

_arXiv · 2026-06-17 · score 0.775_

We propose SpectralDiT, a lightweight modification to flow-matching Diffusion Transformers that adds timestep-conditioned spectral correction to the MLP residual branch. The module decomposes each residual update into low- and high-frequency components on the patch-token grid, then learns a zero-initialized additive gate so the model initially matches the baseline DiT.


[Источник](https://arxiv.org/abs/2606.18765)

<!-- url_hash:8b779fdb1329644af2c66d1ef259c2c3398bc2c1046bf411a7bca85084e3ca65 -->


## ProfiLLM: Utility-Aligned Agentic User Profiling for Industrial Ride-Hailing Dispatch

_arXiv · 2026-06-17 · score 0.775_

Bringing Large Language Models (LLMs) into industrial ride-hailing dispatch as semantic feature extractors over platform-scale behavioral logs is a compelling but under-explored data systems problem. Production matching pipelines remain dominated by structured numerical features, yet decisive behavioral signals (e.g., a driver's habitual aversion to certain regions) are inherently contextual and naturally expressible as LLM-generated user profiles.


[Источник](https://arxiv.org/abs/2606.18803)

<!-- url_hash:d7f6e483940f9d83c705890bb9235cbbba67c88499beee960d153b32330751be -->


## GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents

_arXiv · 2026-06-17 · score 0.775_

Memory benchmarks for LLM agents largely assume single-user settings, leaving shared assistants for hospitals, workplaces, campuses, and households understudied. In these deployments, multiple principals write to a common memory pool and query it under different roles, scopes, and relationships, so memory quality requires governance as well as recall.


[Источник](https://arxiv.org/abs/2606.18829)

<!-- url_hash:3103e0646fa3bc15ad5dbff25da8085e5a12d02b21459aedef0659ea9fd0ab3f -->


## Field Demonstration of a Multi-User Continuous-Variable Quantum Access Network for Quantum-to-the-Home

_arXiv · 2026-06-17 · score 0.775_

Realizing scalable Quantum-to-the-Home (QTTH) faces a bottleneck: link asymmetry in broadcast continuous-variable quantum access networks (CV-QANs) hinders the selection of a globally optimal modulation variance. We demonstrate a downstream broadcast CV-QAN connecting a Quantum Line Terminal (QLT) to multiple Quantum Network Units (QNUs) over commercial fiber.


[Источник](https://arxiv.org/abs/2606.18840)

<!-- url_hash:33db6c2ecd6fd431bfdbd1b9015223e4921941efecd29f9761733877adbeb5d6 -->


## Extracting effective scaling exponents in finite-size hyperuniform systems

_arXiv · 2026-06-17 · score 0.775_

Hyperuniform systems strongly suppress long-wavelength density fluctuations, which is quantitatively characterized by the small-wavenumber scaling. In finite samples, however, accurately estimating the hyperuniformity exponent α can be challenging.


[Источник](https://arxiv.org/abs/2606.18848)

<!-- url_hash:367d847811f1fc8fa57f7c1b320134de0c2c8804559ed6b4287b71f6bff81006 -->


## Learning to Distort: Weakly-Supervised Image Quality Transfer for Prostate DWI Correction

_arXiv · 2026-06-17 · score 0.775_

Single-shot echo-planar prostate diffusion-weighted imaging (DWI) is frequently complicated by geometric distortions, which impact the ability to derive reliable diagnoses from such images. Developing automated correction methods is challenged by the absence of paired distorted and undistorted clinical scans.


[Источник](https://arxiv.org/abs/2606.18869)

<!-- url_hash:134b1b3eafba568130480abce1b9e5445d8afeaa8b7d93a69a1ac3cbf86e44d4 -->


## SAERec: Constructing Fine-grained Interpretable Intents Priors via Sparse Autoencoders for Recommendation

_arXiv · 2026-06-17 · score 0.775_

Intent-based recommender systems have gained significant attention for improving accuracy and interpretability by modeling the underlying motivations behind user behaviors. Most existing models derive intents directly from user sequences via clustering or prototype learning.


[Источник](https://arxiv.org/abs/2606.18897)

<!-- url_hash:fcc76b997bffa0aebabd929ed22b6a05fc7de776a4bfec085ae75e23efdbcd75 -->


## BindEdit: Taming Attention Leakage for Precise Multi-Object Image Editing

_arXiv · 2026-06-17 · score 0.775_

Real image editing enables precise manipulation of visual content, yet existing methods often fail in complex multi-object scenarios, causing semantic blending, object duplication, or incomplete edits. We attribute these failures to attention leakage, where signals across spatial regions and text tokens become entangled during the denoising process.


[Источник](https://arxiv.org/abs/2606.18906)

<!-- url_hash:8d88a895b7aac7fd7ac6dcf49ebc1eef3540d15425c4b2fd5f838d6e131c9b15 -->


## GraphPO: Graph-based Policy Optimization for Reasoning Models

_arXiv · 2026-06-17 · score 0.775_

Reinforcement Learning with Verifiable Rewards (RLVR) has become a standard paradigm for enhancing the capability of large reasoning models. RLVR typically samples responses independently and optimizes the policy using from final answers.


[Источник](https://arxiv.org/abs/2606.18954)

<!-- url_hash:00935e44461b9038889b93bfd9651850f0e94fa5b60c51dcc83066dec0854423 -->


## Audio-to-Audio via Diffusion Warm Initialization

_arXiv · 2026-06-17 · score 0.775_

In this paper, we propose diffusion warm initialization as a simple yet effective approach for a range of audio-to-audio transformation tasks. To illustrate the generality of the approach, we demonstrate its use in timbre transfer, MIDI-to-Real synthesis, and multiple audio enhancement tasks.


[Источник](https://arxiv.org/abs/2606.18968)

<!-- url_hash:50a7adc99376cea1d1fab217ad6c0d3da52512083bbcf225e320af1d35e443bb -->
