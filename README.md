
https://user-images.githubusercontent.com/17003525/115948766-bb35c600-a4ed-11eb-8570-9e7f88e06fba.mp4


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
#### TODO: 
- [x] Add video of installation 
- [x] Node js installation support 
- [x] Powerlevel10k theme installation 
- [x] Mac Gesture installation
- [x] Postman 
- [x] VSCode
- [x] Brave 
- [x] firefox 
- [x] Gnome Tweak Tool 
- [x] qBittorrent 
- [x] copyQ 
- [x] VLC Media Player 
- [x] Stacer 
- [x] oh my zsh terminal 
- [x] zsh plugins i.e. sudo, git, syntax-highlighting, auto-suggestions, fzf, z, fuck


## FAQ 
1. How can I autostart mac gesture on login? 
   - https://github.com/iberianpig/fusuma/blob/master/README.md#autostart-gnome-session-properties
2. How can I change powerlevel10k theme configurations? 
   - Open Terminal and type ```p10k configure```
3. How can I modify the icons positions and number of icons visible in the terminal?
   - https://github.com/romkatv/powerlevel10k