from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
# Here is the list of available scopes:
# https://developers.google.com/drive/api/v2/about-auth
SCOPES = ["https://www.googleapis.com/auth/drive"]


def main():
    """Shows basic usage of the Drive v3 API.
    This shows a sample of three different interactions with Google Drive
    through the Google Drive API v3

    - get_gdrive_results: Gets the top 10 files in your google drive
    - upload_file: Uploads a brand new file to your google drive
    - update_file: Updates an existing file with the contents of the file
                   specified
    """
    creds = authenticate_and_authorize_user()
    drive_service = build("drive", "v3", credentials=creds)

    # Gets the top 10 files in your google drive
    get_gdrive_results(drive_service)

    # Uploads a brand new file to your google drive
    file_to_upload = "requirements.txt"
    upload_file(drive_service, file_to_upload)

    # Updates an existing file with the contents of the file specified
    file_id_to_replace = "1SHaDQ6mrlAD3_D516-6VNeT6cKCUY6fK"
    update_file(drive_service, "requirements.txt", file_id_to_replace)


def upload_file(drive_service, file_path):
    file_metadata = {"name": file_path}
    media = MediaFileUpload(file_path)
    file = (
        drive_service.files()
        .create(body=file_metadata, media_body=media, fields="id")
        .execute()
    )
    print("File ID: %s" % file.get("id"))


def update_file(drive_service, file_path, file_id):
    file_metadata = {"name": file_path}
    media = MediaFileUpload(file_path)
    drive_service.files().update(
        body=file_metadata, media_body=media, fileId=file_id
    ).execute()


def get_gdrive_results(drive_service):
    # Call the Drive v3 API
    results = (
        drive_service.files()
        .list(pageSize=10, fields="nextPageToken, files(id, name)")
        .execute()
    )
    items = results.get("files", [])

    if not items:
        print("No files found.")
    else:
        print("Files:")
        for item in items:
            print(f"{item['name']} // ({item['id']})")


def authenticate_and_authorize_user():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return creds


if __name__ == "__main__":
    main()
