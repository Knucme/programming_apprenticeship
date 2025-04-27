def show_messages(msgs):
    for msg in msgs:
        print(msg)
def send_messages(msgs):
    for msg in msgs:
        print(f"Transfering: {msg}")
        new_msgs.append(msg)

msgs = ["lol", "wyd?", "onm"]
new_msgs = []

print("The following messeges will be transfered:")
show_messages(msgs)
print("***Transfer starting***")
send_messages(msgs)
print("***Transfer Complete!***")
print("New list contains the following messeges:")
show_messages(new_msgs)
