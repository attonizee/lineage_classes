from app import app, db

class L2_classes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    classess = db.Column(db.String(30), index = True, unique = True)
    archers = db.relationship('Archers', backref = 'l2_classes', lazy = 'dynamic')
    warriors = db.relationship('Warriors', backref = 'l2_classes', lazy = 'dynamic')
    mages = db.relationship('Mages', backref = 'l2_classes', lazy = 'dynamic')
    assassins = db.relationship('Assassins', backref = 'l2_classes', lazy = 'dynamic')

    def __repr__(self):
        return f'Class {self.classess}'


class Archers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True, unique = True)
    race = db.Column(db.String(20), index = True, unique = False)
    armor = db.Column(db.String(20), index = True, unique = False)
    weapon = db.Column(db.String(20), index = True, unique = False)
    role = db.Column(db.String(30), index = True, unique = False)
    description = db.Column(db.String(400), index = True, unique = False)
    l2_classes_id = db.Column(db.Integer, db.ForeignKey('l2_classes.id'))

    def __repr__(self):
        return f'Archer class {self.name} main role {self.role}'


class Warriors(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True, unique = True)
    race = db.Column(db.String(20), index = True, unique = False)
    armor = db.Column(db.String(20), index = True, unique = False)
    weapon = db.Column(db.String(20), index = True, unique = False)
    role = db.Column(db.String(30), index = True, unique = False)
    description = db.Column(db.String(400), index = True, unique = False)
    l2_classes_id = db.Column(db.Integer, db.ForeignKey('l2_classes.id'))

    def __repr__(self):
        return f'Warrior class {self.name} main role {self.role}'


class Mages(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True, unique = True)
    race = db.Column(db.String(20), index = True, unique = False)
    armor = db.Column(db.String(20), index = True, unique = False)
    weapon = db.Column(db.String(20), index = True, unique = False)
    role = db.Column(db.String(30), index = True, unique = False)
    description = db.Column(db.String(400), index = True, unique = False)
    l2_classes_id = db.Column(db.Integer, db.ForeignKey('l2_classes.id'))

    def __repr__(self):
        return f'Mage class {self.name} main role {self.role}'


class Assassins(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True, unique = True)
    race = db.Column(db.String(20), index = True, unique = False)
    armor = db.Column(db.String(20), index = True, unique = False)
    weapon = db.Column(db.String(20), index = True, unique = False)
    role = db.Column(db.String(30), index = True, unique = False)
    description = db.Column(db.String(400), index = True, unique = False)
    l2_classes_id = db.Column(db.Integer, db.ForeignKey('l2_classes.id'))

    def __repr__(self):
        return f'Assassin class {self.name} main role {self.role}'