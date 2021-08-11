# samekan052_bot

## Add bot to your Discord server

- [さめちゃん](https://discord.com/api/oauth2/authorize?client_id=863318641647026196&permissions=0&scope=bot%20applications.commands)
- [かしわさん](https://discord.com/api/oauth2/authorize?client_id=874885744068546591&permissions=0&scope=bot%20applications.commands)
- [ばからす様](https://discord.com/api/oauth2/authorize?client_id=874885825123479602&permissions=0&scope=bot%20applications.commands)

## docker-compose

```yml
version: '3.8'

services:
  samekan052_bot:
    container_name: samekan052_bot
    image: slashnephy/samekan052_bot
    restart: always
    environment:
      TOKEN: YOUR_DISCORD_BOT_TOKEN
```
