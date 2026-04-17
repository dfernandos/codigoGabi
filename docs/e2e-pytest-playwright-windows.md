# Testes E2E com pytest + Playwright (Windows)

Guia alinhado ao fluxo “servidor + pytest”, com comandos pensados para **Windows** (Prompt de Comando e PowerShell).

---

## 1. Ambiente virtual (recomendado)

Abre o terminal na pasta do projeto (PowerShell ou CMD).

**Ir para a pasta do projeto** (ajusta o caminho):

```bat
cd C:\caminho\do\teu\projeto
```

**Criar o ambiente virtual** (usa `python`; se não funcionar, tenta `py -3.12` ou o launcher que tiveres):

```bat
python -m venv .venv
```

**Ativar o venv**

- **Prompt de Comando (cmd.exe):**

```bat
.venv\Scripts\activate.bat
```

- **PowerShell** (se der erro de política de execução, vê a secção “Erros comuns”):

```powershell
.\.venv\Scripts\Activate.ps1
```

O prompt deve mostrar `(.venv)` à frente quando estiver ativo.

---

## 2. Instalar pacotes

Com o venv ativado:

```bat
pip install pytest playwright pytest-playwright
```

Ou adiciona ao `requirements.txt` / `pyproject.toml`:

```text
pytest>=8.0
playwright>=1.49.0
pytest-playwright>=0.6.0
```

Depois:

```bat
pip install -r requirements.txt
```

---

## 3. Instalar browsers do Playwright

```bat
playwright install
```

Só **Chromium** (mais leve):

```bat
playwright install chromium
```

Em **Linux** (CI/Docker) às vezes é preciso dependências de sistema (`playwright install-deps` ou `playwright install --with-deps`, conforme a tua versão). **No Windows normalmente não precisas** deste passo para desenvolvimento local.

---

## 4. Configurar o pytest

Cria ou edita `pytest.ini` na **raiz** do projeto:

```ini
[pytest]
pythonpath = .
base_url = http://127.0.0.1:PORTA
```

- **`pythonpath = .`** — importa o teu pacote/app a partir da raiz (ajusta se usares `src/`).
- **`base_url`** — URL onde a aplicação corre; nos testes usas `page.goto("/")` e o plugin junta ao `base_url`.
- Troca **`PORTA`** pela porta real (ex.: Flask **5000**, **5050**, Django **8000**).

Neste projeto o exemplo em `pytest.ini` usa `http://127.0.0.1:5000`.

Se o projeto tiver `pyproject.toml`, podes pôr a mesma config em `[tool.pytest.ini_options]` em vez de `pytest.ini`.

---

## 5. Estrutura de pastas (sugestão)

```text
projeto/
  app.py ou src/...
  pytest.ini
  requirements.txt
  tests/              # testes unitários / API
  e2e/                # só Playwright (opcional mas claro)
    conftest.py
    test_*.py
```

Ou tudo em `tests/e2e/` — o importante é **não misturar** sem querer regras diferentes.

---

## 6. Teste E2E mínimo

Exemplo `e2e/test_smoke.py`:

```python
from playwright.sync_api import Page, expect

def test_home(page: Page):
    page.goto("/")
    expect(page).to_have_title("...")  # ou um texto da página
```

O fixture `page` vem do **pytest-playwright** (não precisas importar o plugin manualmente se o pacote está instalado).

---

## 7. Servidor da aplicação

Os testes E2E **precisam** da app a correr **noutro processo** (a não ser que configures um fixture para subir o servidor — mais avançado).

- **Terminal 1:** sobe a app (ex. `python app.py`, `flask run`, `uvicorn ...`, `python manage.py runserver`).
- **Terminal 2:** corre os E2E (com o **mesmo** Python/venv ativo):

```bat
pytest e2e/ -v
```

Opcional: em `e2e/conftest.py`, um `pytest.skip` se a porta não responder (evita falhas confusas).

---

## 8. Comandos para correr (Windows)

Só unitários / pasta `tests/`:

```bat
pytest tests/ -v
```

Só E2E:

```bat
pytest e2e/ -v
```

Ver o browser (debug):

```bat
pytest e2e/ -v --headed
```

Gerar código (com o servidor já a correr):

```bat
playwright codegen http://127.0.0.1:PORTA
```

Substitui `PORTA` pela mesma do `base_url`.

**Dica:** Se tiveres várias instalações de Python, usa sempre o mesmo interpretador:

```bat
python -m pytest e2e/ -v
```

---

## 9. Checklist rápido

| Passo | O quê |
|--------|--------|
| 1 | `.venv` + `activate` (cmd ou PowerShell) |
| 2 | `pip install pytest playwright pytest-playwright` |
| 3 | `playwright install` (ou só `chromium`) |
| 4 | `pytest.ini` com `pythonpath` e `base_url` |
| 5 | Ficheiros `e2e/test_*.py` com fixture `page` |
| 6 | App a correr na mesma URL/porta do `base_url` |
| 7 | `requirements.txt` atualizado para o resto da equipa/CI |

---

## 10. Erros comuns

- **`No module named 'flask'`** (ou outro) — instala as dependências da app **na mesma venv** onde instalaste o pytest.
- **`pytest` usa outro Python** — ativa o venv e confirma com `where python` (cmd) ou `Get-Command python` (PowerShell); preferível `python -m pytest`.
- **E2E falha com connection refused** — servidor não está a correr ou a **porta** no `base_url` está errada.
- **`base_url` ignorado** — confirma que instalaste **pytest-playwright** e que o nome da opção no `pytest.ini` é `base_url` (documentação oficial do plugin).
- **PowerShell: não pode carregar `Activate.ps1`** — execução de scripts desativada. Soluções típicas: usar **cmd** e `activate.bat`, ou no PowerShell (sessão atual):  
  `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`  
  (só se a política da tua máquina permitir; em ambientes corporativos pergunta ao IT.)

---

Isto cobre o mesmo fluxo noutro projeto em Windows: copiar o padrão de `pytest.ini`, pasta `e2e/`, dependências e o fluxo **servidor + pytest** em dois terminais.
