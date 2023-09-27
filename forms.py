from flask_wtf import FlaskForm
from wtforms import FloatField,DateField,StringField, SubmitField,SelectField, PasswordField, IntegerField, BooleanField, SelectMultipleField, RadioField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf.file import FileField, FileRequired

#Formulario de registro

class cliente(FlaskForm):
    nombre = StringField('Nombre:', validators=[DataRequired(), Length(max=100)])
    correo = StringField('Email:', validators=[DataRequired(), Length(max=150)])
    telefono = StringField('Teléfono:', validators=[DataRequired(), Length(max=20)])
    asunto = StringField('Asunto:', validators=[DataRequired(), Length(max=500)])
    tipo = SelectField('Elija una opción a continuación:*', choices=[
        ('','Tipo'), 
        ('1','Proceso de compra venta de inmmuebles'), 
        ('2','Construcción'),
        ('3','Derecho de sucesiones y herencias internacionales'),
        ('4','Impuestos patrimoniales')], validators=[DataRequired()])
    

    nacionalidad = SelectField('Nacionalidad:*', choices=[
        ('','Tipo'), 
        ('1','español'), 
        ('2','francés'),
        ('3','inglés'),
        ('4','alemán')], validators=[DataRequired()])
    
    descripcion = StringField('Introduzca su mensaje aquí...', validators=[DataRequired(), Length(max=1000)])
    politica = BooleanField('He leído y acepto los términos y condiciones de uso, así como la política de privacidad según mis preferencias publicitarias aquí detalladas (donde puedo darme de baja de todo lo que no quiero recibir) y la política de cookies.')
    info = BooleanField('Acepto recibir información comercial, ofertas y boletines.')
    submit = SubmitField('Aceptar')
    