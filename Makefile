default: freeze

PACKAGE=arsen/arsen.mamikonyan.am
TAG=django

freeze: build 
	docker run -v `pwd`/build:/usr/src/app/build -it arsen_mamikonyan_am python3 ./freeze.py

debug: build 
	echo "\033[44m\033[1m `boot2docker ip`:5000 \033[0m"
	docker run -p 5000:5000 -v `pwd`:/usr/src/app -it arsen_mamikonyan_am python3 ./debug.py

clean:
	find . -type f -name "*.pyc" -delete

build: clean
	docker build -t ${PACKAGE}:${TAG} .
