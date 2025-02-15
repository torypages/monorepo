# TODO
- version numbers of images in tasks.py or latest
- the build an endpoint that will return the commit hash being run

# Longer TODO
- Create some indirection through something like Kong that will allow your local env to point to staging resources. This way you don't have to run every microservice you are working with on your local machine.
- Store passwords in some password service. If this were for AWS it would be secrets manager, but since we're rolling our own K8 cluster and I'm not about to pay for anything, something self-hosted would be good.

# Design Decisions
- The default running setup of the app is locally without docker, so for example, `.env` describes the local setup. This isn't because local is recommended or better, it's just that, it's literally the default, docker is something on top of local
- .docker.env gets combined with .env and supercedes .env
- MySQL and Django were chosen because my workplace uses those. I'd personally use FastAPI and Django, assuming I'd use Python at all, but that's a whole other thing.
- I don't even think I'd use Celery as a way of running async tasks.
- There is one settings.py file, and should only ever by one. Environment variables are used for distinguishing environments.
- Migrations are run as the app starts. I believe when K8 is scaled to more than 1 this should all just magically work because of DB locking n such.
- In real life the DB would be using a managed service like RDS, I would not self host a db in a docker container like this.
- Poetry because it works, it's popular, it's easy. Though it's my understanding that it actually isn't the ideal option anymore. Anyway, I didn't want to get hung up on this detail.

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
- when does playwright run?
- how to you make sure literal images move through envs?
  - this is where commit hash versioning comes into play
  - this is the answer
