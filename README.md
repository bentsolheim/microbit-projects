# Misc BBC Micro:bit Projects

# Development

Set up a virtual env with Python 3.7 and run

    pip install -r requirements.txt
    
This project uses a couple of helper tools to ease development;

* pseudo-microbit to get code completion in PyCharm. See https://mryslab.github.io/pseudo-microbit/install/ 
* uflash to install code to the micro:bit. See https://uflash.readthedocs.io/en/latest/


    pip install pseudo-microbit
    sudo pip install uflash

To upgrade:

    pip install --no-cache --upgrade uflash

To update the requirements file:

    pip freeze > requirements.txt

## uFlash

Code can be installed on the micro:bit using uFlash

    uflash <file>
    
or
    
    uflash --watch <file>
    
to install changes on file save.