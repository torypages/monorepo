# Installing

## Perquisites

### Macos
```
$ brew install mysql-client pkg-config
$ export PKG_CONFIG_PATH="$(brew --prefix)/opt/mysql-client/lib/pkgconfig"
```

that export probably has to be in your zsh config


# Features
- auto restart celery
- auto restart django
- run app and/or worker on host or in docker


# Questions
- when does playright run?
- how to you make sure literal images move through envs?
