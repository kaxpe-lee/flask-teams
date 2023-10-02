from flask import (Flask, redirect,session, render_template, request, send_from_directory, url_for)
# from flask_sqlalchemy import SQLAlchemy
import os
import pymsteams
app = Flask(__name__)
app.debug = True

#app.config.from_object('config.DevelopmentConfig')
app.config['CONNECTORCARD'] = os.environ.get('CONNECTORCARD')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

from forms import cliente

@app.route('/',methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        telefono = request.form.get('telefono')
        asunto = request.form.get('asunto')
        tipo = request.form.get('tipo')
        nacionalidad = request.form.get('nacionalidad')
        descripcion = request.form.get('descripcion')
        politica = request.form.get('politica')
        info = request.form.get('info')

        import pymsteams

        # Initialize the connector card with your webhook URL
        myTeamsMessage = pymsteams.connectorcard(app.config['CONNECTORCARD'])

        # Set the message color
        myTeamsMessage.color("#F8C471")

        # Add your message text
        myTeamsMessage.text("Hello, this is a sample message!")
        # Create Section 1
        Section1 = pymsteams.cardsection()
        Section1.text(nombre)

        # Create Section 2
        Section2 = pymsteams.cardsection()
        Section2.text(correo)

        #3
        Section3 = pymsteams.cardsection()
        Section3.text(telefono)

        #4
        Section4 = pymsteams.cardsection()
        Section4.text(asunto)

        #5
        Section5 = pymsteams.cardsection()
        Section5.text(tipo)

        #6
        Section6 = pymsteams.cardsection()
        Section6.text(nacionalidad)

        #7
        Section7 = pymsteams.cardsection()
        Section7.text(descripcion)


        # Add both Sections to the main card object
        myTeamsMessage.addSection(Section1)
        myTeamsMessage.addSection(Section2)
        myTeamsMessage.addSection(Section3)
        myTeamsMessage.addSection(Section4)
        myTeamsMessage.addSection(Section5)
        myTeamsMessage.addSection(Section6)
        myTeamsMessage.addSection(Section7)
        # Send the message
        myTeamsMessage.send()
        return "POST"
    elif request.method == 'GET':
        form1 = cliente()
        return render_template('form.html',form1=form1)
    
with app.app_context():
    pass
    #db.session.commit()


if __name__ == '__main__':
    app.run()