import discord


client = discord.Client()

	
@client.event
async def on_member_join(member):
	channel=client.get_channel('472729942141042688')
    #await channel.send(msg)
	await client.send_message(channel, 'Welcome, {}! Please read the #rules and get some #roles'.format(member.mention))


	
client.run(token)	