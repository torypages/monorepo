from invoke import task

version = 2


@task
def build_app(c, docker_tag):
    c.run(
        f"docker build --target app --tag localhost:5000/project1-be-app/{docker_tag} ."
    )


@task
def build_worker(c, docker_tag):
    c.run(
        f"docker build --target worker --tag localhost:5000/project1-be-worker/{docker_tag} ."
    )


@task
def build(c, docker_tag):
    build_app(c, docker_tag)
    build_worker(c, docker_tag)


@task
def push_app(c, docker_tag):
    c.run(f"docker push localhost:5000/project1-be-app/{docker_tag}")


@task
def push_worker(c, docker_tag):
    c.run(f"docker push localhost:5000/project1-be-worker/{docker_tag}")


@task
def push(c, docker_tag):
    push_app(c, docker_tag)
    push_worker(c, docker_tag)


@task
def build_push(c, docker_tag):
    build(c, docker_tag)
    push(c, docker_tag)
