from tika import parser
from custom_exceptions import InputError
from os import path as pt
from os import listdir, getcwd, mkdir, rename

class Document:

    def __init__(self, path, w_dir):
        self._path_ = path
        self._name_ = str(pt.basename(path))
        self._parse_flag_ = True
        self.w_dir_ = w_dir


    def parse (self):

        try:
            self.file_ = open(self.w_dir_ + "/" +self._name_+".txt", "w", encoding = "utf8")
            self.parsed_ = parser.from_file(self._path_)
            self.file_.write(self.parsed_["content"])

        except(KeyError):
            self._parse_flag_ = False
            self.file_.close()
            rename(self.w_dir_ + "/" +self._name_+".txt", self.w_dir_ + "/" +self._name_+ "EMPTY.txt")
            raise InputError(self._name_)






class Parsing_Handler:

    def __init__(self, dir="", wd=getcwd()):

        self.wd = wd
        self.Parsecount = 0
        self.failed = []

        if dir:
            self.parse(dir)

    def set_wd(self, iteration: int = 0) -> int:
        if iteration == 100:
            return
        try:
            mkdir(self.wd + "ParsedTexts_" +str(iteration))
            self.wd = self.wd + "ParsedTexts_" +str(iteration)
        except FileExistsError:
            self.set_wd(iteration+1)



    def parse(self, dir):
        try:
            self._dir_list_ = listdir(dir)
            for file in self._dir_list_:
                if not file.startswith(".") and file.endswith(".pdf"):
                    file_path = dir + file
                    try:
                        Document(file_path, self.wd).parse()
                        self.Parsecount = self.Parsecount + 1
                    except InputError as IE: \
                            self.failed.append(str(IE.name))
                    except (KeyboardInterrupt, FileNotFoundError):
                        pass
        finally:
            print("In total " + str(self.Parsecount) + " files were parsed" + "\n")
            print(self.failed)









