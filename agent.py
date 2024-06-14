import os
import dotenv

from llm_selector import LLMSelector
dotenv.load_dotenv(override=True)

AZURE_API_BASE = os.environ['AZURE_API_BASE']
AZURE_API_KEY = os.environ['AZURE_API_KEY']
AZURE_API_VERSION = os.environ['AZURE_API_VERSION']
AZURE_API_TYPE = os.environ['AZURE_API_TYPE']


class Agent:
    def __init__(
        self,
        type_llm : str = 'gpt',
        task : str = 'html',
        flow : str ='function_call'
    ):
        self.type_llm = type_llm
        self.task = task
        self.flow = flow
        self.selector = LLMSelector(
            type_llm=self.type_llm,
            task=self.task,
            flow=self.flow
            )
        
        self.llm = self.selector.match()
        
    
    def run(self, html: str):
        answer = self.llm.generate_text(html=html)
        return answer