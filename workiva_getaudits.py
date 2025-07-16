import os
import workiva_sdk
from workiva_sdk.rest import ApiException

# Configure the API client
# Audits are in the Prototype Platform (https://developers.workiva.com/prototype-platform/prototype-getaudits/)
# They use the prototype base address instead of the production base address
configuration = workiva_sdk.Configuration(
    host="https://api.app.wdesk.com/prototype/platform"
)
configuration.access_token = os.environ["ACCESS_TOKEN"]

# Use the SDK to call the audits endpoint
with workiva_sdk.ApiClient(configuration) as api_client:
    audits_api = workiva_sdk.AuditsApi(api_client)

    try:
        # Retrieve audits (optionally add filters or sorting)
        response = audits_api.get_audits() # This is a full object that may include metadata
        audits = response.data # This is typically a list of audit objects, each with attributes like id, name, status, etc.

        # Print audit names and IDs
        for audit in audits:
            print(f"Audit Name: {audit.name}, ID: {audit.id}")
    except ApiException as e:
        print("Error retrieving audits:", e)
