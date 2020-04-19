from azure.mgmt.resource import ResourceManagementClient
from azure_identity_credential_adapter import AzureIdentityCredentialAdapter
credentials = AzureIdentityCredentialAdapter()

SUBSCRIPTION_IDS = ['', '']
APPLICATION_IDS = ['ea7bb249-5b65-4dea-88c8-15e5aa530fb7', '034cd59b-8363-4f3b-9879-d61e7bcd508e', '351d47b7-5a91-4925-9d60-300d42f4dbbe']
GROUP_NAMES = ['aztagsync1', 'aztagsync2', 'aztagsync3']
LOCATION = 'westus'


resource_client = ResourceManagementClient(credentials, SUBSCRIPTION_IDS[0])
resource_client.resource_groups.create_or_update(GROUP_NAMES[0], {'location': LOCATION, 'tags': {'appid':APPLICATION_IDS[0]}})
resource_client.resource_groups.create_or_update(GROUP_NAMES[1], {'location': LOCATION, 'tags': {'appid':APPLICATION_IDS[1]}})

resource_client = ResourceManagementClient(credentials, SUBSCRIPTION_IDS[1])
resource_client.resource_groups.create_or_update(GROUP_NAMES[2], {'location': LOCATION, 'tags': {'appid':APPLICATION_IDS[2]}})
