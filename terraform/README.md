
# TODO
- don't forget that docker-compose is still being used.
- have some fake build this auto deploy main to staging
  - decide if you want "latest" or to automate the latest hash
  - non latest will result in another commit to master everytime a commit to master is needed
- allow for deploying a hash to prod




# Notes
- state files solve the overwriting issue
- Minikube grinding to a halt after deploying the second env seemed to get solved by increasing memory. The Kubernetes was giving OOM errors.


# Instructions
source ./venc/bin/activate
inv minikube.start

build images from apps

inv terraform.apply --env=staging
inv terraform.apply --env=prod

access app via http://prod.party.central/, update /etc/hosts file to enable this

# Old instructions
`minikube start`

In terminal 1:
`docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:$(minikube ip):5000"`

This is to create network access to the minikube docker registry.

In terminal 2 (optional):
`minikube dashboard`

In terminal 3:
`minikube tunnel`


Update /etc/hosts and access via *.party.central


