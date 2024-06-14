import os
import dotenv

from typing import Union
from transformers import PreTrainedModel
from llms import OpenAILLM, BaseConnetor
from open_source import OpenSourceLLM

dotenv.load_dotenv(override=True)

AZURE_API_BASE = os.environ['AZURE_API_BASE']
AZURE_API_KEY = os.environ['AZURE_API_KEY']
AZURE_API_VERSION = os.environ['AZURE_API_VERSION']
AZURE_API_TYPE = os.environ['AZURE_API_TYPE']


class LLMSelector:
    def __init__(
        self,
        type_llm: str = "gpt",
        task: str = "html",
        flow: str = "function_call"
    ):
        self.type_llm = type_llm
        self.task = task
        self.flow = flow

    def match(self) -> Union[BaseConnetor, PreTrainedModel]:
        if self.type_llm == "gpt":
            llm = OpenAILLM(
                    openai_api_base=AZURE_API_BASE,
                    openai_api_key=AZURE_API_KEY,
                    openai_api_type=AZURE_API_TYPE,
                    openai_api_version=AZURE_API_VERSION,
                    flow=self.flow,
                    task=self.task
                )
        else:
            llm = OpenSourceLLM(
                    flow = self.flow,
                    task = self.task,
                    quant=False
                )
        
        return llm