from voteforindia import app
from flask.ext.script import Manager

manager = Manager(app)

if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()
