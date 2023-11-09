import telethon
from telethon import events
from telethon.sync import functions
from telethon import TelegramClient
from telethon.tl.functions.messages import GetPeerDialogsRequest

StrPython = TelegramClient("pnhp", 12297551, "9d3fd6a2c52c6b01312e02a3abf9999b") 
StrPython.start()
StrPython.send_message("me","مرحبا، الاوامر :\n`حجز + يوزر`")

@StrPython.on(
events.NewMessage(
outgoing=True, pattern=r"حجز"))
async def StrPy(event):
        clicks = 1
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        username = str(msg[0])
        
        await event.reply(f"Done start - @{username}")
        try:
        	while True:
                    clicks += 1
                    await StrPython(GetPeerDialogsRequest(peers=[username]))
        except telethon.errors.rpcerrorlist.UsernameNotOccupiedError:
                    try:
                        await StrPython(functions.account.UpdateUsernameRequest(username=username))           
                    except Exception as error:
                    	if "wait" in str(error):
                    	  	await StrPython.send_message(event.chat.id,f"Flood - {error.seconds} ️.")
                    	  	pass
                    	else:
                    		await StrPython.send_message(event.chat_id, f'''
Err: {error}
User is Error : {username}''')
                    else:
                        await StrPython.send_file(event.chat_id, "https://t.me/x_YaBh/6",caption=f'''We are the strongest @xx_YaBh !'
এ UserName: › @{username} ›
এ ClickS: › Account ›
এ Save: › {clicks} ›''')
                        await StrPython.send_message(event.chat_id,"New Username 🐊:\nt.me/xx_YaBh")
        except telethon.errors.rpcerrorlist.UsernameOccupiedError:
        	while True:
        		continue
        except telethon.errors.rpcerrorlist.ChannelPrivateError:
        	await StrPython(functions.account.UpdateUsernameRequest(username=username))           
        	await StrPython.send_file(event.chat_id, "https://t.me/x_YaBh/6",caption=f'''We are the strongest @xx_YaBh !'
এ UserName: › @{username} ›
এ ClickS: › Account ›
এ Save: › {clicks} ›** ''')
        	await StrPython.send_message(event.chat_id,"New Username 🐊:\n@xx_YaBh")
        
print("Run")
StrPython.run_until_disconnected()
