# AGP Campus Virtual
Campus virtual is a learning tool aimed at all the public so they can learn about cancer, what it is, how it can be treated and to identify early signs of the disease. This tool was developed so educational institutions can use it as a learning aid to teach about cancer.


## Folder structure
```
.
├── app          : Main application folder
│    ├── auth        : Authenthication blueprint
│    ├── cursos     : Course article blueprint
│    ├── main        : Main blueprint
│    ├── static      : Static page files
│    ├── templates   : Jinja templates (ordered by blueprint folders)
│    ├── scheduler   : Schedodule init
│    ├── email.py    : Email service
│    └── models.py   : Database models
├── temp         : Temporary files
├── .gitignore   : Ignored files and extensions
├── .flaskenv    : Flask environment variables
├── .env         : Secret environtment variables
├── Pipfile      : Pipenv dependiencies
├── Pipfile.lock : Pipenv dependencies lock
├── README.md    : This file
└── web_app.py   : Run file


```

## Running for the first time
Install pipenv:
```
pip install pipenv
```

Install virtual environment packages:
```
pipenv install --dev
```

## Regular run
Enter virtual environment shell:
```
pipenv shell
```

\
Call the flask command to run the app (from inside the virtual environment):
```
flask run
```

\
Full example:
```
pip install pipenv
pipenv install --dev
pipenv shell
flask run
```


## Auto formatting
Please disable auto formatting for python files to keep it from messing up imports.

```
mkdir .vscode
touch .vscode/settings.json
```
.vscode/settings.json
```
{
    "[python]": {
        "editor.formatOnsave": false
    }
}
```
