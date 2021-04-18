from os import name
import sys
from typing import Text
import click
from InquirerPy import prompt
import softwares.vscode as vscode
import softwares.browser as browser
import softwares.utilities as utilities

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
    # browsers
    {
        "type": "checkbox",
        "message": "Select Browsers to install",
        "choices": browsers,
        "name": "browser",
    },
]


def main():
    try:
        click.secho(
            "Welcome 😎 to Setup my Linux 💻 (Ubuntu 20.04)",
            fg="bright_yellow",
            blink=True,
            bold=True,
        )
        result = prompt(questions)
        print(result)

        if result.get("editor"):
            vscode.install()

        if len(result.get("browser")):
            click.secho("Browser ... ", fg="bright_blue")
            for item in result.get("browser"):
                if item == "brave":
                    browser.brave()

                if item == "firefox":
                    browser.firefox()

        if len(result.get("utilities")):
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
