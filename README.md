This `discord.py` extension sends logs to the app owner's DMs. Logs may contain
sensitive information, so this probably isn't secure, but it's fun.

# Usage

Install with pip.

```
pip install .
```

Load with a `discord.py` bot.

```python
bot.load_extension("dmlog")
```

Alternatively, this extension is registered as an `entry_point`, so it can be
loaded with `importlib`.

```python
from importlib import metadata

for extension in metadata.entry_points().get("discord.extensions", []):
    bot.load_extension(extension.value)
```

The bot should start DMing you logs when it's turned on.
