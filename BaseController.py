from flask import *

class BaseController:
    def view(page, data):
        return render_template(f"{page}.html", data=data)