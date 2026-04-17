from playwright.sync_api import Page, expect

def test_home(page: Page):
    page.goto("/")
    page.get_by_role("button", name="Iniciar Seção").click()
    expect(page).to_have_title("FocusFluir")  
