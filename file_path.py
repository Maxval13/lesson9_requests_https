import os
from pprint import pprint

class File_:

    def __init__(self, path_to_file):
        self.path_to_f = path_to_file

    def files(self, path_to_f):
        for file in os.listdir(self.path_to_f):
            if os.path.isfile(os.path.join(self.path_to_f, file)):
                yield file

    def file_dict(self):
        list_d = {}
        list_l = []
        for file in self.files("."):
            list_l.append(file)
        for i in range(len(list_l)):
            list_d.setdefault(i, list_l[i])
        pprint(list_d)
        return list_d
