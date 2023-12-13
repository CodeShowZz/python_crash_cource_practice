def send_messages(messages):
    sent_messages = []
    while messages:
        message = messages.pop(0)
        print(message)
        sent_messages.append(message)
    print(messages)
    print(sent_messages)


messages = ["hello world", "please to sit", "go go go"]
send_messages(messages)
