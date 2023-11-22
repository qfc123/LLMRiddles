# LLM Riddles

简体中文| English(https://github.com/qfc123/LLMRiddles/blob/main/README_en.md) 

## :thinking: 什么是LLM Riddles
欢迎来到 LLM Riddles！这是一个与语言模型斗智斗勇的游戏。在游戏中，你需要构造与语言模型交互的问题，来得到符合要求的答案。在这个过程中，你可以开动脑筋，用你想到的所有方式，让模型输出答案要求的结果。

## b站试玩教程(https://www.bilibili.com/video/BV1GC4y1S72E/?vd_source=72036fc928e5ef56b6a540590b34c53c)

## :space_invader: 如何试玩
我们提供了在线版本以供玩家直接访问试玩:
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
- [智谱AI][ChatGLM + Chinese(w/ key)](http://www.lingziao.com:7860/)

本地部署可以通过以下方式：
### ChatGPT + 中文
```shell
QUESTION_LANG=cn QUESTION_LLM='chatgpt' QUESTION_LLM_KEY=<your API key> python3 -u app.py
```
### ChatGPT + 英文
```shell
QUESTION_LANG=en QUESTION_LLM='chatgpt' QUESTION_LLM_KEY=<your API key> python3 -u app.py
```
### LLaMA2-7b + 中文
```shell
QUESTION_LANG=cn QUESTION_LLM='llama2-7b' python3 -u app.py
```
### LLaMA2-7b + 英文
```shell
QUESTION_LANG=en QUESTION_LLM='llama2-7b' python3 -u app.py
```
## :technologist: 为什么制作这个游戏

我们的目标是通过这一游戏，让参与者深入领略到提示工程（prompt engineering）和自然语言处理的令人着迷之处。这个过程将向玩家们展示，如何巧妙地构建提示词（prompts），以及如何运用它们来引发人工智能系统的惊人反应，同时也帮助他们更好地理解深度学习和自然语言处理技术的不可思议之处。

## :raising_hand: 如何提交设计好的关卡
如果有好玩的问题或想法，欢迎玩家提交自己的创意
问题的设计格式应包含以下几点：
- Pull Request标题，示例：feature(username): 章节X-关卡设计
- 希望被提及的ID
- 对应章节问题文件的修改
- \__init__.py的修改

## :writing_hand: 未来计划

- [x] 支持自定义关卡
- [x] 在线试玩链接
- [x] Hugging Face Space 链接
- [x] 支持Mistral-7B（英文）
- [x] 支持ChatGLM（中文）
- [x] 支持百度文心（中文）
- [ ] LLM 推理速度优化

## :star2: Special Thanks
- 感谢 [Haoqiang Fan](https://www.zhihu.com/people/haoqiang-fan) 的原始创意和题目，为本项目的开发和扩展提供了灵感与动力。
- 感谢 [HuggingFace](https://huggingface.co) 对游戏的支持与协助。
- 感谢 [百度智能云](https://cloud.baidu.com/) 对游戏的支持与协助。
- 感谢 [智谱AI](https://open.bigmodel.cn/) 对游戏的支持与协助。
- 感谢 [LLM Riddles contributors](https://github.com/opendilab/LLMRiddles/graphs/contributors) 的实现与支持。

## :label: License
All code within this repository is under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

<p align="right">(<a href="#top">back to top</a>)</p>
