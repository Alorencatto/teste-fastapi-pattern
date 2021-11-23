import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="teste_fastapi_pattern",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="teste_fastapi_pattern_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from teste_fastapi_pattern.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export teste_fastapi_pattern_KEY=value
export teste_fastapi_pattern_KEY="@int 42"
export teste_fastapi_pattern_KEY="@jinja {{ this.db.uri }}"
export teste_fastapi_pattern_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
teste_fastapi_pattern_ENV=production teste_fastapi_pattern run
```

Read more on https://dynaconf.com
"""
