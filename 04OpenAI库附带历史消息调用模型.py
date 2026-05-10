from openai import OpenAI

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role":"system","content":"你是一个python专家，并且不说废话简单回答！"},
        {"role":"assistant","content":"好的，我是一个编程专家，并且不说废话！你要问什么？"},
        {"role":"user","content":"小明有2条狗"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"小红有3条猫"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"总共有多少只宠物，多少只狗多少只猫"}
    ],
    stream=True
)
for chunk in response:
    print(chunk.choices[0].delta.content,end=" ",flush=True)