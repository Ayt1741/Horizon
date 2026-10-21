---
layout: post
title: "Выпуск 2024-12-30 (RU)"
date: 2024-12-30 09:00:00 +0000
lang: ru
---

# Выпуск 2024-12-30


## [r/LocalLLaMA] running VLLM docker  without mandatory model in POST request 

_Reddit r/LocalLLaMA · 2024-12-30 · score 0.85_

How to make vllm not require the model name when requesting? I am running a vllm container on VM using the following command: `docker run --runtime nvidia --gpus all -v /home/myname/_projects/models/:/mnt/model/ -p 8000:8000 --env "TRANSFORMERS_OFFLINE=1" --env "HF_DATASET_OFFLINE=1" --ipc=host vllm/vllm-openai:latest --model="/mnt/model/hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4" --max_model_len=50000 --gpu_memory_utilization=0.85` The model is up and running and whenever I am trying to do a post request like this: `curl -X POST "`[`http://0.0.0.0:8000/v1/completions`](http://0.0.0.0:8000/v1/completions)`" \` `-H "Content-Type: application/json" \` `-d '{"prompt": "What is AI?","max


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1hphnt7/running_vllm_docker_without_mandatory_model_in/)

<!-- url_hash:78b30e082948f34d91e9515facd573e8f382e65b2c1b97e88798b31761b8428a -->


## [r/MachineLearning] [D] How I've Optimized GPU costs while training LLMs

_Reddit r/MachineLearning · 2024-12-30 · score 0.825_

As GPU costs continue to surge amid the exponential growth in AI development, optimizing compute resources has become critical for maintaining sustainable training pipelines. This technical guide explores advanced strategies for maximizing GPU utilization while minimizing costs, with a particular focus on training and fine-tuning large language models.


[Источник](https://www.reddit.com/r/MachineLearning/comments/1hpg3lc/d_how_ive_optimized_gpu_costs_while_training_llms/)

<!-- url_hash:e0b3c2db05e8aa08ecad69cb54371c13daec8c91369934e283e762a28dcc053b -->


## [r/LocalLLaMA] Q: is it a sound idea to build a small computing cluster using 4-8 Orin Nanos?

_Reddit r/LocalLLaMA · 2024-12-30 · score 0.8_

I hope people who know more about GPU hardware can help answer this question — is it possible to set up a small computing cluster using 4-8 [NVIDIA Jetson Orin Nano's](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/nano-super-developer-kit/) (or would it be better to build up such a cluster using a different, likely used NVIDIA GPU?) My goal here is building something that a few others and I can remotely access; I want to primarily use it for the training and inference of deep learning models. I expect that the largest model I will deal with is Llama 3.2 70B, but more typically, models with ~5-40B parameters.


[Источник](https://www.reddit.com/r/LocalLLaMA/comments/1hpwosw/q_is_it_a_sound_idea_to_build_a_small_computing/)

<!-- url_hash:3ad78ef07daab8cf4e731002b7e4a27eda47daba47ceb08d0c9da4fb3b4dff08 -->
