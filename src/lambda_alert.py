import json
import boto3
import os


def lambda_handler(event, context):
    sns_client = boto3.client("sns", region_name="us-east-1")
    SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")

    try:
        if "body" not in event or not event["body"]:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Nenhum arquivo enviado"}),
            }

        pedido = json.loads(event["body"])

        # Publica a mensagem no SNS
        response = sns_client.publish(
            TopicArn=SNS_TOPIC_ARN, Message=json.dumps(pedido), Subject="Novo Pedido"
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "E-mail enviado com sucesso"}),
        }
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
