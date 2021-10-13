from BaseController import *

class HomeController(BaseController):
    def index():
        user = "python"
        return BaseController.view("index", user)