old_message = None
while True:
    readMessage = open('MessageData.txt','r')
    message = (readMessage.read())
    if message != old_message or message != '                                                                                                    ':
        print (message)
        old_message = message
    readMessage.close()
