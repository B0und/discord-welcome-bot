import discord
import os

client = discord.Client()

token = os.environ.get('BOT_TOKEN')
channel_id = os.environ.get('channel_id')
roles_id = os.environ.get('roles_id')
rules_id = os.environ.get('rules_id')
	
@client.event
async def on_member_join(member):
	channel=client.get_channel(channel_id)
	rules = client.get_channel(rules_id)
	roles = client.get_channel(roles_id)
    #await channel.send(msg)
	await client.send_message(channel, 'Welcome, {}! Please read the {} and get some {} !'.format(member.mention, rules.mention, roles.mention))
 
	
client.run(token)