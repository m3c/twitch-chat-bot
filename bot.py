import time, socket, random, threading, datetime

oauth = 'oauth:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # bot oauth code
bot = 'bot_username'
channel = 'your_username'
messageCooldown = 5 # in seconds
announcementCooldown = list(range(1700, 2000)) # in seconds
announcements = ['follow me on twitter! https://twitter.com/','subscribe to me on twitch! https://twitch.tv/']

def openSocket():
	s = socket.socket()
	s.connect(('irc.twitch.tv', 6667))
	s.sendall(b'PASS ' + oauth.encode('utf-8') + b'\r\n')
	s.sendall(b'NICK ' + bot.encode('utf-8') + b'\r\n')
	s.sendall(b'JOIN #' + channel.encode('utf-8') + b'\r\n')
	return s

def sendMessage(s, message):
	s.sendall(b'PRIVMSG #' + channel.encode('utf-8') + b' :' + message.encode('utf-8') + b'\r\n')
	print((bot + ': ' + message))

def sendAnnouncement():
  tempAnnouncement = random.choice(announcements)
  threading.Timer(random.choice(announcementCooldown), sendAnnouncement).start()
  s.sendall(b'PRIVMSG #' + channel.encode('utf-8') + b' :' + tempAnnouncement.encode('utf-8') + b'\r\n')
  print((bot + ': ' + tempAnnouncement))

def getUser(line):
	separate = line.split(':', 2)
	user = separate[1].split('!', 1)[0]
	return user

def getMessage(line):
	separate = line.split(':', 2)
	message = separate[2]
	return message

def joinRoom(s):
	readbuffer = ''
	Loading = True
	while Loading:
		readbuffer = readbuffer + s.recv(1024).decode()
		temp = str.split(readbuffer, '\n')
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			Loading = loadingComplete(line)
#   sendMessage(s, '') # optional initial startup message

def loadingComplete(line):
	if('End of /NAMES list' in line):
		return False
	else:
		return True

s = openSocket()
joinRoom(s)
readbuffer = ''

# announcement cooldown

threading.Timer(random.choice(announcementCooldown), sendAnnouncement).start()
delay = datetime.datetime.now()

while True:

	readbuffer = readbuffer + s.recv(1024).decode()
	temp = str.split(readbuffer, '\n')
	readbuffer = temp.pop()

	for line in temp:

		print(line)

		# keeps connection to twitch server

		if 'PING' in line:
			s.sendall(b'PONG\r\n')
			print('PONG\'ed')
			break

		user = getUser(line)
		message = getMessage(line).lower() # translates every message to lowercase letters

		# message cooldown

		if datetime.datetime.now() - delay > datetime.timedelta(seconds=messageCooldown):
			delay = datetime.datetime.now()
			print((user + ': ' + message))

			# commands (make sure all strings in if statements are lowercase)

      if 'hi' in message or 'hello' in message or 'hey' in message or 'wassup' in message:
        sendMessage(s, 'FutureMan hi!')
        break

      if 'food' in message or 'munch' in message or 'hungry' in message:
        sendMessage(s, 'ChefFrank Kappu')
        break

      if 'kappa' in message:
        sendMessage(s, 'Keepo')
        break

      if '!twit' in message:
        sendMessage(s, 'follow me on twitter! https://twitter.com/')
        break
        
      if '!sub' in message:
        sendMessage(s, 'subscribe to me on twitch! https://twitch.tv/')
        break
