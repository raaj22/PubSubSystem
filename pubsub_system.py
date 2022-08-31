topic = {}
users = {}
topic_counter = 1
def createTopic():
    print ("Enter 0 to exit")
    global topic_counter
    name = input("Enter topic name")
    if name == "0":
        return -1
    msg = input("Enter details")
    if name not in topic:
        topic[name] = {}
        topic[name]['msg'] = msg
        topic[name]['number'] = str(topic_counter)
        topic[name]['client'] = []
        topic_counter += 1
        
    else:
        return

def createClient():
    print ("Enter 0 to exit")
    name = input("Enter user name")
    if name == "0":
        return -1
    users[name] = []
    if len(topic) == 0:
        print("No topics available")
        return
    else:
        for i in topic:
            print (topic[i]['number'], ":", i)
        while 1:
            print ("Enter 0 to exit")
            interest = input("Select topics from the list")
            if interest == "0":
                break
            users[name].append(interest)
            for i in topic:
                print (i)
                if topic[i]['number'] == interest:
                    topic[i]['client'].append(name)
    return
while 1: 
    if  createTopic() == -1:
        break

while 1:
    if createClient() == -1:
        break
def sendTopics():
    for i in topic:
        for j in topic[i]['client']:
            print (j, "has subscribed for ", i)
            print (topic[i]['msg'])
    return
sendTopics()
