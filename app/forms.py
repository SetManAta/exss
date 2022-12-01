from app import app
from flask_wtf import FlaskForm
import wtforms as ws
from flask_login import current_user

from app.models import User

class EmployeeForm(FlaskForm):
    fullname = ws.StringField('ФИО')
    phone = ws.TelField('Номер телефона')
    short_info = ws.TextAreaField('Краткая информация')
    experience = ws.IntegerField('Опыт работы в годах')
    preferred_position = ws.StringField('Желаемая должность')
    user =  current_user #ws.StringField('Пользователь')
    submit = ws.SubmitField('Сохранить')

    def validate_fullname(self, field):
        names_split = field.data.split(' ')
        if len(names_split) == 1:
            raise ws.ValidationError('Полное имя')
        for name in names_split:
            if not name.isalpha():
                raise ws.ValidationError('В ФИО не спец символ')
   


class UserForm(FlaskForm):
    username = ws.StringField('Имя пользователя', validators=[ws.validators.DataRequired(),])
    password = ws.PasswordField('Пароль', validators=[ws.validators.DataRequired(), ws.validators.Length(min=8, max=24)])
    submit = ws.SubmitField('Сохранить')