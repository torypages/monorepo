resource "kubernetes_deployment" "project1-be-broker" {
  metadata {
    name = format("%s-project1-be-broker", var.environment)
    labels = {
      App = "Project1BeBroker"
    }
  }

  spec {
    replicas = 1
    selector {
      match_labels = {
        App = "Project1BeBroker"
      }
    }
    template {
      metadata {
        labels = {
          App = "Project1BeBroker"
        }
      }
      spec {
        container {
          image = "rabbitmq:3.13.3-management"
          name  = "project1-be-broker"

          port {
            container_port = 5672
          }


          env {
            name  = "RABBITMQ_DEFAULT_USER"
            value = "coolrabbit"
          }

          env {
            name  = "RABBITMQ_DEFAULT_PASS"
            value = "8B4819DBAD1951BCCE3"
          }

          env {
            name  = "RABBITMQ_DEFAULT_VHOST"
            value = "project1_vhost"
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


resource "kubernetes_service" "project1-be-broker" {
  metadata {
    name = format("%s-project1-be-broker", var.environment)
  }
  spec {
    selector = {
      App = kubernetes_deployment.project1-be-broker.spec.0.template.0.metadata[0].labels.App
    }
    port {
      # node_port   = 30289
      port        = 5672
      target_port = 5672
    }

    type = "NodePort"
  }
}
