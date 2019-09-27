from flask import Flask, render_template

from wtform_fields import *
from models import *

#Configure app
app = Flask(__name__)
app.secret_key = 'replace later'

#Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jdjznzafstcjft:16bb049550222566b64ba5e638d1814bfb01665df909348132788c3725cb9755@ec2-107-20-251-130.compute-1.amazonaws.com:5432/dang8dsqseqdi6'
db = SQLAlchemy(app)


@app.route("/", methods=['GET','POST'])
def index():

    reg_form = RegistrationForm()

    if reg_form.validate_on_submit(): #is there no validation errors in the form and the form has been submitted with POST method
        username = reg_form.username.data
        password = reg_form.password.data

        #Check username exists
        user_object = User.query.filter_by(username = username).first() #query - SQLAlchemy's attribute that we can use to get the data from the database
        if user_object:
            return "Someone else has taken this username!"
        
        #Add user to the DB
        user = User(username = username, password = password)
        db.session.add(user)
        db.session.commit()
        return "Inserted into DB!"

    return render_template("index.html", form = reg_form)

if __name__ == "__main__":
    app.run(debug=True)