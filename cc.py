from pyrogram import Client, Filters,Emoji
app = Client("mrrr",784180,"8dcbf03f4637910d8c6fba7e1e16edbf")



u = '-1001183391894'

s = '-1001100924541'

@app.on_message(Filters.chat(int(s))& Filters.text & ~Filters.edited)
def forward(client, message):
    text = message.text
    f = False
    words = ['dekho','fix','😱','😢','😳','fixer','👆','👇','match','pass','sab','chase','defend','hai','karvana','link','loss','audio','varna','pura','puri','open','paid','contact','baazigar','market','load','whatsapp','timepass','kamma','book','teenpatti','diya','bhai','😀','😑','😐','😊','😜','😇','😎','😂','😘','😋','😝','🥺','members','🖕','member','only','chut','lund','gand','ma','maa','bhosdi','bahan','loude','lode','lavde','chutiya','🤞','🤟','☝️','mkc','bkc','mc','bc','madarchod','bahanchod','bahnchod','gandu','❓','kya','wbt','line','who',"https://",'joinchat','bullet','fuck','🤔','LUND']
    for word in words:
        if word.casefold() in text.casefold():
            f = True
    if not f:
        if '🕵🏻' in message.text:
            mes = client.send_message(int(u),"**" + message.text.replace('🕵🏻' , '💘') + "**")
            file = open("sure.txt" , "r")
            lines = file.readlines()
            file.close()
            for line in lines:
               files = open("sure.txt" , "w")
               files.write( line + " " + str(message.message_id) +  " " + str(mes.message_id))
               files.close()
        elif '☎️' in message.text :
            mes = client.send_message(int(u),"**" + message.text.replace('☎️' , '🏝') + "**")
            file = open("sure.txt" , "r")
            lines = file.readlines()
            file.close()
            for line in lines:
               files = open("sure.txt" , "w")
               files.write( line + " " + str(message.message_id) +  " " + str(mes.message_id))
               files.close()
        elif message.text.casefold() == 'WKT'.casefold() :
            client.send_message(int(u),'🚾** Wicket Wicket Wicket** 🚾 ') 
        elif 'DRINKS BREAK' in message.text:
            client.send_message(int(u), '🍻** DRINKS BREAK **🍻') 
        elif message.text.casefold() == '🚾WICKET WICKET🚾'.casefold():
            client.send_message(int(u),'🚾** Wicket Wicket Wicket **🚾')
        

@app.on_message(Filters.chat(int(s)) & Filters.sticker)
def forawrd(client, message):
  if message.sticker.file_id == 'CAADBQADkgIAAlTquhpPMfzjWNqQagI' :
    client.send_message(int(u),'🍾 **INNINIGS BREAK** 🍾' )
    
@app.on_message(Filters.chat(int(s))& Filters.text & Filters.edited)
def forward(client, message):
  file = open("sure.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
   x = line.split()
   id = str(message.message_id)
   if id in x:
     if '🕵🏻' in message.text:
        client.edit_message_text(int(u),int(x[x.index(id)+1]), "**" + message.text.replace('🕵🏻' , '💘') + "**" )
     elif '☎️' in message.text :
        client.edit_message_text(int(u),int(x[x.index(id)+1]),"**" + message.text.replace('☎️' , '🏝') + "**")
     
          
     
        
app.run()

