from invoke import Collection

from invoke_tasks.minikube import ns_minikube
from invoke_tasks.terraform import ns_terraform

namespace = Collection()
namespace.add_collection(ns_minikube)
namespace.add_collection(ns_terraform)
