from pyrogram import Client, Filters,Emoji
app = Client('my_account',728044,"a41ddadc9696482aff94a4b37221574a")



u = '-1001378725482'

s = '-1001262096355'

@app.on_message(Filters.chat(int(s))& Filters.text & ~Filters.edited)
def forward(client, message):
    text = message.text
    f = False
    words = ['dekho','fix','😱','😢','😳','fixer','👆','👇','match','pass','sab','chase','defend','hai','karvana','link','loss','audio','varna','pura','puri','open','paid','contact','baazigar','market','load','whatsapp','timepass','kamma','book','teenpatti','diya','bhai','😀','😑','😐','😊','😜','😇','😎','😂','😘','😋','😝','🥺','members','🖕','member','only','chut','lund','gand','ma','maa','bhosdi','bahan','loude','lode','lavde','chutiya','🤞','🤟','☝️','mkc','bkc','mc','bc','madarchod','bahanchod','bahnchod','gandu','❓','kya','wbt','line','who',"https://",'joinchat','bullet','fuck','🤔','LUND']
    for word in words:
        if word.casefold() in text.casefold():
            f = True
    if not f:
        if '🖲' in message.text:
            mes = client.send_message(int(u),message.text.replace('🖲' , '**💘'))
            file = open("sure.txt" , "r")
            lines = file.readlines()
            file.close()
            for line in lines:
               files = open("sure.txt" , "w")
               files.write( line + " " + str(message.message_id) +  " " + str(mes.message_id))
               files.close()
        elif '📟' in message.text :
            mes = client.send_message(int(u),message.text.replace('📟' , '🏝'))
            file = open("sure.txt" , "r")
            lines = file.readlines()
            file.close()
            for line in lines:
               files = open("sure.txt" , "w")
               files.write( line + " " + str(message.message_id) +  " " + str(mes.message_id))
               files.close()
        elif message.text == '6':
            client.send_sticker(int(u),'CAADBQADHAAD271NHXPgZgboyWwDAg')
            client.send_message(int(u),'**Six**')
        elif message.text == '4' :
            client.send_sticker(int(u),'CAADBQADGwAD271NHWpGz0fJOgEPAg')
            client.send_message(int(u),'**Four**')
        elif message.text == 'WD' :
            client.send_sticker(int(u),'CAADBQADHgAD271NHUFx5PgLyzp9Ag')
            client.send_message(int(u),'🤦‍♂️ **WIDE BALL** 🤦‍♂️')
        elif message.text.casefold() == 'WKT'.casefold() :
            client.send_sticker(int(u),'CAADBQADHQAD271NHQimFHP2bU9cAg')
            client.send_message(int(u),'🚾** Wicket Wicket Wicket** 🚾 ') 
        elif 'NO BALL' in message.text:
            client.send_message(int(u),'🔛** NO BALL **🔛' )
        elif 'DRINKS BREAK' in message.text:
            client.send_sticker(int(u),'CAADBQADJQAD271NHRSHuFn7xmbvAg')
            client.send_message(int(u), '🍻** DRINKS BREAK **🍻') 
        elif 'DEAD BALL' in message.text:
            client.send_sticker(int(u),'CAADBQADIQAD271NHd6xC7TBgAsmAg')
            client.send_message(int(u), '🔁** DEAD BALL **🔄') 
        elif message.text.casefold() == 'RUKA'.casefold():
            client.send_message(int(u), '🛑** BOWLER RUKA **🛑')
        elif message.text.casefold() == '🚾WICKET WICKET🚾'.casefold():
            client.send_sticker(int(u),'CAADBQADHQAD271NHQimFHP2bU9cAg')
            client.send_message(int(u),'🚾** Wicket Wicket Wicket **🚾')
        else:
            mes = client.send_message(int(u),message.text.replace('🎾' , '🥎'))
            file = open("sure.txt" , "r")
            lines = file.readlines()
            file.close()
            for line in lines:
               files = open("sure.txt" , "w")
               files.write( line + " " + str(message.message_id) +  " " + str(mes.message_id))
               files.close()
         

@app.on_message(Filters.chat(int(s)) & Filters.sticker)
def forawrd(client, message):
  if message.sticker.file_id == 'CAADBQADkgIAAlTquhpPMfzjWNqQagI' :
    client.send_sticker(int(u),'CAADBQADHwAD271NHQtXw-moeKYWAg')
    client.send_message(int(u),'🍾 **INNINIGS BREAK** 🍾' )
    
@app.on_message(Filters.chat(int(s))& Filters.text & Filters.edited)
def forward(client, message):
  print(message.text)
  file = open("sure.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
   x = line.split()
   id = str(message.message_id)
   if id in x:
     client.edit_message_text(int(u),int(x[x.index(id)+1]), message.text)
  
        
app.run()



   
