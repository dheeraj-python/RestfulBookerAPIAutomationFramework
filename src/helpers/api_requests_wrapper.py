#Here we will put common codes which were reusable many times in API automation.

import json
import requests

def get_request(url, auth):
    response = requests.get(url = url, auth = auth)
    return response.json()

def post_request(url,auth,payload,in_json, headers):
    post_response = requests.post(url = url, auth = auth, headers = headers, data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response

def patch_request(url,auth,payload,in_json, headers):
    patch_response = requests.patch(url = url, auth = auth, headers = headers, data=json.dumps(payload))
    if in_json is True:
        return patch_response.json()
    return patch_response

def put_request(url,auth,payload,in_json, headers):
    put_response = requests.put(url = url, auth = auth, headers = headers, data=json.dumps(payload))
    if in_json is True:
        return put_response.json()
    return put_response

def delete_request(url,auth,in_json, headers):
    delete_response = requests.delete(url = url, auth = auth, headers = headers)
    if in_json is True:
        return delete_response.json()
    return delete_response
