Must install and use Java 8 SDK
If installed Java 11, consider downgrade or update-alternatives

To run the process headlessly (without display), use xvfb-run


Set up virtual environment
python3 -m venv ~/.virtualenvs/minerl
source ~/.virtualenvs/minerl/bin/activate
pip3 install -r requirements.txt

Run codes in Jupyter notebook
pip3 install jupyter
source ~/.virtualenvs/minerl/bin/activate
pip3 install ipykernel
python3 -m ipykernel install --user --name=minerl

Then start the notebook:
jupyter notebook

Or, to suppress display, run:
xvfb-run -s "-screen 0 1400x900x24" jupyter notebook