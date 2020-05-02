import time
while True:
    text = input('What Do You Wanna Say? ---->')
    message = open('MessageData.txt', 'w')
    #appendfile.write('\n')
    message.write(text)
    message.close()

    readMessage = open('MessageData.txt','r')
    print (readMessage.read())
    readMessage.close()

    clearMessage = open('MessageData.txt', 'w')
    #appendfile.write('\n')
    clearMessage.write('                                                                                                    ')
    clearMessage.close()
