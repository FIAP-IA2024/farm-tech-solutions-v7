import requests
import json
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# URL para o endpoint da API AWS Lambda
ALERT_API_URL = "https://wuu3yuphjl.execute-api.us-east-1.amazonaws.com/pedidos"

def send_alert(crop, issue):
    """
    Envia um alerta para o sistema AWS Lambda
    
    Args:
        crop (str): Nome da cultura
        issue (str): Descrição do problema/alerta
    
    Returns:
        dict: Resposta da API ou mensagem de erro
    """
    # Validar os parâmetros
    if not crop or not issue:
        return {
            "success": False,
            "error": "Os campos de cultura e problema são obrigatórios"
        }
    
    # Preparar o payload
    payload = {
        "crop": crop,
        "issue": issue
    }
    
    try:
        # Enviar a requisição POST
        response = requests.post(
            ALERT_API_URL,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )
        
        # Verificar o status da resposta
        if response.status_code == 200:
            logger.info(f"Alerta enviado com sucesso: {payload}")
            return {
                "success": True,
                "message": "Alerta enviado com sucesso!",
                "response": response.json() if response.text else {}
            }
        else:
            logger.error(f"Erro ao enviar alerta: Status {response.status_code}, Resposta: {response.text}")
            return {
                "success": False,
                "error": f"Erro ao enviar alerta: {response.status_code}",
                "details": response.text
            }
    
    except requests.RequestException as e:
        logger.error(f"Erro de requisição ao enviar alerta: {str(e)}")
        return {
            "success": False,
            "error": "Erro de conexão",
            "details": str(e)
        }
    
    except Exception as e:
        logger.error(f"Erro inesperado ao enviar alerta: {str(e)}")
        return {
            "success": False,
            "error": "Erro inesperado",
            "details": str(e)
        }
