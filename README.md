# AI Automation Agent API

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-REST_API-black)
![Swagger](https://img.shields.io/badge/Docs-Swagger-green)
![Deploy](https://img.shields.io/badge/Deploy-Render-purple)

REST API desenvolvida para classificação inteligente de mensagens, roteamento automatizado de ações e monitoramento de estatísticas operacionais.

Este projeto simula um fluxo real de automação de atendimento, aplicando conceitos de backend, integração de serviços e documentação de APIs.

---

## Live Application

**API Base URL**
https://ai-automation-agent.onrender.com

**Swagger Documentation**
https://ai-automation-agent.onrender.com/apidocs/

---

## Overview

A API recebe mensagens, realiza uma classificação automática por categoria e executa uma ação correspondente.

Categorias atualmente suportadas:

* **sales** → direcionamento comercial
* **support** → direcionamento para suporte
* **general** → tratamento genérico

Além disso, a aplicação registra logs das interações e gera estatísticas operacionais para análise.

---

## Architecture

```text id="c1m4qx"
Client Request
     ↓
Flask API
     ↓
Classification Service
     ↓
Action Service
     ↓
Logs + Statistics
```

---

## Core Features

### Intelligent Message Classification

Classificação automática das mensagens recebidas com base no conteúdo.

### Automated Action Routing

Executa ações específicas conforme a classificação retornada.

### Operational Logging

Armazena logs estruturados das interações para rastreabilidade.

### Metrics Endpoint

Disponibiliza estatísticas agregadas por categoria.

### Interactive API Documentation

Documentação automática com Swagger UI.

---

## API Endpoints

### Health Check

```http id="q1m7rw"
GET /health
```

**Response**

```json id="n9m2qz"
{
  "status": "ok"
}
```

---

### Message Classification

```http id="t5m3qw"
POST /classify
```

**Request**

```json id="u2n6qx"
{
  "message": "I want to buy your product"
}
```

**Response**

```json id="v8m1qz"
{
  "classification": "sales",
  "action": "Encaminhado para equipe comercial"
}
```

---

### Logs Retrieval

```http id="r4m8qw"
GET /logs
```

---

### Statistics

```http id="k7n2qx"
GET /stats
```

**Response**

```json id="p3m5qw"
{
  "sales": 12,
  "support": 5,
  "general": 3
}
```

---

## Project Structure

```bash id="j6m1qz"
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

## Technology Stack

* **Python**
* **Flask**
* **Flasgger / Swagger**
* **Gunicorn**
* **Render**
* **GitHub**

---

## Engineering Practices Applied

* Modular service architecture
* Input validation
* Structured logging
* Environment configuration
* Health check endpoint
* API documentation
* Cloud deployment

---

## Business Value

This API simulates real-world automation flows that can be applied to:

* lead triage systems
* automated customer service routing
* CRM integrations
* operational analytics
* AI-assisted workflows

---

## Future Improvements

Planned enhancements:

* Database integration (PostgreSQL)
* Authentication layer
* AI/NLP integration
* Dashboard for analytics
* CRM / WhatsApp integration
* Queue processing

---

## Author

**Kauê Aguiar**

GitHub: https://github.com/kaueagguiar-hub

LinkedIn: **(www.linkedin.com/in/
kaue-aguiar)**

---

## Professional Context

This project was developed to demonstrate backend engineering capabilities involving:

* REST API design
* service modularization
* deployment workflows
* API observability
* intelligent automation concepts

It represents a practical backend solution deployed in cloud environment and documented for external consumption.



