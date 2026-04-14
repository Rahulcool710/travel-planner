def send_message(sender, receiver, data):
    return {
        "from": sender,
        "to": receiver,
        "data": data
    }


def receive_message(message):
    return message["data"]