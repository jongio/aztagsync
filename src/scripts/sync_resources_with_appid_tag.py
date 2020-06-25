import requests
from azure.mgmt.resource.subscriptions import SubscriptionClient
from azure.mgmt.resource.resources import ResourceManagementClient

from azure_identity_credential_adapter import AzureIdentityCredentialAdapter
credentials = AzureIdentityCredentialAdapter()

LOCATION = 'westus'

print('Retrieving AppMetadata')

r = requests.get("http://localhost:5000/appmetadata")
app_metadata = r.json()

print('Retrieving Subscriptions')

subscription_client = SubscriptionClient(credentials)
subscriptions = subscription_client.subscriptions.list()

for subscription in subscriptions:
    resource_client = ResourceManagementClient(
        credentials, subscription.subscription_id)

    resources_with_appid_tag = resource_client.resource_groups.list(
        filter="tagName eq 'appid'")

    for resource in resources_with_appid_tag:
        print(f'Syncing {resource.name}')

        app_metadatum = next(
            (x for x in app_metadata if x['id'] == resource.tags['appid']), None)

        if app_metadata != None:
            resource.tags.update({'business-owner': app_metadata[0]['businessOwner'], 'tech-owner': app_metadata[0]['techOwner']})
            tag_update = resource_client.tags.update_at_scope(resource.id, 'Merge', {'tags': resource.tags})
            print(tag_update)
            #tag_update = resource_client.resource_groups.create_or_update(resource.name, {'location': LOCATION, 'tags': resource.tags})

print('Done')
