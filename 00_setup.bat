set PIPENV_VENV_IN_PROJECT=1
call pyenv install 3.10.5
call pyenv local 3.10.5
call python -m pip install --upgrade pip
call python -m pip install pipenv
call python -m pipenv install --python 3.10.5
