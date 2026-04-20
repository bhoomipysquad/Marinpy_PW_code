from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def fill_otp(self):
        expect(self.page).to_have_url("https://dev-marinapy.pysquad.com/otp")
        self.page.get_by_label("OTP Input 1").fill("1")
        self.page.get_by_label("OTP Input 2").fill("2")
        self.page.get_by_label("OTP Input 3").fill("3")
        self.page.get_by_label("OTP Input 4").fill("4")
        self.page.get_by_label("OTP Input 5").fill("5")
        self.page.get_by_label("OTP Input 6").fill("6")

    def upload_file_by_selector(self, selector, file_path):
        self.page.locator(selector).set_input_files(file_path)

    def upload_file_by_locator(self, locator, file_path):
        self.page.locator(locator).set_input_files(file_path)

    def select_option(self, selector, value):
        field = self.page.locator(selector)
        field.fill(value)
        field.press("Enter")

    def select_dropdown(self, selector):
        self.page.locator(selector).click()
        self.page.locator(selector).press("ArrowDown")
        self.page.locator(selector).press("Enter")

    def click_first_marina(self):
        marina = self.page.locator("div[style*='flex: 1 1 0%'][style*='min-width: 0px']").first
        marina.click()


