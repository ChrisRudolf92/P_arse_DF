from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty
import os
import Document_Class as dc
from custom_exceptions import PathError

class MyApp(App):

    title = "P(arse)DF"

    cwd_ = StringProperty()
    pdf_dir_ = StringProperty()
    AppHandler = dc.Parsing_Handler()

    def set_cwd_(self, path, filename):
        self.cwd_ = str(os.path.join(path, filename))
        return

    def set_pdf_dir_(self, path, filename):
        self.pdf_dir_ = str(os.path.join(path, filename))
        return

    def print_paths(self):
        print(self.cwd_)
        print(self.pdf_dir_)
        return

    def custom_handle(self):
        if self.cwd_:
            self.AppHandler.wd = self.cwd_
        else:
            self.AppHandler.wd = self.pdf_dir_
        try:
            self.AppHandler.set_wd()
        except PermissionError as PE:
            print(PE.strerror+ ":to create the required directory in directory "+ PE.filename)

    def apply_parser(self):
        try:
            self.AppHandler.parse(self.pdf_dir_)
        except(PathError) as PE:
            print(PE.message)




    #Declare Screen

    class MenuScreen(Screen):
        pass

    class FilechooserScreen(Screen):
        pass

    class FilechooserScreenPDF(Screen):
        pass

    class screen_manager(ScreenManager):
        pass

    def build(self):
        pass



if __name__ == '__main__':
    MyApp().run()