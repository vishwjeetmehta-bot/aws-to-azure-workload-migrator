terraform {
  required_version = ">= 1.5.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.90.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "migration_rg" {
  name     = "rg-cloud-migration-target"
  location = "eastus"
}

resource "azurerm_virtual_network" "migration_vnet" {
  name                = "vnet-migration-target"
  address_space       = ["10.200.0.0/16"]
  location            = azurerm_resource_group.migration_rg.location
  resource_group_name = azurerm_resource_group.migration_rg.name
}

resource "azurerm_subnet" "migrated_workloads" {
  name                 = "snet-migrated-vms"
  resource_group_name  = azurerm_resource_group.migration_rg.name
  virtual_network_name = azurerm_virtual_network.migration_vnet.name
  address_prefixes     = ["10.200.1.0/24"]
}

