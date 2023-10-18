import os
import string
import time
from random import random
import random

import pytest
from allure_commons._allure import step
from playwright.sync_api import sync_playwright
from playwright.sync_api import *

from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page
def loginn_ui():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto("https://console.dev.intelcloud.cnvrg.io")
            expect(page.locator("//img[@id='prompt-logo-center']")).to_be_visible(timeout=20000)
            expect(page.locator("//*[contains(text(),'Welcome to Intel AI Cloud')]")).to_be_visible(timeout=20000)
            expect(page.locator("//*[contains(text(),'Welcome to Intel AI Cloud')]")).to_contain_text("Welcome to Intel AI Cloud")
            expect(page.locator("//*[contains(text(),'Enter Email and password to log in')]")).to_be_visible(timeout=20000)
            expect(page.locator("//*[contains(text(),'Enter Email and password to log in')]")).to_contain_text("Enter Email and password to log in")
            expect(page.locator("//input[@inputmode='email']")).to_be_visible(timeout=20000)
            expect(page.locator("//input[@id='password']")).to_be_visible(timeout=20000)
            expect(page.locator("//button[@type='button']")).to_be_visible(timeout=20000)
            expect(page.locator("//*[contains(text(),'Forgot password?')]")).to_be_visible(timeout=20000)
            expect(page.locator("//div[@class='c00346576']//button[contains(text(),'Continue')]")).to_be_visible(timeout=20000)
        finally:
            print("Passed: Test Executed")
            context.close()
            browser.close()
loginn_ui()