import re
from playwright.sync_api import expect
from pages.base_page import BasePage
import random


class Claim_Marina(BasePage):
    def claim_marina_flow(self):
        search_marina_field = self.page.get_by_placeholder("Search marina or destination...")
        search_marina_field.fill(f"{random.randint(10, 500)}")
        # search_marina_field.fill("De Wiel Yacht Harbour")
        entered_marina_id = search_marina_field.input_value(timeout=10000)
        print(f"Entered marina ID = {entered_marina_id}")
        marina = self.page.locator("div[style*='flex: 1 1 0%'][style*='min-width: 0px']").first
        expect(marina).to_be_visible(timeout=10000)
        marina_name = marina.locator("div[style*='font-size: 14px'][style*='font-weight: 600']").inner_text().strip()
        print("Found Marina Name : " , marina_name)
        with self.page.expect_popup() as new_page_info:
         marina.click()
         new_page = new_page_info.value
         print(f"Opened URL: {new_page.url}")
         expect(new_page).to_have_url(re.compile("https://dev-marinapy.pysquad.com/open/marinas/.*"),timeout=10000)
         marina_name_element = new_page.locator("h1.ant-typography").first
         expect(marina_name_element).to_be_visible()
         opened_marina_name = marina_name_element.inner_text().strip()
         print("Marina detailed page : " , opened_marina_name)
         assert opened_marina_name == marina_name
         claim_marina_button = new_page.get_by_role("button",name="Claim this Marina" ,exact=True)
         already_claimed_button = new_page.get_by_role("button",name="Already Claimed" ,exact=True)
         under_process_button = new_page.get_by_role("button",name="Under Process" ,exact=True)
         if claim_marina_button.is_visible():
             print(f"{marina_name} is available to claim.")
             new_page.get_by_role("button",name="Claim this Marina" ,exact=True).click(timeout=10000)
             expect(new_page).to_have_url("https://dev-marinapy.pysquad.com/claim")
             new_page.get_by_role("combobox").fill("+91")
             new_page.get_by_role("combobox").press("Tab")
             new_page.get_by_role("combobox").press("Tab")
             new_page.get_by_placeholder("Enter phone").fill("1234567899")
             new_page.get_by_placeholder("Describe your job role").fill("QA")
             new_page.get_by_placeholder("Additional comments").fill("NO COMMENT")
             new_page.locator("input[type='file']").set_input_files("/home/pys/PycharmProjects/Marinpy_PW_code/Screenshot from 2026-05-22 17-04-23.png")
             new_page.get_by_role("button",name="Submit" ,exact=True).click()
             new_page.get_by_role("button",name="OK" ,exact=True).click()
             expect (new_page.get_by_role("button",name="Withdraw my claim" ,exact=True)).to_be_visible()


         elif already_claimed_button.is_visible() or under_process_button.is_visible():
             print(f"{marina_name} is under process or already claimed")
             new_page.close()
             self.claim_marina_flow()

         return marina_name
