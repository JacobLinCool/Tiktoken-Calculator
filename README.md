---
title: Tiktoken Calculator
emoji: 🤗
colorFrom: yellow
colorTo: orange
sdk: gradio
app_file: app.py
python_version: 3.11
pinned: false
---

# Tiktoken Calculator

Calculate the token count for GPT-4, GPT-3.5, GPT-3, and GPT-2.

> It uses [openai/tiktoken](https://github.com/openai/tiktoken) to calculate the token count.

## How to use

### HuggingFace Spaces

Go to <https://huggingface.co/spaces/JacobLinCool/tiktoken-calculator> and try it out!

### Docker

There is a pre-built Docker image available on Docker Hub: <https://hub.docker.com/r/jacoblincool/tiktoken-calculator>

```bash
docker run -p 7860:7860 jacoblincool/tiktoken-calculator
```

If you prefer to use Docker Compose, you can clone this repository and run:

```bash
docker compose up -d
```

### Local

I use Poetry to manage dependencies.

Setup the virtual environment after cloning this repository:

```bash
poetry install
```

Then run the app:

```bash
poetry run python app.py
```
