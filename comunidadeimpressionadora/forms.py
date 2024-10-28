from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import Email, Length, DataRequired, EqualTo
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[Email(), DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Esse login já existe ! Faça login ou utilize um outro email !')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
    lembrar_dados = BooleanField('Lembra Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[Email(), DataRequired()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])

    curso_excel = BooleanField('Curso de Excel')
    curso_vba = BooleanField('Curso de VBA')
    curso_htmlcss = BooleanField('Curso de HTML e CSS')
    curso_powerbi = BooleanField('Curso de Power BI')
    curso_python = BooleanField('Curso de Python')
    curso_sql = BooleanField('Curso de SQL')
    
    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Esse login já existe ! Faça login ou utilize um outro email !')
            
class FormPost(FlaskForm):
    titulo = StringField('Titulo do Post', validators=[DataRequired()])
    corpo = TextAreaField('Texto do Post', validators=[DataRequired()])
    botao_post = SubmitField('Publicar Post')