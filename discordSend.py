from discordwebhook import Discord
import requests
try:
    with open('Chapter_1.txt', 'r') as file:
        dataFirstFile = file.read().rstrip()
except FileNotFoundError:
    pass
try:
    with open('Chapter_2.txt', 'r') as file:
        dataSecondFile = file.read().rstrip()
except FileNotFoundError:
    pass


try:
    with open('Chapter_3.txt', 'r') as file:
        dataThirdFile = file.read().rstrip()
except FileNotFoundError:
    pass
try:
    with open('Chapter_4.txt', 'r') as file:
        dataForthFile = file.read().rstrip()
except FileNotFoundError:
    pass

try:
    with open('Chapter_5.txt', 'r') as file:
        dataFifthFile = file.read().rstrip()
except FileNotFoundError:
    pass
try:
    with open('Chapter_6.txt', 'r') as file:
        dataSixthFile = file.read().rstrip()
except FileNotFoundError:
    pass
try:
    with open('Chapter_7.txt', 'r') as file:
        dataSeventhFile = file.read().rstrip()
except FileNotFoundError:
    pass

try:
    with open('Chapter_8.txt', 'r') as file:
        dataEgithsFile = file.read().rstrip()
except FileNotFoundError:
    pass


try:
    with open('Chapter_9.txt', 'r') as file:
        dataNinthFile = file.read().rstrip()
except FileNotFoundError:
    pass

try:
    with open('Chapter_10.txt', 'r') as file:
        dataTenthFile = file.read().rstrip()
except FileNotFoundError:
    pass


discord = Discord(url='https://discord.com/api/webhooks/1002749565662924852/YGnW8SZno4rti0ZzrPcP7thz03AgorJN1vzwDDsGvziX0Zcshz_ceoIcxuO_d9TvUYT-')
discord.post(content=dataFirstFile)

discord = Discord(url='https://discord.com/api/webhooks/1002749565662924852/YGnW8SZno4rti0ZzrPcP7thz03AgorJN1vzwDDsGvziX0Zcshz_ceoIcxuO_d9TvUYT-')
discord.post(content=dataSecondFile)