from flask import render_template, url_for, request, redirect

from models import db, Pet, app


@app.route('/')
def index():
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    if request.form:
        print(request.form)
        print(request.form['name'])
        new_pet = Pet(
            name=request.form['name'],
            age=request.form['age'],
            breed=request.form['breed'],
            color=request.form['color'],
            size=request.form['size'],
            weight=request.form['weight'],
            url=request.form['url'],  # Use lowercase 'url'
            alt_tag=request.form['alt_tag'],  # Use lowercase 'alt'
            pet_type=request.form['pet'],  # Use lowercase 'pet'
            gender=request.form['gender'],  # Use lowercase 'gender'
            spay=request.form['spay'],  # Use lowercase 'spay'
            house_trained=request.form['housetrained'],
            description=request.form['description']
        )
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addpet.html')

@app.route('/pet/<id>')
def pet(id):
    pet = Pet.query.get_or_404(id)
    return render_template('pet.html', pet=pet)


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_pet(id):
    pet = Pet.query.get_or_404(id)
    if request.form:
        pet.name = request.form['name']
        pet.age = request.form['age']
        pet.breed = request.form['breed']
        pet.color = request.form['color']
        pet.size = request.form['size']
        pet.weight = request.form['weight']
        pet.url = request.form['url']  # Use lowercase 'url'
        pet.alt_tag = request.form['alt_tag']  # Use lowercase 'alt'
        pet.pet_type = request.form['pet']  # Use lowercase 'pet'
        pet.gender = request.form['gender']  # Use lowercase 'gender'
        pet.spay = request.form['spay']  # Use lowercase 'spay'
        pet.house_trained = request.form['housetrained']
        pet.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editpet.html', pet=pet)

@app.route('/delete/<id>')
def delete_pet(id):
    pet = Pet.query.get_or_404(id)
    db.session.delete(pet)
    db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')