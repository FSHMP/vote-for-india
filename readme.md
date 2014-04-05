# Vote for India
Vote for India is an app which will try to match your ideology with the political parties.

# Setting up this Project
## Step 1 - Clone the repository
1. Open your terminal
2. Install `git` if you do not have one (apt-get for ubuntu, yum for fedora)

            sudo apt-get install git-core
            sudo yum install git-core

3. git clone git@github.com:PuduvaiGLUG/vote-for-india.git

## Step 2 - Install Flask
1. Before installing Flask, please try to install virtualenvironment and virtualenvwrapper. Follow this link (http://www.pythoncentral.io/how-to-install-virtualenv-python/)

2. Activate the Virtualenv
3. Install Flask using Pip like this

                pip install -U Flask
                
## Step 3 - Run the application
1. Now cd into the cloned directory and also into wsgi dir
2. Start the app like this

                python manage.py
                
3. This will start the app in the default port number 5000 and will be available at

                http://localhost:5000
                or
                http://127.0.0.1:5000
                
4. Visit the above address in your web-browser. If everything are fine, the app will be up and running and you should see the homepage of the website.

This application is licenced under GPL V3.0. Developed by Team PuduvaiGLUG and FSFTN-VPM.
