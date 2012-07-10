import urllib2
import json


dict = {
    u'ru': [u'Donbaron', u'Minamur'], 
    u'fr': [u'No public mods online'], 
    u'en': [u'Amavauno', u'Harrytrotter', u'Muitomice', u'Tsjak'], 
    u'cn': [u'No public mods online'], 
    u'vk': [u'No public mods online'], 
    u'tr': [u'No public mods online'], 
    u'br': [u'No public mods online'], 
    u'es': [u'Levols']
}

#RU: Nick1, Nick2 
#:: 
#FR: None 
#:: 
#EN: Amavauno
stringlist = []
req = urllib2.Request('http://anvilgod.com/apis/onlinemods.php')
response = urllib2.urlopen(req)
source = response.read()
data = json.loads(source.decode("ascii", "ignore"))
print data
for k,v in data.items():
    string = ""
    string += k.upper()+": "
    for i in v:
        if i != 'No public mods online':
            string += ', '.join(i for i in v)
            break
        else:
            string += "None"
    stringlist.append(string)
data = ' :: '.join(i for i in stringlist)
print data

def tfm(self, irc, msg, args, target):
    string = ""
    stringlist = []
    if target == "mods":
        try:
            req = urllib2.Request('http://anvilgod.com/apis/onlinemods.php')
            response = urllib2.urlopen(req)
            source = response.read()
            data = json.loads(source.decode("ascii", "ignore"))
        except:
            print irc.reply("YOU SUCK AT ERROR HANDLING AHA2Y!...Now i even have a http fail QQ")
        else:
            for k,v in data.items():
                string += k.upper()+": "
                for i in v:
                    if i != 'No public mods online':
                        string += ', '.join(i for i in v)
                        break
                    else:
                        string += "None"
                stringlist.append(string)
            data = ' :: '.join(i for i in stringlist)
            irc.reply(data)
    tfm = wrap(tfm, ['something'])