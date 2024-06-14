import os
import json

from typing import Union, Dict

class FileWriter:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.prefix = "[No Json]"
        self.output_path = 'results/'
        self.output_format = "-" * 30 + "Doc {}th\n" + "[Model Output]\n{}\nElapsed Time : {}\n[Label]\n{}\n"

        self._check_output_path()

        self.file_path = os.path.join(self.output_path, file_name)
        self.file = open(self.file_path, mode='w', encoding='utf-8')

    def _check_output_path(self):
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path, exist_ok=True)

    def write(
        self,
        predict: Union[str, Dict],
        label: Dict,
        index: int,
        elapsed_time: float
    ):
        if isinstance(predict, dict):
            predict = json.dumps(predict, indent=4)
        else:
            predict = self.prefix + predict
        
        label = json.dumps(label, indent=4)
        instance = self.output_format.format(str(index), predict, elapsed_time, label)
        self.file.write(instance)

    def close(self):
        self.file.close()
