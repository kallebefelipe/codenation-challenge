import json


class FileUtils:

    def __init__(self):
        self.file_path = 'answer.json'

    def read(self):
        with open(self.file_path) as json_file:
            return json.load(json_file)

    def write(self, data):
        with open(self.file_path, 'w') as outfile:
            json.dump(data, outfile)
