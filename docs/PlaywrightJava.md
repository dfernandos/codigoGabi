# projeto-spring-jpa-v1

Projeto para exercitar e aprender JPA com Spring Boot.

O **`pom.xml` já inclui** a dependência **Playwright para Java** (`com.microsoft.playwright:playwright`, escopo `test`), a propriedade `playwright.version`, o plugin **exec-maven-plugin** e um teste de fumaça em `src/test/java/.../e2e/PlaywrightSmokeTest.java` (abre `https://playwright.dev/` e valida o título).

Na primeira máquina, após clonar, é preciso **instalar os binários dos navegadores** (veja os passos abaixo conforme o sistema).

Este documento inclui o **Maven Wrapper**: no **Windows** use `mvnw.cmd`; no **Linux e macOS** use `./mvnw` (script shell, não o `.cmd`).

---

## Linux e macOS (bash / zsh)

Na raiz do projeto:

```bash
chmod +x mvnw   # só se o script não estiver executável
./mvnw -q dependency:resolve
```

**Instalar os navegadores do Playwright** — use **aspas** nas propriedades `-Dexec...`. Sem aspas, o terminal pode quebrar o argumento e o Maven interpreta `.mainClass=...` como fase do ciclo de vida (`Unknown lifecycle phase ".mainClass=..."`). Esse problema é **comum no PowerShell do Windows**; no bash/zsh do Linux/macOS a mesma regra se aplica.

```bash
./mvnw exec:java -e "-Dexec.mainClass=com.microsoft.playwright.CLI" "-Dexec.args=install"
```

**Codegen (exemplo):**

```bash
./mvnw exec:java -e "-Dexec.mainClass=com.microsoft.playwright.CLI" "-Dexec.args=codegen https://demo.playwright.dev/todomvc"
```

**Teste de fumaça:**

```bash
./mvnw -Dtest=PlaywrightSmokeTest test
```

Cache dos browsers no Linux costuma ficar em `~/.cache/ms-playwright`.

---

## Pré-requisitos (Windows)

- **JDK 17** (alinhado ao `java.version` do `pom.xml`).
- Terminal: **Prompt de Comando (cmd)** ou **PowerShell** na pasta do projeto.

### Navegar até a pasta do projeto

Ajuste o caminho se o seu clone estiver em outro lugar:

**Prompt de Comando:**

```cmd
cd C:\caminho\para\projeto-spring-jpa-v1
```

**PowerShell:**

```powershell
cd C:\caminho\para\projeto-spring-jpa-v1
```

### Como usar o Maven neste projeto

No Windows, use o wrapper **`mvnw.cmd`** na raiz do repositório:

| Ambiente        | Comando Maven |
|----------------|----------------|
| Prompt (cmd)   | `mvnw.cmd`    |
| PowerShell     | `.\mvnw.cmd`  |

Se você tiver Maven instalado globalmente, pode usar `mvn` no lugar de `mvnw.cmd`, mas o projeto já inclui o wrapper para não depender da instalação global.

### PowerShell e o erro `Unknown lifecycle phase ".mainClass=..."`

No **PowerShell**, argumentos como `-Dexec.mainClass=...` são repartidos de um jeito que o Maven **não** recebe a propriedade inteira — e aparece exatamente esse erro. **Sempre** use os comandos **com aspas** nas propriedades `-D`, como nos exemplos da seção **Comandos no Windows → passo 2** abaixo (forma `"-Dexec.mainClass=..."` e `"-Dexec.args=..."`). No **cmd.exe** a forma com aspas também é a mais segura.

---

## Playwright para Java — configuração no `pom.xml`

> **Já aplicado neste repositório:** propriedade `playwright.version`, dependência `playwright`, plugin `exec-maven-plugin`. Os trechos abaixo servem de referência ou para ajustes manuais.

