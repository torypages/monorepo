from invoke import Collection, task


@task
def start(c):
    # c.run('minikube start --insecure-registry "10.0.0.0/24"')
    # c.run("minikube addons enable registry")
    # c.run("minikube addons enable ingress")
    c.run(
        'docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:$(minikube ip):5000" & minikube tunnel & minikube dashboard ; fg',
        pty=True,
    )
    # c.run(
    #     'docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:$(minikube ip):5000"',
    #     pty=True,
    # )


@task
def delete(c):
    c.run("minikube delete")


@task
def test(c):
    c.run("yes hii & yes water ; fg", pty=True)


from invoke import Collection

ns_minikube = Collection("minikube")
ns_minikube.add_task(start)
ns_minikube.add_task(delete)
ns_minikube.add_task(test)
