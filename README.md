# llama-honeypot-python
![drawed by stable diffusion](https://cdn.studyinglover.com/pic/2023/07/e9a49d4a404ed9bc4b0f119249194e3d.png)

llama-honeypot-python 是一个使用 llama 大语言模型作为后端的蜜罐项目。它模拟了一个 shell 环境，但实际上并不执行任何指令。相反，它使用 llama 模型来生成看起来像是 shell 指令输出的文本，以欺骗攻击者。

## 开发笔记
请查看我的两篇博客
1. [使用llama构建一个蜜罐(后端)](https://studyinglover.com/2023/07/29/%E4%BD%BF%E7%94%A8llama%E6%9E%84%E5%BB%BA%E4%B8%80%E4%B8%AA%E8%9C%9C%E7%BD%90(%E5%90%8E%E7%AB%AF)/)
2. [使用llama构建一个蜜罐(前端)](https://studyinglover.com/2023/08/01/%E4%BD%BF%E7%94%A8llama%E6%9E%84%E5%BB%BA%E4%B8%80%E4%B8%AA%E8%9C%9C%E7%BD%90(%E5%89%8D%E7%AB%AF)/)
## 安装和使用

要使用 llama-honeypot-python，你需要安装 Python 3 和 pip。然后，你可以按照以下步骤进行操作：

1. 克隆此仓库并进入项目目录：
```
git clone https://github.com/your-username/llama-honeypot-python.git cd llama-honeypot-python
```

2. 安装依赖项：
```
pip install -r requirements.txt
```


3. 启动 llama-honeypot-python：
启动llama服务器,修改/path/to/为真实地址
```
python3 -m llama_cpp.server --model /path/to/llama-2-13b-chat.ggmlv3.q4_1.bin
```

启动后端
```
python honeypot_backend.py
```

启动前端
```
python honeypot_frontend.py
```

## 参考项目
[cutecuteyu/chatgpt-honeypot](https://gitee.com/cutecuteyu/chatgpt-honeypot)
[Coldwave96/llama-honeypot](https://github.com/Coldwave96/llama-honeypot)
[ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp)
[abetlen/llama-cpp-python](https://github.com/abetlen/llama-cpp-python)

## TODO
1. 微调llama，或者使用更好的prompt,使其更好的输出。
2. 优化假的终端，模拟一个终端的各种功能。

## 许可证
llama-honeypot-python 使用 Apache License 2.0 许可证。有关更多信息，请参见 LICENSE 文件。