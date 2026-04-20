from pages.base_page import BasePage


# class Booking_Flow(BasePage):
#     def booking_flow(self,marina_name):
#         search_marina_field = self.page.get_by_placeholder("Search Marina Name and Id")
#         search_marina_field.fill(marina_name)
#         print("success")

class Booking_Flow(BasePage):
    def booking_flow(self):
        search_marina_field = self.page.get_by_placeholder("Search Marina Name and Id")
        search_marina_field.fill("")
        print("success")



