from dataclasses import asdict

from sqlalchemy import select

from fastapi_zero.models import User


def test_create_user(session, mock_db_time):  # fixture session e mock_db_time
    with mock_db_time(model=User) as time:
        new_user = User(
            username='alice', password='secret', email='teste@test'
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))
    # breakpoint()

    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'password': 'secret',
        'email': 'teste@test',
        'created_at': time,
        'updated_at': time,  # Exercício
    }


# def test_create_user(session, mock_db_time):
#     user = User(username='alice', password='secret', email='teste@test')
#     session.add(user)
#     session.commit()

#     # Scalar: Transforma tudo que vem do banco de dados em um objeto python
#     user = session.scalar(
#         select(User).where(User.username == 'alice')
#     )

#     assert user.username == 'alice'
