.PHONY: all run pack clean doc profile profile_with_log test test_with_coverage init build

all: init run

run:
	python main.py

pack: build doc
	python utils/create_folder.py "..\..\xdousa00_xslama32_xschin05"
	xcopy /s /c /q "..\\docs\\" "..\\..\\xdousa00_xslama32_xschin05\\docs\\"
	xcopy /s /c /q "..\\install\\" "..\\..\\xdousa00_xslama32_xschin05\\install\\"
	make clean
	python utils/create_folder.py "..\..\xdousa00_xslama32_xschin05\repo"
	xcopy /s /c /q "..\\.git\\" "..\\..\\xdousa00_xslama32_xschin05\\repo\\.git\\"
	xcopy /s /c /q "..\\*" "..\\..\\xdousa00_xslama32_xschin05\\repo\\*"
	python utils/pack_files.py
	rmdir /q /s "..\..\xdousa00_xslama32_xschin05"

clean:
	python utils/remove.py "..\docs"
	python utils/remove.py "..\install"
	python utils/remove.py "build"
	python utils/remove.py "dist"
	python utils/remove.py "Calculator.spec"
	python utils/remove.py ".coverage"

doc:
	python utils/create_folder.py "..\docs"
	Doxygen Doxyfile

profile:
	python profiling.py

profile_with_log:
	python profiling_with_log.py

test:
	python library_tests.py

test_with_coverage:
	coverage run library_tests.py
	coverage report -m
	python utils/remove.py ".coverage"

init:
	pip install -r requirements.txt

build:
	pyinstaller --onefile --noconsole --clean -n Calculator main.py
	python utils/create_folder.py "..\install"
	copy dist\Calculator.exe ..\install\Calculator.exe
	python utils/remove.py "build"
	python utils/remove.py "dist"
	python utils/remove.py "Calculator.spec"