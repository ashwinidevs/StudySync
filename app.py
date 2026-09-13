from flask import *
from db import *
import model
from functools import wraps
app=Flask(__name__)
Base.metadata.create_all(bind=engine)
app.secret_key="secrete123"
@app.route("/")
def home():
    return redirect("/login")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    db=sessionLocal()
    if request.method=="POST":
        username=request.form.get("username")
        email=request.form.get("email")
        password=request.form.get("password")
        existing_user=db.query(model.User).filter_by(email=email).first()
        if existing_user:
            return render_template("login.html")
        else:
            user=model.User(email=email,username=username,password=password)
            db.add(user)
            db.commit()
            return redirect("/dashboard")
    return render_template("signup.html")
    
@app.route("/login", methods=["GET", "POST"])
def login():
    db=sessionLocal()
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        user = db.query(model.User).filter(model.User.username == username,model.User.password == password).first()        
        if user:
            session["user"]=user.email #tell to remember the user when they move from one page to another
            return redirect("/dashboard")
        else:
            return redirect("/signup")
    return render_template("login.html")

@app.route("/forgot",methods=["GET", "POST"])
def forgot():
    db=sessionLocal()
    if request.method=="POST":
        username=request.form.get("username")
        email=request.form.get("email")
        new_pass=request.form.get("newpassword")
        user=db.query(model.User).filter_by(username=username,email=email).first()
        if user:
            user.password=new_pass
            db.commit()
            db.close()
            return redirect("/login")
        db.close()
        return redirect("/login")
    return render_template("forgot.html")
        

def login_required(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        if "user" not in session:
            return redirect(url_for("home"))
        return f(*args,**kwargs)
    return wrapper

@app.route("/base")
@login_required
def base():
    return render_template("base.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/add_sub", methods=["GET", "POST"])
@login_required
def add_sub():
    db = sessionLocal()

    if request.method == "POST":
        sub_name = request.form.get("subjectnm")
        exam_date = request.form.get("exam_date")
        difficulty_lvl = request.form.get("difficulty")

        if sub_name and exam_date and difficulty_lvl:
            try:
                sub = model.Subject(
                    subject_name=sub_name,
                    exam_date=exam_date,
                    difficulty_lvl=difficulty_lvl
                )

                db.add(sub)
                db.commit()

                flash("Subject added successfully!")
                return redirect("/add_sub")

            except IntegrityError:
                db.rollback()
                flash("Subject already exists!")
                return redirect("/add_sub")

    return render_template("subject.html") 

@app.route("/today_plan")
@login_required
def today_plan():
    return render_template("today_plan.html")

@app.route("/progress")
@login_required
def progress():
    return render_template("progress.html")

@app.route("/analytics")
@login_required
def analytics():
    return render_template("analytics.html")



@app.route("/edit_sub")
@login_required
def edit_sub():
    return render_template("edit_sub.html")

@app.route("/setting")
@login_required
def setting():
    return render_template("setting.html")

    
if __name__ == "__main__":
    app.run(debug=True)