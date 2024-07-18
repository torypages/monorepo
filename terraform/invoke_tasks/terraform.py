from invoke import Collection, task


@task
def apply(c, env: str, docker_tag: str):
    # TODO should not always auto approve
    c.run(
        f"terraform apply --var-file=configs/{env}.tfvars --state=state/{env}.tfstate -var='docker_tag={docker_tag}' -auto-apply",
        pty=True,
    )


ns_terraform = Collection("terraform")
ns_terraform.add_task(apply)
