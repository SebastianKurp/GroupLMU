# GroupLMU

This assignment allows the user to store several text files in memory and then search them for keywords or special characters.  In addition to this, users can write notes, highlight them, and store them for access anywhere, all from a new GUI.

Latest version is from commit 8ce5769, made 10/19

To run:

    download git branch or other terminal

    clone into the directory of your choice
    git clone git@github.com:SebastianKurp/GroupLMU.git

    ensure python version installed (version 3 at least)

    To run project (Unix machine): 
    Set up virtualenv (optional, but suggested).
	
	1. Navigate to the GroupLMU/testweb directory
	2. In terminal type:'virtualenv name-of-your-virtual-environment' (let's call it env)
	3. Terminal: 'env/bin/pip install requests'
	4. Terminal:'source env/bin/activate'
	
	You should now be in a virtualenv and any installations will not be global.
	
	5. Terminal:'pip install -r requirements.txt'
	6. Terminal:'python manage.py runserver'
	7. Navigate to the development server noted in the terminal. This seems to generally be 127.0.0.1:8000
	8. Append /admin to those numbers for the admin page and /notes for the main page users would see. 
		Ex: 127.0.0.1:8000/notes
		
For Windows users: Step 3 would be 'env\Scripts\activate.bat'

**NOTE**: If you encounter error **PEP 263** this means your virtualenv was created in Python 2. Deactivate your virtualenv (Terminal: 'deactivate') and type the following commands:

	1. virtualenv -p /usr/bin/python3 name-of-env (call it env3)
	2. source env3/bin/activate
	3. Follow steps 5 - 8 above

The hosted version of this website can be found at http://evercat2.pdu95b9ven.us-east-2.elasticbeanstalk.com/

**NOTE FOR SOCIAL AUTH**: The GitHub social auth feature only works on the hosted version of the website.

A brief overview of how to use the web-cat-app can be found in the Wiki under 'Get Started'

See Wiki for more detailed information on construction and outline

Paul Narup, Eva Martinuzzi, Cat Litten, Sebastian Kurpiel, and Abdul Zakkar © 2017, Loyola University Chicago
