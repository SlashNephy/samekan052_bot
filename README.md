# samekan052_bot

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
