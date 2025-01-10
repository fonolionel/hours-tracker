from app import db


class Subject(db.Model):
    class_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    hours = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Subject with name {self.name} inserted'