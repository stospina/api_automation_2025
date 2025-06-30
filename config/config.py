import os
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv("TOKEN_API")
url_base = os.getenv("URL_BASE")
program_uuid = os.getenv("PROGRAM_UUID")

web_hook = os.getenv("WEB_HOOK")

url_clockify = os.getenv("URL_BASE_CLOCKIFY")
api_token_clockify = os.getenv("TOKEN_CLOCKIFY")
workspace_id = os.getenv("WORKSPACE_CLOCKIFY")

headers = {
    "Authorization": "Bearer {}".format(api_token),
    "Content-Type": "application/json",
}


headers_clockify = {
    "x-api-key": f"{api_token_clockify}",
    "Content-Type": "application/json",
}