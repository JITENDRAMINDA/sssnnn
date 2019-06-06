from pyrogram import Client, Filters,Emoji
app = Client('my_account',728044,"a41ddadc9696482aff94a4b37221574a")



u = '-1001163982951'

s = '-1001369162545'

@app.on_message(Filters.chat(int(s)) & Filters.text & ~ Filters.edited)
def forawrd(client, message):
    file = open("text.txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
      if not line == 'closed':
        if '🖲' in message.text:
            client.send_message(int(u),message.text.replace('🖲' , '**💘'))
        elif '📟' in message.text :
            client.send_message(int(u),message.text.replace('📟' , '🏝'))
        elif message.text == '6':
            client.send_sticker(int(u),'CAADBQADHAAD271NHXPgZgboyWwDAg')
            client.send_message(int(u),'**Six**')
        elif message.text == '4' :
            client.send_sticker(int(u),'CAADBQADGwAD271NHWpGz0fJOgEPAg')
            client.send_message(int(u),'**Four**')
        elif message.text == 'WD' :
            client.send_sticker(int(u),'CAADBQADHgAD271NHUFx5PgLyzp9Ag')
            client.send_message(int(u),message.text.replace('WD' , '🤦‍♂️ **WIDE BALL** 🤦‍♂️'))
        elif message.text == 'WKT' :
            client.send_sticker(int(u),'CAADBQADHQAD271NHQimFHP2bU9cAg')
            client.send_message(int(u),message.text.replace('WKT' , '🚾** Wicket Wicket Wicket** 🚾 ')) 
        elif 'NO BALL' in message.text:
            client.send_message(int(u),message.text.replace('NO BALL' , '🔛** NO BALL **🔛') )
        elif 'DRINKS BREAK' in message.text:
            client.send_sticker(int(u),'CAADBQADJQAD271NHRSHuFn7xmbvAg')
            client.send_message(int(u), '🍻** DRINKS BREAK **🍻') 
        elif 'DEAD BALL' in message.text:
            client.send_sticker(int(u),'CAADBQADIQAD271NHd6xC7TBgAsmAg')
            client.send_message(int(u), '🔁** DEAD BALL **🔄') 
        elif message.text == 'RUKA':
            client.send_message(int(u), '🛑** BOWLER RUKA **🛑')
        elif message.text == '🚾WICKET WICKET🚾':
            client.send_sticker(int(u),'CAADBQADHQAD271NHQimFHP2bU9cAg')
            client.send_message(int(u),message.text.replace('🚾WICKET WICKET🚾' , '🚾** Wicket Wicket Wicket **🚾'))
        elif "bullet".casefold() in message.text.casefold():
          print(".")
        elif "who".casefold() in message.text.casefold():
          print(".")
        elif "bahanchod".casefold() in message.text.casefold():
          print(".")
        elif "lund".casefold() in message.text.casefold():
          print(".")
        elif "mkc".casefold() in message.text.casefold():
          print(".")
        elif "loude".casefold() in message.text.casefold():
          print(".")
        elif "member".casefold() in message.text.casefold():
          print(".")
        elif "🖕".casefold() in message.text.casefold():
          print(".")
        elif "chut".casefold() in message.text.casefold():
          print(".")
        elif "gand".casefold() in message.text.casefold():
          print(".")
        elif "maa".casefold() in message.text.casefold():
          print(".")
        elif "bhosdi".casefold() in message.text.casefold():
          print(".")
        elif "chutiya".casefold() in message.text.casefold():
          print(".")
        elif "madarchod".casefold() in message.text.casefold():
          print(".")
        elif "kya".casefold() in message.text.casefold():
          print(".")
        elif "🤟".casefold() in message.text.casefold():
          print(".")
        elif "☝️".casefold() in message.text.casefold():
          print(".")
        elif "😜".casefold() in message.text.casefold():
          print(".")
        elif "😎".casefold() in message.text.casefold():
          print(".")
        elif "😂".casefold() in message.text.casefold():
          print(".")
        elif "😂".casefold() in message.text.casefold():
          print(".")
        elif "😋".casefold() in message.text.casefold():
          print(".")
        elif "🥺".casefold() in message.text.casefold():
          print(".")
        elif "members".casefold() in message.text.casefold():
          print(".")
        elif "only".casefold() in message.text.casefold():
          print(".")
        elif "chut".casefold() in message.text.casefold():
          print(".")
        elif "karvana".casefold() in message.text.casefold():
          print(".")
        elif "link".casefold() in message.text.casefold():
          print(".")
        elif "loss".casefold() in message.text.casefold():
          print(".")
        elif "audio".casefold() in message.text.casefold():
          print(".")
        elif "varna".casefold() in message.text.casefold():
          print(".")
        elif "pura".casefold() in message.text.casefold():
          print(".")
        elif "puri".casefold() in message.text.casefold():
          print(".")
        elif "open".casefold() in message.text.casefold():
          print(".")
        elif "paid".casefold() in message.text.casefold():
          print(".")
        elif "contact".casefold() in message.text.casefold():
          print(".")
        elif "baazigar".casefold() in message.text.casefold():
          print(".")
        elif "market".casefold() in message.text.casefold():
          print(".")
        elif "load".casefold() in message.text.casefold():
          print(".")
        elif "whatsapp".casefold() in message.text.casefold():
          print(".")
        elif "timepass".casefold() in message.text.casefold():
          print(".")
        elif "kamma".casefold() in message.text.casefold():
          print(".")
        elif "book".casefold() in message.text.casefold():
          print(".")
        elif "teenpatti".casefold() in message.text.casefold():
          print(".")
        elif "diya".casefold() in message.text.casefold():
          print(".")
        elif "bhai".casefold() in message.text.casefold():
          print(".")
        elif "😀".casefold() in message.text.casefold():
          print(".")
        elif "😑".casefold() in message.text.casefold():
          print(".")
        elif "😐".casefold() in message.text.casefold():
          print(".")
        elif "ID".casefold() in message.text.casefold():
          print(".")
        elif "dekho".casefold() in message.text.casefold():
          print(".")
        elif "fix".casefold() in message.text.casefold():
          print(".")
        elif "😱".casefold() in message.text.casefold():
          print(".")
        elif "😳".casefold() in message.text.casefold():
          print(".")
        elif "fixer".casefold() in message.text.casefold():
          print(".")
        elif "👆".casefold() in message.text.casefold():
          print(".")
        elif "👇".casefold() in message.text.casefold():
          print(".")
        elif "match".casefold() in message.text.casefold():
          print(".")
        elif "pass".casefold() in message.text.casefold():
          print(".")
        elif "sab".casefold() in message.text.casefold():
          print(".")
        elif "chase".casefold() in message.text.casefold():
          print(".")
        elif "id".casefold() in message.text.casefold():
          print(".")
        elif "kama".casefold() in message.text.casefold():
          print(".")
        elif "lu".casefold() in message.text.casefold():
          print(".")
        elif "script".casefold() in message.text.casefold():
          print(".")
        elif "paise".casefold() in message.text.casefold():
          print(".")
        elif "UDEGA".casefold() in message.text.casefold():
          print(".")
        elif "dam".casefold() in message.text.casefold():
          print(".")
        elif "😒".casefold() in message.text.casefold():
          print(".")
        elif "LOOT".casefold() in message.text.casefold():
          print(".")
        elif "HTTPS".casefold() in message.text.casefold():
          print(".")
        else:
            client.send_message(int(u),message.text.replace('🎾' , '🥎'))
            print(message.text)


@app.on_message(Filters.chat(int(s)) & Filters.sticker)
def forawrd(client, message):
    file = open("text.txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
      if not line == 'closed':
        if message.sticker.file_id == 'CAADBQADkgIAAlTquhpPMfzjWNqQagI' :
            client.send_sticker(int(u),'CAADBQADHwAD271NHQtXw-moeKYWAg')
            client.send_message(int(u),'🍾 **INNINIGS BREAK** 🍾' )

@app.on_message(Filters.command('status'))
def main(client, message) :
    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
      file = open("text.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
        if line == "started":
           message.reply("line is on ! ")
        if line == "closed":
           message.reply("line is stopped ! ")
    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
      file = open("text.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
        if line == "started":
           message.reply("line is on ! ")
        if line == "closed":
           message.reply("line is stopped ! ")        
@app.on_message(Filters. private)
def ran( client, message) :
  client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
@app.on_message(Filters.command('offline'))
def main(client, message) :
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
    file = open("text.txt" , "w")
    file.write("closed")
    file.close()
    message.reply("line is off ! ")
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
    file = open("text.txt" , "w")
    file.write("closed")
    file.close()
    message.reply("line is off ! ")
@app.on_message(Filters.command('online'))
def main(client, message) :
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
    file = open("text.txt" , "w")
    file.write("started")
    file.close()
    message.reply("line is on !")
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
    file = open("text.txt" , "w")
    file.write("started")
    file.close()
    message.reply("line is on !")
app.run()
