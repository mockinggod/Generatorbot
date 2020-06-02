import discord
import asyncio
from discord.ext import commands
import interface
import homebrew as hb
import random
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import psqlfunctions as psqlf

sched = AsyncIOScheduler()
sched.start()

try:  
	TOKEN = os.environ["TOKEN"]
except KeyError: 
	with open("token.txt", encoding='UTF-8') as f:
		TOKEN = f.read() 

try:  
	idnum = os.environ["DISCORDID"]
except KeyError: 
	with open("discordid.txt", encoding='UTF-8') as f:
		idnum = f.read() 
	
try:  
	serverinfo = os.environ["DATABASE_URL"]
except KeyError: 
	with open("serverinfo.txt", encoding='UTF-8') as f:
		serverinfo = f.read() 
	
	
feedbackusedtoday = [] 
	


with open("helptext.txt", encoding='UTF-8') as f:
		helptext = f.read().splitlines() 
	
with open("itemlisttext.txt", encoding='UTF-8') as f:
    itemlisttext = f.read().splitlines()

with open("Infotext.txt", encoding='UTF-8') as f:
    infotext = f.read().splitlines()
	
def prefix(bot, message): # Function finds the prefix used by the guild
	
	prefix = "!"
	if isinstance(message.channel, discord.abc.GuildChannel):
		for n in range(len(prefixes)):
			if int(prefixes[n-1][0]) == message.guild.id:
				prefix = str(prefixes[n-1][1])
				break
			
	return(prefix)	

prefixes = psqlf.readprefixes(serverinfo)	
	
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")


@bot.event
async def on_ready():
	activity = discord.Activity(name="you | Default prefix is ! | Type (prefix)help for a list of commands", type=discord.ActivityType.watching)
	await bot.change_presence(activity=activity)
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print(idnum)
	print('------')
	
@bot.event
async def on_guild_remove(guild):

	for n in range(len(prefixes[0])):
		if int(prefixes[n-1][0]) == guild.id:
			psqlf.removeprefix(serverinfo, guild.id)
			del prefixes[n-1]
			break
	
def clearfeedbacklist():	

	feedbackusedtoday.clear()
	print('Feedback list cleared')
	
sched.add_job(clearfeedbacklist, 'cron', hour = 0)
	

	
@bot.command()
async def hi(ctx): # For testing

	output = "Hello there, General " + ctx.message.author.name
	await ctx.send(output)
	await delete_command(ctx)
	
	
# The most important function, calls interface to generate all the bots content
@bot.command()
async def gen(ctx, item = "nothing was entered0", *args):

	await delete_command(ctx)
	
	openoutput, secretoutput = interface.main(ctx, item, *args)
	
	if max(len(openoutput), len(secretoutput)) > 1999:
		await ctx.send("The generated message is too long, one of us was too ambitious, try again.")
	else:
		if openoutput == secretoutput:
			await ctx.send(openoutput)
		else:
			if isinstance(ctx.message.channel, discord.abc.GuildChannel):
				await ctx.send(openoutput)
				await ctx.message.author.send(secretoutput)
			else:
				await ctx.send(secretoutput)
				
# Same as before just with g instead
@bot.command()
async def g(ctx, item = "nothing was entered0", *args):

	await delete_command(ctx)

	openoutput, secretoutput = interface.main(ctx, item, *args)
	
	if max(len(openoutput), len(secretoutput)) > 1999:
		await ctx.send("The generated message is too long, one of us was too ambitious, try again.")
	else:
		if openoutput == secretoutput:
			await ctx.send(openoutput)
		else:
			if isinstance(ctx.message.channel, discord.abc.GuildChannel):
				await ctx.send(openoutput)
				await ctx.message.author.send(secretoutput)
			else:
				await ctx.send(secretoutput)
				

		
@bot.command()
async def help(ctx):

	await delete_command(ctx)

	output = ""
	for i in helptext:
		output += i + "\n"
		
	output = output.replace("@prefix@", prefix(bot, ctx.message))
		
	await ctx.send(output)
	
# Prints out the list of things that can be generated
@bot.command()	
async def itemlist(ctx):

	await delete_command(ctx)

	output = ""
	for i in itemlisttext:
		output += i + "\n"
		if i == "":
			await ctx.send(output + "_ _")
			output = ""
		
	await ctx.send(output)

@bot.command()	
async def info(ctx):

	await delete_command(ctx)

	output = ""
	for i in infotext:
		output += i + "\n"
		
	await ctx.send(output)
	
@bot.command()	
async def myid(ctx):

	output = ctx.message.author.id
		
	await ctx.send(output)

@bot.command()	
async def cf(ctx):

	await delete_command(ctx)

	coin = ['Heads', 'Tails']

	output = random.choice(coin)
		
	await ctx.send(output)
	
# Allows to change the bot prefix for one server
@bot.command()
async def gbchangeprefix(ctx, arg1):

	if isinstance(ctx.message.channel, discord.abc.GuildChannel):
	
		if arg1 == None:
			output = "You need to chose a prefix."	
			
		else:

			indb = False
			for n in range(len(prefixes)):
				if int(prefixes[n-1][0]) == ctx.message.guild.id:
					indb = True
					del prefixes[n-1]
					break
					
			if indb:
				psqlf.updateprefix(serverinfo, ctx.message.guild.id, arg1)
				
				
			else:
				psqlf.addprefix(serverinfo, ctx.message.guild.id, arg1)
				
				
			prefixes.append((ctx.message.guild.id, arg1))
			output = "prefix changed to \"" + prefix(bot, ctx.message) + "\" for this server."
		
	else:
	
		output = "This hasn't been implemented for private messages. "
		
	await ctx.send(output)
	
# Allows to send me feedback as a private discord message
@bot.command()
async def feedback(ctx, arg1 = None):

	if ctx.message.author.id in feedbackusedtoday:	
		await ctx.send("You have already given feedback today, try again tomorrow.")
		
	else:
		
		if arg1 == None:
			await ctx.send("You need to say something after feedback.")		
		else:
			await bot.get_user(int(idnum)).send(ctx.message.content)
			feedbackusedtoday.append(ctx.message.author.id)
			await ctx.send("Thank you for your feedback")		
		

# Terminates the bot, can only be called by the id in "discordid.txt"
@bot.command()	
async def kill(ctx, arg = 0):


	if ctx.message.author.id == int(idnum):
		await ctx.send("Bot terminated.")
		print("Bot terminated.")
		await bot.logout()
	else:
		await ctx.send("You are not the chosen one.")
		
def my_background_task():
    schedule.run_pending()
    time.sleep(1)
	
async def delete_command(ctx):
	if isinstance(ctx.message.channel, discord.abc.GuildChannel):
		try:
			await ctx.message.delete()
		except discord.Forbidden:
			dum = 0
bot.run(TOKEN)
	
