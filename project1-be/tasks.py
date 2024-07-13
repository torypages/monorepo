from invoke import task

version = 2


@task
def build_app(c):
    c.run(f"docker build --target app --tag localhost:5000/project1-be-app/version/1 .")


@task
def build_worker(c):
    c.run(
        "docker build --target worker --tag localhost:5000/project1-be-worker/version/1 ."
    )


@task
def build(c):
    build_app(c)
    build_worker(c)


@task
def push_app(c):
    c.run("docker push localhost:5000/project1-be-app/version/1")


@task
def push_worker(c):
    c.run("docker push localhost:5000/project1-be-worker/version/1")


@task
def push(c):
    push_app(c)
    push_worker(c)


@task
def build_push(c):
    build(c)
    push(c)
