from pyrogram import Client, Filters
app = Client('my_account',814511,"44462f0f278503255d5cc30941b617a9")


u = '-1001356076506'
s = '-1001378725482'
@app.on_message(Filters.chat(int(s)) & Filters.text)
def forawrd(client, message):
    print(message.text)
    file = open("text.txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
      if not line == 'closed':
        if '🖲' in message.text :
            client.send_message(int(u),message.text.replace('🖲' , '**💘'))
        else:
          if '📟' in message.text :
            client.send_message(int(u),message.text.replace('📟' , '🏝'))
          else:
            if message.text == '6' :
               client.send_sticker(int(u),'CAADBQADHAAD271NHXPgZgboyWwDAg')
               client.send_message(int(u),'**Six**')
            else:
              if message.text == '4' :
               client.send_sticker(int(u),'CAADBQADGwAD271NHWpGz0fJOgEPAg')
               client.send_message(int(u),'**Four**')
              else:
                if message.text == 'WD' :
                  client.send_sticker(int(u),'CAADBQADHgAD271NHUFx5PgLyzp9Ag')
                  client.send_message(int(u),message.text.replace('WD' , '🤦‍♂️ **WIDE BALL** 🤦‍♂️'))
                else:
                    if message.text == 'WKT' :
                     client.send_sticker(int(u),'CAADBQADHQAD271NHQimFHP2bU9cAg')
                     client.send_message(int(u),message.text.replace('WKT' , '🚾** Wicket Wicket Wicket** 🚾 ')) 
                    else:
                       if 'NO BALL' in message.text:
                         client.send_message(int(u),message.text.replace('NO BALL' , '🔛** NO BALL **🔛') )
                       else:
                          if 'DRINKS BREAK' in message.text:
                            client.send_sticker(int(u),'CAADBQADJQAD271NHRSHuFn7xmbvAg')
                            client.send_message(int(u), '🍻** DRINKS BREAK **🍻') 
                          else:
                            if 'DEAD BALL' in message.text:
                               client.send_sticker(int(u),'CAADBQADIQAD271NHd6xC7TBgAsmAg')
                               client.send_message(int(u), '🔁** DEAD BALL **🔄') 
                            else:
                              if message.text == 'RUKA':
                                 client.send_message(int(u), '🛑** BOWLER RUKA **🛑')
                              else:
                                if message.text == '🚾WICKET WICKET🚾':
                                   client.send_sticker(int(u),'CAADBQADHQAD271NHQimFHP2bU9cAg')
                                   client.send_message(int(u),message.text.replace('🚾WICKET WICKET🚾' , '🚾** Wicket Wicket Wicket **🚾 '))
                                else:
                                   client.send_message(int(u),message.text.replace('🎾' , '🥎'))


@app.on_message(Filters.chat(int(s)) & Filters.sticker)
def forawrd(client, message):
    file = open("text.txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
      if not line == 'closed':
        if message.sticker.file_id == 'CAADBQADFAQAAlrCoBKRHyVMca5GGQI' :
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
