from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from http import HTTPStatus
from backend.schemas import UserSchema, UserPublic, UserDB, UserList

app = FastAPI()

# Banco de dados simulado (uma lista para armazenar os usuários)
database = []

# API Endpoints
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
async def create_user(user: UserSchema):
    """
    Cria um novo usuário e o adiciona ao banco de dados simulado.

    Args:
        - user: Dados do usuário a ser criado (username, email, password).
    
    Returns:
        - UserPublic: Dados do usuário recém-criado (id, username, email).
    """
    # Criar um novo usuário com ID único
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    # Retornar dados públicos do usuário
    new_user = UserPublic(id=user_with_id.id, username=user_with_id.username, email=user_with_id.email)
    return new_user


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
async def get_users():
    """
    Retorna a lista de usuários registrados no banco de dados simulado.

    Retorna:
        - Uma UserList com todos os usuários.
    """
    # Criar uma lista de usuários com as informações públicas
    return {'users': [UserPublic(id=user.id, username=user.username, email=user.email) for user in database]}

@app.get('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
async def get_user(user_id: int):
    for existing_user in database:
        if existing_user.id == user_id:
            return existing_user
    raise HTTPException(status_code=404, detail="User not found")


@app.put('/users/{user_id}', response_model=UserPublic)
async def update_user(user_id: int, user: UserSchema):
    for existing_user in database:
        if existing_user.id == user_id:
            user_with_id = UserPublic(**user.model_dump(), id=user_id)
            database[user_id - 1] = user_with_id
            return user_with_id
    raise HTTPException(status_code=404, detail="User not found")


@app.delete('/users/{user_id}', response_model=UserPublic)
async def delete_user(user_id: int):
    for existing_user in database:
        if existing_user.id == user_id:
            database.remove(existing_user)
            return existing_user
    raise HTTPException(status_code=404, detail="User not found")


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (ou substitua pelo domínio específico do frontend)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)