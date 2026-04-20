from playwright.sync_api import expect
from pages.base_page import BasePage


class Profile_Edit(BasePage):
     def add_profile_info(self):
         self.page.get_by_label("user").click()
         self.page.get_by_text("Edit",exact=True).click()
         expect(self.page).to_have_url("https://dev-marinapy.pysquad.com/profile")
         self.upload_file_by_selector('input[type="file"]', "/home/pys/Downloads/pexels-pixabay-358588.jpg")
         expect(self.page.get_by_role("button",name="Remove",exact=True))
         print(self.page.get_by_placeholder("Elizabeth").get_attribute("value"))
         print(self.page.get_by_placeholder("Olsen").get_attribute("value"))
         print(self.page.get_by_placeholder("username").get_attribute("value"))
         expect(self.page.get_by_role("textbox" , name="userName")).to_be_disabled()
         print(self.page.get_by_placeholder("example@email.com").get_attribute("value"))
         expect(self.page.get_by_role("textbox" , name="email")).to_be_disabled()
         self.select_option("#rc_select_4", "+91")
         self.page.get_by_placeholder("Enter phone").fill("1234567899")
         self.select_option("#rc_select_5", "India")
         self.select_option("#rc_select_6", "Gujarat")
         self.select_option("#rc_select_7", "Ahmedabad")
         self.page.get_by_placeholder("123 Main St").fill("shilp Aaron")
         self.page.get_by_placeholder("Apt 4B").fill("Sindhu bhavan road")
         self.page.get_by_placeholder("10010").fill("123456")
         self.page.get_by_role("button", name="Save Changes").click()
         success_msg = self.page.get_by_text("Profile updated successfully!" , exact=False)
         expect(success_msg).to_be_visible(timeout=10000)

