provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_deployment" "nginx" {
  metadata {
    name = "scalable-nginx-example"
    labels = {
      App = "ScalableNginxExample"
    }
  }

  spec {
    replicas = 2
    selector {
      match_labels = {
        App = "ScalableNginxExample"
      }
    }
    template {
      metadata {
        labels = {
          App = "ScalableNginxExample"
        }
      }
      spec {
        container {
          image = "nginx:latest"
          name  = "example"

          port {
            container_port = 80
          }

          resources {
            limits = {
              cpu    = "0.5"
              memory = "512Mi"
            }
            requests = {
              cpu    = "250m"
              memory = "50Mi"
            }
          }
        }
      }
    }
  }
}


resource "kubernetes_service" "nginx" {
  metadata {
    name = "nginx-example"
  }
  spec {
    selector = {
      App = kubernetes_deployment.nginx.spec.0.template.0.metadata[0].labels.App
    }
    port {
      node_port   = 30201
      port        = 80
      target_port = 80
    }

    type = "NodePort"
  }
}

resource "kubernetes_deployment" "project1-be" {
  metadata {
    name = "project1-be"
    labels = {
      App = "Project1Be"
    }
  }

  spec {
    replicas = 2
    selector {
      match_labels = {
        App = "Project1Be"
      }
    }
    template {
      metadata {
        labels = {
          App = "Project1Be"
        }
      }
      spec {
        container {
          image = "localhost:5000/project1-be/1"
          name  = "project1-ve"

          port {
            container_port = 80
          }

          resources {
            limits = {
              cpu    = "0.5"
              memory = "512Mi"
            }
            requests = {
              cpu    = "250m"
              memory = "50Mi"
            }
          }
        }
      }
    }
  }
}


resource "kubernetes_service" "project1-be" {
  metadata {
    name = "project1-be"
  }
  spec {
    selector = {
      App = kubernetes_deployment.project1-be.spec.0.template.0.metadata[0].labels.App
    }
    port {
      # node_port   = 30201
      port        = 80
      target_port = 80
    }

    type = "NodePort"
  }
}
