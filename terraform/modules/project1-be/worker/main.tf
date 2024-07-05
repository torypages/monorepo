resource "kubernetes_deployment" "worker" {
  metadata {
    name = format("%s-project1-be-worker", var.environment)
    labels = {
      App = "Project1BeWorker"
    }
  }

  spec {
    replicas = 2
    selector {
      match_labels = {
        App = "Project1BeWorker"
      }
    }
    template {
      metadata {
        labels = {
          App = "Project1BeWorker"
        }
      }
      spec {
        container {
          image = "localhost:5000/project1-be-worker/1"
          name  = "project1-be-worker"

          port {
            container_port = 80
          }

          env {
            name  = "celery_broker_host"
            value = format("%s-project1-be-broker.default.svc.cluster.local", var.environment)
          }

          env {
            name  = "celery_broker_port"
            value = "5672"
          }

          env {
            name  = "celery_broker_user"
            value = "coolrabbit"
          }

          env {
            name  = "celery_broker_password"
            value = "8B4819DBAD1951BCCE3"
          }

          env {
            name  = "celery_broker_vhost"
            value = "project1_vhost"
          }

          env {
            name  = "celery_autorestart_workers"
            value = "true"
          }

          env {
            name  = "database_name"
            value = "project1"
          }

          env {
            name  = "database_user"
            value = "root"
          }

          env {
            name  = "database_password"
            value = "922C1C34B4F197C88369AAED08"
          }

          env {
            name  = "database_host"
            value = format("%s-project1-be-database.default.svc.cluster.local", var.environment)
          }

          env {
            name  = "database_port"
            value = "3306"
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


resource "kubernetes_service" "project1-be-worker" {
  metadata {
    name = format("%s-project1-be-worker", var.environment)
  }
  spec {
    selector = {
      App = kubernetes_deployment.worker.spec.0.template.0.metadata[0].labels.App
    }
    port {
      # node_port   = 30251
      port        = 7665
      target_port = 7665
    }

    type = "NodePort"
  }
}
