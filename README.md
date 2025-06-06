# 🏎️ Análise de Desempenho na Fórmula 1 – Power BI + ETL com Python

Este projeto apresenta uma solução de Business Intelligence sobre o histórico da Fórmula 1, utilizando um pipeline de ETL desenvolvido em Python e um dashboard interativo no Power BI. A análise abrange dados oficiais de corridas, pilotos e montadoras, organizados em uma modelagem dimensional otimizada para extração de insights estratégicos.

---

## 📌 Objetivos

- Construir um pipeline de ETL confiável para extração, tratamento e padronização de dados da F1
- Modelar os dados em formato estrela para otimizar a performance e clareza analítica no Power BI
- Desenvolver um dashboard interativo que responda perguntas-chave sobre desempenho histórico

---

> **Cobertura histórica:** 1950 até 2023  
> **Fonte dos dados:** Projeto Ergast (via GitHub)

---

## ⚙️ Stack Utilizada

| Camada       | Ferramenta       |
|--------------|------------------|
| ETL          | Python 3.11, Pandas, Requests |
| Visualização | Power BI Desktop |
| Modelagem    | Star Schema (Dimensões e Fato) |
| Organização  | Git + GitHub     |

---
## 🛠️ Execução do ETL

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/dashboard-formula1-powerbi.git
cd dashboard-formula1-powerbi
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instale os requisitos:

```bash
pip install -r etl/requirements.txt
```

4. Execute o script principal:

```bash
python etl/main.py
```

✔️ Os arquivos `.xlsx`  tratados serão gerados automaticamente na pasta:  
```bash
etl/saida/
```

---

## 📊 Dashboard Power BI

O arquivo `.pbix` está disponível na raiz do projeto:

```bash
dashboard_f1.pbix
```

Recomendo abrir com o **Power BI Desktop atualizado**.  

---

## 📂 Estrutura do Repositório

```
├── etl/
│   ├── main.py               # Pipeline ETL completo
│   ├── requirements.txt      # Dependências do projeto
│   └── saida/                # Dados transformados (Excel)
├── dashboard_f1.pbix         # Arquivo Power BI finalizado
├── README.md                 # Documentação principal
```

---

## 📷 Preview do Dashboard

```markdown
![Dashboard Preview](./img/dashboard_preview.png)
```

---

## 👨‍💻 Autor

**Mikaias Santos**  
Analista de Dados | Recife - PE  
Análise e Desenvolvimento de Sistemas  
📧 Contato: mikaiassantos28@gmail.com  
