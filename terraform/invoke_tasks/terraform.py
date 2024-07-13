from invoke import Collection, task


@task
def apply(c, env: str):
    c.run(
        f"terraform apply --var-file=configs/{env}.tfvars --state=state/{env}.tfstate",
        pty=True,
    )


ns_terraform = Collection("terraform")
ns_terraform.add_task(apply)
