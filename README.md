# Google Drive API v3

This repository shows basic usage of the Drive v3 API.

This shows a sample of three different interactions with Google Drive through the Google Drive API v3

Note-worthy functions in the code:

- get_gdrive_results: Gets the top 10 files in your google drive
- upload_file: Uploads a brand new file to your google drive
- update_file: Updates an existing file with the contents of the file
                specified

## Running the code

- Download a credentials.json file by turning on the [Drive API](https://developers.google.com/drive/api/v3/quickstart/python#step_1_turn_on_the)
- Install the required dependencies

```shell
pip install -r requirements.txt
```

- Run the code

```shell
python3 quickstart.py
```

The above command will prompt you to log in to your google account through a browser. Once you've logged in, it will create a `token.pickle` file in your directory so you don't have to use your browser to log in again.

- You're done!
