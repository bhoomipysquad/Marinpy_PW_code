from playwright.sync_api import expect
from pages.base_page import BasePage


class Super_Admin_Marina_Claims(BasePage):
    def open_claiming_option(self):
        self.page.get_by_label("menu-unfold").click()
        expect(self.page.get_by_role("button", name="Collapse")).to_be_visible()
        self.page.locator("ul[role='menu'] div[title='Marina Claims']").click()
        expect(self.page).to_have_url("https://admin-marinapy.pysquad.com/marinas")
        expect(self.page.get_by_role("heading", name="Marinas")).to_be_visible(timeout=10000)

    def select_marina(self):
        self.open_claiming_option()
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

    def claim_approved_super_admin(self):
        self.open_claiming_option()
        self.select_marina()
        self.page.get_by_role("button", name="Approve Claim").click()
        print("Claim Approved Successfully")

    def claim_rejected_super_admin(self):
        self.open_claiming_option()
        self.select_marina()
        self.page.get_by_role("button", name="Reject Claim").click()
        self.page.get_by_placeholder("Write a reason...").fill("rejected your claim")
        self.page.get_by_role("button", name="Submit").click()
        print("Claim Rejected Successfully")

    def claim_needs_clarification(self):
        self.open_claiming_option()
        self.select_marina()
        self.page.get_by_role("button", name="Request clarification").click()
        expect(self.page.get_by_text("Claim Request Clarification Pending")).to_be_visible()
        self.page.get_by_placeholder("Go ahead, we're listening...").fill("Hii")

    def marina_active_to_inactive(self):
        self.open_claiming_option()
        self.page.locator("#rc-tabs-0-tab-active").click()
        expect(self.page.get_by_role("columnheader", name="SWITCH")).to_be_visible(timeout=10000)
        marina_name = "Kirstula Marina"
        row = self.page.locator("tr").filter(has=self.page.locator(f"a:text-is('{marina_name}')"))
        expect(row).to_be_visible(timeout=10000)
        row.get_by_role("switch").click()
        self.page.get_by_role("button", name="Yes").click()
        expect(self.page.get_by_text("Marina Inactived successfully")).to_be_visible(timeout=10000)
        print(f"{marina_name} Inactived successfully")
        self.page.get_by_placeholder("Search marina or destination or Id...").fill(marina_name)
        self.page.locator("#rc-tabs-0-tab-inactive").click()
        expect(self.page.get_by_text(marina_name)).to_be_visible(timeout=10000)
        print(f"{marina_name} successfully moved in inactive tab")


