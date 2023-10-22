## About 
This project is a simple CLI app which emulates a Linux bash session using .zip files as the file system.

## Contents 
1. [Installation](##installation)
2. [How to use it](##how-to-use-it)
3. [Documentation](##documentation)

## Installation 
The project uses the syntax avaliable since Python 3.10. The perfomance was tested under Manjaro Linux OS. 

Download the source code using `git clone https://github.com/makashinmi/virtual-shell.git && cd virtual-shell/`

To start up the program, run `python main.py demo.zip`

## How to use it 
The vshell currently supports the following commands:

- **cat** path — print the contents of a file under *path* 
- **cd** path — change the current working directory to the directory under *path* 
- **ls** path — print the contents of a directory under *path* (unless specified, the current working directory is used) 
- **pwd** — show the absolute path to the current working directory 

You can use both absolute and relative path when specifying the *path* argument.

## Documentation 
*Coming soon... Maybe. Unlikely, to be honest.*
