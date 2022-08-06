from flask import Flask ,render_template,request
import model
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def data():
    if request.method=="POST":
        data=request.form["data"]
        
        
    p=model.accuracy()    
    return render_template("index.html",my_data=p)

# @app.route("/sub",methods=['GET','POST'])  
# def submit():
#     #html ->py
#     if request.method =="POST":
#         name=request.form["username"]
#     #py ->html    
#     return render_template("sub.html",n=name)

if __name__ == "__main__":
    #app.run
    app.run(debug=True) 
