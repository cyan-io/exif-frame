default: install

clean:
	rm -r -f build/ dist/ *.egg-info/

install:
	pip install .

dev:
	pip install -e .

wheel:
	python setup.py bdist_wheel

exe:
	pyinstaller -y -D --add-data ./frame/font;./frame/font --add-data ./frame/logo;./frame/logo -n frame -i icon.ico main.py
