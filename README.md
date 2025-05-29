# AutoRenameWatcher

Um utilitário leve em Python para **monitorar uma pasta do usuário atual em tempo real** e **renomear automaticamente arquivos com extensões inválidas** (ex: `.jpg_`, `.pdf_`, etc.), corrigindo seus nomes. Ideal para ambientes corporativos onde arquivos são frequentemente salvos com sufixos incorretos.

---

## 🚀 Visão Geral

Esse utilitário:

- Verifica e renomeia arquivos já existentes na pasta `Downloads` ou qualquer outra pasta.
- Monitora novos arquivos em tempo real e renomeia assim que forem criados
- Corrige extensões como `.jpg_`, `.jpeg_`, `.pdf_`, `.png_`
- Evita conflitos de nomes: se o arquivo já existir, cria versões como `nome (1).jpg`
- Pode ser executado como serviço no Windows via **NSSM**
- Funciona em qualquer máquina Windows, inclusive sem Python (via `.exe` compilado) utilizando pyinstaller

---

## 🧩 Exemplos de Renomeação

| Antes               | Depois              |
|---------------------|---------------------|
| `documento.pdf_`    | `documento.pdf`     |
| `imagem.jpg_`       | `imagem.jpg`        |
| `imagem.jpg_` (repetido) | `imagem (1).jpg`    |

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Watchdog](https://pypi.org/project/watchdog/) (para monitoramento de arquivos)
- [PyInstaller](https://pyinstaller.org/) (para gerar executável)
- [NSSM](https://nssm.cc/) (para rodar como serviço no Windows)

---

## 📦 Instalação

### 📍 1. Clonar o repositório

```bash
git clone https://github.com/seunome/AutoRenameWatcher.git
cd AutoRenameWatcher
```

### 💻 2. Rodar via Python (modo desenvolvimento)

> Requer Python 3.10+ instalado.

```bash
pip install watchdog
python rename_service.py
```

### 🧊 3. Compilar `.exe` (modo produção)

> Requer PyInstaller instalado.

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole rename_service.py
```

O executável será gerado em:  
`dist/rename_service.exe`

---

## 🖥️ Rodando como Serviço (via NSSM)

1. Baixe e instale o [NSSM](https://nssm.cc/download)
2. Execute no terminal como administrador:

```cmd
nssm install AutoRenameWatcher
```

3. Configure:
- **Application path**: `C:\Scripts\dist\rename_service.exe`
- **Startup directory**: `C:\Scripts\dist`
- **Log on**: configure para rodar como o **usuário logado atual**, ex: `.\seunome`

4. Após configurar:
```cmd
nssm start AutoRenameWatcher
```

---

## 📝 Logs

Se o script estiver com logging ativado, os logs serão salvos em:

```
C:\Scripts\renomeador.log
```

---

## 📁 Estrutura do Projeto

```
AutoRenameWatcher/
├── rename_service.py       # Script principal
├── dist/                   # Arquivos gerados pelo PyInstaller
│   └── rename_service.exe  # Executável compilado
├── icon.ico                # Ícone opcional do .exe
└── README.md               # Este documento
```

---

## 📚 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para abrir issues ou enviar pull requests.

---

## 👤 Autor

**Neto Santos**  
