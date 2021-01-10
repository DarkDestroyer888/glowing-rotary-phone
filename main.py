import discord
import os


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')
        if message.content.lower() == 'josh is baf':
            await message.channel.send('I agree')
        if message.content.lower() == 'shim is baf':
            await message.channel.send('I agree')


client = MyClient()
client.run(os.environ['DISCORD_TOKEN'])
