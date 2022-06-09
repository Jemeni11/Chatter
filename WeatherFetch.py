import requests
from discord import Embed
from BeaufortScale import wind_speed
from dotenv import load_dotenv
import os

load_dotenv()


def message_reply(message):
	api_key = os.getenv('API_KEY')

	# Example: https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=77854068949f3f3b8a9c6bcd807b0a70
	try:
		payload = {'q': str(message), 'units': 'imperial', 'APPID': api_key}
		response_data = requests.get("https://api.openweathermap.org/data/2.5/weather", params=payload).json()
		print(requests.get("https://api.openweathermap.org/data/2.5/weather", params=payload).text)
		if response_data['cod'] != '200':
			embed_reply = Embed(
				title="Error :(",
				url='',
				description="I'm sorry but I can't help you right now. Please try again later or contact my creator.",
				color=0x6A0DAD
			)
			return embed_reply
		else:
			weather_conditions = ['Thunderstorm', 'Drizzle', 'Rain', 'Snow', 'Atmosphere', 'Clear', 'Clouds']
			clothing = [
				[-100, 24, 'a Winter jacket'],
				[25, 44, 'a Light to medium coat'],
				[45, 64, 'a Fleece'],
				[65, 79, 'a Short sleeves'],
				[80, 500, 'a pair of shorts']
			]
			for i in clothing:
				if i[0] <= response_data['main']['feels_like'] <= i[1]:
					wear_this = i[2]
			weather_advice = f"""
			Hey! We think you should wear **{wear_this}**
			
			
			"""
			print(weather_advice)

			embed = Embed(
				title="Chatter!",
				url="https://github.com/Jemeni11/Chatter",
				description=weather_advice,
				color=0xE09319
			)

			# Add author, thumbnail, fields, and footer to the embed
			embed.set_author(
				name=f"It's {response_data['weather'][0]['main'].lower()} in {message.strip()}!",
				url="https://github.com/Jemeni11/Chatter",
				icon_url="https://avatars.githubusercontent.com/u/52603291?v=4"
			)

			embed.set_thumbnail(url=f"http://openweathermap.org/img/wn/{response_data['weather'][0].icon}@4x.png")

			embed.add_field(
				name="Temperature",
				value=
				f"""
				Min: {response_data['main']['temp_min']} • Main: {response_data['main']['temp']} \
				• Max: {response_data['main']['temp_max']} • Feels Like: {response_data['main']['feels_like']}
				""",
				inline=False
			)

			for i in wind_speed:
				if i[1] <= response_data['wind']['speed'] <= i[2]:
					embed.add_field(
						name="Wind",
						value=f"Description: {i[0]}\nLand Conditions: {i[3]}\n"
							  f"Speed: {response_data['wind']['speed']}\nBuilt with the Beaufort Scale.",
						inline=False
					)

			return embed

	except Exception as e:
		print(e)
