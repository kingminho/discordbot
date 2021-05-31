import hcskr
import discord
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("wakki is alive")

@bot.command()
async def 자가진단(ctx, name, birth, area, school, level, password):
    if name == "도움":
        await ctx.send("!자가진단 이름 생년월일(숫자4개) 지역 학교이름 학교종류(초등학교/중학교/고등학교) 비밀번호")
    else:
        hcskr.selfcheck(name,birth,area,school,level,password)
        await ctx.send("자가진단 참여 완료")


bot.run("ODQyMDU4MzM1OTE4NDg5NjEw.YJvx7w.HgKeOlU7hjNRNAliyA88v44cxvQ")
