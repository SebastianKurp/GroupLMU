# GroupLMU

This assignment allows the user to store several text files in memory and then search them for keywords or special characters.  In addition to this, users can write notes, highlight them, and store them for access anywhere, all from a new GUI.

To run:

    download git branch or other terminal

    clone into the directory of your choice
    git clone git@github.com:SebastianKurp/GroupLMU.git

    ensure python version installed (version 3 at least)

    To run project (Unix machine): 
    Set up virtualenv (optional, but suggested)
	1. 'virtualenv name-of-your-virtual-environment' (let's call it env)
	2. 'env/bin/pip install requests'
	3. 'source env/bin/activate'
	You should now be in a virtualenv and any installations will not be global
	4. make sure the directory you're in had requirements.txt. It should be in GroupLMU/testweb/testweb
	5. 'pip install -r requirements.txt'
	6. 'python manage.py runserver'
	7. navigate to the development server noted in the terminal. This seems to generally be 127.0.0.1:8000
	8. Append /admin to those numbers for the admin page and /notes for the main page users would see. 
		Ex: 127.0.0.1:8000/notes
For Windows users: Step 3 would be 'env\Scripts\activate.bat'


See Wiki for more detailed information on construction and outline

Paul Narup, Eva Martinuzzi, Cat Litten, Sebastian Kurpiel, and Abdul Zakkar © 2017, Loyola University Chicago
