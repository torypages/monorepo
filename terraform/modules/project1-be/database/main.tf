resource "kubernetes_deployment" "database" {
  metadata {
    name = format("%s-project1-be-database", var.environment)
    labels = {
      App = format("%s-project1-be-database", var.environment)
    }
  }

  spec {
    replicas = 1
    selector {
      match_labels = {
        App = format("%s-project1-be-database", var.environment)
      }
    }
    template {
      metadata {
        labels = {
          App = format("%s-project1-be-database", var.environment)
        }
      }
      spec {
        container {
          image = "mysql:8.4.0"
          name  = format("%s-project1-be-database", var.environment)

          port {
            container_port = 3306
          }


          env {
            name  = "MYSQL_DATABASE"
            value = "project1"
          }

          env {
            name  = "MYSQL_ROOT_PASSWORD"
            value = "922C1C34B4F197C88369AAED08"
          }

          resources {
            limits = {
              cpu    = "0.5"
              memory = "1024Mi"
            }
            requests = {
              cpu    = "250m"
              memory = "1024Mi"
            }
          }
        }
      }
    }
  }
}


resource "kubernetes_service" "project1-be-database" {
  metadata {
    name = format("%s-project1-be-database", var.environment)
  }
  spec {
    selector = {
      App = kubernetes_deployment.database.spec.0.template.0.metadata[0].labels.App
    }
    port {
      # node_port   = 30209
      port        = 3306
      target_port = 3306
    }

    type = "NodePort"
  }
}
