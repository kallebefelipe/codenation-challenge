import os
import requests

from decouple import config
from .file_utils import FileUtils


class ApiInterct:

    def __init__(self):
        self.file_utils = FileUtils()
        self.token = config('TOKEN')
        self.url = config('URL')
        self.params = {'token': self.token}
        self.file_path = 'answer.json'

    def get_info(self):
        response = requests.get(
            self.url + 'generate-data',
            params=self.params)
        data_json = response.json()

        self.file_utils.write(data_json)

    def post_info(self):
        _file = open(self.file_path, 'rb')
        _file = {
            'answer': _file
        }

        response = requests.post(
            self.url + 'submit-solution',
            files=_file,
            params=self.params)

        return response
