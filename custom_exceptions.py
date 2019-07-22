class InputError(Exception):
    def __init__(self, name):
        self.expression = "Input Error"
        self.message = "An Input Error Occured while Parsing - PDF "+ str(name) + " got skipped"
        self.name = name
    def return_name(self):
        return str(self.name)

class PathError(Exception):
    def __init__(self):
        self.expression = "Path Error"
        self.message = "An invalid or empty Path was selected"