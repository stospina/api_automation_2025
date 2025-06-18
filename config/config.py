import os
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv("TOKEN_API")
url_base = os.getenv("URL_BASE")
program_uuid = os.getenv("PROGRAM_UUID")

headers = {
    "Authorization": "Bearer {}".format(api_token),
    "Content-Type": "application/json",
}
