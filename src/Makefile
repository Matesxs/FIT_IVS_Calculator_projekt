.PHONY: all run clean doc profile profile_with_log test test_with_coverage init build build_standalone build_installer

all: init run

run:
	python main.py

clean:
	python utils/remove.py "..\docs"
	python utils/remove.py "..\install"
	python utils/remove.py "build"
	python utils/remove.py "dist"
	python utils/remove.py "Calculator.spec"
	python utils/remove.py ".coverage"

doc:
	Doxygen Doxyfile

profile:
	python profiling.py

profile_with_log:
	python profiling_with_log.py

test:
	python library_tests.py

test_with_coverage:
	-coverage run library_tests.py
	coverage report -m
	python utils/remove.py ".coverage"

init:
	pip install -r requirements.txt

build: build_standalone build_installer

build_standalone:
	pyinstaller --onefile --noconsole --clean -n CalculatorStandalone main.py
	python utils/create_folder.py "..\install"
	copy dist\CalculatorStandalone.exe ..\install\CalculatorStandalone.exe
	python utils/remove.py "build"
	python utils/remove.py "dist"
	python utils/remove.py "CalculatorStandalone.spec"

build_installer:
	pyinstaller --onedir --noconsole --clean -n Calculator main.py
	python utils/create_folder.py "..\install"
	-iscc .\utils\installer_compile_script.iss
	python utils/remove.py "build"
	python utils/remove.py "dist"
	python utils/remove.py "Calculator.spec"