@echo off

SET DIR=%~dp0

SET PARENT_DIR=%DIR%..\

python -m venv "%PARENT_DIR%.venv" 
call "%PARENT_DIR%.venv\Scripts\activate"

python -m pip install --upgrade pip setuptools wheel
python -m pip install -r "%DIR%requirements.txt"

deactivate

exit /b
