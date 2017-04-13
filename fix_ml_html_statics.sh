#!/bin/bash

find templates/ml_afternoon -type f | xargs gsed -i 's+src="presentation_data+src="/static/ml_afternoon/presentation_data+'
find templates/ml_afternoon -type f | xargs gsed -i 's+href="presentation_data+href="/static/ml_afternoon/presentation_data+'
find templates/ml_afternoon -type f | xargs gsed -i 's+src="homeworks+src="/static/ml_afternoon/homeworks+'
find templates/ml_afternoon -type f | xargs gsed -i 's+href="homeworks+href="/static/ml_afternoon/homeworks+'
find templates/ml_afternoon -type f | xargs gsed -i 's+"reveal.js/+"/static/reveal.js/+'
find templates/ml_afternoon -type f | xargs gsed -i "s+'reveal.js/+'/static/reveal.js/+"

find templates/ml_evening -type f | xargs gsed -i 's+src="presentation_data+src="/static/ml_evening/presentation_data+'
find templates/ml_evening -type f | xargs gsed -i 's+href="presentation_data+href="/static/ml_evening/presentation_data+'
find templates/ml_evening -type f | xargs gsed -i 's+src="homeworks+src="/static/ml_evening/homeworks+'
find templates/ml_evening -type f | xargs gsed -i 's+href="homeworks+href="/static/ml_evening/homeworks+'
find templates/ml_evening -type f | xargs gsed -i 's+"reveal.js/+"/static/reveal.js/+'
find templates/ml_evening -type f | xargs gsed -i "s+'reveal.js/+'/static/reveal.js/+"
