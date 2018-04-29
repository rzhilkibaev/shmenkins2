def run(event, context):
    print("handling push notification")
    print("event")
    print(str(event))
    print("context")
    print(str(context))
    return {"statusCode": 201, "body": ""}
