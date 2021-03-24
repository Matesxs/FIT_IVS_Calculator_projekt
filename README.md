<div align="center">
    <h1>Calculator</h1>
    <p>IVS Project 2</p>
    <p>2020/2021</p>
    <p>
    <img src="screenshot.jpg">
    <br>
    </p>
</div>

## About

A simple calculator made in python using buildin math library, buildin functions and Qt for UI.
This software is targeted for **Windows** because it's platfor all of us using but in theory you can use it on whatever
system with graphical interface you want because python can run almost anywhere.
This software comes with two versions:
* standalone - slower starts but its only one executable
* installer - needs to be installed (and uninstalled), but it is faster to start

## Getting Started

If you want to play with code yourself clone this repository like this
```
git clone https://github.com/Matesxs/IVS-Projekt-2-Kalkulacka
```

or you can download finished product [here](https://github.com/Matesxs/ivs_calculator_test_repository/releases)

## Setup for developement
```
install python 3.7+
create python venv and activate it (optional)
cd src
pip install -r requirements.txt or make init

If you want compile installer you need to install Inno Setup Compiler and add it to 
path for automatic compiling or you can do it by hand using .iss script in utils folder.
```

### Makefile endpoints
```
init - install packages from requirements.txt
all - make tests and run app
run - run app
doc - generate doxygen code documentation
build - build standalone version and installer of app
build_standalone - build only standalone version of app
build_installer - build only installer of app (Inno Setup Compiler required)
clean - clean all files that will not be submitted
test - run tests on app
test_with_coverage - run tests on app with test code coverage
profile - start profiling program with input from console
profile_with_log - start profiling with random data input and output log data
pack - create .exe files from app, generate docomentation and pack it to zip for submit (Windows required)
pip - show installed packages
```

## Tools

* [Python](https://www.python.org/)
* [PyQt](https://wiki.python.org/moin/PyQt)

## Authors
Name of team: "Název týmu:"
* **Martin Douša**
* **Ondřej Sláma**
* **Vojtěch Schindler**

## License

This project is licensed under the GNU GPL v.3 License.

## Credits

Part of the project was inspired by github.com/davidcallanan/ and his project about custom scripting language