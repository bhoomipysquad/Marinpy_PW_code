from playwright.sync_api import expect
from pages.base_page import BasePage


class Super_Admin_claim_Approved(BasePage):
    def claim_approved_super_admin(self):
        self.page.get_by_label("menu-unfold").click()
        expect(self.page.get_by_role("button", name="Collapse")).to_be_visible()
        self.page.locator("ul[role='menu'] div[title='Marina Claims']").click()
        expect(self.page).to_have_url("https://admin-marinapy.pysquad.com/marinas")
        expect(self.page.get_by_role("heading", name="Marinas")).to_be_visible(timeout=10000)
        first_row_text = self.page.locator("td.ant-table-cell a").first.inner_text()
        print(f"Approved Marina Name : ", first_row_text)
        self.page.locator('tbody tr:nth-child(2) td:nth-child(4) div:nth-child(1) div:nth-child(2) div:nth-child(1)').click()
        self.page.locator("input[readonly]").first.wait_for()
        fields = ["First Name","Last Name","Requested Marina", "Email","Phone number","Job Profile","Note"]
        values = [self.page.locator("div.ant-form-item-row")
                    .filter(has=self.page.locator("label", has_text=field))
                    .locator("input, textarea")
                    .first
                    .input_value()
                    .strip()
            for field in fields
        ]
        for field,value in zip(fields,values):
            print(f"{field}: {value}")
        marina_name_in_model = (self.page.locator("div.ant-form-item-row").
                                filter(has=self.page.locator("label", has_text="Requested Marina"))).locator("input, textarea").first.input_value()
        if first_row_text == marina_name_in_model :
         self.page.get_by_role("button", name="Approve Claim").click()
         print("Claim Approved Successfully")
