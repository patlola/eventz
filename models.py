from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    Phone = db.Column(db.String(12), unique=True)
    events = db.relationship('EventPerson', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return '<User %r>' % (self.Name)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.Integer, index=True)
    Category = db.Column(db.String(100), index=True);
    Start_date = db.Column(db.String(100), index=True)
    End_date = db.Column(db.String(100), index=True)
    SelectedVenue = db.Column(db.String(200), index=True)
    events = db.relationship('EventPerson', backref='author', lazy='dynamic')

class EventPerson(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	event = db.Column(db.Integer, db.ForeignKey('event.id'))
	person = db.Column(db.Integer, db.ForeignKey('person.id'))
	Is_Organiser = db.Column(db.Boolean)
	
