# 🤖 AI Automation Agent API

API REST desenvolvida para classificação automática de mensagens e execução de ações inteligentes, simulando um agente de atendimento com base em Inteligência Artificial.

---

## 🚀 Demonstração

🔗 API Online:
https://ai-automation-agent.onrender.com

🔗 Documentação Swagger:
https://ai-automation-agent.onrender.com/apidocs/

---

## 🎯 Objetivo do Projeto

Criar um agente inteligente capaz de:

* Classificar mensagens automaticamente (vendas, suporte ou geral)
* Executar ações com base na classificação
* Registrar logs das interações
* Gerar estatísticas de uso

Esse projeto simula um sistema real de automação utilizado em empresas para atendimento e triagem de leads.

---

## 🧠 Tecnologias Utilizadas

* Python
* Flask
* Flasgger (Swagger)
* Gunicorn
* JSON (armazenamento de dados)

---

## ⚙️ Funcionalidades

### 📌 Classificação de mensagens

**POST /classify**

Classifica a mensagem e executa uma ação.

#### Exemplo de requisição:

```json
{
  "message": "Quero comprar seu produto"
}
```

#### Exemplo de resposta:

```json
{
  "classification": "sales",
  "action": "Encaminhado para equipe comercial"
}
```

---

### 📌 Listagem de logs

**GET /logs**

Retorna todas as interações registradas.

---

### 📌 Estatísticas

**GET /stats**

Retorna a contagem de mensagens por tipo:

```json
{
  "sales": 10,
  "support": 5,
  "general": 3
}
```

---

### 📌 Health Check

**GET /health**

Verifica se a API está online:

```json
{
  "status": "ok"
}
```

---

## 🗂️ Estrutura do Projeto

```
ai-automation-agent/
│
├── app.py
├── requirements.txt
├── services/
│   ├── ai_service.py
│   └── action_service.py
└── data/
    └── logs.json
```

---

## ☁️ Deploy

Projeto publicado em ambiente cloud utilizando:

* Render (deploy)
* GitHub (versionamento)

---

## 📈 Possíveis melhorias

* Integração com API de IA (OpenAI, etc)
* Banco de dados (PostgreSQL)
* Autenticação de usuários
* Dashboard frontend
* Integração com WhatsApp / CRM

---

## 💼 Valor para o negócio

Esse tipo de solução pode ser utilizado para:

* Automação de atendimento
* Triagem de leads
* Redução de custo operacional
* Aumento de produtividade

---

## 👨‍💻 Autor

Desenvolvido por Kauê Aguiar
🔗 LinkedIn: (adicione aqui)
🔗 GitHub: https://github.com/kaueagguiar-hub

---

## ⭐ Contribuição

Sinta-se à vontade para contribuir ou sugerir melhorias.
