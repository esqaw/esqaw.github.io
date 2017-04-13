#!/bin/bash

find templates/ml_afternoon -type f | xargs gsed -i 's+src="presentation_data+src="/static/ml_afternoon/presentation_data+'
find templates/ml_afternoon -type f | xargs gsed -i 's+"reveal.js/+"/static/reveal.js/+'
find templates/ml_afternoon -type f | xargs gsed -i "s+'reveal.js/+'/static/reveal.js/+"

find templates/ml_evening -type f | xargs gsed -i 's+src="presentation_data+src="/static/ml_evening/presentation_data+'
find templates/ml_evening -type f | xargs gsed -i 's+"reveal.js/+"/static/reveal.js/+'
find templates/ml_evening -type f | xargs gsed -i "s+'reveal.js/+'/static/reveal.js/+"
