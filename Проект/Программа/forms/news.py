from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField
from wtforms.validators import DataRequired, ValidationError, InputRequired
    


def github_check(self, project):
    if self.project.data.find('https://github.com') != 0:
        raise ValidationError('Incorrect GitHub URL')
        

class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField("Содержание", validators=[DataRequired()])
    project = StringField('Ссылка GitHub на проект', validators=[InputRequired(), github_check])
    submit = SubmitField('Применить')
