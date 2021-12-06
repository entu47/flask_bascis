from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Test*1234@localhost/fynd"
db = SQLAlchemy(app)


class Student(db.Model):
    roll_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(30))

# db.create_all()


@app.route('/result', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # import pdb;pdb.set_trace()
        form_dict = request.form
        student_obj = Student()
        student_dict = vars(student_obj)
        for k, v in form_dict.items():
            student_dict[k] = v
        db.session.add(student_obj)
        db.session.commit()
        return "success"
    else:
        return render_template('home.html')


@app.route('/result/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        form_dict = request.form
        student = Student.query.filter_by(roll_no=id).update(form_dict)
        # student_dict = vars(student)
        # import pdb;pdb.set_trace()
        # for k, v in form_dict.items():
        #     student_dict[k] = v
        # db.session.update()
        # student.update(form_dict)
        db.session.commit()
        import pdb
        pdb.set_trace()
        return "success"
    else:
        return render_template('update.html')
