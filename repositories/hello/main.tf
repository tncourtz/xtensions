terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "4.28.0"
    }
  }
  backend "azurerm" {
    key = "repositories/template-repositories/terraform.tfstate"
  }
}

provider "github" {
  token = var.token
  owner = "NintexGlobal"
}

#--------------------------------------------------------------
# Templates Repositories
#--------------------------------------------------------------

module "repository-template-hackathon-first-order" {
  source                          = "../../modules/github-repository"
  repository_name                 = "hello"
  description                     = "[Owner: group:default/guardians] this is a test for templates"
  topics                          = ""
  branches                        = ""
  default_branch_name             = ""
  required_status_check_names     = ""
  branch_protection_bypasss_users = ""
  labels                          = ""
}
