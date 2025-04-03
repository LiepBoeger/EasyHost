from datetime import date
from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, SelectField, SubmitField
from wtforms.fields.datetime import DateField
from wtforms.validators import DataRequired, NumberRange, ValidationError


class AluguelForm(FlaskForm):
    casa = SelectField('Casa', coerce=int, validators=[DataRequired()])
    quantidade_pessoas = IntegerField('Quantidade de Pessoas', validators=[DataRequired(), NumberRange(min=1)])
    observacoes = TextAreaField('Observações')
    data_inicio = DateField('Data de Início',
                            format='%Y-%m-%d',
                            validators=[DataRequired()],
                            default=date.today)  # Data atual como padrão
    submit = SubmitField('Cadastrar Aluguel')

def validate_casa(self, field):
    if field.data == '' or field.data is None:
        raise ValidationError('Por favor selecione uma residência')