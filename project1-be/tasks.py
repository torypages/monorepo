from invoke import task


@task
def build(c, docs=False, bytecode=False, extra=""):
    c.run("rm -rf {}".format(pattern))


@task
def push(c, docs=False, bytecode=False, extra=""):
    c.run("rm -rf {}".format(pattern))
