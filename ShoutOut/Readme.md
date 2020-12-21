# ShoutOut

ShoutOut is a script to add more control to shoutouts. Create a list of streamers you want to enable shoutouts for and add custom messages to fit their streams topic/theme/whatever.

## Installation

Create a zip file containing the ShoutOut folder including all subfiles, or use the zip file provided. Add the zip file in your bot under Scripts->Import. Note: you need to connect your bots aswell as your streaming account to use scripts within the bot.

## Usage

Click on the script in your scripts list. The setting dialogue contains two options to check: the location of your ShoutOut-file and a custom message if someone tries to use the command on an unknown user. Fill in the text fields with your according values and click 'save'.

In twitch chat, simply type !so <username/usermention> to trigger the shoutout.

## ShoutOut-File
The ShoutOut-File has the following structure:

```
<twitch-username>|<custom message>
``` 

For obvious reasons, neither the username nor the message may contain a pipe-symbol |.

An example configuration could look like this:

```
tharealnino|Best streamer in the world, check him out: https://twitch.tv/tharealnino
tharobbynino|Best bot in the world, although you don't need to watch his streams

```

## License
[MIT](https://choosealicense.com/licenses/mit/)