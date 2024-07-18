from invoke import Collection, task


@task
def apply(c, env: str, docker_tag: str):
    c.run(
        f"terraform apply --var-file=configs/{env}.tfvars --state=state/{env}.tfstate -var='docker_tag={docker_tag}'",
        pty=True,
    )


ns_terraform = Collection("terraform")
ns_terraform.add_task(apply)
