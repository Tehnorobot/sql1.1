from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    user2 = User()
    user2.surname = "John"
    user2.name = "Gastings"
    user2.age = 30
    user2.position = "coock"
    user2.speciality = "coocks food"
    user2.address = "module_2"
    user2.email = "John@mars.org"
    user2.hashed_password = "coock"
    db_sess = db_session.create_session()
    db_sess.add(user2)
    db_sess.commit()
    user3 = User()
    user3.surname = "Majer"
    user3.name = "Bambula"
    user3.age = 25
    user3.position = "security captain"
    user3.speciality = "security"
    user3.address = "module_3"
    user3.email = "Banbula@mars.org"
    user3.hashed_password = "life"
    db_sess = db_session.create_session()
    db_sess.add(user3)
    db_sess.commit()
    user4 = User()
    user4.surname = "Arthur"
    user4.name = "Reigan"
    user4.age = 54
    user4.position = "chemist"
    user4.speciality = "chemist"
    user4.address = "module_4"
    user4.email = "Reigan@mars.org"
    user4.hashed_password = "chemist"
    db_sess = db_session.create_session()
    db_sess.add(user4)
    db_sess.commit()


if __name__ == '__main__':
    main()