run:
	python ./src/ncpypp_run.py
	echo foo

all:
	$(MAKE) doc
	$(MAKE) run

doc:
	cd ./docu && doxygen  && cd ..

