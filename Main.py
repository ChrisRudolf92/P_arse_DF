import Document_Class as dc
from tkinter import Tk
from tkinter import filedialog as fd

if __name__ == "__main__":

    root = Tk()
    root.title("P(arse)DF")
    Handler = dc.Parsing_Handler()
    Handler.set_wd()
    dirname = fd.askdirectory(parent=root, initialdir="/", title='Please select a directory')
    Handler.parse(dirname)





