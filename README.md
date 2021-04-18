## Execute below shell commmands
```
1. git clone https://github.com/immayurpanchal/setup-my-linux.git ~/Documents/
2. cd setup-my-linux
3. sudo apt install python3.9
4. sudo apt-get install python3.9-dev
5. pip3 install -r requirements.txt
```

## Execute the Setup-my-linux script 
```
python3.9 ./setup-my-linux.py
```
---
## Development environment setup
```
sudo apt install python3.9
sudo apt-get install python3.9-venv
sudo apt-get install python3.9-dev
alias python="python3.9"
python -m venv env
To Activate virtual env : source ./env/bin/activate
To Deactive virtual env : deactivate 
pip3 install -r requirements.txt
```

## After installing zsh plugins 
---
#### Open terminal and type: 
```
exec zsh 
zshconfig 
```

#### Now zshrc file will be open in editor, search for plugins and add those plugins which you selected at the time of installation from the below list 
```
plugins=(
  git
  zsh-syntax-highlighting
  zsh-autosuggestions
  z
  sudo
  fzf
)
```


