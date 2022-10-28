import requests
from pprint import pprint


class YaUploader:
    host = 'https://cloud-api.yandex.net'

    # принимаем токен
    def __init__(self, token):
        self.token = token

    # формируем заголовки
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    # метод для получения данных
    def get_files_list(self):
        url = f'{self.host}/v1/disk/resources/files/'
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        pprint(response.json())

    # функция получения ссылки для загрузки
    def _get_upload_link(self, path):
        url = f'{self.host}/v1/disk/resources/upload/'
        headers = self.get_headers()
        params = {'path': path, 'overwrite': True}
        response = requests.get(url, params=params, headers=headers)
        return response.json().get('href')

    # функция загрузки
    def upload_file(self, path, file_name):
        upload_link = self._get_upload_link(path)
        headers = self.get_headers()
        response = requests.put(upload_link, data=open(file_name, 'rb'), headers=headers)
        response.raise_for_status()
        if response.status_code == 201:
            print('Файл успешно загружен')
