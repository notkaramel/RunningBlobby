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
- On a terminal session, run the game with Python (version 3)
```sh
(.venv) python main.py
```

- **Your task:** Edit the `SynthDefs` in the `gameServer.scd` file and compile it on the SuperCollider IDE. Make sure to have a SuperCollider server up and running via `s.boot`, or via key shortcuts `Ctrl`/`Cmd` + `B`.

# Misc
- To run the "stock" sound effects, run the `server.scd` file on a separate terminal session:
```sh
sclang server.scd
```
