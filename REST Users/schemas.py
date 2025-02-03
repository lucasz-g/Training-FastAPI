from pydantic import field_validator, BaseModel, EmailStr
import re

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

    @field_validator('email')
    def validate_email(cls, email):
        if '@' not in email:
            raise ValueError('Email inválido.')
        return email
    
    @field_validator('password')
    def validate_password(cls, password):
        # Validação: A senha deve ter pelo menos 8 caracteres, 1 letra maiúscula e 1 número
        if len(password) < 8:
            raise ValueError('A senha deve ter pelo menos 8 caracteres.')
        if not re.search(r'[A-Z]', password):
            raise ValueError('A senha deve conter pelo menos uma letra maiúscula.')
        if not re.search(r'[0-9]', password):
            raise ValueError('A senha deve conter pelo menos um número.')
        return password

class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr

# Dados do usuário no banco de dados (inclui informações essenciais)
class UserDB(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: str  # Adicionando a senha aqui, se necessário

class UserList(BaseModel):
    users: list[UserPublic]