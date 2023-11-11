# LLM Riddles

简体中文(https://github.com/qfc123/LLMRiddles/blob/main/README.md) | English

## :thinking: What's This
Welcome to LLM Riddles! This is a game of wits and courage with language models. In the game, you need to construct questions that interact with the language model to get answers that meet the requirements. In this process, you can use your brain and use all the methods you can think of to get the model to output the results required by the answer.

## :space_invader: How to Play
We provide an online version for players to directly access and try out.
- [Hugging Face][ChatGPT + English(w/o key)](https://huggingface.co/spaces/OpenDILabCommunity/LLMRiddlesChatGPTEN)
- [Hugging Face][ChatGPT + Chinese(w/o key)](https://huggingface.co/spaces/OpenDILabCommunity/LLMRiddlesChatGPTCN)
- [Hugging Face][ChatGLM + English(w/ key)](https://huggingface.co/spaces/OpenDILabCommunity/LLMRiddlesChatGLMEN)
- [Hugging Face][ChatGLM + Chinese(w/ key)](https://huggingface.co/spaces/OpenDILabCommunity/LLMRiddlesChatGLMCN)
- [OpenXLab][ChatGPT + Chinese(w/o key)](https://openxlab.org.cn/apps/detail/OpenDILab/LLMRiddlesChatGPTCN)
- [OpenXLab][ChatGPT + English(w/o key)](https://openxlab.org.cn/apps/detail/OpenDILab/LLMRiddlesChatGPTEN)
- [OpenXLab][ChatGLM + Chinese(w/ key)](https://openxlab.org.cn/apps/detail/OpenDILab/LLMRiddlesChatGLMCN)
- [OpenXLab][ChatGLM + English(w/ key)](https://openxlab.org.cn/apps/detail/OpenDILab/LLMRiddlesChatGLMEN)
- [Private Server][Mistral + English(w/ key)](https://d9b451a97791dd8ef3.gradio.live)
- [Private Server][ChatGPT + Chinese(w/ key)](http://llmriddles.opendilab.net/)

Local deployment can be done in the following ways:
### ChatGPT + Chinese
```shell
QUESTION_LANG=cn QUESTION_LLM='chatgpt' QUESTION_LLM_KEY=<your API key> python3 -u app.py
```
### ChatGPT + English
```shell
QUESTION_LANG=en QUESTION_LLM='chatgpt' QUESTION_LLM_KEY=<your API key> python3 -u app.py
```
### Mistral-7B-Instruct-v0.1 + English
```shell
QUESTION_LANG=en QUESTION_LLM='mistral-7b' python3 -u app.py
```
## :technologist: Why Doing This

Our goal is to use this game to give participants a deeper understanding of the fascinating aspects of prompt engineering and natural language processing. This process will show players how to cleverly construct prompts and how to use them to trigger surprising responses from artificial intelligence systems, while also helping them better understand the incredible power of deep learning and natural language processing technologies. .

## :raising_hand: How to Submit a Custom Level
If you have interesting questions or ideas, players are welcome to submit their own ideas.
The question format should include the following points:
- Pull Request title, example: feature(username): Chapter X-Level Design
- The ID you want to be mentioned
- Modify the corresponding chapter question files
- Modification of \__init__.py

## :writing_hand: Roadmap

- [x] Support custom levels
- [x] Online trial link
- [x] Hugging Face Space link
- [x] Support Mistral-7B（English version）
- [x] Support ChatGLM（Chinese version）
- [x] Support Baidu version）
- [ ] LLM inference speed optimization

## :star2: Special Thanks
- Thanks to [Haoqiang Fan](https://www.zhihu.com/people/haoqiang-fan) for his original idea and title, which provided inspiration and motivation for the development and expansion of this project.
- Thanks to [HuggingFace](https://huggingface.co) for supporting and assisting the game.
- Thanks to [百度智能云](https://cloud.baidu.com/) for supporting and assisting the game.
- Thanks to [智谱AI](https://open.bigmodel.cn/)  for supporting and assisting the game.
- Thanks to [LLM Riddles contributors](https://github.com/opendilab/LLMRiddles/graphs/contributors) for their implementation and support.

## :label: License
All code within this repository is under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

<p align="right">(<a href="#top">back to top</a>)</p>
