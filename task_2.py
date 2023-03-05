# sec = int(input('Enter seconds: '))
# hours = sec // 3600
# minutes = (sec - hours * 3600) // 60
# seconds = sec - hours * 3600 - minutes * 60
# print (f'hours: {hours} minutes: {minutes} seconds: {seconds} ')


sec = int(input('Enter seconds: '))
hours = sec // 3600
hours_and_seconds = hours * 3600
minutes = (sec - hours_and_seconds) // 60
seconds = sec - hours_and_seconds - minutes * 60
print (f'hours: {hours} minutes: {minutes} seconds: {seconds} ')

