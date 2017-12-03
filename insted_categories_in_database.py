from item_database_cat import Category_table
from DB_operation import DB_operations

db = DB_operations()
new_categories = [Category_table(name='Soccer'),
                  Category_table(name='Basketball'),
                  Category_table(name='Frisbee'),
                  Category_table(name='Football'),
                  Category_table(name='Rock Climbing'),
                  Category_table(name='Snow boarding'),
                  Category_table(name='Hockey')]

for new_cat in new_categories:
    db.addDatabase(new_cat)

