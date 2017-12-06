from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine

from item_database_cat import Base, Category_table, Item, user_table

url = "postgresql://graderdb:pasword@localhost:5432/catalogdb"

engine = create_engine(url)

Base.metadata.bind = engine

database_session = sessionmaker(bind=engine)

session = database_session()

# create operations class


class DB_operations:
    # add new user
    def adduser(self, login_session):
        newUser = user_table(
            name=login_session['userName'],
            email=login_session['email'],
            img_user=login_session['img_user'])
        session.add(newUser)
        session.commit()
        return

# check if user in database or add it
    def GetUserBy(self, login_session):
        try:
            user = session.query(user_table).filter_by(
                   email=login_session['email']).one()
            return user
        except:
            self.adduser(login_session)
            return session.query(
                user_table).filter_by(email=login_session['email']).one()
# get the category which i want

    def GetCategoryBy(self, cat_id):
        return session.query(Category_table).filter_by(id=cat_id).one()
    # get all categories

    def GetAllCategoryBy(self):
        return session.query(Category_table).all()
    # get the item which i want to the fouces Category

    def GetOneItemBy(self, i_id):
        return session.query(Item).filter_by(id=i_id).join(Category_table).one()

    # get all item which in the fouces Category
    def GetItemBy(self, cat_id):
        return session.query(Item).filter_by(cat_id=cat_id).all()
    # the last 10 item in data

    def Get_last_item(self):
        return session.query(Item).limit(10)

    # add in database or updata
    def addDatabase(self, add_or_updated_element):
        session.add(add_or_updated_element)
        session.commit()
        return

    # delete from database
    def deleteDatabase(self, item):
        session.delete(item)
        session.commit()
        return

