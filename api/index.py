from flask import Flask, request, abort
import os
import random
import time
import datetime

from gradio_client import Client

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

LINE_CHANNEL_SECRET = os.environ["TRESCHA_LINE_CHANNEL_SECRET"]
LINE_MESSAGE_ACCESS = os.environ["TRESCHA_LINE_MESSAGE_ACCESS"]

app = Flask(__name__)

try:
    configuration = Configuration(access_token=LINE_MESSAGE_ACCESS)
    handler = WebhookHandler(LINE_CHANNEL_SECRET)
except:
    print("ERoor")


chat_url = "https://deniandriancode-trescha-chatbot.hf.space/"
chat_url_stranger = "https://deniandriancode-trescha-stranger-chatbot.hf.space/"

@app.route("/")
def greeting_default():
    return "<p>You are viewing a working website built with Flask.</p>"

@app.route("/callback", methods=['POST'])
def callback():
    return {
        "message": "OK POST",
        "channel_secret": LINE_CHANNEL_SECRET,
        "message_access": LINE_MESSAGE_ACCESS
    }
    # # get X-Line-Signature header value
    # signature = request.headers['X-Line-Signature']

    # # get request body as text
    # body = request.get_data(as_text=True)
    # app.logger.info("Request body: " + body)

    # # handle webhook body
    # try:
    #     handler.handle(body, signature)
    # except InvalidSignatureError:
    #     app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
    #     abort(400)

    # return 'OK'


# @handler.add(MessageEvent, message=TextMessageContent)
# def handle_message(event):
#     with ApiClient(configuration) as api_client:
#         client = Client(chat_url)
#         prompt = event.message.text
#         result = client.predict(
#             prompt,	# str in 'Message' Textbox component
#             0.9,
#             500,
#             0.95,
#             1.0,
# 	    api_name="/chat"
#         )
#         result = result.replace("</s>", "")
#         line_bot_api = MessagingApi(api_client)
#         line_bot_api.reply_message_with_http_info(
#             ReplyMessageRequest(
#                 reply_token=event.reply_token,
#                 messages=[TextMessage(text=result)]
#             )
#         )


