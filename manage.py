from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Note

# from  flask_migrate import Migrate, MigrateCommand# Creating app instance
app = create_app()

manager = Manager(app)
manager.add_command('server',Server)
# migrate = Migrate(app,db)
# manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db,User = User, Note = Note)

if __name__ == '__main__':
    manager.run()