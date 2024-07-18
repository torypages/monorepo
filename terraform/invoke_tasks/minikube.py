import concurrent.futures
import getpass
import threading
from subprocess import Popen

from invoke import Collection, task


@task
def start_repository_tunnel(c):
    print("starting repository tunnel")
    c.run(
        'docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:$(minikube ip):5000"',
        pty=True,
    )


@task
def start_dashboard(c):
    print("starting dashboard")
    c.run("minikube dashboard", pty=True)


@task
def start_tunnel(c, sudo_pass):
    print("starting tunnel")
    c.run("echo {} | sudo -S minikube tunnel".format(sudo_pass), pty=True)


@task
def start(c):
    sudo_password = getpass.getpass("Enter your sudo password: ")
    c.run('minikube start --insecure-registry "10.0.0.0/24" --memory 20000')
    c.run("minikube addons enable registry")
    c.run("minikube addons enable ingress")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_repo_tunnel = executor.submit(start_repository_tunnel, c)
        future_dashboard = executor.submit(start_dashboard, c)
        future_tunnel = executor.submit(start_tunnel, c, sudo_pass)

        # Wait for all tasks to complete
        concurrent.futures.wait([future_repo_tunnel, future_dashboard, future_tunnel])

    # repo_tunnel_thread = threading.Thread(target=start_repository_tunnel, args=(c,))
    # tunnel_thread = threading.Thread(target=start_tunnel, args=(c,))
    # dashboard_thread = threading.Thread(target=start_dashboard, args=(c,))
    #
    # repo_tunnel_thread.start()
    # tunnel_thread.start()
    # dashboard_thread.start()
    #
    # repo_tunnel_thread.join()
    # tunnel_thread.join()
    # dashboard_thread.join()

    # processes = []
    # commands = [
    #     ["yes", "hi"],
    #     ["yes", "cool"],
    #     # Add more commands as needed
    # ]
    #
    # for cmd in commands:
    #     process = Popen(cmd)
    #     processes.append(process)
    #
    # # Wait for all processes to finish
    # for process in processes:
    #     process.wait()

    # c.run(
    #     'docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:$(minikube ip):5000" & minikube tunnel & minikube dashboard ; fg',
    #     pty=True,
    # )
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
