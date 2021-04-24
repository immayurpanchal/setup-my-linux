import click
import os


def copy_zshrc():
    try:
        click.secho(
            "Copying zshrc-final config file\n It will automatically setup your config, plugins ",
            fg="bright_yellow",
            bold=True,
        )
        os.system("cp ./.zshrc ~/.zshrc")
        click.secho(
            "Successfully Copied zshrc config ✅",
            fg="bright_green",
            bold=True,
        )
    except:
        click.secho(
            "Failed to copy zshconfig file ❌",
            fg="red",
            bold=True,
        )


def change_shell_to_zsh():
    try:
        click.secho(
            "Chaging default shell to ZSH",
            fg="bright_yellow",
            bold=True,
        )
        os.system("chsh -s /bin/zsh")
        click.secho(
            "Successfully Changed default shell to ZSH ✅, make sure to logout and login again",
            fg="bright_green",
            bold=True,
        )
    except:
        click.secho(
            "Failed to change the default shell ❌",
            fg="red",
            bold=True,
        )


def upgrade_zsh():
    try:
        click.secho(
            "Upgrading ZSH to the latest version",
            fg="bright_yellow",
            bold=True,
        )
        os.chdir(f"/home/{os.getlogin()}/.oh-my-zsh/tools")
        os.system("./upgrade.sh")
        click.secho(
            "Successfully upgraded Oh My Zsh to the latest version ✅",
            fg="bright_green",
            bold=True,
        )
    except:
        click.secho(
            "Failed to upgrade Oh My Zsh ❌",
            fg="red",
            bold=True,
        )


def zsh_syntax_highlighting():
    try:
        click.secho(
            "Installing Syntax Highlighting 🚧",
            fg="bright_yellow",
            bold=True,
        )
        os.system(
            f"rm -rf /home/{os.getlogin()}/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting"
        )
        os.system(
            f"git clone https://github.com/zsh-users/zsh-syntax-highlighting.git /home/{os.getlogin()}/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting"
        )
        click.secho(
            "Successfully installed Syntax highliting 🆗",
            fg="bright_green",
            bold=True,
        )
    except:
        click.secho("Failed to install zsh syntax highlighting ❌", fg="red", bold=True)


def zsh_autosuggestions():
    try:
        click.secho(
            "Installing Zsh Auto suggestions 🚧",
            fg="bright_yellow",
            bold=True,
        )
        os.system(
            f"rm -rf /home/{os.getlogin()}/.oh-my-zsh/custom/plugins/zsh-autosuggestions"
        )
        os.system(
            f"git clone https://github.com/zsh-users/zsh-autosuggestions /home/{os.getlogin()}/.oh-my-zsh/plugins/zsh-autosuggestions"
        )
        click.secho(
            "Successfully installed Zsh Auto suggestions 🆗",
            fg="bright_green",
            bold=True,
        )
    except:
        click.secho("Failed to install Zsh autosuggestions ❌", fg="red", bold=True)


def the_fuck():
    try:
        click.secho(
            "Installing the fuck 🚧",
            fg="bright_yellow",
            bold=True,
        )
        os.system("sudo pip3 install thefuck")
        click.secho(
            "Successfully installed the fuck 🆗",
            fg="bright_green",
            bold=True,
        )
    except:
        click.secho("Failed to install the fuck ❌", fg="red", bold=True)


def z():
    try:
        click.secho(
            "Installing z plugin 🚧",
            fg="bright_yellow",
            bold=True,
        )
        os.system("sudo pip3 install thefuck")
        click.secho(
            "Successfully installed z plugin 🆗",
            fg="bright_green",
            bold=True,
        )
    except:
        click.secho("Failed to z plugin ❌", fg="red", bold=True)


def fzf():
    try:
        click.secho(
            "Installing fuzzy finder 🚧",
            fg="bright_yellow",
            bold=True,
        )
        os.system("sudo apt-get install fzf")
        click.secho(
            "Successfully installed fuzzy finder 🆗",
            fg="bright_green",
            bold=True,
        )
    except:
        click.secho("Failed to install z plugin ❌", fg="red", bold=True)


def powerlevel10ktheme():
    try:
        click.secho(
            "Installing Powerlevel10k theme 🔥",
            fg="bright_yellow",
            bold=True,
        )
        os.system(
            f"git clone --depth=1 https://github.com/romkatv/powerlevel10k.git /home/{os.getlogin()}/.oh-my-zsh/custom/themes/powerlevel10k"
        )
        click.secho(
            "Successfully Powerlevel10k theme in Oh My Zsh ✅",
            fg="bright_green",
            bold=True,
        )
        click.secho(
            "Copying default theme of powerlevel10k",
            fg="bright_yellow",
            bold=True,
        )
        os.system("cp ./.p10k.zsh ~/.p10k.zsh")
        click.secho(
            "Successfully copied Powerlevel10k theme in ~/.p10k.zsh ✅",
            fg="bright_green",
            bold=True,
        )
        click.secho(
            "To configure the theme, restart your terminal using 'exec zsh' command and then type 'p10k configure' ✅",
            fg="bright_green",
            bold=True,
            blink=True,
        )
    except:
        click.secho(
            "Failed to install Powerlevel10k theme ❌",
            fg="red",
            bold=True,
        )


def install():
    try:
        click.secho(
            "Installing ZSH 🔥",
            fg="bright_yellow",
            bold=True,
        )
        os.system("sudo apt install zsh")
        click.secho(
            "Successfully installed ZSH ✅",
            fg="bright_green",
            bold=True,
        )
        click.secho(
            "Installing powerline fonts 🔥",
            fg="bright_yellow",
            bold=True,
        )
        os.system("sudo apt-get install powerline fonts-powerline")
        click.secho(
            "Successfully installed powerline fonts ✅",
            fg="bright_green",
            bold=True,
        )
        click.secho(
            "Configuring Oh My Zsh 🔥",
            fg="bright_yellow",
            bold=True,
        )
        os.system(f"rm -rf /home/{os.getlogin()}/.oh-my-zsh ")
        os.system(
            "git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh"
        )
        # copy .zshrc
        copy_zshrc()
        # change shell to zsh
        change_shell_to_zsh()
        # upgrade to latest version
        upgrade_zsh()
        click.secho(
            "Successfully installed Oh My Zsh ✅",
            fg="bright_green",
            bold=True,
        )
        # install powerlevel10k theme
        powerlevel10ktheme()
    except:
        click.secho(
            "Failed to install Oh My Zsh ❌",
            fg="red",
            bold=True,
        )
