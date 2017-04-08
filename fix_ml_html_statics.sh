#!/bin/bash

find templates/ml_lectures -type f | xargs gsed -i 's+src="presentation_data+src="/static/ml_lectures/presentation_data+'

find templates/ml_lectures -type f | xargs gsed -i 's+"reveal.js/+"/static/reveal.js/+'
find templates/ml_lectures -type f | xargs gsed -i "s+'reveal.js/+'/static/reveal.js/+"
