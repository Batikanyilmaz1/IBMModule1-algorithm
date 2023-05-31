  
To set up the environment for this project, you need to follow these steps:

1-Install Python: To run this code, you need to have Python installed on your computer. You can download and install Python from the official Python website (https://www.python.org/downloads/).

2-Install required libraries: This code uses the defaultdict module from the collections library, so you don't need to install any external libraries for this project.

3-Create a virtual environment (optional): It is a good practice to create a virtual environment to isolate the project's dependencies from the rest of your system. To create a virtual environment, you can use the built-in venv module. Open a command prompt/terminal and navigate to the project directory. Then, run the following command:

python -m venv env

This will create a virtual environment named env in the project directory.

4-Activate the virtual environment (optional): To activate the virtual environment, run the following command:

On Windows: env\Scripts\activate.bat

On Unix or Linux: source env/bin/activate

After activating the virtual environment, you should see the (env) prefix in your command prompt/terminal.

5-Run the code: You can run the code by executing the script file (ibm_model_1.py) using the following command: python ibm_model_1.py

This will run the code and print the translation probabilities for each Turkish-English word pair.
