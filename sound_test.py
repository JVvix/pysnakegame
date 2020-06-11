import winsound

# winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
# print('test')
winsound.PlaySound("./aud_chomp.wav", winsound.SND_ASYNC)
delay = input("press enter to finish")
