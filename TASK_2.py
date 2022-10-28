from pprint import pprint
from ya_disk import YaUploader
from file_path import File_


if __name__ == '__main__':
    with open('TOKEN.txt') as file:
        token = file.readline()
        print(token)
    path_to_file = str(input('Введите путь до файла: '))
    if path_to_file[-1] != '\\':
        path_to_file = path_to_file + '\\'
    file_path = File_(path_to_file)
    list_dict = file_path.file_dict()
    name = int(input('Введите номер загружаемого файла: '))
    file_name = path_to_file + str(list_dict[name])
    print(file_name)
    ya_disk = YaUploader(token)
    ya_disk.upload_file(str(list_dict[name]), file_name)


