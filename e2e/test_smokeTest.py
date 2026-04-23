import re
import uuid

from playwright.sync_api import Page, expect

# URL esperada após "Pronto" com estes dados de formulário (Flask url_for).
_ESTUDO_QUERY = (
    "http://127.0.0.1:5000/estudo"
    "?min_foco=25&min_pausa=5&playlist_id=7&objetivos=%5B%22sadsada%22%5D"
)



def test_iniciar_sessao(page: Page):

    page.goto("/")

    page.get_by_role("button", name="Iniciar Seção").click()

    page.locator('input[name="duracao_estudo"]').fill("30")

    page.locator('input[name="duracao_pausa"]').fill("25")

    page.get_by_placeholder("Digite um objetivo").fill("estudar")


    page.get_by_role("button", name="+", exact=True).click()

    page.locator('input[name="playlist_id"]').first.click()
    
    page.get_by_role("button", name="Pronto").click()
    expect(page).to_have_title("FocusFluir")


def test_apos_pronto_redireciona_para_estudo_com_parametros(page: Page):
    """
    Exige playlist com id 7 na BD (rádio value="7" na página /sessao).
    """
    page.goto("/")
    page.get_by_role("button", name="Iniciar Seção").click()

    page.locator('input[name="duracao_estudo"]').fill("25")
    page.locator('input[name="duracao_pausa"]').fill("5")
    page.get_by_placeholder("Digite um objetivo").fill("sadsada")
    page.get_by_role("button", name="+", exact=True).click()

    page.locator('input[name="playlist_id"][value="7"]').click()
    page.get_by_role("button", name="Pronto").click()

    expect(page).to_have_url(_ESTUDO_QUERY)


def test_deletar_playlist(page: Page):
    """
    Cria uma playlist em /playlists, depois remove pelo link ❌.
    Criar exige um URL do YouTube (o servidor resolve o título) — precisa de rede.
    """
    nome = f"e2e-del-{uuid.uuid4().hex[:12]}"
    page.goto("/playlists")

    page.locator('input[name="nome_playlist"]').fill(nome)
    page.locator('textarea[name="links_musica"]').fill(
        "https://www.youtube.com/watch?v=jNQXAC9IVRw"
    )
    page.get_by_role("button", name="Salvar Playlist").click()

    expect(page).to_have_url(re.compile(r".*\/playlists$"))
    expect(page.get_by_text(nome)).to_be_visible()

    item = page.locator(".playlist-list li").filter(has_text=nome)
    item.get_by_role("link", name="❌").click()

    expect(page).to_have_url(re.compile(r".*\/playlists$"))
    expect(page.locator("body")).not_to_contain_text(nome)
