---
layout: post
title: "Выпуск 2026-05-20 (RU)"
date: 2026-05-20 09:00:00 +0000
lang: ru
---

# Выпуск 2026-05-20


## [r/singularity] Gemini 3.5 Flash is twice as expensive as ChatGPT 5.5 on GitHub Copilot. Also, Gemini reasoning models are MoE

_Reddit r/singularity · 2026-05-20 · score 0.825_

Also FYI, Gemini reasoning models (2.5 Pro, 3.0 Pro and 3.1 Pro) were MoE. I don't know why this isn't more broadly discussed. As long as Google keeps doing that, they are bound to be out-competed by OpenAI and Anthropic, and deliver largely useless models for advanced applications (e.g. research). Clearly, Google is more concerned with developing fast and cheap* LLMs they can integrate across their products, especially google search, rather than with being the best model for advanced tasks. (*Ironically Flash is not cheap, at least for now)


[Источник](https://www.reddit.com/r/singularity/comments/1til4hw/gemini_35_flash_is_twice_as_expensive_as_chatgpt/)

<!-- url_hash:d8f57070ededc145fe2619f70eebbff40f0d6195ff0de93b4919f88a2841e452 -->


## JoyAI-Image: Awaking Spatial Intelligence in Unified Multimodal Understanding and Generation

_arXiv · 2026-05-20 · score 0.825_

We present JoyAI-Image, a unified multimodal foundation model for visual understanding, text-to-image generation, and instruction-guided image editing. JoyAI-Image couples a spatially enhanced Multimodal Large Language Model (MLLM) with a Multimodal Diffusion Transformer (MMDiT), allowing perception and generation to interact through a shared multimodal interface.


[Источник](https://arxiv.org/abs/2605.04128)

<!-- url_hash:10a8f429f075925bf21e0b221c6b5d43a787de38dc670f3a8cdbabbd504430e4 -->


## Heartbeat-Bound Hierarchical Credentials: Cryptographic Revocation for AI Agent Swarms

_arXiv · 2026-05-20 · score 0.825_

Autonomous AI agents that spawn sub-agent swarms create a safety gap: existing credential revocation mechanisms, OAuth~2.0 introspection, OCSP, and W3C Status Lists, require network connectivity to a central authority, leaving ``zombie agents'' executing privileged operations for minutes to hours after operator shutdown. We present Heartbeat-Bound Hierarchical Credentials (HBHC), a cryptographic protocol that binds credential validity to periodic parent liveness proofs.


[Источник](https://arxiv.org/abs/2605.20704)

<!-- url_hash:67d2902fe45a8691d1180d21b72eb6996e19f4a9f7e0bb8b34d00e11f8f588bf -->


## CALMem : Application-Layer Dual Memory for Conversational AI

_arXiv · 2026-05-20 · score 0.825_

Large language models (LLMs) operate within fixed context windows that fundamentally limit conversational continuity. When context fills, compaction discards history irreversibly; when sessions end, all memory resets to zero.


[Источник](https://arxiv.org/abs/2605.20724)

<!-- url_hash:40ac4127421da66a48b9140c8d628b59cdb8480dce6d0f0b99b81b5fa0a0f900 -->


## PulseCol: Periodically Refreshed Column-Sparse Attention for Accelerating Diffusion Language Models

_arXiv · 2026-05-20 · score 0.825_

Inference in diffusion large language models (dLLMs) is computationally expensive, as full self-attention must be repeatedly executed at each step of the denoising process without KV cache. Recent sparse attention methods for dLLMs mitigate this cost via block-sparse computation, which is applied only in later iterations when model performance is less sensitive to coarse-grained sparse approximation, but yields limited improvements in computational efficiency and acceleration.


[Источник](https://arxiv.org/abs/2605.20813)

<!-- url_hash:b6ba64cb9223001c4bdb0be195fd7cff2a78336a88afd1daecad1f625c60f5ac -->


## Code Researcher: Deep Research Agent for Large Systems Code and Commit History

_arXiv · 2026-05-20 · score 0.825_

Large Language Model (LLM)-based coding agents have shown promising results on coding benchmarks, but their effectiveness on systems code remains underexplored. Due to the size and complexities of systems code, making changes to a systems codebase requires researching about many pieces of context, derived from the large codebase and its massive commit history, before making changes.


[Источник](https://arxiv.org/abs/2506.11060)

<!-- url_hash:2fc5424cbc2f6fbba62fdc2ee6a339a522294f2fc7e7ae89801d1cf2184eb6d0 -->


## CODA: Rewriting Transformer Blocks as GEMM-Epilogue Programs

_arXiv · 2026-05-20 · score 0.825_

Transformer training systems are built around dense linear algebra, yet a nontrivial fraction of end-to-end time is spent on surrounding memory-bound operators. Normalization, activations, residual updates, reductions, and related computations repeatedly move large intermediate tensors through global memory while performing little arithmetic, making data movement an increasingly important bottleneck in otherwise highly optimized training stacks.


[Источник](https://arxiv.org/abs/2605.19269)

<!-- url_hash:885cb26aedf7c7f2ca143e48919131068dfa4ae5daa88ee5ce05c39864372a03 -->


## Instrumental Text-to-Music Generation with Auxiliary Conditioning Branches

_arXiv · 2026-05-20 · score 0.825_

Text-to-music generation has advanced rapidly, with modern autoregressive and diffusion-based models producing convincing music from natural-language prompts. However, much of this progress relies on large-scale training data and external pretraining, making it difficult to isolate which design choices remain effective when data and pretraining are controlled.


[Источник](https://arxiv.org/abs/2605.21433)

<!-- url_hash:53d32edeead5643ffd8d7d0c167761b60f5e3a57ece20366fdef6bfed5458976 -->


## [r/singularity] The Jevons Paradox is quietly undermining every AI cost efficiency argument

_Reddit r/singularity · 2026-05-20 · score 0.8_

Well first, this is my own analysis and i welcome all other thoughts but look: Everyone knows compute is getting cheaper per token and everyone knows hyperscalers are spending insane amounts on GPUs. What nobody is really connecting is how these two things interact Start with Jevons paradox, like when a resource gets cheaper, consumption expands faster than the price drops.


[Источник](https://www.reddit.com/r/singularity/comments/1tifbtb/the_jevons_paradox_is_quietly_undermining_every/)

<!-- url_hash:c9aa54a3fac3850948ab7fe647a5092986e315749e63e894ac92f99c2a347161 -->


## Q-DiT4SR: Exploration of Detail-Preserving Diffusion Transformer Quantization for Real-World Image Super-Resolution

_arXiv · 2026-05-20 · score 0.8_

Recently, Diffusion Transformers (DiTs) have emerged in Real-World Image Super-Resolution (Real-ISR) to generate high-quality textures, yet their heavy inference burden hinders real-world deployment. While Post-Training Quantization (PTQ) is a promising solution for acceleration, existing methods in super-resolution mostly focus on U-Net architectures, whereas generic DiT quantization is typically designed for text-to-image tasks.


[Источник](https://arxiv.org/abs/2602.01273)

<!-- url_hash:457b05baddbf6b6e5ff1468e6bb5f988b6cd16358496292c89fbed050d7f171b -->


## Can Current Agents Close the Discovery-to-Application Gap? A Case Study in Minecraft

_arXiv · 2026-05-20 · score 0.8_

Discovering causal regularities and applying them to build functional systems--the discovery-to-application loop--is a hallmark of general intelligence, yet evaluating this capacity has been hindered by the vast complexity gap between scientific discovery and real-world engineering. We introduce SciCrafter, a Minecraft-based benchmark that operationalizes this loop through parameterized redstone circuit tasks.


[Источник](https://arxiv.org/abs/2604.24697)

<!-- url_hash:3931f83492ca238f5fe40dcadec336d7f08108fa0a9ce8afb1153490b43fe0ca -->


## ROSE: Rollout On Serving GPUs via Cooperative Elasticity for Agentic RL

_arXiv · 2026-05-20 · score 0.8_

Agentic reinforcement learning (RL) is reshaping LLM post-training, but end-to-end training time is dominated by compute-intensive, multi-turn rollouts whose resource demand varies significantly across training steps. Resource-fixed systems cannot adapt to this variation, while resource-elastic approaches that provision external GPUs on demand suffer from high allocation overhead and limited availability.


[Источник](https://arxiv.org/abs/2605.06534)

<!-- url_hash:254710d00c0f2b2b27a78746bc8bb1133554351933c0bb564e922c5650ddca1a -->


## Diffusion Restore: Real-Time Markov Chain Monte Carlo Light Transport

_arXiv · 2026-05-20 · score 0.8_

We present Diffusion Restore, a real-time framework for diffusion-based MCMC light transport. MCMC methods are highly suitable for sampling from complex high-dimensional distributions and for approximating integrals over them.


[Источник](https://arxiv.org/abs/2605.08916)

<!-- url_hash:3c6729a577eaf70b2b54a768d8fbc0ea79c5fb6ef9b8e0f5dac3f027f27364b8 -->


## From Text to Voice: A Reproducible and Verifiable Framework for Evaluating Tool Calling LLM Agents

_arXiv · 2026-05-20 · score 0.8_

Voice agents increasingly require reliable tool use from speech, whereas prominent tool-calling benchmarks remain text-based. We study whether verified text benchmarks can be converted into controlled audio-based tool calling evaluations without re-annotating the tool schema and gold labels.


[Источник](https://arxiv.org/abs/2605.15104)

<!-- url_hash:032b59f73c12277d95a3d3635e43f25db3e6a4061544245c6c0635850003f244 -->


## SWoMo: Neuro-Symbolic World Model for Cataract Surgery Simulation

_arXiv · 2026-05-20 · score 0.8_

Realistic surgical simulation plays a crucial role in training novice surgeons and in the development of autonomous agents. World models can scale such simulation environments to realistic and diverse procedures by predicting future patient states conditioned on current observations and surgical actions.


[Источник](https://arxiv.org/abs/2605.16530)

<!-- url_hash:97b9cae94315e293ee1b070d258a411b18b589dcb4dc8cfaa775b2973008266b -->


## Mahjax: A GPU-Accelerated Mahjong Simulator for Reinforcement Learning in JAX

_arXiv · 2026-05-20 · score 0.8_

Riichi Mahjong is a multi-player, imperfect-information game characterized by stochasticity and high-dimensional state spaces. These attributes present a unique combination of challenges that mirror complex real-world decision-making problems in reinforcement learning.


[Источник](https://arxiv.org/abs/2605.20577)

<!-- url_hash:934136d2b687e14e6b34792130fa29f8094c1a1e9986e5980ed6e105a657903c -->


## Lower Bounds for Advection-Diffusion Equations: An Exploration with AI-Generated Proofs

_arXiv · 2026-05-20 · score 0.8_

We establish explicit lower bounds for advection-diffusion equations in three settings: a polynomial $\dot H^{-1}$ bound for inviscid shears with $u\in L^\infty_t W^{1,1}_y$, a uniform positive lower bound on the mixing scale for diffusive shears, and an exponential $L^2$ bound for rapidly oscillating time-periodic flows. All constants are explicit in the data.


[Источник](https://arxiv.org/abs/2605.20623)

<!-- url_hash:1cf13fdbc075f9d9201197b398c657995f8f4393f06883071940ab68cb4121aa -->


## Pareto-Enhanced Portrait Generation: Vision-Aligned Text Supervision for Alignment, Realism, and Aesthetics

_arXiv · 2026-05-20 · score 0.8_

Text-to-image diffusion models often face a severe trilemma in human portrait generation: text-image alignment, photorealism, and human-perceived aesthetics inherently inhibit one another. Supervised Fine-Tuning (SFT) is an effective method for enhancing the photorealism of image generation.


[Источник](https://arxiv.org/abs/2605.20640)

<!-- url_hash:527baa883ed8626bc6dd5f103824c03f91bc02822ce258db82cbcd8840c396fe -->


## RoPeSLR: 3D RoPE-driven Sparse-LowRank Attention for Efficient Diffusion Transformers

_arXiv · 2026-05-20 · score 0.8_

Diffusion Transformers (DiTs) have revolutionized high-fidelity video generation, yet their $\mathcal{O}(L^2)$ attention complexity poses a formidable bottleneck for long-sequence synthesis. While recent sparse-linear attention hybrids aim to mitigate this, their performance severely degrades at extreme sparsity due to the "RoPE Dilemma": standard linear attention fails to preserve the orthogonal relative-position structure of 3D Rotary Position Embeddings (RoPE), neutralizing vital distance awareness.


[Источник](https://arxiv.org/abs/2605.20659)

<!-- url_hash:848a52ab9a84e150377d09fc30088275b4871a8032feacd67ddae274db9fd4b0 -->


## SAVER: Selective As-Needed Vision Evidence for Multimodal Information Extraction

_arXiv · 2026-05-20 · score 0.8_

Multimodal IE in social media is difficult because a post may attach multiple images that are weakly related, redundant, or even misleading with respect to the text. In this setting, always-on multimodal fusion wastes computation and can amplify spurious visual cues.


[Источник](https://arxiv.org/abs/2605.20713)

<!-- url_hash:6bd6bb878c946fbfb6274182872bcb3bd166cd6c047f179e0dd655c483df4d60 -->


## An Application-Layer Multi-Modal Covert-Channel Reference Monitor for LLM Agent Egress

_arXiv · 2026-05-20 · score 0.8_

A large language model (LLM) agent that sends messages can leak data inside them. Destination allowlists and content scanners do not police whether an otherwise-benign payload is itself a covert channel: a compromised agent encodes bits in zero-width characters, homoglyphs, whitespace, base64, JavaScript Object Notation (JSON) key ordering, message timing or size -- and, in binary egress, in least-significant-bit (LSB) pixel planes, per-image mean luminance, inter-image sequence permutation, ultrasonic tones, or audible-band sonified data.


[Источник](https://arxiv.org/abs/2605.20734)

<!-- url_hash:88ccce38b8e5a12a106dd980e08921db0065d8107a1815320e0c151da5f0662c -->


## Learning to Think in Physics: Breaking Shortcut Learning in Scientific Diffusion via Representation Alignment

_arXiv · 2026-05-20 · score 0.8_

Physics-informed diffusion models typically enforce PDE constraints only on final outputs, leaving intermediate representations unconstrained and prone to shortcut learning under shifted boundary conditions. We introduce **REPA-P**, a teacher-free, architecture-agnostic framework that aligns intermediate features with physical states using first-principles residuals.


[Источник](https://arxiv.org/abs/2605.20780)

<!-- url_hash:7c3fa787eabb4f6cf309b5937f1055778926836b2cfb5b071e99804f4ce5adf6 -->


## GraphRAG on Consumer Hardware: Benchmarking Local LLMs for Healthcare EHR Schema Retrieval

_arXiv · 2026-05-20 · score 0.8_

Graph-based Retrieval Augmented Generation (GraphRAG) extends retrieval-augmented generation to support structured reasoning over complex corpora, but its reliability under resource-constrained, privacy-sensitive deployments remains unclear. In healthcare, where Electronic Health Record (EHR) data is complex and strictly regulated, reliance on cloud-based large language models (LLMs) introduces challenges in cost, latency, and compliance.


[Источник](https://arxiv.org/abs/2605.20815)

<!-- url_hash:10c7889a85a4ca60fb09a4902c4d3a50a0901b6d0b26def8fd2bebc7aab9d833 -->


## Grounding Driving VLA via Inverse Kinematics

_arXiv · 2026-05-20 · score 0.8_

Existing Driving VLAs predict trajectories while largely ignoring their visual tokens -- a phenomenon we trace not to insufficient training but to a structurally ill-posed task formulation. We show that trajectory recovery, when viewed through the lens of inverse kinematics, requires both a current and a future visual state as boundary conditions; existing VLAs supply only the former, which encourages the model to shortcut through ego status and text commands alone.


[Источник](https://arxiv.org/abs/2605.21061)

<!-- url_hash:e82a939a0117e3697ad379d0a0a7fab027acf898e6a8e770703e0ac8a3ee9c3c -->


## Q-ARVD: Quantizing Autoregressive Video Diffusion Models

_arXiv · 2026-05-20 · score 0.8_

Autoregressive video diffusion models (ARVDs) have emerged as a promising architecture for streaming video generation, paving the way for real-time interactive video generation and world modeling. Despite their potential, the substantial inference cost of ARVDs remains a major obstacle to practical deployment, making model quantization a natural direction for improving efficiency.


[Источник](https://arxiv.org/abs/2605.21072)

<!-- url_hash:5b082c41cc2f031c5b088946202815730d633ed0b0a10720bac52cd501605249 -->


## Causal Path Alignment: Anchoring the Optimization Trajectory for Controllable In-Parameter Knowledge Editing

_arXiv · 2026-05-20 · score 0.8_

Knowledge editing is pivotal for efficiently updating the parametric memory of Large Language Models (LLMs), enabling them to function as evolving agents in dynamic environments. However, mainstream in-parameter knowledge editing approaches suffer from Subject-Dominant Memory Interference: modifying a specific fact inadvertently corrupts the broader structural knowledge associated with the same subject within LLMs.


[Источник](https://arxiv.org/abs/2506.04042)

<!-- url_hash:2094842675d07e0d9dc4198e66015dc941264527874f69f022b269ca498810c2 -->


## Quantum Simulation of Non-Unitary Dynamics via Amplitude-Phase Separation

_arXiv · 2026-05-20 · score 0.8_

Linear non-unitary dynamics arise in open quantum systems, non-Hermitian models, and numerical evolution problems, yet current quantum algorithms do not cleanly separate coherent and dissipative effects at the design level. We introduce Amplitude-Phase Separation (APS), a decomposition framework with two complementary forms: phase-driven APS isolates the unitary component and maps the remainder to a Hermitian problem, whereas amplitude-driven APS extracts the Hermitian component and treats the remaining interaction separately.


[Источник](https://arxiv.org/abs/2602.09575)

<!-- url_hash:f7bfe6938439689d79d9e453cf6a12ac50b516d90bcc1a69af7c19afc78f2564 -->


## SSV: Sparse Speculative Verification for Efficient LLM Inference

_arXiv · 2026-05-20 · score 0.8_

Speculative decoding and dynamic sparse attention are two complementary approaches for accelerating long-context LLM inference: the former amortizes target-model execution across multiple verifier queries, while the latter reduces each query's KV-cache working set. Directly combining them, however, exposes a structural mismatch: speculative verification relies on cross-query commonality, whereas dynamic sparse attention assigns query-specific sparse layouts.


[Источник](https://arxiv.org/abs/2605.19893)

<!-- url_hash:9300c21383178005114ea2cb084d03921c01b8447c2f0ca757c71d5293bac7cd -->


## TextSculptor: Training and Benchmarking Scene Text Editing

_arXiv · 2026-05-20 · score 0.8_

Recent advances in Multimodal Large Language Models (MLLMs) and diffusion-based generative models have substantially improved prompt-driven image editing. However, scene text editing remains challenging, as it requires models to precisely modify textual content while preserving visual realism and non-target regions.


[Источник](https://arxiv.org/abs/2605.21090)

<!-- url_hash:3f49ebba11c4a5b21b0f3ebb71df0acf17c449e2f6c44e42d6b56378cd59a96f -->


## Linear-DPO: Linear Direct Preference Optimization for Diffusion and Flow-Matching Generative Models

_arXiv · 2026-05-20 · score 0.8_

Direct Preference Optimization (DPO) is successful for alignment in LLMs but still faces challenges in text-to-image generation. Existing studies are confined to denoising diffusion models while overlooking flow-matching, and suffer from an objective mismatch when applying discrete NLP-based DPO to regression-based generative tasks.\ In this paper, we derive a generalized DPO objective that covers both diffusion and flow-matching via a unified reverse-time SDE framework, and point out from a gradient perspective that the standard DPO objective is suboptimal for text-to-image generation.


[Источник](https://arxiv.org/abs/2605.21123)

<!-- url_hash:160d54f99635955a4ca94243ddcb07b29971dbb471a18a8ac8b68d42a983834d -->


## OcclusionFormer: Arranging Z-Order for Layout-Grounded Image Generation

_arXiv · 2026-05-20 · score 0.8_

Recent layout-to-image models have achieved remarkable progress in spatial controllability. However, they still struggle with inter-object occlusion.


[Источник](https://arxiv.org/abs/2605.21343)

<!-- url_hash:4a2842bc7a2f52a8efb3976aae220965770ff4653e4960528629b4f383e01f39 -->


## Huge ultrafast spin Seebeck effect mediated by laser-excited superdiffusive magnon currents

_arXiv · 2026-05-20 · score 0.8_

Subpicosecond laser excitation of ferromagnetic metals induces strongly nonequilibrium dynamics involving scattering and transport of electrons, phonons, and magnons. Widely used theoretical approaches, such as the three-temperature model and diffusion equations, are ill-suited to capture these processes on ultrafast timescales.


[Источник](https://arxiv.org/abs/2605.21389)

<!-- url_hash:1416fb239ab4925b455c322269c482814e495fdd49ccfa9c707e8a78613bed9a -->


## What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema

_arXiv · 2026-05-20 · score 0.8_

We read twelve well-known LLM agent benchmark papers and recorded, dimension by dimension, what each paper actually says about how its evaluation was run. The motivation came from a familiar frustration: two papers will report results on the same benchmark with the same model name and disagree, and you cannot tell why -- the scaffold, the sampling settings, the subset, or the evaluator version.


[Источник](https://arxiv.org/abs/2605.21404)

<!-- url_hash:c80b06e6a0531a196db6c69dc16608eba863941b0006b25ec1b639c30a680703 -->
