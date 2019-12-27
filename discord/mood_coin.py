import asyncio
import discord
import requests
import json


url = "http://localhost:8080"
client = discord.Client()
name = "성범이이"
# 생성된 토큰을 입력해준다.
token = "NjU3MDI1MDY4OTI0MjcyNjUx.Xfrfrg.BMv0UsWn5_EVB-WI97iYWg_ZwJo"

# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    id = message.author.id

    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.author.bot:
        return None

    if message.content.startswith('!안녕'):
        channel = message.channel
        await channel.send('반가워!')

    username = message.author.name
    print(username)
    if name != username:
        if message.content:
            channel = message.channel
            await channel.send(message.content)
            data = {'msg': message.content}
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            r = requests.post(url, data=json.dumps(data), headers=headers) 
client.run(token)
