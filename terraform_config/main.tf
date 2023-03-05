provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "de_zoomcamp" {
  name     = "${var.prefix}-resources"
  location = var.location
}

resource "azurerm_storage_account" "de_zoomcamp_storage_account" {
  name                = "${var.prefix}storageacct"
  resource_group_name = azurerm_resource_group.de_zoomcamp.name
  location            = azurerm_resource_group.de_zoomcamp.location

  account_tier                    = "Standard"
  account_kind                    = "StorageV2"
  account_replication_type        = "LRS"
  enable_https_traffic_only       = true
  access_tier                     = "Hot"
  allow_nested_items_to_be_public = true
}

resource "azurerm_storage_container" "de_zoomcamp_storage_container" {
  name                  = "${var.prefix}storagecontainer"
  storage_account_name  = azurerm_storage_account.de_zoomcamp_storage_account.name
  container_access_type = "blob"
}