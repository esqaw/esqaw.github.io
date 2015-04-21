default: freeze

freeze: build 
	docker run -v `pwd`/build:/usr/src/app/build -it arsen_mamikonyan_am python3 ./freeze.py

clean:
	find . -type f -name "*.pyc" -delete

build: clean
	docker build -t arsen_mamikonyan_am .
