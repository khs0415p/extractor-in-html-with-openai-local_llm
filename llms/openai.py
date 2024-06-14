from openai import AzureOpenAI
from typing import Optional, Dict
from tool import HTML_TOOL, CSS_TOOL
from prompt import HTML_PROMPT, CSS_PROMPT

TOOL_MAPPING = {
    "html" : HTML_TOOL,
    "css" : CSS_TOOL
}

PROMPT_MAPPING = {
    "html" : HTML_PROMPT,
    "css" : CSS_PROMPT
}

SYS_PROMPT_MAPPING = {
    "html" : "You are HTML parser. Responding with reference to the PREREQUISITES.",
    "css" : "You are a css selector extrator. Responding with reference to the PREREQUISITES."
}

FUNC_PROMPT = "You're an assistant to help with function calling."



class BaseConnetor:
    def __init__(
        self,
        deployment: str = "gpt-4o",
        model: str = "gpt-4o",
        openai_api_base: Optional[str] = None,
        openai_api_key: Optional[str] = None,
        openai_api_type: Optional[str] = None,
        openai_api_version: Optional[str] = "2023-05-15",
    ):
        self.deployment = deployment
        self.model = model
        self.openai_api_base = openai_api_base
        self.openai_api_key = openai_api_key
        self.openai_api_type = openai_api_type
        self.openai_api_version = openai_api_version
        self.temperature = .0
        self.max_tokens = 4096
        
        self.client = AzureOpenAI(
            azure_endpoint=self.openai_api_base,
            api_key=self.openai_api_key,
            api_version=self.openai_api_version
        )

    def _get_input_items(
            self,
            content: str,
            ):
        if self.flow == 'function_call':
            messages = [
                {
                    "role": "system",
                    "content": self.system_function_calling,
                },
                {
                    "role": "user",
                    "content": content,
                },
            ]

            return {
                "model" : self.model,
                "messages" : messages,
                "temperature" : self.temperature,
                "max_tokens" : self.max_tokens,
                "tools" : [
                    self.tools
                ],
                "tool_choice" : "auto",
            }
        
        elif self.flow == 'prompt':
            messages = [
                {
                    "role": "system",
                    "content": self.system_prompt,
                },
                {
                    "role": "user",
                    "content": self.prompt.format(content),
                },
            ]

        return {
            "model" : self.model,
            "messages" : messages,
            "temperature" : self.temperature,
            "max_tokens" : self.max_tokens,
        }

    def generate_text(self, html: str):

        response = self.client.chat.completions.create(
                **self._get_input_items(html)
            )
        if self.flow == 'function_call':
            try:
                answer = response.choices[0].message.tool_calls[0].function.arguments
            except:
                answer = response.choices[0].message.content
        else:
            answer = response.choices[0].message.content

        return answer


class OpenAILLM(BaseConnetor):
    def __init__(
            self,
            deployment: str = "gpt-4o",
            model: str = "gpt-4o",
            openai_api_base: str | None = None,
            openai_api_key: str | None = None,
            openai_api_type: str | None = None,
            openai_api_version: str | None = "2023-05-15",
            flow: str = "function_call",
            task: str = "html"
            ):
        super().__init__(deployment, model, openai_api_base, openai_api_key, openai_api_type, openai_api_version)
        self.flow = flow
        self.task = task
        
        self.system_function_calling = FUNC_PROMPT
        self.system_prompt = SYS_PROMPT_MAPPING[self.task]
        self.tools = TOOL_MAPPING[self.task]
        self.prompt = PROMPT_MAPPING[self.task]