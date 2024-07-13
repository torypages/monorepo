# TODO
- version numbers of images in tasks.py or latest
- the build an endpoint that will return the commit hash being run

# Longer TODO
- Create some indirection through something like Kong that will allow your local env to point to staging resources. This way you don't have to run every microservice you are working with on your local machine.

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
- run app and/or worker on host or in docker, up to the developer desertion.


# Questions
- when does playright run?
- how to you make sure literal images move through envs?
  - this is where commit hash versioning comes into play
