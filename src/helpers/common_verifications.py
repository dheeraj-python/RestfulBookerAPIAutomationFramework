#here we add common verififcations like - status code verification, JSON Schema Validation

def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data,"Failed Status Code Matched"

def verify_response_key(key, expected_data):
    assert key == expected_data

def verify_json_key_not_null(key):
    assert key != 0
    assert key > 0

def verify_json_token_not_null(token):
    assert token != 0, "Failed, Key is not null" + token

def verify_header_content_type_not_null(content_type):
    assert content_type != 0