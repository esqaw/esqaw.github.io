#!/bin/bash

find templates/ml_lectures -type f | xargs sed -i '' 's+src="presentation_data+src="/static/ml_lectures/presentation_data+'
