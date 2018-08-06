import discord
import os


client = discord.Client()

token = os.environ.get('BOT_TOKEN')
channel_id = os.environ.get('channel_id')
roles_id = os.environ.get('roles_id')
rules_id = os.environ.get('rules_id')
timer = int(os.environ.get("timer"))
	
@client.event
async def on_member_join(member):
	channel=client.get_channel(channel_id)
	rules = client.get_channel(rules_id)
	roles = client.get_channel(roles_id)
 
	def check(msg):
		return msg.content.startswith('Welcome') and member.mention in msg.content

	message = await client.wait_for_message(timeout=timer,check=check)
	if not message:
		await client.send_message(channel, 'Welcome, {}! Please read the {} and get some {} !'\
		' It`s  important, in order to understand how to navigate through the text channels quickly.'.format(member.mention, rules.mention, roles.mention))


	
client.run(token)