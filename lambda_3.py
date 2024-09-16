import json

THRESHOLD = 0.9

def lambda_handler(event, context):
    inferences = event["body"]['inferences']
    meets_threshold = max(list(inferences))>THRESHOLD

    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_NOT_MET")

    return {
        'statusCode': 200,
        'body': event
    }