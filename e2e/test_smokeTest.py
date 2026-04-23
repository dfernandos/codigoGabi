import re
import uuid

from playwright.sync_api import Page, expect


def test_playlist_criar(page: Page):
    """
    Home → Criar Playlists → preenche nome e links (YouTube) → salva → remove com ❌.
    Criar exige URLs do YouTube (o servidor resolve títulos via oEmbed) — precisa de rede.
    """
    nome = f"e2e-pl-{uuid.uuid4().hex[:12]}"
    page.goto("/")
    page.get_by_role("link", name="Criar Playlists").click()

    page.locator('input[name="nome_playlist"]').fill(nome)
    page.locator('textarea[name="links_musica"]').fill(
        "https://www.youtube.com/watch?v=a1vHjBy85TU&list=RDa1vHjBy85TU&start_radio=1\n"
        "https://www.youtube.com/watch?v=wWvu34x2INc&list=RDwWvu34x2INc&start_radio=1"
    )
    page.locator('button[type="submit"]').click()

    expect(page).to_have_url(re.compile(r".*\/playlists$"))
    expect(page.get_by_text(nome)).to_be_visible()

    item = page.locator(".playlist-list li").filter(has_text=nome)
    item.get_by_role("link", name="❌").click()

    expect(page).to_have_url(re.compile(r".*\/playlists$"))
    expect(page.locator("body")).not_to_contain_text(nome)
