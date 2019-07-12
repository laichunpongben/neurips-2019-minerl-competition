# NeurIPS 2019 MineRL Competition
This repository is for the team to develop the solution of the competition. 

## Prepare the development environment
### Some basics
Install Git and Python3 (and Homebrew if using Mac) if not already installed.

On Mac:

Homebrew:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
Git:

    brew install git
Python3:

    brew install python

### Set up Java 8
Check Java runtime version.

    java -version
It should display something similar to:

    openjdk version "1.8.0_212"
If not using Java 8, install it.

On Mac:

    brew tap AdoptOpenJDK/openjdk
    brew cask install adoptopenjdk8


On Debian/Ubuntu:

    sudo add-apt-repository ppa:openjdk-r/ppa
    sudo apt-get update
    sudo apt-get install openjdk-8-jdk

### Set up xvfb
    sudo apt-get install xvfb

### Set up Python virtual environment
    python3 -m venv ~/.virtualenvs/minerl
    source ~/.virtualenvs/minerl/bin/activate
    pip3 install -r requirements.txt

### Prepare Jupyter notebook and kernels
    pip3 install jupyter
    source ~/.virtualenvs/minerl/bin/activate
    pip3 install ipykernel
    python3 -m ipykernel install --user --name=minerl

## Open the Jupyter notebook
Then start the notebook (Caution! A game window will pop up!): 

    jupyter notebook

Or, to suppress display, run:

    xvfb-run -s "-screen 0 1400x900x24" jupyter notebook
    
Select "navigate_dense.ipynb" to play! 
