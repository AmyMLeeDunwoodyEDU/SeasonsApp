You must have these installed in VSCode before you continue:
1. Python Extension
  | Made by Microsoft
  | Go into VScode, click on the 4 boxes and search up the extension name.
    | a. Pylance
    | b. Python Debugger
    | c. Python Environments
    | d. Flask*
      | To install Flask in VSCode, you must open up a terminal and enter in the following
      | command.
        | pip install flask python-dotenv
2. Jinja Extension
  | Made by wholroyd

Now to set up the website:
You must enter in the following commands into the terminal in order.
  | python -m venv venv
  | venv\Scripts\activate
  | flask run
    | This command should give you an IP of http://127.0.0.1:5000.
