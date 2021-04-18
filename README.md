# Initial Setup to run the script
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

# After installing zsh plugins 

### Open terminal and type: 
```
exec zsh 
zshconfig 
```

### Now zshrc file will be open in editor, search for plugins and add plugins in the list 
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


