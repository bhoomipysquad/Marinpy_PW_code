from playwright.sync_api import expect
from pages.base_page import BasePage


class Add_New_Boat(BasePage):
    boat_name= "boat 2"
    boat_model= "Model 2"
    shipyard= "Ship yard 2"
    construction_year = "2020"
    length = "20"
    width= "30"
    draft= "40"
    air_draft= "50"
    weight= "60"
    country= "india"
    home_port= "home port 1"
    registration_number= "2563256"


    def add_new_boat(self):
        self.page.get_by_label("menu-unfold").click()
        expect(self.page.get_by_role("button" , name= "Collapse")).to_be_visible()
        self.page.locator("//ul[@role='menu']//div[@title='My Boats']").click()
        expect(self.page).to_have_url("https://dev-marinapy.pysquad.com/boats")
        expect(self.page.get_by_role("heading",name="My Boats")).to_be_visible(timeout=10000)
        self.page.get_by_role("button", name="Add New Boat").click()
        expect(self.page).to_have_url("https://dev-marinapy.pysquad.com/boats/add-new-boat")
        expect(self.page.get_by_role("heading",name="Add New Boat")).to_be_visible(timeout=10000)
        self.page.get_by_role("textbox",name="Boat Name").fill(self.boat_name)
        self.page.get_by_role("textbox",name="Model").fill(self.boat_model)
        self.page.get_by_role("textbox",name="Shipyard").fill(self.shipyard)
        self.page.get_by_role("textbox",name="Construction Year").fill(self.construction_year)
        self.page.get_by_role("textbox",name="Construction Year").press("Tab")
        self.page.locator("#unit_system").press("ArrowDown")
        self.page.locator("#unit_system").press("Enter")
        self.page.locator("#length").fill(self.length)
        self.page.locator("#width").fill(self.width)
        self.page.locator("#draft").fill(self.draft)
        self.page.locator("#airDraft").fill(self.air_draft)
        self.page.locator("#weight").fill(self.weight)
        self.select_dropdown("#propulsion")
        self.select_dropdown("#hullMaterial")
        self.page.locator("#country").fill(self.country)
        self.page.locator("#country").press("ArrowDown")
        self.page.locator("#country").press("Enter")
        self.page.locator("#homePort").fill(self.home_port)
        self.page.locator("#registrationNumber").fill(self.registration_number)
        self.upload_file_by_locator('input[type="file"]',"/home/pys/Downloads/pexels-pixabay-358588.jpg")
        self.page.get_by_role("button", name="Add Boat").click()
        expect(self.page).to_have_url("https://dev-marinapy.pysquad.com/boats")
        expect(self.page.get_by_role("heading",name="My Boats")).to_be_visible(timeout=10000)


