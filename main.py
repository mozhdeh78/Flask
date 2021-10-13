from flask            import *
from KinderController import *
from HomeController   import *

app = Flask(__name__)

@app.route("/")
def index():
     return KinderController.index()

@app.route("/reserve_class", methods=['POST', 'GET'])
def reserve_class():
    return KinderController.reserve_class()

@app.route("/reserve_delete", methods=['POST','GET'])
def reserve_delete():
    return KinderController.reserve_delete()

if __name__ == "__main__":
    app.run(debug=True) 