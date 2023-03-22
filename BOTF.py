import discord
from discord.ext import commands
from datetime import datetime
import datetime
from datetime import date
import os
import time





intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
intents.message_content = True
intents.members = True
intents.presences = True
intents.members = True

def starttime():
    p = open("dane/stime.txt", mode='a')
    h = round((time.time()))
    h = str(h)
    p.write(h + "\n")
    p.close()

def stoptime():
    s = open("dane/endtime.txt", mode='a')
    j = round(time.time())
    j = str(j)
    s.write(j + "\n")
    s.close()

def czasuz():
    ep = 0
    n = 0
    f = open("dane/stime.txt", 'r')
    numss = f.readlines()
    numss = [int(i) for i in numss]
    f.close()
    e = open("dane/endtime.txt", 'r')
    numse = e.readlines()
    numse = [int(i) for i in numse]
    e.close()
    ep = [numse[i] - numss[i] for i in range(min(len(numse), len(numss)))]
    n = sum(ep)
    return n
def wlacz():
    with open("dane/wl.txt") as d:
        wlp = d.readlines()
    for k in wlp:
        k = int(k)
        if k == 1:
            return 1
        else:
            return 0

def data():
    today = date.today()
    today = str(today)
    return today
def godz():
    teraz = datetime.datetime.now()
    godzina = teraz.strftime("%H:%M:%S")
    return(godzina)

f = open("log.txt", mode='a')
f.write("-----!?!?! Rozpoczeto wlaczanie" + " " + godz() + " " + data() + "\n" + "\n" + "\n")
f.close()

if wlacz() == 1:
    time.sleep(600)
    f = open("log.txt", mode='a')
    #os.write("ssh root@192.168.1.106 'shutdown now'")
    f.write("!!! serwer nie został wcześniej wyłączony" + " " + data() + " " + godz() + "\n")
    f.close()

# Proces włączanie akcjie wykonywane raz#
p = open("dane/wl.txt", mode='w')
p.write("0")
p.close()
open('dane/stime.txt', 'w').close()
open('dane/endtime.txt', 'w').close()

@bot.command()
async def lps(ctx):
    await ctx.send('+1')

@bot.command()
async def wls(ctx):
    f = open("log.txt", mode='a')
    user = ctx.author
    guild = ctx.guild
    member = guild.get_member(user.id)
    member = str(member)
    if czasuz() < 14400:
        if wlacz() == 0:
            starttime()
            print(godz(), "wywołano włączenie", member)
            await ctx.send("Serwer Włączony Godzina:")
            await ctx.send(godz())
            #os.write("wakeonlan A0:B3:CC:EE:16:34")
            f.write(data() + ": " + godz() + " " + "Wywalono wlaczenie przez" + " " + member + "\n")
            p = open("dane/wl.txt", mode='w')
            p.write("1")
            p.close()

        else:
            await ctx.send("Serwer jest już włączony")
            f.write("BLAD:serwer jest juz wlaczony" + " (" + data() + ": " + godz() + " " + "Wywalono wlaczenie przez" + " " + member + ")" "\n")
        f.close()
    else:
        await ctx.send("Serwer przekroczył swój dzienny limit proszę wrócić jutro")
        f.write("BLAD:serwer jest juz wlaczony" + " (" + data() + ": " + godz() + " " + "Wywalono wlaczenie przez" + " " + member + ")" "\n")

@bot.command()
async def wys(ctx):
    f = open("log.txt", mode='a')
    user = ctx.author
    guild = ctx.guild
    member = guild.get_member(user.id)
    member = str(member)
    if wlacz() == 1:
        p = open("dane/wl.txt", mode='w')
        p.write("0")
        stoptime()
        print(godz(), "wywołano wyłączenie" , member)
        await ctx.send("Serwer Wyłączony Godzina:")
        await ctx.send(godz())
        #os.write("ssh root@192.168.1.106 'shutdown now'")
        f.write(data() + ": " + godz()+" " + "Wywalano wylaczenie przez"+" " + member+"\n")
        p.close()
    else:
        await ctx.send("Serwer nie został wczesniej włączony")
        f.write("BLAD:serwer nie zostal wczescniej wlaczony" + " (" + data() + ": " + godz() + " " + "Wywalono wlaczenie przez" + " " + member + ")" "\n")
    f.close()

@bot.command()
async def ss(ctx):
    if wlacz() == 1:
        await ctx.send("Serwer jest włączony")
    else:
        await ctx.send("Serwer jest wyłączony")

@bot.command()
async def infos(ctx):
    mn = 0
    lk = "s"
    p = 14400 - czasuz()
    if p >= 60:
        p = p/60
        mn += 1
        if p >= 60:
            p = p/60
            mn += 1
    if mn == 1:
        lk = "min"
    if mn == 2:
        lk = "h"
    p = round(p,2)
    p = str(p)
    await ctx.send("Zostało" + " " + p + lk + " " + "dzisiejszego limitu")

@bot.command()
async def helps(ctx):
    await ctx.send("!ss- serwer status, !infos - info dzienny limit, !wys - wyłączanie serwera, !wls - włączanie serwera, !lps - sprawdzenie czy bot działa")
bot.run("MTA3OTQ5MTg5MTU4Mzc4MzA0Mg.G569If.clNZ8qBrbwS-iWltMl_6YmQOFngelCzwe2akz0")