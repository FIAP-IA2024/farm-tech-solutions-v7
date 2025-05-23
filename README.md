# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="https://raw.githubusercontent.com/lfusca/templateFiap/main/assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

## 👨‍🎓 Integrantes do Grupo

- RM559800 - [Jonas Felipe dos Santos Lima](https://www.linkedin.com/in/jonas-felipe-dos-santos-lima-b2346811b/)
- RM560173 - [Gabriel Ribeiro](https://www.linkedin.com/in/ribeirogab/)
- RM559926 - [Marcos Trazzini](https://www.linkedin.com/in/mstrazzini/)
- RM559645 - [Edimilson Ribeiro](https://www.linkedin.com/in/edimilson-ribeiro/)

## 👩‍🏫 Professores

### Coordenador(a)

- [André Godoi](https://www.linkedin.com/in/profandregodoi/)

---

## 📌 Entregas do Projeto

Este projeto representa a Fase 7 - A Consolidação de um Sistema, onde integramos todos os serviços desenvolvidos nas Fases 1 a 6 para consolidar um sistema completo de gestão para o agronegócio.

### Resumo das Fases Anteriores

- **Fase 1 - Base de Dados Inicial:** Implementação de cálculos de área de plantio, manejo de insumos e conexão com API meteorológica.
- **Fase 2 - Banco de Dados Estruturado:** Estruturação de banco de dados relacional completo (MER e DER) integrando dados de manejo agrícola.
- **Fase 3 - IoT e Automação Inteligente:** Desenvolvimento de sistema IoT com ESP32 integrando sensores físicos para irrigação automatizada.
- **Fase 4 - Dashboard Interativo com Data Science:** Integração de Machine Learning com Scikit-Learn e Streamlit em dashboard online para visualização interativa.
- **Fase 5 - Cloud Computing & Segurança:** Hospedagem da infraestrutura na AWS, garantindo segurança, disponibilidade e escalabilidade.
- **Fase 6 - Visão Computacional com Redes Neurais:** Desenvolvimento de sistema de visão computacional com YOLO para monitoramento visual da saúde das plantações.

---

## 🛠 **Entrega 1 - Dashboard Integrado**

### 🎯 Objetivos Entrega 1

- Aprimorar a dashboard da Fase 4, integrando os serviços de cada Fase (1, 2, 3 e 6) usando botões ou comandos de terminal
- Unificar todos os programas em uma única pasta de projeto

---

### 📁 Estrutura de Pastas

```plaintext
/farm-tech-solutions-v7
├── src/
│   ├── dashboard.py          # Dashboard principal integrado
│   ├── lambda_alert.py       # Integração com a Lambda AWS para alertas
│   ├── utils/
│   │   ├── __init__.py        # Define o diretório como pacote Python
│   │   └── helpers.py         # Funções auxiliares para o sistema de alertas
│   └── phases/
│       ├── v1/                 # Fase 1: Plantio e Dados Meteorológicos
│       ├── v2/                 # Fase 2: Banco de Dados Estruturado
│       ├── v3/                 # Fase 3: IoT e Automação Inteligente
│       ├── v4/                 # Fase 4: Dashboard com Data Science
│       ├── v5/                 # Fase 5: Cloud Computing & Segurança
│       └── v6/                 # Fase 6: Visão Computacional
├── results/                # Resultados da visão computacional (Fase 6)
```

---

### 🔧 Como Executar

#### Configuração Inicial

1. Clone este repositório:

   ```bash
   git clone https://github.com/FIAP-IA2024/farm-tech-solutions-v7.git
   cd farm-tech-solutions-v7
   ```

2. Instale as dependências Python:

   ```bash
   pip install -r requirements.txt
   ```

3. Instale os pacotes R necessários para a Fase 1:

   ```bash
   cd src/phases/v1
   Rscript -e "renv::restore()"
   cd ../../..
   ```

4. Configure as variáveis de ambiente:

   ```bash
   # Crie um arquivo .env na pasta raíz do projeto
   cp src/phases/v1/.env.example src/phases/v1/.env
   # Edite o arquivo .env com sua chave de API do OpenWeather
   ```

#### Executando o Dashboard Integrado

1. Inicie o dashboard principal:

   ```bash
   streamlit run src/dashboard.py
   ```

2. Navegue pelo menu lateral para acessar as diferentes fases do projeto.

### 💻 Tecnologias Utilizadas

- **Linguagens de Programação:**
  - Python 3.x (principal linguagem do projeto)
  - R (para análise estatística e visualizações na Fase 1)
  - C/C++ (para programação do ESP32 na Fase 3)
  - SQL (para gerenciamento de banco de dados na Fase 2)

- **Bibliotecas e Frameworks:**
  - **Python**:
    - Streamlit (para dashboard interativo)
    - Pandas, NumPy (para manipulação de dados)
    - Matplotlib (para visualizações)
    - Scikit-learn (para Machine Learning na Fase 4)
    - Ultralytics/YOLO (para visão computacional na Fase 6)
    - Flask (para APIs web na Fase 3)
    - Requests (para integração com APIs externas e sistema de alertas)
    - JSON (para formatação de dados de alertas)
  - **R**:
    - dplyr (para manipulação de dados)
    - ggplot2 (para visualizações gráficas)
    - httr, jsonlite (para API de previsão do tempo)

- **Ferramentas e Serviços:**
  - **AWS**:
    - EC2 (para hospedagem do dashboard)
    - S3 (para armazenamento de dados)
    - CloudWatch (para monitoramento)
    - Lambda (para processamento serverless do sistema de alertas)
    - API Gateway (para exposição de endpoints REST)
    - SNS (Simple Notification Service para envio de alertas por email)
  - **Hardware**:
    - ESP32 (microcontrolador para IoT)
    - Sensores (umidade, pH, temperatura, etc.)
  - **Outros**:
    - Git (controle de versão)
    - Jupyter Notebooks (análise de dados)

---

## 🌩️ **Entrega 2 - Serviço de Alerta AWS**

### 🎯 Objetivos Entrega 2

- Gerar um serviço de alerta utilizando a infraestrutura AWS criada na Fase 5
- Implementar um serviço de mensageria na AWS que integre a dashboard geral da fazenda
- Enviar alertas via e-mail ou SMS para funcionários com ações corretivas baseadas nos dados das Fases 1, 3 ou 6

### 🔧 Implementação do Sistema de Alertas

#### Arquitetura do Sistema

O sistema de alertas foi implementado usando uma arquitetura serverless na AWS, com os seguintes componentes:

1. **Frontend**: Interface de usuário integrada ao dashboard principal para envio de alertas
2. **API Gateway**: Endpoint REST que recebe as solicitações de alerta
3. **Lambda Function**: Processa os alertas recebidos e aciona o serviço de notificação
4. **Amazon SNS**: Serviço de notificação que envia emails para a equipe de campo

#### Tipos de Alertas

O sistema suporta diversos tipos de alertas, incluindo:

- **Alertas de Irrigação**: Detectados quando sensores de umidade reportam níveis abaixo do ideal
- **Alertas de Pragas**: Identificados pelo sistema de visão computacional ao processar imagens das plantações
- **Alertas Meteorológicos**: Baseados nas previsões do tempo obtidas pela API na Fase 1
- **Alertas Nutricionais**: Quando análises de solo indicam deficiências de nutrientes específicos

#### Como Usar o Sistema de Alertas

1. Acesse a seção "Alertas" no menu lateral do dashboard
2. Preencha o formulário com as informações do alerta:
   - Selecione a cultura afetada
   - Indique o tipo de problema
   - Adicione uma descrição detalhada (opcional)
   - Defina o nível de prioridade
3. Clique em "Enviar Alerta"
4. O sistema mostrará uma confirmação de envio bem-sucedido
5. Os destinatários receberão um email com as informações do alerta e ações recomendadas

#### Endpoint da API

O sistema de alertas utiliza o seguinte endpoint:

```
https://wuu3yuphjl.execute-api.us-east-1.amazonaws.com/pedidos
```

A API espera um payload JSON no seguinte formato:

```json
{
  "crop": "Nome da cultura",
  "issue": "Descrição do problema"
}
```

#### Beneficios do Sistema de Alertas

- **Tempo de Resposta**: Redução significativa no tempo entre a detecção de problemas e a execução de ações corretivas
- **Precisão**: Informações detalhadas sobre o problema e ações recomendadas
- **Monitoramento Contínuo**: Alertas podem ser gerados automaticamente a partir de dados dos sensores IoT e análises de imagens
- **Escala**: A arquitetura serverless permite escalar automaticamente conforme o número de alertas aumenta

## 🎥 Demonstração no YouTube

[Link para o vídeo demonstrativo do projeto](https://youtu.be/NmzBoj4OdX4)

Neste vídeo, demonstramos o funcionamento completo do sistema integrado, incluindo todas as funcionalidades das Fases 1 a 6.

## 📋 Licença

Este projeto segue o modelo de licença da FIAP e está licenciado sob **Attribution 4.0 International**. Para mais informações, consulte o [MODELO GIT FIAP](https://github.com/agodoi/template).
