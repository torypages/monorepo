# TODO
- don't forget that docker-compose is still being used for local dev, not Minikube
- have some fake build that will auto deploy main to staging
  - decide if you want "latest" or to automate the latest hash
  - non latest will result in another commit to master everytime a commit to master is needed
- allow for deploying a hash to prod
- Fake CI

# Notes
- There was a problem where resources of one env would overwrite the resources of another, state files solve the overwriting issue
- Minikube grinding to a halt after deploying the second env seemed to get solved by increasing memory. The Kubernetes was giving OOM errors.
- Will use commit hashes or maybe md5 sums for docker tags
- staging may use latest, but other envs will probably use actual versions
- deploy non staging envs by setting version variables in the configs/ folder
- the idea is that project1-is just one example of a project, you can have many others
- maybe prod would want it's own kubernetes clusters, but as for the rest, and maybe even prod, I believe there is way to launch images on particular nodes/hardware in a kubernetes cluster
- Would good to have standard library of PyInvoke tasks. But it would be good if this was a bit more abstracted because we should not force Python on FE folks.
  - maybe the projects could have a file like CI.sh which could define started CI commands, like for linting, building, etc.
  - maybe even instead of CI.sh, it could be some sort a toml or whatever for metadata about the projects


# Design Decisions
- Minikube for experimentation, in real life an actual K8 cluster would be needed, self hosted or as a service, or container services like Fargate would be used.
- No Terragrunt for handling different terraform envs because it would be another thing to learn, I haven't hit a hard enough wall to justify it
- Similarly, no Helm Charts. No ArgoCD.
- Each folder in the root describes a project, which really should be pretty isolated from everything else.


# Instructions

Start Minikube, and tunnels with required addons etc.
```
cd terraform/
poetry shell
inv minikube.start
```

instead of poetry shell I personally use 
```
 source ./venc/bin/activate
```
because I have Poetry configured to create the env in the project folder and sourcing the env with Poetry shell mucks with my Neovim config

In another terminal, build and push images from apps/projects, e.x.:
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


