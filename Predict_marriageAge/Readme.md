# Problem Statement

Predicing Year of Marriage model deployment with Flask-AWS

# Steps for Model Building and  hosting local API
1. Data Preparation
2. Machine Learning Modelling
3. Model Evaluation
4. Export Trained Model
5. LOCAL REST API with Flask web-server 
6. Create a website for predicing marriage age calling REST API

# Steps for Deploying Public API to AWS EC2 server and launch website service 

1. Spin up an EC2 server
2. Configure EC2 with security group and private key
3. Install libraries and dependencies on the EC2 server
4. Move trained model and app.py flask files to EC2 (winscp)
5. Configure flaskapp.wsgi file and Apache vhost file
6. Restart apache webserver and Check API status
7. Launch a website with domain name and host webpage.

# Notes about how to create ec2 server

1.set appropriate security groups conf and save private key (pem)
2.Using puttygen to convert private pem key to ppk (for MAC this is not necessary)

3.Login into ec2 server

Commands:
python3 -V

curl -O https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

sudo apt-get update

sudo pip install flask, flask_cors, sklearn, apache2 , libapache2-mod-wsgi-py3

4.Configure  /etc/apache2/sites-enabled/000-default.conf

------- Apache Host file configuration
------- file: /etc/apache2/sites-enabled/000-default.conf add this below content 
DocumentRoot /home/ubuntu/mlapp
WSGIDaemonProcess flaskapp threads=5 python-home=/usr/local/lib/python3.5/site-packages/ user=ubuntu
        WSGIScriptAlias / /home/ubuntu/mlapp/flaskapp.wsgi
<Directory /home/ubuntu/mlapp>
            WSGIProcessGroup flaskapp
            WSGIApplicationGroup %{GLOBAL}
            Require all granted
        </Directory>
———————

Create directory  /home/ubuntu/mlapp
Create file flaskapp.wsgi  at mlapp directory with content below

----------------- file : Flaskapp.wsgi
import sys
import site
site.addsitedir(‘/home/ubuntu/.local/lib/python3.5/site-packages’)
sys.path.insert(0, ‘/home/ubuntu/mlapp’)
from app import app as application
------------

5.copy app.py and predict_model.ml files to EC2  /home/ubuntu/mlapp
(recommended winscp app in windows, scp command line in Mac)

sudo apachectl restart

6.On succesful deployment, below url should work and return predicted age of marriage.
http://<your API public ip>/predict?gender=1&caste=2&religion=2&mother_tongue=5&country=4&height_cms=176

