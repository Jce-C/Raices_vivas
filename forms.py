from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SelectField, IntegerField, DecimalField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange, ValidationError
from models import User

class LoginForm(FlaskForm):
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recordar por 30 días')

class RegisterForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired(), Length(min=4, max=20)])
    first_name = StringField('Nombre', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Apellido', validators=[DataRequired(), Length(max=50)])
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirmar contraseña', 
                             validators=[DataRequired(), EqualTo('password')])
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Este nombre de usuario ya está en uso.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Este correo electrónico ya está registrado.')

class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=100)])
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    subject = StringField('Asunto', validators=[Length(max=200)])
    message = TextAreaField('Mensaje', validators=[DataRequired(), Length(max=1000)])

class CheckoutForm(FlaskForm):
    # Billing information
    billing_first_name = StringField('Nombre', validators=[DataRequired(), Length(max=50)])
    billing_last_name = StringField('Apellido', validators=[DataRequired(), Length(max=50)])
    billing_email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    billing_phone = StringField('Teléfono', validators=[DataRequired(), Length(max=20)])
    billing_address = TextAreaField('Dirección', validators=[DataRequired()])
    billing_city = StringField('Ciudad', validators=[DataRequired(), Length(max=50)])
    billing_country = SelectField('País/Región', 
                                 choices=[('CO', 'Colombia'), ('US', 'Estados Unidos'), ('MX', 'México')],
                                 validators=[DataRequired()])
    billing_postal_code = StringField('Código postal', validators=[Length(max=20)])
    
    # Payment method
    payment_method = SelectField('Método de pago',
                                choices=[('bank_transfer', 'Transferencia bancaria'), 
                                        ('cash_on_delivery', 'Pago contra entrega')],
                                validators=[DataRequired()])

class AddToCartForm(FlaskForm):
    product_id = HiddenField('Product ID', validators=[DataRequired()])
    quantity = IntegerField('Cantidad', validators=[DataRequired(), NumberRange(min=1)], default=1)
    selected_color = SelectField('Color', choices=[], coerce=str)
