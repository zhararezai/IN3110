<h1>Instapy </h1>
This package adds a sepia and/or gray filter to any .jpg file. The implementation for both filters is done in python, numpy and numba.

<h3>Installation</h3>
To install the package, write the following commands in the terminal:

>python3 -m pip install .

If you want the editable version, write the following command:
>python3 -m pip install . --editable

Pytest also has to be installed. This can be done the following way:
>python3 -m pytest -v test/test_package.py

<h3>How to run the instapy package</h3>
To run the package, and thereby apply the chosen filter to your image, write the following command:

>python3 -m instapy _arguments_ 

_arguments_ consists of:

>file -o _output file_ -i _implementation language_ -g/-se -sc _scale factor to resize the image_

Either --gray (-g) or --sepia (-se) has to be chosen.
python3 -m instapy test/rain.jpg -i "numba" -g -sc "1" 
