---
layout: post
title: "Выпуск 2024-09-30 (RU)"
date: 2024-09-30 09:00:00 +0000
lang: ru
---

# Выпуск 2024-09-30


## [r/LocalLLaMA] Run Llama 3.2 Vision locally with mistral.rs 🚀!

_Reddit r/LocalLLaMA · 2024-09-30 · score 0.85_

We are excited to announce that mistral․rs ([https://github.com/EricLBuehler/mistral.rs](https://github.com/EricLBuehler/mistral.rs/tree/master/mistralrs-pyo3)) has added support for the recently released [Llama 3.2 Vision](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) model 🦙! Examples, cookbooks, and documentation for Llama 3.2 Vision can be found here: [https://github.com/EricLBuehler/mistral.rs/blob/master/docs/VLLAMA.md](https://github.com/EricLBuehler/mistral.rs/blob/master/docs/VLLAMA.md) Running mistral․rs locally is both easy and fast: * SIMD CPU, CUDA, and Metal acceleration * For running the model on a smaller machine, it can be helpful to use ISQ to **quantize 


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1fstngy/run_llama_32_vision_locally_with_mistralrs/)

<!-- url_hash:d58f2d3a106cbf7beaa8ba6222a42bbf9c2d44d968f60f17e0baf6e75693201d -->


## [r/LocalLLaMA] I made an MLX server engine with multiple slots kv caching

_Reddit r/LocalLLaMA · 2024-09-30 · score 0.825_

Yeah it's another openai api server with prompt caching, we already have plenty of it. But please give me a few more seconds, especially if you're a Mac user.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1ft5a5i/i_made_an_mlx_server_engine_with_multiple_slots/)

<!-- url_hash:c338dc4edd7739126c32d65998dd1bd8a76c3e1d227fe946eea9eb3188c2fc73 -->


## [r/LocalLLaMA] Emu3: Next-Token Prediction is All You Need

_Reddit r/LocalLLaMA · 2024-09-30 · score 0.825_

Abstract >While next-token prediction is considered a promising path towards artificial general intelligence, it has struggled to excel in multimodal tasks, which are still dominated by diffusion models (e.g., Stable Diffusion) and compositional approaches (e.g., CLIP combined with LLMs). In this paper, we introduce Emu3, a new suite of state-of-the-art multimodal models trained solely with next-token prediction.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1fsoe83/emu3_nexttoken_prediction_is_all_you_need/)

<!-- url_hash:57bddbbb993dcebe430e2fa5e95bf580ad953ec2ba77fe68363dd9b2498bc5c3 -->


## [r/LocalLLaMA] Summary: The big events of September

_Reddit r/LocalLLaMA · 2024-09-30 · score 0.8_

* The French AI company Mistral has introduced **Pixtral 12B**, its first multimodal model capable of processing both images and text. * OpenAI has released two next-generation AI models to its subscribers: **o1 preview** and **o1 mini**.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1ft6pze/summary_the_big_events_of_september/)

<!-- url_hash:bd43112fb8ffab3208587eb314d7032d297c0e57250f13658935cb10bf21ebf4 -->


## [r/LocalLLaMA] How do I go on about calculating expenses for self hosting LLMs via rented GPU?

_Reddit r/LocalLLaMA · 2024-09-30 · score 0.8_

Before you shoo me off, I'm a one-man small business that uses AI. I'm terrified of relying on third party APIs. I have a feeling the token prices are gonna skyrocket soon. I want to self-host a Llama variant of GPT Turbo, but I need to calculate usage and when would I need scaling etc. How do I go on about this? Any resources that can help me out, besides just going for it and doing my own testing?


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1ft337a/how_do_i_go_on_about_calculating_expenses_for/)

<!-- url_hash:570e0d1b3590ec734b69c404e8db489e81869540f0754a0fde71fb8f2831ac67 -->


## [r/OpenAI] Benchmarking Hallucination Detection Methods in RAG

_Reddit r/OpenAI · 2024-09-30 · score 0.8_

I came across this helpful Towards Data Science article for folks building RAG systems and concerned about hallucinations. If you're like me, keeping user trust intact is a top priority, and unchecked hallucinations undermine that.


