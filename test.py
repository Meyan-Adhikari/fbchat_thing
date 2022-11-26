from fbchat import Client
from fbchat.models import *
from functions import *
from threading import Thread
import time

meyan = "100078863451761"
on=True
prev = time.time()
def do():
    global prev
    while on:
        if(time.time()-prev) >300:
            print("WORKING")
            with open("school.text",'r',encoding="utf8") as file1:
                st = file1.read()
                print(st)
            stuff=get_pos()
            print(stuff)
            if(stuff!=st):
                print("OK NOT COME")
                client.send(Message(text=stuff),"5354113521302706",thread_type=ThreadType.GROUP)
                
            with open("school.text",'w',encoding="utf8") as file1:
                file1.write(stuff)   
            prev = time.time()
            print("HERE")

on1=True
prev1 = time.time()

def do1():
    global prev
    while on1:
        if(time.time()-prev) >3600:          
            stuff=get_pos_ronb()
            client.send(Message(text=stuff),"5354113521302706",thread_type=ThreadType.GROUP) 
            prev1= time.time()
            print("HERE")
            prev = time.time()

class Bot(Client):
    def onMessage(self, mid, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
        
   
        # Do something with message_object here
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        if author_id != self.uid:
            if message_object.text[0:5]=="/post":
                self.send(Message(text=get_pos()),thread_id,thread_type=thread_type)

            if message_object.text[0:5]=="/wiki":
                self.send(Message(text=get_s(message_object.text[6:])),thread_id,thread_type=thread_type)
            
            if message_object.text[0:5]=="/help":
                self.send(Message(text="Hey!!\n/wiki anything -Searches and displays info about anything\n\n\n/show something -Shows the pic of any items(Doesn't work great with people though (WIll fix later))\n\n/say quote -says a random quote\n\n/say joke -says a random joke\n\n/date -to tell the current date a and time\n\n/date nepal to say the current date and time in nepali\n\n/post -shows the newest post by the school\n\n/show routine -shows the rountin of the class(also use today or tommorow for specific day)\n\n/ronb -shows recent news by RONB"),thread_id,thread_type=thread_type)
            
            if message_object.text[0:5]=="/show":
                if "ronb" in message_object.text.lower():
                    self.send(Message(text=get_pos_ronb()),thread_id,thread_type=thread_type)
                if not  "routine" in message_object.text.lower():
                        client.sendRemoteFiles(
            file_urls=get_im(message_object.text[6:]),
            message=Message(text="Hopefully this works!:)"),
            thread_id=thread_id,
            thread_type=thread_type,
        )

                else:
                    if "today" in message_object.text.lower():
                        self.send(Message(text=today_routine()),thread_id,thread_type=thread_type)
                    elif "tommorow" in message_object.text.lower():
                        self.send(Message(text=tomm_routine()),thread_id,thread_type=thread_type)
                    else:
                        client.sendLocalFiles(file_paths="routine.jpg",
            message=Message(text="Hopefully this works!:)"),
            thread_id=thread_id,
            thread_type=thread_type,
        )
            if message_object.text[0:5].lower()=="/date":
                if "nepal" in message_object.text.lower():
                    self.send(Message(text=nep_date()),thread_id,thread_type=thread_type)
                else:
                    self.send(Message(text=date()),thread_id,thread_type=thread_type)
            
            if message_object.text[0:5].lower()=="/ronb":
                    self.send(Message(text=get_pos_ronb()),thread_id,thread_type=thread_type)
            if message_object.text[0:5].lower()=="/news":
                    self.send(Message(text=get_pos_ronb()),thread_id,thread_type=thread_type)
               

            if message_object.text[0:4].lower()=="/say":
                if "quote" in message_object.text.lower():
                    self.send(Message(text=rand_quote()),thread_id,thread_type=thread_type)
                if "date" in message_object.text.lower():
                    if "nepal" in message_object.text.lower():
                        self.send(Message(text=nep_date()),thread_id,thread_type=thread_type)
                    else:
                        self.send(Message(text=date()),thread_id,thread_type=thread_type)
                elif "joke" in message_object.text.lower():
                    if not "mama" in message_object.text.lower():
                        self.send(Message(text=joke()),thread_id,thread_type=thread_type)
                    else:
                        self.send(Message(text=yo_mama()),thread_id=thread_id,thread_type=thread_type)
                
                else:
                    if not "nepali" in message_object.text.lower():
                        conv_mp3(message_object.text[4:])
                        self.sendLocalVoiceClips("welcome.mp3",message=None,thread_id=thread_id,thread_type=thread_type)
                    else:
                        conv_mp3(message_object.text[4:].lower().replace("nepali","").replace("in",""),'ne')
                        self.sendLocalVoiceClips("welcome.mp3",message=None,thread_id=thread_id,thread_type=thread_type)


                

client = Bot('meyanadhikaripython@gmail.com', 'kritiistheone')
Thread(target=do).start()
Thread(target=do1).start()
try:
    client.listen()
except:
    on=False
    on1=False
on=False
on1=False


