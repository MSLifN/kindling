targetScope = 'resourceGroup'

@description('Azure region for the hackathon environment. Pick a region that supports the Foundry Agent Service and gpt-4.1-mini on Global Standard. swedencentral is the EU default, eastus2 the US default. Full list: https://learn.microsoft.com/azure/ai-foundry/openai/how-to/responses#supported-regions')
param location string = 'swedencentral'

@description('Environment name for the azd deployment path.')
param environmentName string = 'kindling-dev'

@description('Name of the chat model deployment created in the Foundry account.')
param chatModelDeploymentName string = 'gpt-4.1-mini'

@description('Model name to deploy. Must be available in the chosen region.')
param chatModelName string = 'gpt-4.1-mini'

@description('Model version to pin the deployment to.')
param chatModelVersion string = '2025-04-14'

@description('Capacity (in thousands of tokens per minute) for the model deployment. Hackathon default is 1.')
param chatModelCapacity int = 1

var uniqueSuffix = toLower(uniqueString(resourceGroup().id, environmentName))
var aiFoundryName = 'foundry-${environmentName}-${uniqueSuffix}'
var aiProjectName = '${aiFoundryName}-proj'

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

resource aiFoundry 'Microsoft.CognitiveServices/accounts@2025-06-01' = {
  name: aiFoundryName
  location: location
  identity: {
    type: 'SystemAssigned'
  }
  sku: {
    name: 'S0'
  }
  kind: 'AIServices'
  properties: {
    allowProjectManagement: true
    customSubDomainName: aiFoundryName
    disableLocalAuth: false
  }
}

resource aiProject 'Microsoft.CognitiveServices/accounts/projects@2025-06-01' = {
  name: aiProjectName
  parent: aiFoundry
  location: location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {}
}

resource chatModel 'Microsoft.CognitiveServices/accounts/deployments@2025-06-01' = {
  parent: aiFoundry
  name: chatModelDeploymentName
  sku: {
    capacity: chatModelCapacity
    name: 'GlobalStandard'
  }
  properties: {
    model: {
      name: chatModelName
      format: 'OpenAI'
      version: chatModelVersion
    }
  }
}

output FOUNDRY_PROJECT_ENDPOINT string = 'https://${aiFoundry.properties.customSubDomainName}.services.ai.azure.com/api/projects/${aiProject.name}'
output AZURE_OPENAI_ENDPOINT string = aiFoundry.properties.endpoint
output AZURE_OPENAI_DEPLOYMENT_NAME string = chatModel.name
output APPLICATIONINSIGHTS_CONNECTION_STRING string = appInsights.properties.ConnectionString
output AZURE_AIFOUNDRY_NAME string = aiFoundry.name
output AZURE_AIFOUNDRY_PROJECT_NAME string = aiProject.name
output AZURE_LOG_ANALYTICS_WORKSPACE_ID string = logAnalyticsWorkspace.id
output AZURE_LOCATION string = location
output AZURE_ENV_NAME string = environmentName
