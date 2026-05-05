# qa-automation-suite

Projeto de automação de testes cobrindo API REST (Swagger Petstore) e Web E2E (SauceDemo), com CI/CD via GitHub Actions.

---

## Estrutura do Repositório
qa-automation-suite/
├── api-tests/
│   ├── tests/
│   │   ├── test_pet.py
│   │   ├── test_user.py
│   │   └── test_store.py
│   ├── utils/
│   │   └── api_client.py
│   ├── conftest.py
│   ├── pytest.ini
│   └── requirements.txt
│
├── web-tests/
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   ├── tests/
│   │   └── test_e2e_purchase.py
│   ├── conftest.py
│   ├── pytest.ini
│   └── requirements.txt
│
└── .github/
└── workflows/
├── api-tests.yml
└── web-tests.yml

---

## Tecnologias

| Camada | Tecnologia | Versão |
|---|---|---|
| Linguagem | Python | 3.11 |
| Framework | Pytest | 8.2.2 |
| API Testing | Requests | 2.32.3 |
| Web Testing | Selenium | 4.22.0 |
| Relatórios | pytest-html | 4.1.1 |
| CI/CD | GitHub Actions | — |

---

## Instalação e Execução

### Pré-requisitos
- Python 3.10+
- Google Chrome instalado

### API Tests
```bash
cd api-tests
pip install -r requirements.txt
mkdir reports
python -m pytest
```

### Web Tests
```bash
cd web-tests
pip install -r requirements.txt
mkdir reports
python -m pytest
```

---

## Cobertura de Testes

### API — Petstore
- **Pet**: criar, buscar, atualizar, buscar por status, atualizar via form, deletar, validar 404
- **User**: criar, criar em lote, login, buscar, atualizar, logout, deletar
- **Store**: inventário, criar pedido, buscar pedido, deletar pedido, validar 404

### Web — SauceDemo
- Login com sucesso
- Login com credenciais inválidas
- Adicionar 1 produto ao carrinho
- Adicionar 2 produtos ao carrinho
- Fluxo E2E completo: login → produtos → carrinho → checkout → confirmação

---

## CI/CD

| Workflow | Trigger |
|---|---|
| `api-tests.yml` | Push em `api-tests/**` |
| `web-tests.yml` | Push em `web-tests/**` |

---

## Design Patterns

- **Page Object Model** — cada página do SauceDemo tem sua própria classe
- **APIClient** — centraliza configuração do `requests.Session`