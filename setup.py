from setuptools import setup
from os import path

pwd = path.abspath(path.dirname(__file__))
with open(path.join(pwd, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup (
    name = "dmlog",
    description = "An extension for discord.py to dm logs to the app owner.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords = "discord discord.py extension",
    author = "Programming Socks",
    author_email = "pgsocks@pm.me",
    packages = [ "dmlog" ],
    install_requires = [ "discord" ],
    entry_points = {
        "discord.extensions" : [
            "dmlog = dmlog"
        ]
    }
)
