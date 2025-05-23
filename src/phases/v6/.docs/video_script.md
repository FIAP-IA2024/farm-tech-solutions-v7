# Roteiro para Vídeo de Demonstração - Projeto Fase 6 FIAP

## Duração: até 5 minutos

---

## 0. Introdução (30 segundos)

**Fala:**
"Olá! Neste vídeo vou demonstrar o projeto da Fase 6 do curso de IA da FIAP. Este projeto consiste na implementação de um sistema de visão computacional utilizando o modelo YOLO para detecção de objetos."

**Mostrar na tela:** Tela inicial mostrando a página do GitHub do projeto (`farm-tech-solutions-v6/README.md`)

**Fala:**
"Aqui está o repositório do projeto. No arquivo README.md, contém todas as instruções necessárias para executar o projeto e obter os resultados. As boas práticas de versionamento com Git foram seguidas, e todo o processo está devidamente commitado."

---

## 1. Contextualização do Projeto (30 segundos)

**Fala:**
"Um contexto geral sobre o projeto: Desenvolvemos um sistema de visão computacional utilizando o modelo YOLO para detectar dois objetos distintos: escolhemos gatos como objeto A e cachorros como objeto B."

**Fala:**
"Aqui um exemplo de uma imagem de gato, e uma imagem de cachorro:"

**Mostrar na tela:** Exemplo de foto de gato e exemplo de foto de cachorro

---

## 2. Estrutura do Dataset (45 segundos)

**Fala:**
"Para treinar o modelo, organizamos um dataset contendo 80 imagens, sendo 40 de gatos e 40 de cachorros, o nome de arquivo das images de gato começam com o prefixo A e as de cachorro começam com prefixo B. Estas imagens foram distribuídas da seguinte forma: 80% para treinamento, 10% para validação e 10% para testes. Todas as imagens foram rotuladas utilizando a ferramenta Make Sense IA."

**Mostrar na tela:** Pasta `data` e as imagens

---

## 3. Implementação e Treinamento (60 segundos)

**Fala:**
"Para implementar a solução, desenvolvemos um script Python que utiliza o modelo YOLOv5. Este script realiza o download e configuração do repositório YOLOv5, prepara o ambiente de treinamento, e executa o treinamento do modelo com os parâmetros definidos. Realizamos dois treinamentos com diferentes configurações: um com 30 épocas e outro com 60 épocas, ambos com batch size de 16.

Para facilitar a comparação, o script possui uma opção `--compare` que automaticamente treina os dois modelos (30 e 60 épocas) e gera um relatório comparativo, possibilitando uma análise direta dos resultados."

**Mostrar na tela:**

- Script Python principal
- `farm-tech-solutions-v6/notebooks/GabrielRibeiro_rm560173_pbl_fase6.py`
- Notebook Jupyter
- `farm-tech-solutions-v6/notebooks/GabrielRibeiro_rm560173_pbl_fase6.ipynb`
- Comandos de execução do script:
- `python notebooks/GabrielRibeiro_rm560173_pbl_fase6.py --epochs 30 --batch-size 16`
- `python notebooks/GabrielRibeiro_rm560173_pbl_fase6.py --compare`

---

## 4. Análise de Resultados (75 segundos)

**Mostrar na tela:**

- Resultados da análise comparativa
- `farm-tech-solutions-v6/results/comparison/analysis_summary.md`
- Gráficos de comparação de métricas
- `farm-tech-solutions-v6/results/comparison/analysis_output/` (gráficos relevantes)
- Matrizes de confusão dos dois modelos

**Fala:**
"Após o treinamento, realizamos uma análise comparativa detalhada entre os modelos treinados com 30 e 60 épocas. Os resultados mostraram que o modelo com 30 épocas teve um desempenho significativamente melhor, com um mAP@0.5 de 0,21 contra 0,12 do modelo com 60 épocas. A precisão do modelo de 30 épocas foi de 0,28, superior aos 0,10 do modelo com 60 épocas. Observamos que o treinamento estendido até 60 épocas resultou em overfitting, onde o modelo se especializou demais nos dados de treinamento, perdendo capacidade de generalização."

---

## 5. Demonstração do Resultados dos Modelos (45 segundos)

**Mostrar na tela:** Mostrar os arquivos gerados

**Fala:**
"Agora vou mostrar os arquivos gerados no treinamento dos modelos. Aqui temos os relatórios de análise, gráficos de comparação entre os modelos treinados, e as matrizes de confusão. Esses arquivos foram produzidos automaticamente após a execução dos scripts e ajudam a documentar e visualizar os resultados obtidos de forma clara e organizada."

---

## 6. Conclusões (30 segundos)

**Fala:**
“Com base nos resultados, o modelo treinado com 30 épocas apresentou o melhor desempenho para a proposta da aplicação. O script Python e o notebook utilizados estão disponíveis na pasta notebooks, e a pasta scripts contém o script responsável por gerar o relatório comparativo entre os dois modelos.”

---

## 7. Encerramento (30 segundos)

**Fala:**
“Essa foi a apresentação do projeto Despertar da Rede Neural, desenvolvido na Fase 6 do curso de Inteligência Artificial da FIAP. Muito obrigado pela atenção!”
