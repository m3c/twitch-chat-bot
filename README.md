# Twitch Chat Bot
This is a very simple Twitch.tv chat bot written in Python 3.9! It's perfect to run in the background while you stream, to keep you and your viewers company.

You need Python 3.9 *(tested using Python 3.9.1)* unstalled on your computer. Download Python 3.9 [here](https://www.python.org/downloads/).

The script currently supports commands and timed announcements, each with specified cooldowns.

## Adding announcements 
You can add your own custom, timed announcements. To add an announcement, go to **line 8**, and simply type the announcement into the array of announcements *(where the . . . is)*.
```python
announcements = ['follow me on twitter! https://twitter.com/','...']
```

## Announcement cooldown
You can adjust the time interval between announcements sent. The default is set to send an announcement every 1700 to 2000 seconds. See **line 7**.
```python
announcementCooldown = list(range(1700, 2000)) # in seconds
```

## Adding commands
You can add your own custom commands. To add a command, go to **line 94**, and follow the setup of the default 'hi' command. You can set multiple 'trigger words' to send the same message.
```python
if 'hi' in message or 'hello' in message or 'hey' in message or 'wassup' in message:
	sendMessage(s, 'FutureMan hi!')
	break
```
*Example: the trigger words **hi**, **hello**, **hey**, and **wassap** all send the same message: **FutureMan hi!***

**IMPORTANT:**
Make sure all command trigger words are **lowercase**. The scirpt is setup to translate all in-chat messages to lowercase, so any commands with uppercase letters will not be triggered. If you'd like commands to be case-sensitive, go to **line 84**, and remove *.lower()*.
```python
message = getMessage(line).lower() # translates every message to lowercase letters
```

## Command cooldown
You can adjust the time interval between messages sent. The default is set to only send a command response every 5 seconds. See **line 6**.
```python
messageCooldown = 5 # in seconds
```
