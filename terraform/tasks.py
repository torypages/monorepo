from invoke import Collection

from invoke_tasks.minikube import ns_minikube

namespace = Collection()
namespace.add_collection(ns_minikube)