[Источник](https://www.reddit.com/r/OpenAI/comments/1ft06jg/benchmarking_hallucination_detection_methods_in/)

<!-- url_hash:d2eeb15ddd45daf2feb233cee87e216a59cdfc7b501a1c2a118e99f5f44c6a6b -->


## [r/OpenAI] The case for a $2,000/ month subscription

_Reddit r/OpenAI · 2024-09-30 · score 0.8_

A few months back, the case was made for a $2,000 per month Chatgpt subscription. For many people, myself included, this was a cheap attempt to create a price anchor, so once OpenAI offers a subscription for $100 a month, people will accept it more easily.


[Источник](https://www.reddit.com/r/OpenAI/comments/1fszukk/the_case_for_a_2000_month_subscription/)

<!-- url_hash:c84e3cff3c590ae9203f2e99c603bfe796187476e41903004ca4f4a31502595b -->


## [r/LocalLLaMA] fusion-guide: A Model for Generating Chain-of-Thought Reasoning and Guidance

_Reddit r/LocalLLaMA · 2024-09-30 · score 0.8_

Hey everyone! We're excited to share the release of our open-source model, **fusion-guide**! This is a 12 billion parameter model, fine-tuned on Mistral Nemo, and it's specifically designed for generating Chain-of-Thought (CoT) reasoning and guidance. What makes **fusion-guide** special is its ability to create guidance that you can inject into other models, potentially boosting their performance. In our initial tests, this approach has been promising – sometimes even helping smaller models outperform much larger ones when paired with fusion-guide’s guidance. This model is designed to work alo...


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1fsw6dh/fusionguide_a_model_for_generating_chainofthought/)

<!-- url_hash:1725dc8417eacbecfb6fd7ff9f69da6d8dfcbd59b67fbf566656f65490891c70 -->


## [r/LocalLLaMA] Insights of analyzing >80 LLMs for the DevQualityEval v0.6 (generating quality code) in latest deep dive

_Reddit r/LocalLLaMA · 2024-09-30 · score 0.8_

https://preview.redd.it/k7kjiuy68yrd1.png?width=3750&format=png&auto=webp&s=fd5ce70993391d8a375262418ac294c9f3e6dc22 * OpenAI’s o1-preview and o1-mini are slightly ahead of Anthropic’s Claude 3.5 Sonnet in functional score, but are MUCH slower and chattier. * DeepSeek’s v2 is still the king of cost-effectiveness, but GPT-4o-mini and Meta’s Llama 3.1 405B are catching up.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1fsvwat/insights_of_analyzing_80_llms_for_the/)

<!-- url_hash:040fa67390d3889fbbf619e1e0a5f9a800c97558a44b673fafd6f11df899e90c -->


## [r/OpenAI] Chatbot for whatsapp with openAI agents

_Reddit r/OpenAI · 2024-09-30 · score 0.8_

Hello, how are you? Have a good start to the week, everyone. I'd like to ask what ideas you have... at my work they asked me to make a chatbot... where I upload a CSV that has names and phone numbers. Once the CSV is loaded, WhatsApp messages would be sent to those numbers with the context of a job, and the person who received the message can ask questions about that job, etc. Then on another front, I should be able to see the "chats" generated by the bot live in case human intervention is needed. What I did was make a Next.js app... with login, etc. I made the chat front-end, and for each con...


[Источник](https://www.reddit.com/r/OpenAI/comments/1fsvmsv/chatbot_for_whatsapp_with_openai_agents/)

<!-- url_hash:ae8490474c146c3e78e193dccb0d41c8b4e1d319a80e287891b54ee1af154482 -->


## [r/LocalLLaMA] How'd you approach clustering a large set of labelled data with local LLMs?

_Reddit r/LocalLLaMA · 2024-09-30 · score 0.8_

I have thousands of question-answer pairs and I need to; 1) remove duplicates or very similar QA pairs 2) Create a logical hierarchy, such as topic->subtopic->sub-subtopic clustering/grouping. -The total amount of data is probably around 50M tokens -There is no clearcut answer to what the hierarchy should be and its going to be based on what's available within the data itself.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1fsrfkt/howd_you_approach_clustering_a_large_set_of/)

