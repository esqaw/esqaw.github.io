default: freeze

freeze: build 
	./fix_ml_html_statics.sh
	./insert_raw_to_ml_lectures.sh
	docker run -v `pwd`/build:/usr/src/app/build -it arsen_mamikonyan_am python3 ./freeze.py

debug: build 
	docker run -p 5000:5000 -v `pwd`:/usr/src/app -it arsen_mamikonyan_am python3 ./debug.py

clean:
	find . -type f -name "*.pyc" -delete

build: clean
	docker build -t arsen_mamikonyan_am .
