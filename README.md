# Running Blobby

# Requirement
- Python 3
- `python-pip`

# Setup:
- Clone this repository
```sh
git clone https://github.com/notkaramel/BlobbyRun
```
- Change directory
```sh
cd BlobbyRun
```

- Create a Python virtual environment inside a folder called `.venv`:
```sh
python -m venv .venv
```

- Activate the virtual environment based on the command line you are using
```sh
source .venv/bin/activate       # for bash, zsh on Linux, MacOS, WSL
source .venv/bin/Activate.ps1   # for PowerShell on Windows
source .venv/bin/activate.fish  # for fish
source .venv/bin/activate.csh   # for csh
```

- Install the requirement `python-osc`
```sh
(.venv) pip install python-osc
# or
(.venv) pip install -r requirements.txt
```

# Run the game
- Make sure to have a SuperCollider server up and running, either via the IDE or `scsynth`
```sh
scsynth -u 57120
```
- Run the SuperCollider `gameServer.scd` file to set up your SynthDefs
```sh
sclang gameServer.scd
```

- Run the game on a separated terminal
```sh
(.venv) python main.py
```