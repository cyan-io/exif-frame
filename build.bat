pyinstaller -y -D --add-data ./font;font --add-data ./logo;logo --add-data config.yml;. -n frame -i icon.ico index.py