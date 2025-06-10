# TechFlow - Sistema de Gerenciamento de Tarefas com Flask

## 📌 Objetivo

Este projeto tem como objetivo desenvolver um sistema de **gerenciamento de tarefas (To-Do List)** utilizando **Python com Flask**, aplicando os conceitos de **CRUD** (Create, Read, Update, Delete).

---

## 📋 Escopo

- ✅ Cadastro de tarefas com título e status (concluído ou não)
- ✅ Listagem de todas as tarefas
- ✅ Atualização do título e status das tarefas
- ✅ Exclusão de tarefas
- ✅ Filtro de tarefas por status (`?completed=true/false`)
- ✅ Front-end com HTML e CSS simples, interativo
- ✅ Testes automatizados com `pytest`
- ✅ Pipeline de CI com **GitHub Actions**

---

## 🧪 Metodologia

Foi utilizada uma abordagem ágil no desenvolvimento, com:
- **GitHub Projects** para planejamento visual (Kanban)
- Divisão de tarefas em colunas: _A Fazer_, _Em Progresso_ e _Concluído_
- **Commits frequentes e bem descritos**, garantindo rastreabilidade
- Testes automatizados para assegurar a qualidade
- Simulação de uma **mudança de escopo**, registrada abaixo

---

## 🔁 Simulação de Mudança no Escopo

Inicialmente, o projeto focaria apenas em uma API com rotas para operações CRUD. Durante o desenvolvimento, foi identificado o valor de adicionar um front-end básico para facilitar a visualização e uso das tarefas.

**Alterações feitas:**
- Criação de um `index.html` com layout responsivo e interativo
- Atualização do README.md para refletir o novo escopo
- Inclusão de tarefas no Kanban para cobrir a nova funcionalidade

---

## ▶️ Como Executar o Projeto

### ✅ Pré-requisitos
- Python 3.11 ou superior
- `pip` instalado

### 🚀 Executando localmente

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/TechFlow-TaskManager.git
cd TechFlow-TaskManager

# Instalar as dependências
pip install -r requirements.txt

# Executar a aplicação
python app.py
