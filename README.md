# 🖥️ InfraWatch

![CI](https://github.com/pedroviana-UX/InfraWatcher/actions/workflows/ci.yml/badge.svg)

InfraWatch é uma ferramenta de troubleshooting inicial desenvolvida em Python com o objetivo de simular funcionalidades presentes em ambientes de monitoramento de infraestrutura, como NOCs (Network Operations Centers).

O projeto busca aplicar, na prática, conceitos de **automação, qualidade de software, redes de computadores e DevOps**, evoluindo gradualmente de uma ferramenta simples de diagnóstico para uma solução mais completa de monitoramento.

---

## 🎯 Objetivos

- Aplicar Python em cenários reais de infraestrutura
- Desenvolver boas práticas de programação e organização de código
- Criar automações para auxiliar processos de troubleshooting
- Aplicar conceitos de QA através de testes automatizados
- Implementar práticas utilizadas em ambientes DevOps
- Construir um projeto de portfólio voltado para infraestrutura e automação

---

## 🚀 Funcionalidades atuais

### Monitoramento e diagnóstico

- ✅ Menu interativo via terminal (CLI)
- ✅ Cadastro de hosts para monitoramento
- ✅ Teste de conectividade utilizando ICMP (Ping)
- ✅ Compatibilidade com Windows e Linux
- ✅ Estrutura modular utilizando separação entre aplicação e lógica de monitoramento

### Qualidade e DevOps

- ✅ Testes automatizados utilizando Pytest
- ✅ Pipeline de Integração Contínua (CI) utilizando GitHub Actions
- ✅ Gerenciamento de dependências separado para ambiente de produção e desenvolvimento

---

## 🏗️ Estrutura do projeto

```text
InfraWatcher
│
├── .github/
│   └── workflows/
│       └── ci.yml                 # Pipeline de integração contínua
│
├── src/
│   ├── main.py                    # Interface principal da aplicação
│   └── monitoramento.py            # Funções de monitoramento
│
├── tests/
│   └── test_monitoramento.py       # Testes automatizados
│
├── requirements.txt                # Dependências do projeto
├── requirements-dev.txt            # Dependências de desenvolvimento
├── .gitignore
└── README.md
```

---

## 🧪 Testes automatizados

O projeto utiliza **Pytest** para validar o funcionamento das principais funcionalidades.

A cada novo commit enviado ao GitHub, a pipeline de CI executa automaticamente:

- Instalação das dependências
- Configuração do ambiente Python
- Execução dos testes automatizados

Dessa forma, alterações no código são verificadas automaticamente antes de serem consideradas estáveis.

---

## 🛠️ Tecnologias utilizadas

- Python 3.12
- Pytest
- Git
- GitHub
- GitHub Actions
- Linux / GitHub Codespaces

---

## 📌 Roadmap

### Concluído:

- [x] Criar estrutura inicial do projeto
- [x] Criar menu interativo
- [x] Cadastro de hosts
- [x] Implementar teste de Ping
- [x] Organizar projeto utilizando estrutura de pacotes
- [x] Adicionar testes automatizados
- [x] Implementar pipeline CI/CD inicial

### Próximos passos:

- [ ] Implementar monitoramento SNMP
- [ ] Coletar informações de memória e recursos do sistema
- [ ] Implementar sistema de logs
- [ ] Exportar métricas
- [ ] Criar API para comunicação externa
- [ ] Criar dashboard de visualização
- [ ] Integração com ferramentas como Zabbix e Grafana
- [ ] Containerização utilizando Docker
- [ ] Implementar deploy automatizado

---

## 📚 Conceitos aplicados

Durante o desenvolvimento do InfraWatch são praticados conceitos de:

- Desenvolvimento em Python
- Redes de computadores
- Monitoramento de infraestrutura
- Automação de tarefas
- Testes automatizados
- Integração contínua (CI)
- Controle de versão com Git
- Boas práticas de desenvolvimento

---

## 👨‍💻 Autor

**Pedro Viana**

Projeto desenvolvido como laboratório prático de estudos em **Python, QA, DevOps e infraestrutura de redes**.