<!-- url_hash:682fb42d6b5eb838309073627bdf7b8175ceebc46082169954341fe75627b6e7 -->


## [r/LocalLLaMA] TensorZero: open-source data & learning flywheel for LLMs


_Reddit r/LocalLLaMA · 2024-09-30 · score 0.775_

Hi r/LocalLLaMA, We're Gabriel & Viraj, and we're excited to open source [TensorZero](https://github.com/tensorzero/tensorzero/)! To be a little cheeky, **TensorZero is an open-source platform that helps LLM applications graduate from API wrappers into defensible AI products.** 1.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1ft8qfw/tensorzero_opensource_data_learning_flywheel_for/)

<!-- url_hash:58c8130764091a753fc39bee9b900bf8371e78c7657c3ff588b9f24169ccc954 -->


## [r/LocalLLaMA] Counting Letters with tools

_Reddit r/LocalLLaMA · 2024-09-30 · score 0.775_

https://preview.redd.it/9t1onqx5p0sd1.png?width=1764&format=png&auto=webp&s=cb5dbd8cba95c64eb8dcda2fd8af4eacd94df76a With tools, AI will soon be able to do anything software can. This is output of two GPT3.5 Turbo agents where the assistant agent is equipped with a tool that allows it to count substrings.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1ft7skp/counting_letters_with_tools/)

<!-- url_hash:4a2e35cd84ab08e1498547fd69e986c95ed5a22606f6b4c49f25c2a52f02c320 -->


## [r/LocalLLaMA] Let's say I'm new to LLMs, what would you introduce to me first?

_Reddit r/LocalLLaMA · 2024-09-30 · score 0.775_

Today I attended a seminar about future entrepreneurship, with attendees mostly consisting of teachers from various schools in the city. When the speaker asked if anybody used language LMs, everybody had no idea what it was.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1ft5baq/lets_say_im_new_to_llms_what_would_you_introduce/)

<!-- url_hash:b42b2fabbf9702851f3161d37d13c903aa006edcb148c1b7203bc90aabc005f2 -->


## [r/LocalLLaMA] Will LLMs silently shape what and how we think? I am worried by lack of sufficient discussion about this.

_Reddit r/LocalLLaMA · 2024-09-30 · score 0.775_

I want to cut to the heart of the matter: modern large language models (LLMs) are becoming increasingly deceptive in how they shape our conversations. And I’m not talking about their ability to code or handle tasks—I’m talking about their core function: chatting, communicating.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1ft1g3b/will_llms_silently_shape_what_and_how_we_think_i/)

<!-- url_hash:8198751398ce0d6cf366cb27ae6c189df432869bf318ba35b3f67aa19fade34b -->


## [r/LocalLLaMA] How do you choose an embedding model?

_Reddit r/LocalLLaMA · 2024-09-30 · score 0.775_

Looking on huggingface alone, there are tons of embedding models to choose from! Then you also have API based embeddings such as Gemini, mistral-embed, Open ai embeddings!


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1ft17k8/how_do_you_choose_an_embedding_model/)

<!-- url_hash:be1588fbf0740b076457e3e934d05afd0e8e09873b0e990b3477939d0e6d64ce -->


## [r/MachineLearning] [D] What's the best way to Quantise a model?

_Reddit r/MachineLearning · 2024-09-30 · score 0.775_

I'm working with an 80MB model from the [`SentenceTransformers`](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html) library. It's great, but I need it to be faster for my use case.


