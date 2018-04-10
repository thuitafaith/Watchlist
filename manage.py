from app import create_app,db
from app.models import  User
from flask_script import Manager,Server
app = create_app('development')
manager = Manager(app)
manager.add_command('server',Server)
@manager.command
def test():
    """
    Run unit Tests
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
if __name__=='__main__':
    manager.run()