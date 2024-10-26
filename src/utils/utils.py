#here we basically add - headers, cookies, authentications etc..

class Utils(object):
    def common_headers(self):
        headers = {
            "Content-Type": "application/json",
        }
        return headers

    def common_headers_put_patch_delete_basic_auth(self, basic_auth_value):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic" + str(basic_auth_value),
        }
        return headers

    def common_headers_put_patch_delete_cookie(self, token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token),
        }
        return headers