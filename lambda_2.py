import json
import base64
import boto3
ENDPOINT = "new-endpoint"
def lambda_handler(event, context):
    image = base64.b64decode(event["body"]["image_data"])
    runtime = boto3.client('sagemaker-runtime')
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType='application/x-image',  
        Body=image
    )

    inferences = json.loads(response['Body'].read().decode('utf-8'))
    event["inferences"] = inferences
    return {
        'statusCode': 200,
        'body': {
            "image_data": event["body"]['image_data'],
            "s3_bucket": event["body"]['s3_bucket'],
            "s3_key": event["body"]['s3_key'],
            "inferences": event['inferences'],
       }
    }
