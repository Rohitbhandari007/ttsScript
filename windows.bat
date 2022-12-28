@echo off

echo Installing requirements from requirements.txt...
pip install -r requirements.txt

echo Running tts.py...
python tts.py
