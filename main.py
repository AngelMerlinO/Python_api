from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/MovilesApi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de datos para Rutine
class Rutine(db.Model):
    __tablename__ = 'rutines'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name

# Modelo de datos para Exercise
class Exercise(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rutine_id = db.Column(db.Integer, db.ForeignKey('rutines.id'), nullable=False)

    def __init__(self, name, rutine_id):
        self.name = name
        self.rutine_id = rutine_id

# Modelo de datos para Register
class Register(db.Model):
    __tablename__ = 'registers'
    id = db.Column(db.Integer, primary_key=True)
    kilogram = db.Column(db.Float, nullable=False)
    repetitions = db.Column(db.Integer, nullable=False)
    series = db.Column(db.Integer, nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)

    def __init__(self, kilogram, repetitions, series, exercise_id):
        self.kilogram = kilogram
        self.repetitions = repetitions
        self.series = series
        self.exercise_id = exercise_id

# Creación de la base de datos
with app.app_context():
    db.create_all()

# Endpoint para agregar una nueva rutina
@app.route('/rutine', methods=['POST'])
def add_rutine():
    data = request.get_json()
    new_rutine = Rutine(name=data['name'])
    db.session.add(new_rutine)
    db.session.commit()
    return jsonify({'id': new_rutine.id, 'name': new_rutine.name})

# Endpoint para obtener todas las rutinas
@app.route('/rutines', methods=['GET'])
def get_rutines():
    rutines = Rutine.query.all()
    result = [{'id': rutine.id, 'name': rutine.name} for rutine in rutines]
    return jsonify(result)

# Endpoint para agregar un nuevo ejercicio a una rutina
@app.route('/exercise', methods=['POST'])
def add_exercise():
    data = request.get_json()
    new_exercise = Exercise(name=data['name'], rutine_id=data['rutine_id'])
    db.session.add(new_exercise)
    db.session.commit()
    return jsonify({'id': new_exercise.id, 'name': new_exercise.name, 'rutine_id': new_exercise.rutine_id})

# Endpoint para obtener todos los ejercicios de una rutina específica
@app.route('/rutine/<int:rutine_id>/exercises', methods=['GET'])
def get_exercises_by_rutine(rutine_id):
    exercises = Exercise.query.filter_by(rutine_id=rutine_id).all()
    result = [{'id': exercise.id, 'name': exercise.name, 'rutine_id': exercise.rutine_id} for exercise in exercises]
    return jsonify(result)

# Endpoint para agregar un nuevo registro a un ejercicio
@app.route('/register', methods=['POST'])
def add_register():
    data = request.get_json()
    new_register = Register(kilogram=data['kilogram'], repetitions=data['repetitions'], series=data['series'], exercise_id=data['exercise_id'])
    db.session.add(new_register)
    db.session.commit()
    return jsonify({'id': new_register.id, 'kilogram': new_register.kilogram, 'repetitions': new_register.repetitions, 'series': new_register.series, 'exercise_id': new_register.exercise_id})

# Endpoint para obtener todos los registros de un ejercicio específico
@app.route('/exercise/<int:exercise_id>/registers', methods=['GET'])
def get_registers_by_exercise(exercise_id):
    registers = Register.query.filter_by(exercise_id=exercise_id).all()
    result = [{'id': register.id, 'kilogram': register.kilogram, 'repetitions': register.repetitions, 'series': register.series, 'exercise_id': register.exercise_id} for register in registers]
    return jsonify(result)

# Endpoint para eliminar una rutina
@app.route('/rutine/<int:rutine_id>', methods=['DELETE'])
def delete_rutine(rutine_id):
    rutine = Rutine.query.get(rutine_id)
    if rutine is None:
        return jsonify({'error': 'Rutine not found'}), 404

    # Opcional: eliminar ejercicios y registros asociados
    exercises = Exercise.query.filter_by(rutine_id=rutine_id).all()
    for exercise in exercises:
        Register.query.filter_by(exercise_id=exercise.id).delete()
        db.session.delete(exercise)

    db.session.delete(rutine)
    db.session.commit()
    return jsonify({'message': 'Rutine deleted successfully'})

# Endpoint para actualizar el nombre de un ejercicio
@app.route('/exercise/<int:exercise_id>', methods=['PUT'])
def update_exercise(exercise_id):
    data = request.get_json()
    exercise = Exercise.query.get(exercise_id)
    if exercise is None:
        return jsonify({'error': 'Exercise not found'}), 404

    exercise.name = data['name']
    db.session.commit()
    return jsonify({'id': exercise.id, 'name': exercise.name, 'rutine_id': exercise.rutine_id})

if __name__ == '__main__':
    app.run(debug=True)