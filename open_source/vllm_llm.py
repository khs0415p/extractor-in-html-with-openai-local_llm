from transformers import AutoTokenizer
from vllm import LLM, SamplingParams
from prompt import HTML_PROMPT, CSS_PROMPT

SYS_PROMPT_MAPPING = {
    "html" : "You are HTML parser. Responding with reference to the PREREQUISITES.",
    "css" : "You are a css selector extrator. Responding with reference to the PREREQUISITES."
}

PROMPT_MAPPING = {
    "html" : HTML_PROMPT,
    "css" : CSS_PROMPT
}

class OpenSourceLLM:
    def __init__(
        self,
        flow: str = "prompt",
        task: str = "html",
        quant: bool = True,
    ):
        self.flow = flow
        self.task = task
        if self.flow != "prompt":
            raise ValueError(f"Don't Use {self.flow} in open-source llm.")
        
        self.sampling_params = SamplingParams(temperature=0., max_tokens=8192, stop=['```', '### INPUT'])
        
        self.model = LLM(model="microsoft/Phi-3-medium-128k-instruct", max_model_len=35000, dtype="bfloat16", )

        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-medium-128k-instruct", cache_dir="/data")

        self.promp = PROMPT_MAPPING[self.task]


    def generate_text(self, html: str):
        # TODO: css selector
        messages = [
            {
                "role": "user",
                "content": SYS_PROMPT_MAPPING[self.task] + self.promp.format(html)}
        ]

        content = self.tokenizer.apply_chat_template(messages, tokenize=False)

        output = self.model.generate(content, sampling_params=self.sampling_params)
        answer = output[0].outputs[0].text

        return answer


        