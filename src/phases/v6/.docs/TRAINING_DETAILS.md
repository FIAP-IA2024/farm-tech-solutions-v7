# Detalhes do Treinamento do Modelo YOLO

## Configuração do Ambiente

O treinamento do modelo YOLO foi realizado utilizando o framework YOLOv5, que é clonado automaticamente pelo script Python se ainda não estiver presente no ambiente.

```bash
git clone https://github.com/ultralytics/yolov5.git
pip install -r yolov5/requirements.txt
```

## Configuração do Dataset

Foi criado um arquivo de configuração YAML para o dataset, definindo os caminhos para os conjuntos de treinamento, validação e teste, além dos nomes das classes:

```yaml
path: /path/to/data
train: /path/to/data/train/images
val: /path/to/data/val/images
test: /path/to/data/test/images
nc: 2  # Número de classes
names: ["A_Cat", "B_Dog"]  # Nomes das classes
```

## Parâmetros de Treinamento

Os seguintes parâmetros foram utilizados para o treinamento do modelo:

- **Modelo**: YOLOv5s (versão pequena e rápida do YOLOv5)
- **Tamanho da imagem**: 640x640 pixels
- **Batch size**: 16
- **Épocas**: 30 (treinamento inicial)
- **Weights**: Inicialização com pesos pré-treinados do YOLOv5s

O comando de treinamento foi executado com os seguintes argumentos:

```bash
python train.py --img 640 --batch 16 --epochs 30 --data /path/to/dataset.yaml --weights yolov5s.pt --project ./results --name train_e30_bs16_timestamp
```

## Resultados do Treinamento

O treinamento foi concluído com sucesso, gerando diversos arquivos de resultado:

- **Métricas**: Precision, Recall, mAP@.5, mAP@.5:.95
- **Gráficos**: Curvas P, R, PR, F1, curvas de confusão
- **Pesos**: Modelo best.pt salvo no diretório weights/
- **Visualizações**: Batches de treinamento e validação

Os resultados completos podem ser encontrados no diretório:

```plaintext
results/train_e1_bs16_20250419_185121/
```

## Validação do Modelo

Após o treinamento, o modelo foi validado usando o conjunto de validação:

```bash
python val.py --img 640 --batch 16 --data /path/to/dataset.yaml --weights /path/to/best.pt --project ./results --name val_timestamp --task val
```

Os resultados da validação estão disponíveis em:

```plaintext
results/val_best_20250419_185253/
```

## Testes do Modelo

O modelo treinado foi testado com o conjunto de teste:

```bash
python detect.py --img 640 --source /path/to/test/images --weights /path/to/best.pt --project ./results --name test_timestamp --save-txt --save-conf
```

Os resultados dos testes estão disponíveis em:

```plaintext
results/test_best_20250419_185337/
```

## Próximos Passos

Para melhorar o modelo, poderiam ser realizados os seguintes ajustes:

1. Treinar com um número maior de épocas para avaliar se há melhorias significativas
2. Experimentar diferentes tamanhos de modelos YOLOv5 (s, m, l, x)
3. Aplicar técnicas de data augmentation para melhorar a generalização
4. Ajustar hiperparâmetros como learning rate e batch size
