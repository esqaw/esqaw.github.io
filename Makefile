default: copy_from_build

copy_from_build:
	rsync -vr build/ ./
