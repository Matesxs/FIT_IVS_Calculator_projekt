all: pip test run

pip:
	pip freeze

run:
	python main.py

pack: build doc
	mkdir "..\xdousa00_xslama32_xschin05"
	xcopy /s /c /q "..\\src\\mathLib\\" "..\\xdousa00_xslama32_xschin05\\src\\mathLib\\"
	xcopy /s /c /q "..\\installers\\" "..\\xdousa00_xslama32_xschin05\\installers\\"
	xcopy /s /c /q "..\\docs\\" "..\\xdousa00_xslama32_xschin05\\docs\\"
	xcopy /s /c /q "..\\profiling" "..\\xdousa00_xslama32_xschin05\\profiling\\"
	copy "..\src\app_ui.py" "..\xdousa00_xslama32_xschin05\src\app_ui.py"
	copy "..\src\calculator.py" "..\xdousa00_xslama32_xschin05\src\calculator.py"
	copy "..\src\Doxyfile" "..\xdousa00_xslama32_xschin05\src\Doxyfile"
	copy "..\src\library_tests.py" "..\xdousa00_xslama32_xschin05\src\library_tests.py"
	copy "..\src\main.py" "..\xdousa00_xslama32_xschin05\src\main.py"
	copy "..\src\Makefile" "..\xdousa00_xslama32_xschin05\src\Makefile"
	copy "..\src\profiling.py" "..\xdousa00_xslama32_xschin05\src\profiling.py"
	copy "..\src\profiling_with_log.py" "..\xdousa00_xslama32_xschin05\src\profiling_with_log.py"
	copy "..\src\requirements.txt" "..\xdousa00_xslama32_xschin05\src\requirements.txt"
	copy "..\debugging.jpg" "..\xdousa00_xslama32_xschin05\debugging.jpg"
	copy "..\hodnoceni.txt" "..\xdousa00_xslama32_xschin05\hodnoceni.txt"
	copy "..\plan.txt" "..\xdousa00_xslama32_xschin05\plan.txt"
	copy "..\skutecnost.txt" "..\xdousa00_xslama32_xschin05\skutecnost.txt"
	copy "..\README.md" "..\xdousa00_xslama32_xschin05\README.md"
	tar.exe -c -f "..\xdousa00_xslama32_xschin05.zip" "..\xdousa00_xslama32_xschin05"
	rmdir /q /s "..\xdousa00_xslama32_xschin05"

doc:
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
	del .coverage

init:
	pip install -r requirements.txt

executable: main.py calculator.py app_ui.py mathLib
	pyinstaller --onefile --noconsole --clean -n Calculator main.py
	copy dist\Calculator.exe ..\installers\Calculator.exe
	rmdir /q /s build
	rmdir /q /s dist
	del Calculator.spec

build: executable