`minikube start`

In terminal 1:
`docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:$(minikube ip):5000"`

This is to create network access to the minikube docker registry.

In terminal 2 (optional):
`minikube dashboard`

In terminal 3:
`minikube tunnel`


Update /etc/hosts and access via *.party.central


