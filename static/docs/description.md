> Designed with ❤️ by [mianfg](https://mianfg.me)

This is **PictoMaker Lite**, an API to translate sentences into pictograms. You can use **PictoMaker** at [pictomaker.mianfg.me](https://pictomaker.mianfg.me/).

# Introduction

This is a simple API that provides two capabilities:

* A **tokenizer** that syntactically analizes a sentence and lemmatizes its componentes using Natural Language Processing.
* A **generator**, that generates a PNG image or ZIP file composed of pictograms.

## About PictoMaker

### 🤷 Why pictograms?

Learning through pictograms is an essential tool for children with special educational needs, as well as crutial for elder people with Alzheimer's disease and dementia. I developed PictoMaker to make it easy for people to communicate using the power of images.

### 👓 Why do a syntactical analysis?

PictoMaker leverages the power of AI to lemmatize the different words you input (getting the basic form of the word) to search for the images, as well as it uses it to construct a syntactical analysis tree and allow people (and especially children) to better distinguish between words.

### Where are the pictograms coming from?

All pictograms used by PictoMaker are property of [ARASAAC](https://arasaac.org/), from the Aragonese Center of Augmentive and Alternative Communication (Spain).

> This API extensively uses ARASAAC's [API](https://arasaac.org/developers/api).

### Where is PictoMaker Lite used?

This API has been used:

* In [this Cisco WebEx bot](https://github.com/mianfg/Incu2022/tree/main/webex-api-session) developed for Cisco Incubator Program 9.0.

## Source code

You can deploy this API anywhere you like, because it's containerized with **Docker**. Some commands to get you started on a local development environment:

1. Make sure you can use `docker-compose`.
2. Create the container with `docker compose up --build`.
3. Use Docker whenever you want to restart the process!
