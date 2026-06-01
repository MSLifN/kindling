targetScope = 'resourceGroup'

@description('Azure region for the demo environment.')
param location string = resourceGroup().location

@description('Environment name for the azd deployment path.')
param environmentName string = 'kindling-dev'

var uniqueSuffix = toLower(uniqueString(resourceGroup().id, environmentName))

resource logAnalyticsWorkspace 'Microsoft.OperationalInsights/workspaces@2022-10-01' = {
  name: 'law-${environmentName}-${uniqueSuffix}'
  location: location
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 30
    features: {
      enableLogAccessUsingOnlyResourcePermissions: true
    }
  }
}

resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: 'appi-${environmentName}-${uniqueSuffix}'
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: logAnalyticsWorkspace.id
    Flow_Type: 'Bluefield'
    Request_Source: 'rest'
  }
}

output environmentName string = environmentName
output location string = location
output logAnalyticsWorkspaceId string = logAnalyticsWorkspace.id
output applicationInsightsConnectionString string = 'InstrumentationKey=${appInsights.properties.InstrumentationKey}'
