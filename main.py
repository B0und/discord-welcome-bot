import discord
import os

client = discord.Client()

token = os.environ.get('BOT_TOKEN')
channel_id = os.environ.get('channel_id')

	
@client.event
async def on_member_join(member):
	channel=client.get_channel(channel_id)
    #await channel.send(msg)
	await client.send_message(channel, 'Welcome, {}! Please read the #rules and get some #roles'.format(member.mention))
	#await self.bot.responses.success(message='Channel <#{}> will be ignored.'.format(channel.id)) 

	
client.run(token)