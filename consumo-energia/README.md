# ⚡ Calculadora de Consumo de Energia

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)

> Um programa em Python desenvolvido para estimar o consumo mensal de energia elétrica de aparelhos eletrodomésticos e calcular o custo estimado em reais.

---

## 🎯 Objetivo

O objetivo deste projeto é fornecer uma ferramenta simples via linha de comando para conscientização do uso de energia elétrica, permitindo ao usuário calcular quanto um determinado aparelho impacta na conta de luz final.

---

## 🧮 Fórmula Utilizada

O consumo mensal é calculado em **kWh** (quilowatt-hora) a partir da potência do aparelho em Watts e das horas de uso diário, considerando um mês padrão de 30 dias:

$$\text{Consumo Mensal (kWh)} = \frac{\text{Potência (W)} \times \text{Horas/Dia} \times 30}{1000}$$

> **Custo Estimado:** Multiplica-se o consumo mensal obtido pela tarifa de energia (ex: **R$ 0,75/kWh**).

---

## 💻 Pré-requisitos

- **Python 3.x** instalado na sua máquina.

---

## 🚀 Como Executar o Programa

1. **Clone ou navegue até a pasta do projeto:**
   ```bash
   cd projetos/consumo-energia