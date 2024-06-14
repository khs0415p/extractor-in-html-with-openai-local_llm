# OpenAI 및 Local LLM을 이용하여 HTML에서 정보 추출

## arguments

- type_llm : "gpt" or "local"로 인자로 줄 수 있으며, 각각 gpt-4o와 phi-3-medium을 사용함
- task : "html" or "css"로 인자를 줄 수 있으며, 둘의 차이는 아래에 서술
- flow : "prompt"와 "function_call"로 인자를 줄 수 있으며, prompt를 사용할지 function call 기능을 사용할지 선택

<br>

## 1. --task가 html인 경우

### 개요
주어진 html에서 제목, 날짜, 본문(텍스트, 이미지, 표)의 텍스트를 및 url을 추출하는 task

### 실행
```
python main.py --type_llm [gpt|local] --task html --flow [prompt|function_call]
```

_type_llm이 local인 경우, function_call을 사용할 수 없다._

## 2. --task가 css인 경우

### 개요
주어진 html에서 제목, 날짜, 본문(텍스트, 이미지, 표)의 css selector를 추출하는 task

### 실행
```
python main.py --type_llm [gpt|local] --task css --flow [prompt|function_call]
```

_type_llm이 local인 경우, function_call을 사용할 수 없다._

<br>

## 결과

결과는 `results/`폴더에 `{type_llm}-{task}-{flow}-text.txt`파일로 저장됨

<br>

__결과 예시__

```
[Model Ouput]
{
    "title" : "~~~",
    "date" : "YYYY.MM.DD",
    "content" : [
        {
            "type" : "txt",
            "data" : "text ..."
        },
        {
            "type" : "image",
            "source" : "url ..."
        },
        {
            "type" : "table"
            "data" : "text ..."
        }
    ]
}
Elapsed Time : 00.00000
[Label]
{
    ...
}
```
