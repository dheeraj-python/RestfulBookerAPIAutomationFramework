# This python file will contains all the URL's with it's endpoints

class APIConstants():
    def base_url(self):
        return "https://restful-booker.herokuapp.com/"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_authentication(self):
        return "https://restful-booker.herokuapp.com/auth"

# For Update - PUT, PATH & DELETE we will create a sepearte function because we need booking_id to perform the crud operations

    def url_patch_put_del(booking_id):
        return "https://restful-booker.herokuapp.com/booking" + str(booking_id)