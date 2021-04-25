from os import name
import sys
from typing import Text
import click
from InquirerPy import prompt
import softwares.vscode as vscode
import softwares.browser as browser
import softwares.utilities as utilities
import softwares.oh_my_zsh as oh_my_zsh
import softwares.nodejs as nodejs
import softwares.mac_gesture as mac_gesture

extensions_to_be_installed = [
    "https://extensions.gnome.org/extension/1401/bluetooth-quick-connect/",
    "https://extensions.gnome.org/extension/1082/cpufreq/",
    "https://extensions.gnome.org/extension/307/dash-to-dock/",
    "https://extensions.gnome.org/extension/1465/desktop-icons/",
    "https://extensions.gnome.org/extension/1162/emoji-selector/",
    "https://extensions.gnome.org/extension/770/force-quit/",
    "https://extensions.gnome.org/extension/545/hide-top-bar/",
    "https://extensions.gnome.org/extension/2980/internet-speed-meter/",
    "https://extensions.gnome.org/extension/1305/more-columns-in-applications-view/",
    "https://extensions.gnome.org/extension/905/refresh-wifi-connections/",
    "https://extensions.gnome.org/extension/19/user-themes/",
]

browsers = [
    {"enabled": True, "name": "Brave (Recommended)", "value": "brave"},
    {"enabled": False, "name": "Firefox", "value": "firefox"},
]

utility_softwares = [
    {"enabled": False, "value": "stacer", "name": "Stacer"},
    {"enabled": False, "value": "copyq", "name": "copyQ"},
    {"enabled": False, "value": "vlc", "name": "VLC"},
    {"enabled": False, "value": "qbittorrent", "name": "qbittorrent"},
    {"enabled": False, "value": "gnome_tweak_tool", "name": "Gnome Tweak Tool"},
]

programming_languages = [
    {"enabled": False, "value": "nodejs", "name": "NodeJS"},
]

zsh_plugins = [
    {
        "enabled": True,
        "value": "zsh_syntax_highlighting",
        "name": "Zsh Syntax Highlighting",
    },
    {
        "enabled": True,
        "value": "z",
        "name": "Z directory changer",
    },
    {
        "enabled": True,
        "value": "fzf",
        "name": "Fzf",
    },
    {
        "enabled": True,
        "value": "sudo",
        "name": "Sudo",
    },
    {
        "enabled": True,
        "value": "zsh_autosuggestions",
        "name": "Zsh Autosuggestions",
    },
    {
        "enabled": True,
        "value": "git",
        "name": "Git",
    },
]


def is_node_selected(result):
    for item in result["programming_languages"]:
        if item == "nodejs":
            return True
    return False


questions = [
    # editor
    {
        "type": "confirm",
        "message": "Do you want to install VSCode",
        "name": "editor",
        "default": True,
    },
    # utilities
    {
        "type": "checkbox",
        "message": "Select Utility tools to install",
        "name": "utilities",
        "choices": utility_softwares,
    },
    # programming languages
    {
        "type": "checkbox",
        "message": "Select Programming language(s) to install",
        "name": "programming_languages",
        "choices": programming_languages,
    },
    # if node is selected, give stable / latest installation choice
    {
        "type": "rawlist",
        "name": "node_version",
        "choices": [
            {"name": "latest", "value": "latest"},
            {"name": "stable", "value": "stable"},
        ],
        "multiselect": False,
        "validate": lambda result: len(result) > 1,
        "message": "Select Stable/Latest version to install",
        "when": lambda result: is_node_selected(result),
    },
    # browsers
    {
        "type": "checkbox",
        "message": "Select Browsers to install",
        "choices": browsers,
        "name": "browser",
    },
    # OH My ZSH
    {
        "type": "confirm",
        "message": "Do you want give your terminal super power 💪 by installting 👨‍🎤 Oh My Zsh  🧰",
        "name": "ohmyzsh",
        "default": True,
    },
    {
        "type": "checkbox",
        "message": "Select plugins to install",
        "name": "zsh_plugins",
        "choices": zsh_plugins,
        "when": lambda result: result["ohmyzsh"],
    },
    # Mac Gestures
    {
        "type": "confirm",
        "message": "Do you want to install Mac Gestures?",
        "name": "gesture",
        "default": True,
    },
]


def install_zsh_plugins(plugins_list):
    for item in plugins_list:
        if item == "zsh_syntax_highlighting":
            oh_my_zsh.zsh_syntax_highlighting()
        if item == "zsh_autosuggestions":
            oh_my_zsh.zsh_autosuggestions()
        if item == "fuck":
            oh_my_zsh.the_fuck()
        if item == "z":
            oh_my_zsh.z()
        if item == "fzf":
            oh_my_zsh.fzf()


def main():
    try:
        click.secho(
            "Welcome 😎 to Setup my Linux 💻 (Ubuntu 20.04)",
            fg="bright_yellow",
            bold=True,
        )
        result = prompt(questions)
        print(result)

        if result.get("editor"):
            vscode.install()

        if len(result.get("browser") or []):
            click.secho("Browser ... ", fg="bright_blue")
            for item in result.get("browser"):
                if item == "brave":
                    browser.brave()

                if item == "firefox":
                    browser.firefox()

        if len(result.get("utilities") or []):
            click.secho("Installing Utilities...", fg="bright_blue")
            for item in result.get("utilities"):
                if item == "stacer":
                    utilities.stacer()

                if item == "copyq":
                    utilities.copyq()

                if item == "vlc":
                    utilities.vlc()

                if item == "qbittorrent":
                    utilities.qbittorrent()

                if item == "gnome_tweak_tool":
                    utilities.gnome_tweak_tool()

        if result.get("ohmyzsh" or []):
            oh_my_zsh.install()
            install_zsh_plugins(result.get("zsh_plugins", []))

        if result.get("programming_languages" or []):
            for item in result.get("programming_languages"):
                if item == "nodejs":
                    nodejs.install()

                    if result["node_version"] == "stable":
                        nodejs.install_stable_nodejs()
                    if result["node_version"] == "latest":
                        nodejs.install_latest_nodejs()

        if result.get("gesture"):
            mac_gesture.install()

        for item in extensions_to_be_installed:
            click.secho(f"💡 {item}", fg="bright_cyan")
            click.secho("=================", fg="yellow")

        click.launch("https://www.pling.com/p/1403328", wait=True)
        click.secho(
            "Theme, Cursor, Icons to install => https://www.pling.com/p/1403328",
            fg="bright_blue",
        )
    except KeyboardInterrupt:
        click.secho(
            "Pressed Ctrl+C, Aborting the script 🔥",
            fg="bright_red",
            bold=True,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
