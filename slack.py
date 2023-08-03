import requests

def send_slack_message(message):
    payload = '{"text": "%s"}' % message
    response = requests.post(
        'https://hooks.slack.com/services/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',
        data = payload
    )
    print(response.text)



send_slack_message("hello")
