from flask_migrate import MigrateCommand
from flask_script import Manager, Server

from APPS import create_app

app = create_app()
manager = Manager(app)

manager.add_command('start', Server())
manager.add_command('db', MigrateCommand)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manager.run()