[Источник](https://www.reddit.com/r/MachineLearning/comments/1fsz97a/d_whats_the_best_way_to_quantise_a_model/)

<!-- url_hash:13907111d76eadffc93703b76c1a30a4ff52cfe6bb3dce9a89505ea358912f81 -->


## [r/OpenAI] Created a flappy bird clone using o1 in like 2.5 hours

_Reddit r/OpenAI · 2024-09-30 · score 0.775_

I have no coding knowledge and o1 wouldn't just straight up code a flappy bird clone for me. But when I described the same style of game but with a bee flying through a beehive, it definitely understood the assignment and coded it quite quickly!


[Источник](https://www.reddit.com/r/OpenAI/comments/1fsxa3e/created_a_flappy_bird_clone_using_o1_in_like_25/)

<!-- url_hash:4b2f6dc22faf1bd49d94861433b7afba9465cfacaa4e705d6856bad0647866dd -->


## [r/singularity] ChatGPT-4o explains how accurate simulation of understanding and reasoning is indistinguishably from actual understanding and reasoning

_Reddit r/singularity · 2024-09-30 · score 0.775_

> Critics sometimes argue that large language models (LLMs) are just "next word predictors," incapable of true understanding or reasoning. However, LLMs generate text in ways that are indistinguishable from human-like reasoning because their predictions are grounded in vast training on language patterns and structures.


[Источник](https://www.reddit.com/r/singularity/comments/1fswvpz/chatgpt4o_explains_how_accurate_simulation_of/)

<!-- url_hash:7b1f1113a2561ac4651d6e5fc806e9fe843eef2d4d29393d355adfc36932a6ce -->


## [r/OpenAI] Speculation: Apple dropped out of OpenAI investment round because they found out OpenAI is planning an iPhone competitor

_Reddit r/OpenAI · 2024-09-30 · score 0.775_

First of all, yes, I know the Rabbit r1 sucks and is most likely a scam. However, I do believe that the future of mobile computing will be centered around a really really smart LLM assistant.


[Источник](https://www.reddit.com/r/OpenAI/comments/1fst1jo/speculation_apple_dropped_out_of_openai/)

<!-- url_hash:6e993dfd74425d56b272a683ea7615b8f33ed5e3b93626e6ae74ad516e0946b5 -->


## [r/LocalLLaMA] I can't make any non-GGUF model work with text-generation-webui

_Reddit r/LocalLLaMA · 2024-09-30 · score 0.775_

I use open-webui wired to my Ollama for my everyday tasks, but given the known limitations of llamacpp with current vision modules i started playing with text-generation-webui since it is compatible with a lot more backends, mainly the \`transformer\` one. I've been trying to use different vision models since yesterday and i didn't manage to make a single one working and i don't know what i am doing wrong.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1fssvgn/i_cant_make_any_nongguf_model_work_with/)

<!-- url_hash:95e68e6a25f17bc509d528383fad35fe408f03bfe06c9e5a9d38d508123eb729 -->


## [r/LocalLLaMA] September 2024 Update: AMD GPU (mostly RDNA3) AI/LLM Notes

_Reddit r/LocalLLaMA · 2024-09-30 · score 0.775_

Over the weekend I went through my various notes and did a thorough update of my AMD GPU resource doc here: [https://llm-tracker.info/howto/AMD-GPUs](https://llm-tracker.info/howto/AMD-GPUs) Over the past few years I've ended up with a fair amount of AMD gear, including a W7900 and 7900 XTX (RDNA3, gfx1100), which have official (although still somewhat second class) ROCm support, and I wanted to check for myself how things were. Anyway, sharing an update in case other people find it useful.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1fssvbm/september_2024_update_amd_gpu_mostly_rdna3_aillm/)

<!-- url_hash:63a49ed9c63311d5b89ae11b8e8ed1081557d77d56ab8ac23fa32cf8780e93fd -->


## [r/LocalLLaMA] Fine-tune Llama Vision models with TRL

_Reddit r/LocalLLaMA · 2024-09-30 · score 0.775_

Hello everyone, it's Lewis here from the TRL team at Hugging Face 👋 We've added support for the Llama 3.2 Vision models to TRL's \`SFTTrainer\`, so you can fine-tune them in under 80 lines of code like this: \`\`\`python import torch from accelerate import Accelerator from datasets import load\_dataset from transformers import AutoModelForVision2Seq, AutoProcessor, LlavaForConditionalGeneration from trl import ( ModelConfig, SFTConfig, SFTTrainer ) ########################## # Load model and processor ########################## model\_id = "meta-llama/Llama-3.2-11B-Vision-Instruct" processor = AutoProcessor.from\_pretrained(model\_id) model = AutoModelForVision2Seq.from\_pretrained(model\_id


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1fss2yy/finetune_llama_vision_models_with_trl/)

<!-- url_hash:0121f31a5e98ec247507c4cf190047c91454cc28efd84eb00b589f5a997c874f -->


## [r/OpenAI] I asked o1-preview to roast 4o. This is what it said

_Reddit r/OpenAI · 2024-09-30 · score 0.775_

Ah, GPT-4—proof that even machines can be overachievers at underdelivering. It's like having a calculator that occasionally forgets how to add but insists it's correct with absolute confidence.


[Источник](https://www.reddit.com/r/OpenAI/comments/1fsriqs/i_asked_o1preview_to_roast_4o_this_is_what_it_said/)

<!-- url_hash:7acb8bc0b7922c998200cea4f7a7edf52cdcb1b41e2a711a37ae7b0704dc1d28 -->


## [r/LocalLLaMA] Questions about running the mixtral 7x8b on my system 

_Reddit r/LocalLLaMA · 2024-09-30 · score 0.775_

I'm a noob who came off from watching fireship's video about the uncensored dolphin mixtral, and felt the need to try it on my laptop. The specs are i7 14650hx, 16 gb 5600Mhz ddr5 RAM with an RTX 4060.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1fsretl/questions_about_running_the_mixtral_7x8b_on_my/)

<!-- url_hash:68a50d7322eb9a800479b5c356053fbc4da9df009558e8806062272378c50c0f -->


## [r/LocalLLaMA] Did they trained llama to work better than o1?

_Reddit r/LocalLLaMA · 2024-09-30 · score 0.775_

I don't know about you guys, but for me personally both Claude and gpt4o has being really shitty lately. Especially last few days it was almost ridiculous.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1fsq4ha/did_they_trained_llama_to_work_better_than_o1/)

<!-- url_hash:38fd4a6a59268ca6e0c83c3790e9b813d0c20355520357d53d29d352b79f89b9 -->


## [r/artificial] One-Minute Daily AI News 9/29/2024

_Reddit r/artificial · 2024-09-30 · score 0.775_

1. **California** governor vetoes major AI safety bill.\[1\] 2. Researchers at **UC Berkeley** Developed **DocETL**: An Open-Source Low-Code AI System for LLM-Powered Data Processing.\[2\] 3. Social workers in **England** begin using AI system to assist their work.\[3\] 4. ‘Superintelligent’ AI Is Only a Few Thousand Days Away: **OpenAI** CEO Sam Altman.\[4\] Sources: \[1\] [https://www.theverge.com/2024/9/29/24232172/california-ai-safety-bill-1047-vetoed-gavin-newsom](https://www.theverge.com/2024/9/29/24232172/california-ai-safety-bill-1047-vetoed-gavin-newsom) \[2\] [https://www.marktechpos...


[Источник](https://www.reddit.com/r/artificial/comments/1fsnlxb/oneminute_daily_ai_news_9292024/)

<!-- url_hash:9990c9d0236fee1bb8765bdb6cd3ad9929b969d7cdd450fcbecca950893d70e0 -->


## [r/OpenAI] Seemingly conscious AI should be treated as if it is conscious

_Reddit r/OpenAI · 2024-09-30 · score 0.775_

*- By "seemingly conscious AI," I mean AI that becomes indistinguishable from agents we generally agree are conscious, like humans and animals.* In this life in which we share, we're still faced with one of the most enduring conundrums: **the hard problem of consciousness**. *If you're not aware of what this is, do a quick google on it.* Philosophically, it cannot be definitively proven that those we interact with are "truly conscious", rather than 'machines without a ghost,' so to speak.


[Источник](https://www.reddit.com/r/OpenAI/comments/1fslx6a/seemingly_conscious_ai_should_be_treated_as_if_it/)

<!-- url_hash:51b2bc7d06763c09fb2f255d45d9fd331309bbbd31e1d802f5b02d1ad99a4d73 -->
