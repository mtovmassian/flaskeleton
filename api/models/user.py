from sqlalchemy import Column, Integer, String, Boolean
from api.models import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    is_admin = Column(Boolean, default=False)

    def __repr__(self):
        return "<User(username={0}, first_name={1}, last_name={2}), is_admin={3}>".format(
            self.username, self.first_name, self.last_name, self.is_admin
        )

class UserRepository:

    def __init__(self, session):
        self.session = session

    def find_by_username(self, username: str) -> User:
        try:
            return self.session.query(User).filter(User.username == username).one()
        except Exception as e:
            print(e)
            return None
    
    def save(self, user: User):
        self.session.add(user)
        self.session.commit()