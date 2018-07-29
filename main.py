import discord
import os

client = discord.Client()

token = os.environ.get('BOT_TOKEN')
#channel_id = 
#"NDcyNzUwMzY5ODk4NzU4MTY0.Dj38LA.BfKc1hS0xKEpUBFGfFso7WYqnDE"
	
@client.event
async def on_member_join(member):
	channel=client.get_channel('472729942141042688')
    #await channel.send(msg)
	await client.send_message(channel, 'Welcome, {}! Please read the #rules and get some #roles'.format(member.mention))
	#await self.bot.responses.success(message='Channel <#{}> will be ignored.'.format(channel.id)) 

	
client.run(token)