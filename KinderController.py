from BaseController import *
from DB import *

class KinderController(BaseController):
    def index():
        data = DB("kindergard.db", "reserve").get()
        
        return BaseController.view("index", data)

    def reserve_class():
        name = request.args.get("name",False)
        mobile = request.args.get("mobile",False)
        cls=request.args.get("cls",False)

        DB("kindergard.db", "reserve").add( 
            "(name, mobile, classid)", 
            f"('{name}', '{mobile}', '{cls}')"
        )

        return redirect("/#register")
    
    def reserve_delete():
        rowid = request.args.get("rowid")
        
        if rowid is not None:
            DB("kindergard.db", "reserve").remove(rowid)
            
        return redirect("/#register")