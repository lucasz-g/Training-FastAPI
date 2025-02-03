from sqlalchemy import select
from backend.models import User


def test_create_user(session):
    # Criação do usuário
    new_user = User(username="alice", password="secret", email="teste@test.com")
    session.add(new_user)
    session.commit()
    session.refresh(new_user)  # Garante que os dados foram realmente persistidos

    # Consulta ao banco de dados
    user = session.scalar(select(User).where(User.username == "alice"))

    # Asserts para validar a criação do usuário
    assert user is not None, "Usuário não foi encontrado no banco de dados"
    assert user.username == "alice"
    assert user.email == "teste@test.com"
    assert user.password == "secret"  # Idealmente, a senha deveria ser hash