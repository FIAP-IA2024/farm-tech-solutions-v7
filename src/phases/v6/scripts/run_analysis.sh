#!/bin/bash
# Script para executar a análise de resultados e gerar relatórios
# Codificado em UTF-8

set -e

# Definir diretórios
RESULTS_DIR="results/comparison"
OUTPUT_DIR="${RESULTS_DIR}/analysis_output"
REPORT_FILE="${RESULTS_DIR}/analysis_summary.md"

# Caminhos dos modelos
MODEL_30_TRAIN="${RESULTS_DIR}/train_e30_bs16_20250429_103607"
MODEL_60_TRAIN="${RESULTS_DIR}/train_e60_bs16_20250429_105247"
MODEL_30_VAL="${RESULTS_DIR}/val_best_20250429_112355"
MODEL_60_VAL="${RESULTS_DIR}/val_best_20250429_112434"

# Criar diretório de saída se não existir
mkdir -p "$OUTPUT_DIR"

echo "Iniciando análise de resultados de treinamento de modelos YOLO..."

# Executar o script de análise
python scripts/results_analysis.py \
  --model1_train "$MODEL_30_TRAIN" \
  --model2_train "$MODEL_60_TRAIN" \
  --model1_val "$MODEL_30_VAL" \
  --model2_val "$MODEL_60_VAL" \
  --save_dir "$OUTPUT_DIR" \
  --model1_name "30 Épocas" \
  --model2_name "60 Épocas"

# Verificar se a análise foi bem-sucedida
if [ $? -eq 0 ]; then
  echo "Análise concluída com sucesso."
  echo "Resultados salvos em $OUTPUT_DIR"
  echo "Relatório de análise disponível em $REPORT_FILE"
  
  # Abrir o resumo da análise se estiver no macOS
  if [[ "$OSTYPE" == "darwin"* ]]; then
    open "$REPORT_FILE"
  # Abrir com xdg-open no Linux
  elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open "$REPORT_FILE"
  fi
else
  echo "A análise falhou com código de erro $?"
  exit 1
fi

# Imprimir resumo das visualizações geradas
echo -e "\nVisualizações geradas:"
find "$OUTPUT_DIR" -name "*.png" | sort | while read -r file; do
  echo " - $(basename "$file")"
done

exit 0 