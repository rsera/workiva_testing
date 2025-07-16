import os
import workiva_sdk
from workiva_sdk.models.file import File
from workiva_sdk_rest import ApiException


# Configure the API client
configuration = workiva_sdk.Configuration(
    host="https://api.app.wdesk.com/platform/v1"
)
configuration.access_token = os.environ["ACCESS_TOKEN"]

# Use the SDK to create a file
with workiva_sdk.ApiClient(configuration) as api_client:
    files_api = workiva_sdk.FilesApi(api_client)

    new_file = File(
        name="Board Presentation",
        kind="Presentation"  # Options: Document, Spreadsheet, Presentation, Folder
    )

    try:
        response = files_api.create_file(new_file)
        print("Created file ID:", response.id)
    except ApiException as e:
        print("Error creating file:", e)
