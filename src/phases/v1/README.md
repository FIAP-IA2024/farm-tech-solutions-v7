# FIAP - Farm Tech Solutions

Este é um sistema de gestão agrícola que ajuda a gerenciar dados relacionados a diferentes culturas, calcular a área de plantio e estimar os insumos necessários (por exemplo, fertilizantes, pesticidas) com base no tipo de cultura e na área plantada. A aplicação usa Python e Tkinter para fornecer uma interface gráfica simples que permite aos usuários inserir, atualizar, deletar, visualizar e analisar (com a linguagem R) os dados das culturas.

## Funcionalidades

- Adicionar novos dados de cultura selecionando o tipo de cultura, inserindo as dimensões (comprimento e largura) e calculando automaticamente a área de plantio e os insumos necessários.
- Atualizar dados de cultura existentes selecionando uma linha na tabela e modificando os valores.
- Deletar culturas selecionadas da tabela.
- Carregar e salvar dados de culturas de/para um arquivo CSV (`data.csv`).
- **Consultar previsão do tempo** para uma cidade específica utilizando a API OpenWeather.
- Analisar os dados de plantio e insumos usando uma aplicação em R que calcula estatísticas básicas, como média e desvio padrão, e gera visualizações gráficas.

## Demonstração

Assista ao vídeo no YouTube que mostra todas as funcionalidades do sistema:  
[FIAP - Farm Tech Solutions - Demonstração](https://youtu.be/TA8ZpcP39e0)

## Tecnologias

- **Python 3.x**
- **Tkinter** para a GUI
- **CSV** para armazenamento de dados
- **R** para análise estatística e visualizações
  - **dplyr** para manipulação de dados
  - **ggplot2** para visualizações gráficas
  - **httr** e **jsonlite** para consultar a previsão do tempo
- **OpenWeather API** para dados meteorológicos

## Instalação

1. Clone o repositório ou baixe o código-fonte.

   ```bash
   git clone git@github.com:ribeirogab/fiap-farm-tech-solutions.git
   cd fiap-farm-tech-solutions
   ```

2. Verifique se o Python está instalado. Você pode verificar com o comando:

   ```bash
   python --version
   ```

3. Verifique se o R está instalado e certifique-se de usar o `renv` para restaurar o ambiente R:

   ```bash
   Rscript -e "renv::restore()"
   ```

4. Execute o script Python e gere o arquivo `data.csv`.

5. Previsão do tempo: Crie um arquivo `.env` com sua chave de API do OpenWeather, seguindo o exemplo do arquivo `.env.example`.

## Como Executar

1. **Execução do Python**:
   - Abra o terminal ou prompt de comando na pasta do projeto.
   - Execute o script Python para gerar o arquivo CSV:

     ```bash
     python main.py
     ```

2. **Análise de Dados com R**:
   - Execute o script R para calcular estatísticas e visualizar os dados:

     ```bash
     Rscript data_analysis.r
     ```

   - O script R irá calcular a média e o desvio padrão das colunas **Área** e **Insumos**, além de gerar gráficos (histograma e boxplot) e realizar uma análise de outliers.

3. **Consulta de Previsão do Tempo**:
   - No terminal, forneça o nome da cidade como argumento ao executar o script R:

     ```bash
     Rscript weather.r "São Paulo"
     ```

   - O script retornará informações como a temperatura atual, condições climáticas, umidade e velocidade do vento da cidade especificada.

## Como Usar

1. **Adicionar Dados**:
   - Selecione uma cultura no menu suspenso.
   - Insira os valores de `Length` e `Width` (ambos devem ser numéricos).
   - Clique em **Add Data** para calcular a área e os insumos necessários para aquela cultura.
   - Os dados serão exibidos na tabela e salvos no arquivo `data.csv`.

2. **Atualizar Dados**:
   - Selecione uma linha na tabela.
   - Clique em **Update** para modificar a cultura, o comprimento e a largura.
   - Os dados atualizados serão refletidos na tabela e salvos no arquivo `data.csv`.

3. **Deletar Dados**:
   - Selecione uma ou mais linhas na tabela.
   - Clique em **Delete Selected** para remover as entradas.
   - Os dados serão atualizados na tabela e salvos no arquivo `data.csv`.

4. **Analisar Dados**:
   - Execute o script R `data_analysis.r` para calcular estatísticas básicas e gerar gráficos de análise dos dados de plantio e insumos.

5. **Consultar Previsão do Tempo**:
   - Execute o script `weather.r` para consultar a previsão do tempo para uma cidade específica, utilizando a API do OpenWeather.
