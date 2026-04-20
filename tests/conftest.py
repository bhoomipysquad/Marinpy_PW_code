import random
import pytest
from playwright.sync_api import sync_playwright, expect
from pages.base_page import BasePage

@pytest.fixture()
def http_auth():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False , slow_mo=500, args=["--start-maximized"])
        context = browser.new_context(http_credentials={"username": "mp-admin","password": "mp-secret"} ,no_viewport=True)
        page = context.new_page()
        page.goto("https://admin-marinapy.pysquad.com/login")
        yield page
        browser.close()

@pytest.fixture
def common_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture
def boater_acc_signup(common_flow):
        page= common_flow
        page.goto("https://dev-marinapy.pysquad.com/")
        print(page.title())
        expect(page).to_have_url("https://dev-marinapy.pysquad.com/")
        page.get_by_role("button" , name = "Sign Up").click()
        expect(page).to_have_url("https://dev-marinapy.pysquad.com/signup")
        expect(page.get_by_role("heading" , name = "Create Account!")).to_be_visible()
        page.get_by_role("textbox", name="First Name").fill("Bhoomi")
        page.get_by_role("textbox" , name="Last Name").fill("Testing")
        page.get_by_role("textbox" , name="Email").fill(f"bhoomi+abcclaim{random.randint(10, 500)}@pysquad.com")
        page.get_by_role("textbox" , name="Password").fill("bhumiB2111@")
        page.get_by_role("button" , name="Create account").click()
        expect(page).to_have_url("https://dev-marinapy.pysquad.com/otp")
        base_page = BasePage(page)
        base_page.fill_otp()
        expect(page).to_have_url("https://dev-marinapy.pysquad.com/map")
        return page



email_id = "bhoomi+abcclaim289@pysquad.com"
password = "bhumiB2111@"
@pytest.fixture
def boater_acc_login(common_flow):
        page= common_flow
        page.goto("https://dev-marinapy.pysquad.com/")
        print(page.title())
        expect(page).to_have_url("https://dev-marinapy.pysquad.com/")
        page.get_by_role("button" , name = "Login").click()
        expect(page).to_have_url("https://dev-marinapy.pysquad.com/login")
        expect(page.get_by_role("heading", name="Welcome back!")).to_be_visible()
        page.get_by_role("textbox" , name="Email").fill(email_id)
        page.get_by_role("textbox" , name="Password").fill(password)
        page.get_by_role("button" , name="Login").click()
        expect(page).to_have_url("https://dev-marinapy.pysquad.com/otp")
        base_page = BasePage(page)
        base_page.fill_otp()
        expect(page).to_have_url("https://dev-marinapy.pysquad.com/map")
        return page

@pytest.fixture
def super_admin_acc_login(http_auth):
        page = http_auth
        page.goto("https://admin-marinapy.pysquad.com/login")
        page.get_by_role("button" , name = "Login").click()
        page.get_by_role("textbox", name="Email").fill("super-aneri@gmail.com")
        page.get_by_role("textbox", name="Password").fill("SA@12345*an")
        page.get_by_role("button", name="Login").click()
        expect(page).to_have_url("https://admin-marinapy.pysquad.com/dashboard")
        return page


