# projeto-spring-jpa-v1

Projeto para exercitar e aprender JPA com Spring Boot.

Este documento inclui um **guia para configurar testes E2E com Playwright para Java** no Windows, usando o **Maven Wrapper** (`mvnw.cmd`).

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

---

## Playwright para Java — configuração no `pom.xml`

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

**cmd:**

```cmd
mvnw.cmd exec:java -e -Dexec.mainClass=com.microsoft.playwright.CLI -Dexec.args=install
```

**PowerShell:**

```powershell
.\mvnw.cmd exec:java -e -Dexec.mainClass=com.microsoft.playwright.CLI -Dexec.args="install"
```

> No **cmd**, às vezes é mais simples passar `install` sem aspas externas, como acima. No PowerShell, use `"install"` como no exemplo.

**Instalar só o Chromium:**

**cmd:**

```cmd
mvnw.cmd exec:java -e -Dexec.mainClass=com.microsoft.playwright.CLI -Dexec.args=install chromium
```

**PowerShell:**

```powershell
.\mvnw.cmd exec:java -e -Dexec.mainClass=com.microsoft.playwright.CLI -Dexec.args="install chromium"
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
mvnw.cmd -Dtest=SmokePlaywrightTest test
```

**PowerShell:**

```powershell
.\mvnw.cmd -Dtest=SmokePlaywrightTest test
```

### 5. Gerador de testes (codegen)

Com o Playwright configurado e os browsers instalados.

**Exemplo com URL local:**

**cmd:**

```cmd
mvnw.cmd exec:java -e -Dexec.mainClass=com.microsoft.playwright.CLI -Dexec.args=codegen http://localhost:8080
```

**PowerShell:**

```powershell
.\mvnw.cmd exec:java -e -Dexec.mainClass=com.microsoft.playwright.CLI -Dexec.args="codegen http://localhost:8080"
```

**Exemplo com site de demonstração:**

**cmd:**

```cmd
mvnw.cmd exec:java -e -Dexec.mainClass=com.microsoft.playwright.CLI -Dexec.args=codegen https://demo.playwright.dev/todomvc
```

---

## Atualizar o Playwright depois

1. Altere a versão no `pom.xml`.
2. Rode de novo:

**cmd:**

```cmd
mvnw.cmd -q dependency:resolve
mvnw.cmd exec:java -e -Dexec.mainClass=com.microsoft.playwright.CLI -Dexec.args=install
```

---

## Problemas comuns no Windows

| Situação | O que verificar |
|----------|------------------|
| `mvnw` não é reconhecido | Use `mvnw.cmd` (cmd) ou `.\mvnw.cmd` (PowerShell) na pasta do projeto. |
| Erro ao executar `exec:java` | Confira se o `exec-maven-plugin` está no `pom.xml`. |
| Browser não encontrado | Execute o comando `install` dos navegadores novamente após mudar a versão do Playwright. |
| Política de execução no PowerShell | Se scripts estiverem bloqueados: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (apenas se o seu ambiente permitir). |

---

## Referências

- [Playwright Java — Introdução](https://playwright.dev/java/docs/intro)
- [Playwright Java — Navegadores e instalação](https://playwright.dev/java/docs/browsers)
- [Playwright Java — Codegen](https://playwright.dev/java/docs/codegen)
- [Playwright Java — Escrevendo testes](https://playwright.dev/java/docs/writing-tests)
