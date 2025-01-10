from flask import render_template, request

from models import Subject

from app import create_app

app = create_app()
# def register_routes(app, db):
@app.route('/', methods=['GET', 'POST'])
def index():
    print("index")
    if request.method == 'GET':
        subject = Subject.query.all()
        return render_template ('index.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        hours = request.form.get('hours')
        
        subject = Subject(name=name, hours=hours)
        db.session.add(subject)
        db.session.commit()

        subjects = Subject.query.all()
        return render_template('index.html', subjects=subjects)
    

@app.route('/delete/<sid>', methods=['DELETE'])
def delete(sid):
    Subject.query.filter(Subject.class_id == sid).delete()
    db.session.commit()
    subjects = Subject.query.all()
    return render_template('index.html', subjects=subjects)

@app.route('/details/<sid>')
def details(sid):
    subject = Subject.query.filter(Subject.class_id == sid).first()

    return render_template('details.html', subject=subject)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)