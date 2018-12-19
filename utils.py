import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAcgWhQRBasBAL2jHylz1ZAPdFWmevj1khBgUoUaTTdvxAyy3orqtEA3u3XuREPcZB9cqwJSc9LkfvTOZAkDAXl5k21PYSJqv7f2uxeJjZCAc8ta0Gsr0ldQxlZBQYMdt9VliBdQSIqjCZBBuHXuUx5t4l63shgF93GztZBeJri0QZDZD"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response



def send_image_url(id, img_url):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload ={
        "recipient":{
            "id":id
        },
        "message":{
            "attachment":{
                "type":"image", 
                "payload":{
                    "url":img_url, 
                    "is_reusable":True
                }
            }
        }
    }
    response = requests.post(url,json=payload)
    
    if response.status_code != 200:
        print("Unable to send img: ")
    return response
"""
def send_button_message(id, text, buttons):
    pass

"""
