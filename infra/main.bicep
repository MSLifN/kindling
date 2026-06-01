targetScope = 'resourceGroup'

@description('Azure region for the demo environment.')
param location string = resourceGroup().location

@description('Environment name for the azd deployment path.')
param environmentName string = 'kindling-dev'

output environmentName string = environmentName
output location string = location
