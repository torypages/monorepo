# TODO
- don't forget that docker-compose is still being used.
- have some fake build that will auto deploy main to staging
  - decide if you want "latest" or to automate the latest hash
  - non latest will result in another commit to master everytime a commit to master is needed
- allow for deploying a hash to prod

# Notes
- There was a problem where resources of one env would overwrite the resources of another, state files solve the overwriting issue
- Minikube grinding to a halt after deploying the second env seemed to get solved by increasing memory. The Kubernetes was giving OOM errors.
- Will use commit hashes or maybe md5 sums for docker tags
- staging may use latest, but other envs will probably use actual versions
- deploy non staging envs by setting version variables in the configs/ folder
- the idea is that project1-is just one example of a project, you can have many others
- maybe prod would want it's own kubernetes clusters, but as for the rest, and maybe even prod, I believe there is way to launch images on particular nodes/hardware in a kubernetes cluster


# Instructions

Start Minikube, and tunnels with required addons etc.
```
source ./venc/bin/activate
inv minikube.start
```

build and push images from apps/projects, e.x.:
```
tory@tory ~/Torypages/monorepo/project1-be % inv build-push
```

Deploy staging
```
inv terraform.apply --env=staging
```

Deploy prod
```
inv terraform.apply --env=prod
```

access app via http://<env>.party.central/, update /etc/hosts file to enable this, e.x.:

```
(terraform-py3.12) tory@tory ~/Torypages/monorepo/terraform % cat /etc/hosts
127.0.0.1       localhost
127.0.0.1       party.central
127.0.0.1       prod.party.central
127.0.0.1       staging.party.central
255.255.255.255 broadcasthost
::1             localhost
```

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


