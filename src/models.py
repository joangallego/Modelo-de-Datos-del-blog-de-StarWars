from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    fecha_suscripcion = db.Column(db.DateTime, nullable=False)
    favoritos = db.relationship('Favorito', backref='usuario', lazy=True)

class Personaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    descripcion = db.Column(db.String(250))
    favoritos = db.relationship('Favorito', backref='personaje', lazy=True)

class Planeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    clima = db.Column(db.String(50))
    terreno = db.Column(db.String(50))
    favoritos = db.relationship('Favorito', backref='planeta', lazy=True)

class Favorito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    personaje_id = db.Column(db.Integer, db.ForeignKey('personaje.id'), nullable=True)
    planeta_id = db.Column(db.Integer, db.ForeignKey('planeta.id'), nullable=True)

    def __repr__(self):
        return f'<Favorito usuario={self.usuario_id} personaje={self.personaje_id} planeta={self.planeta_id}>'
