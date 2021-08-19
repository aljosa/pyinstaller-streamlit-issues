rm -rf build dist main.spec  __pycache__
pyinstaller --additional-hooks-dir=hooks --clean -w main.py
