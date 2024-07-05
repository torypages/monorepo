provider "kubernetes" {
  config_path = "~/.kube/config"
}

module "project1-be-app" {
  source      = "./modules/project1-be/app"
  environment = var.environment
}

module "project1-be-database" {
  source      = "./modules/project1-be/database"
  environment = var.environment
}

module "project1-be-broker" {
  source      = "./modules/project1-be/broker"
  environment = var.environment
}

module "project1-be-worker" {
  source      = "./modules/project1-be/worker"
  environment = var.environment
}


resource "kubernetes_ingress_v1" "example_ingress" {
  metadata {
    name = format("%s-ingress", var.environment)
  }

  spec {
    default_backend {
      service {
        name = format("%s-project1-be-app", var.environment)
        port {
          number = 7665
        }
      }
    }

    rule {
      host = format("%s.party.central", var.environment)
      http {
        path {
          backend {
            service {
              name = format("%s-project1-be-app", var.environment)
              port {
                number = 7665
              }
            }
          }

          path = "/*"
        }
      }
    }

    # tls {
    #   secret_name = "tls-secret"
    # }
  }
}