Documentação oficial: [Playwright Java — Introdução](https://playwright.dev/java/docs/intro).

### 1. Propriedade da versão (opcional)

Dentro de `<properties>`:

```xml
<playwright.version>1.52.0</playwright.version>
```

Confira a versão mais recente em [Maven Central — playwright](https://central.sonatype.com/artifact/com.microsoft.playwright/playwright).

### 2. Dependência

Dentro de `<dependencies>`:

```xml
<dependency>
    <groupId>com.microsoft.playwright</groupId>
    <artifactId>playwright</artifactId>
    <version>${playwright.version}</version>
    <scope>test</scope>
</dependency>
```

Se não usar a propriedade, substitua `${playwright.version}` por um número de versão fixo (por exemplo `1.52.0`).

### 3. Plugin Exec (CLI do Playwright)

Dentro de `<build><plugins>`, junto ao `spring-boot-maven-plugin`:

```xml
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>exec-maven-plugin</artifactId>
    <version>3.5.1</version>
</plugin>
```

O CLI é usado para **instalar os navegadores** e para o **`codegen`**.

---

## Comandos no Windows (passo a passo)

Execute os comandos **na pasta raiz do projeto** (onde está o `mvnw.cmd`).

### 1. Baixar dependências Maven

**cmd:**

```cmd
mvnw.cmd -q dependency:resolve
```

**PowerShell:**

```powershell
.\mvnw.cmd -q dependency:resolve
```

### 2. Instalar os binários dos navegadores (Chromium, Firefox, WebKit)

Obrigatório após adicionar ou atualizar o Playwright. Os arquivos vão para o cache do usuário no Windows (por exemplo em `%USERPROFILE%\AppData\Local\ms-playwright`).

Prefira **sempre** as propriedades `-Dexec...` **entre aspas** (funciona no cmd, no PowerShell e evita erros parecidos com o do Linux):

**cmd:**

```cmd
mvnw.cmd exec:java -e "-Dexec.mainClass=com.microsoft.playwright.CLI" "-Dexec.args=install"
```

**PowerShell:**

```powershell
.\mvnw.cmd exec:java -e "-Dexec.mainClass=com.microsoft.playwright.CLI" "-Dexec.args=install"
```

**Instalar só o Chromium:**

**cmd:**

```cmd
mvnw.cmd exec:java -e "-Dexec.mainClass=com.microsoft.playwright.CLI" "-Dexec.args=install chromium"
```

**PowerShell:**

```powershell
.\mvnw.cmd exec:java -e "-Dexec.mainClass=com.microsoft.playwright.CLI" "-Dexec.args=install chromium"
```

**Ajuda do `install`:**

**cmd:**

```cmd
mvnw.cmd exec:java -e "-Dexec.mainClass=com.microsoft.playwright.CLI" "-Dexec.args=install --help"
```

**PowerShell:**

```powershell
.\mvnw.cmd exec:java -e "-Dexec.mainClass=com.microsoft.playwright.CLI" "-Dexec.args=install --help"
```

(Consulte também a [documentação de browsers](https://playwright.dev/java/docs/browsers).)

### 3. Subir a aplicação Spring Boot (para testes contra `http://localhost:8080`)

**Terminal 1 — cmd:**

```cmd
mvnw.cmd spring-boot:run
```

**Terminal 1 — PowerShell:**

```powershell
.\mvnw.cmd spring-boot:run
```

Deixe rodando até a aplicação estar de pé (porta padrão **8080**, salvo configuração diferente).

### 4. Rodar os testes (outro terminal)

**Todos os testes — cmd:**

```cmd
mvnw.cmd test
```

**Todos os testes — PowerShell:**

```powershell
.\mvnw.cmd test
```

**Uma classe de teste só (exemplo):**

**cmd:**

```cmd
mvnw.cmd -Dtest=PlaywrightSmokeTest test
```

**PowerShell:**

```powershell
.\mvnw.cmd -Dtest=PlaywrightSmokeTest test
```

### 5. Gerador de testes (codegen)

Com o Playwright configurado e os browsers instalados.

**Exemplo com URL local:**

**cmd:**

```cmd
mvnw.cmd exec:java -e "-Dexec.mainClass=com.microsoft.playwright.CLI" "-Dexec.args=codegen http://localhost:8080"
```

**PowerShell:**

```powershell
.\mvnw.cmd exec:java -e "-Dexec.mainClass=com.microsoft.playwright.CLI" "-Dexec.args=codegen http://localhost:8080"
```

**Exemplo com site de demonstração:**

**cmd:**

```cmd
mvnw.cmd exec:java -e "-Dexec.mainClass=com.microsoft.playwright.CLI" "-Dexec.args=codegen https://demo.playwright.dev/todomvc"
```

---

## Atualizar o Playwright depois

1. Altere a versão no `pom.xml`.
2. Rode de novo:

**cmd:**

```cmd
mvnw.cmd -q dependency:resolve
mvnw.cmd exec:java -e "-Dexec.mainClass=com.microsoft.playwright.CLI" "-Dexec.args=install"
```

---

## Problemas comuns no Windows

| Situação | O que verificar |
|----------|------------------|
| `Unknown lifecycle phase ".mainClass=..."` | **PowerShell (causa frequente):** use **aspas** em cada `-D`: `"-Dexec.mainClass=com.microsoft.playwright.CLI"` e `"-Dexec.args=install"`. Copie os comandos da seção *Comandos no Windows → passo 2* sem remover as aspas. |
| `mvnw` não é reconhecido | Use `mvnw.cmd` (cmd) ou `.\mvnw.cmd` (PowerShell) na pasta do projeto. |
| Erro ao executar `exec:java` | Confira se o `exec-maven-plugin` está no `pom.xml`. |
| Browser não encontrado | Execute o comando `install` dos navegadores novamente após mudar a versão do Playwright. |
| Política de execução no PowerShell | Se scripts estiverem bloqueados: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (apenas se o seu ambiente permitir). |

### Linux e macOS

| Situação | O que verificar |
|----------|------------------|
| `Unknown lifecycle phase ".mainClass=..."` | Mesma causa: use aspas nos `-D`. No bash/zsh isso também evita o argumento ser repartido errado. |
| Script do Maven | Use `./mvnw`, não `mvnw.cmd` (este é só para Windows). |
| Permissão negada | `chmod +x mvnw` na raiz do projeto. |

---

## Referências

- [Playwright Java — Introdução](https://playwright.dev/java/docs/intro)
- [Playwright Java — Navegadores e instalação](https://playwright.dev/java/docs/browsers)
- [Playwright Java — Codegen](https://playwright.dev/java/docs/codegen)
- [Playwright Java — Escrevendo testes](https://playwright.dev/java/docs/writing-tests)
