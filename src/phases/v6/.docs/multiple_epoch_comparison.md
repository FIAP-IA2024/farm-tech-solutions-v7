# Comparação de Modelos com Diferentes Números de Épocas

## Visão Geral

Este documento apresenta uma análise comparativa entre dois modelos YOLO treinados com diferentes configurações: um com 30 épocas e outro com 60 épocas. O objetivo é avaliar o impacto do número de épocas no desempenho do modelo e determinar a configuração ideal para o dataset específico.

## Configurações de Treinamento

Ambos os modelos foram treinados com a mesma configuração base, exceto pelo número de épocas:

- **Modelo Base**: YOLOv5s
- **Tamanho da Imagem**: 640x640 pixels
- **Batch Size**: 16
- **Dataset**: Dataset personalizado com duas classes (A_Cat e B_Dog)
- **Configuração 1**: 30 épocas de treinamento
- **Configuração 2**: 60 épocas de treinamento

## Resultados da Comparação

### Modelo com 30 Épocas

- **Tempo de Treinamento**: Aproximadamente 1 hora e 30 minutos
- **Métricas de Validação**:
  - **mAP@0.5**: 0.204
  - **mAP@0.5-0.95**: 0.0361
  - **Precisão**: 0.31
  - **Recall**: 0.25

### Modelo com 60 Épocas

- **Tempo de Treinamento**: Aproximadamente 2 horas e 30 minutos
- **Métricas de Validação**:
  - **mAP@0.5**: 0.299
  - **mAP@0.5-0.95**: 0.0603
  - **Precisão**: 0.5
  - **Recall**: 0.232

### Comparação por Classe

#### Classe A_Cat

- **Modelo 30 épocas**: mAP@0.5 = 0.0456, mAP@0.5-0.95 = 0.0136
- **Modelo 60 épocas**: mAP@0.5 = 0.0621, mAP@0.5-0.95 = 0.0117

#### Classe B_Dog

- **Modelo 30 épocas**: mAP@0.5 = 0.363, mAP@0.5-0.95 = 0.0587
- **Modelo 60 épocas**: mAP@0.5 = 0.536, mAP@0.5-0.95 = 0.109

## Análise dos Resultados

1. **Melhoria com Mais Épocas**: O modelo treinado com 60 épocas apresentou desempenho superior em quase todas as métricas quando comparado ao modelo de 30 épocas.

2. **Precisão vs. Recall**: O modelo de 60 épocas mostrou um aumento significativo na precisão (de 0.31 para 0.5), indicando que produz menos falsos positivos.

3. **Desempenho por Classe**: A classe B_Dog teve um desempenho consistentemente melhor em ambos os modelos, mas a diferença foi mais pronunciada no modelo de 60 épocas.

4. **Tempo de Treinamento**: Duplicar o número de épocas aumentou o tempo de treinamento em aproximadamente 66%, mas com ganhos significativos de desempenho.

## Conclusões

- O aumento do número de épocas de 30 para 60 resultou em melhorias significativas de desempenho, especialmente em termos de precisão e mAP@0.5.
  
- A classe B_Dog apresentou melhor desempenho do que a classe A_Cat em ambos os modelos, sugerindo que o modelo pode reconhecer mais facilmente os padrões desta classe.

- O trade-off entre tempo de treinamento e ganho de desempenho parece favorável, já que o modelo com 60 épocas teve ganhos significativos de desempenho com um aumento relativamente modesto no tempo de treinamento.

- Não foram observados sinais claros de overfitting mesmo com o aumento para 60 épocas, sugerindo que o modelo poderia potencialmente se beneficiar de treinamento com ainda mais épocas ou técnicas adicionais de regularização.

## Recomendações

1. **Modelo Preferido**: Para este dataset específico, o modelo com 60 épocas é claramente preferível devido ao seu desempenho superior.

2. **Melhorias Futuras**: Considerar:
   - Aumento adicional no número de épocas
   - Técnicas de data augmentation para melhorar a detecção da classe A_Cat
   - Experimentar modelos YOLOv5 maiores (como YOLOv5m ou YOLOv5l) para classes difíceis de detectar

3. **Balanceamento de Classes**: Investigar por que a classe A_Cat tem desempenho inferior e considerar medidas para equilibrar o treinamento.
