# Howde Networking
## Create discord server
Foster community connections through Discord, facilitating meaningful interactions among disabled individuals.

## How to run 
[Link demo code](https://drive.google.com/drive/u/0/folders/1SAhdXQeGf6mglOQVCIV2e2ipsKXpTYZ5)
### 1. Find the Bot Token 
To regenerate your Discord bot token:
* Go to the Discord Developer Portal.
* Select your application (bot).
* Navigate to the "Bot" tab.
* Under the "TOKEN" section, click on the "Generate Token" button.

### 2.Find the Guild ID 
Enable Developer Mode on Discord:
* Open Discord and go to User Settings (click on the gear icon near your username).
* Go to the "Appearance" section.
* Scroll down to the "Advanced" section and toggle on "Developer Mode." 

Get the Server ID:
* Right-click on your server's icon in the server list.
* Click on "Copy Server ID" from the context menu.

### 3. python create_discord_server.py 
### 4. Invite the bot to your server:
* Go to the Discord Developer Portal.
* Select your application (bot).
* Navigate to the "OAuth2" tab.
* In the "OAuth2 URL Generator" section, select the "bot" scope.
* Under "Bot Permissions," select the permissions your bot needs (e.g., "Read Messages," "Send Messages," and "Manage Channels").
* Copy the generated OAuth2 URL and open it in your browser to invite the bot to your server.
