# -*- coding: utf-8 -*-
'''
© 2018SelfBot ProtectV2.2
'''
from important import *
# Setup Argparse
parser = argparse.ArgumentParser(description='© 2018SelfBot ProtectV2.2')
parser.add_argument('-t', '--token', type=str, metavar='', required=False, help='Token | Example : Exxxx')
parser.add_argument('-e', '--email', type=str, default='', metavar='', required=False, help='Email Address | Example : example@xxx.xx')
parser.add_argument('-p', '--passwd', type=str, default='', metavar='', required=False, help='Password | Example : xxxx')
parser.add_argument('-a', '--appName', type=str, default='', metavar='', required=False, choices=list(ApplicationType._NAMES_TO_VALUES), help='Application Type | Example : CHROMEOS')
parser.add_argument('-s', '--systemname', type=str, default='', metavar='', required=False, help='System Name | Example : Chrome_OS')
parser.add_argument('-c', '--channelid', type=str, default='', metavar='', required=False, help='Channel ID | Example : 1341209950')
parser.add_argument('-T', '--traceback', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Using Traceback | Use : True/False')
parser.add_argument('-S', '--showqr', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Show QR | Use : True/False')
args = parser.parse_args()

# Login line
start_runtime = datetime.now()    
line = LINE("",appType="CHROMEOS")
kicker = LINE("nirassalatan1@gmail.com","what4130")
print ("===============[PRO 1 LOGIN NOSELF TOKEN]===============\n")
kicker2 = LINE("nirassalatan2@gmail.com","what4130")
print ("===============[PRO 2 LOGIN SUKSES]===============\n")
kicker3 = LINE("nirassalatan3@gmail.com","what4130")
print ("===============[PRO 3 LOGIN SUKSES]===============\n")
kicker4 = LINE("nirassalatan4@gmail.com","what4130")
print ("===============[PRO 4 LOGIN SUKSES]===============\n")
kicker5 = LINE("nirassalatan5@gmail.com","what4130")
print ("===============[PRO 5 LOGIN SUKSES]===============\n")
kicker6 = LINE("nirassalatan6@gmail.com","what4130")
print ("===============[PRO 6 LOGIN NOSELF TOKEN]===============\n")
kicker7 = LINE("nirassalatan7@gmail.com","what4130")
print ("===============[PRO 7 LOGIN SUKSES]===============\n")
kicker8 = LINE("nirassalatan8@gmail.com","what4130")
print ("===============[PRO 8 LOGIN SUKSES]===============\n")
kicker9 = LINE("nirassalatan9@gmail.com","what4130")
print ("===============[PRO 9 LOGIN SUKSES]===============\n")
kicker10 = LINE("nirassalatan10@gmail.com","what4130")
print ("===============[PRO 10 LOGIN SUKSES]===============\n")
kicker11 = LINE("zabakuno1@gmail.com","what4130")
print ("===============[PRO 11 LOGIN SUKSES]===============\n")
kicker12 = LINE("zabakuno2@gmail.com","what4130")
print ("===============[PRO 12 LOGIN SUKSES]===============\n")
kicker13 = LINE("zabakuno3@gmail.com","what4130")
print ("===============[PRO 13 LOGIN SUKSES]===============\n")
kicker14 = LINE("zabakuno4@gmail.com","what4130")
print ("===============[PRO 14 LOGIN SUKSES]===============\n")
kicker15 = LINE("zabakuno5@gmail.com","what4130")
print ("===============[PRO 15 LOGIN SUKSES]===============\n")
kicker16 = LINE("zabakuno6@gmail.com","what4130")
print ("===============[PRO 16 LOGIN SUKSES]===============\n")
kicker17 = LINE("zabakuno7@gmail.com","what4130")
print ("===============[PRO 17 LOGIN SUKSES]===============\n")
kicker18 = LINE("zabakuno8@gmail.com","what4130")
print ("===============[PRO 18 LOGIN SUKSES]===============\n")
kicker19 = LINE("zabakuno9@gmail.com","what4130")
print ("===============[PRO 19 LOGIN SUKSES]===============\n")
kicker20 = LINE("zabakuno10@gmail.com","what4130")
print ("===============[PRO 20 LOGIN SUKSES]===============\n")
g1 = LINE("dtxlcdi@it-simple.net","gaara4130")
print ("===============[PRO Ghost LOGIN SUKSES]===============\n")
client = line
myMid = line.profile.mid
creator = ["u384b0bc30e28b9e7c38b9ad82a8ab9ce"]
owner = ["u384b0bc30e28b9e7c38b9ad82a8ab9ce"]
admin = ["u384b0bc30e28b9e7c38b9ad82a8ab9ce"]
staff = ["u384b0bc30e28b9e7c38b9ad82a8ab9ce"]
Amid = kicker.getProfile().mid
Bmid = kicker2.getProfile().mid
Cmid = kicker3.getProfile().mid
Dmid = kicker4.getProfile().mid
Emid = kicker5.getProfile().mid
Fmid = kicker6.getProfile().mid
Gmid = kicker7.getProfile().mid
Hmid = kicker8.getProfile().mid
Imid = kicker9.getProfile().mid
Jmid = kicker10.getProfile().mid
ga1 = kicker11.getProfile().mid
ga2 = kicker12.getProfile().mid
ga3 = kicker13.getProfile().mid
ga4 = kicker14.getProfile().mid
ga5 = kicker15.getProfile().mid
ga6 = kicker16.getProfile().mid
ga7 = kicker17.getProfile().mid
ga8 = kicker18.getProfile().mid
ga9 = kicker19.getProfile().mid
ga10 = kicker20.getProfile().mid
g1MID = g1.getProfile().mid
KAC = [kicker,kicker2,kicker3,kicker3,kicker5,kicker6,kicker7,kicker8,kicker9,kicker10,kicker11,kicker12,kicker13,kicker14,kicker15,kicker16,kicker17,kicker18,kicker19,kicker20]
ABC = [kicker,kicker2,kicker3,kicker3,kicker5,kicker6,kicker7,kicker8,kicker9,kicker10,kicker11,kicker12,kicker13,kicker14,kicker15,kicker16,kicker17,kicker18,kicker19,kicker20]
Bots = [myMid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,ga1,ga2,ga3,ga4,ga5,ga6,ga7,ga8,ga9,ga10,g1MID]
#Autoadd
armylist = [myMid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,ga1,ga2,ga3,ga4,ga5,ga6,ga7,ga8,ga9,ga10,g1MID]
botlist = [line,kicker,kicker2,kicker3,kicker3,kicker5,kicker6,kicker7,kicker8,kicker9,kicker10,kicker11,kicker12,kicker13,kicker14,kicker15,kicker16,kicker17,kicker18,kicker19,kicker20,g1MID]
#Autoadd
Ariff = creator + admin + owner + staff + Bots
programStart = time.time()
oepoll = OEPoll(line)
tmp_text = []
lurking = {}
protectqr = []
protectkick = []
protecARoin = []
protectinvite = []
protectcancel = []
protectcanceljs = []
protectantijs = []
ghost = []
numlist= {}
zxcvzx = myMid
with open('protectcancel.json', 'r') as fp:
    protectcancel = json.load(fp)
with open('protectcanceljs.json', 'r') as fp:
    protectcanceljs = json.load(fp)    
with open('protectantijs.json', 'r') as fp:
    protectantijs = json.load(fp)
with open('ghost.json', 'r') as fp:
    ghost = json.load(fp)
with open('protectinvite.json', 'r') as fp:
    protectinvite = json.load(fp)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)

settings = livejson.File('setting.json', True, False, 4)

numlist= {}


bool_dict = {
    True: ['Yes', 'Active', 'Success', 'Open', 'On'],
    False: ['No', 'Not Active', 'Failed', 'Close', 'Off']
}



responsename1 = kicker.getProfile().displayName
responsename2 = kicker2.getProfile().displayName
responsename3 = kicker3.getProfile().displayName
responsename4 = kicker4.getProfile().displayName
responsename5 = kicker5.getProfile().displayName
responsename6 = kicker6.getProfile().displayName
responsename7 = kicker7.getProfile().displayName
responsename8 = kicker8.getProfile().displayName
responsename9 = kicker9.getProfile().displayName
responsename10 = kicker10.getProfile().displayName
responsename11 = kicker11.getProfile().displayName
responsename12 = kicker12.getProfile().displayName
responsename13 = kicker13.getProfile().displayName
responsename14 = kicker14.getProfile().displayName
responsename15 = kicker15.getProfile().displayName
responsename16 = kicker16.getProfile().displayName
responsename17 = kicker17.getProfile().displayName
responsename18 = kicker18.getProfile().displayName
responsename19 = kicker19.getProfile().displayName
responsename20 = kicker20.getProfile().displayName

# Backup profile
profile = line.getContact(myMid)
settings["myProfile"]["displayName"] = profile.displayName
settings["myProfile"]["statusMessage"] = profile.statusMessage
settings["myProfile"]["pictureStatus"] = profile.pictureStatus
cont = line.getContact(myMid)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = line.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

def sendflex(to, data):
    n1 = LiffChatContext(to)
    n2 = LiffContext(chat=n1)
    view = LiffViewRequest('1602687308-GXq4Vvk9', n2)
    token = line.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
# Check Json Data
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
def restartProgram():
    print ('##----- PROGRAM RESTARTED -----##')
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(error, write=True):
    errid = str(random.randint(100, 999))
    filee = open('tmp/errors/%s.txt'%errid, 'w') if write else None
    if args.traceback: traceback.print_tb(error.__traceback__)
    if write:
        traceback.print_tb(error.__traceback__, file=filee)
        filee.close()
        with open('errorLog.txt', 'a') as e:
            e.write('\n%s : %s'%(errid, str(error)))
    print ('++ Error : {error}'.format(error=error))       
def command(text):
    pesan = text.lower()
    if settings['setKey']['status']:
        if pesan.startswith(settings['setKey']['key']):
            cmd = pesan.replace(settings['setKey']['key'],'')
        else:
            cmd = 'Undefined command'
    else:
        cmd = text.lower()
    return cmd

def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = line.genOBSParams({'oid': myMid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = line.server.postContent('{}/talk/vp/upload.nhn'.format(str(line.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        line.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

def genImageB64(path):
    with open(path, 'rb') as img_file:
        encode_str = img_file.read()
        b64img = base64.b64encode(encode_str)
        return b64img.decode('utf-8')

def genUrlB64(url):
    return base64.b64encode(url.encode('utf-8')).decode('utf-8')

def removeCmd(text, key=''):
    if key == '':
        setKey = '' if not settings['setKey']['status'] else settings['setKey']['key']
    else:
        setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(' ')
    return text_[len(sep[0] + ' '):]

def multiCommand(cmd, list_cmd=[]):
    if True in [cmd.startswith(c) for c in list_cmd]:
        return True
    else:
        return False

def replaceAll(text, dic):
    try:
        rep_this = dic.items()
    except:
        rep_this = dic.iteritems()
    for i, j in rep_this:
        text = text.replace(i, j)
    return text

def help():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help.txt', 'r') as f:
        text = f.read()
    helpMsg = text.format(key=key.title())
    return helpMsg

def helpbot():
    with open('helpbot.txt', 'r') as f:
        text = f.read()
    helpMsg1 = text.format()
    return helpMsg1
def parsingRes(res):
    result = ''
    textt = res.split('\n')
    for text in textt:
        if True not in [text.startswith(s) for s in ['╭', '├', '│', '╰']]:
            result += '\n│ ' + text
        else:
            if text == textt[0]:
                result += text
            else:
                result += '\n' + text
    return result

def sendMentionxd(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def Musik(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+line.getContact(myMid).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': line.getContact(myMid).statusMessage if line.getContact(myMid).statusMessage != '' else 'creator By rat |ID LINE|\njamekillover', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': line.getContact(myMid).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+myMid,'MSG_SENDER_NAME':  line.getContact(myMid).displayName,}
    return line.sendMessage(to, line.getContact(myMid).displayName, contentMetadata, 19)
            
def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention2(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker2.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker2.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention3(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker3.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker3.sendMessage(to, "[ INFO ] Error :\n" + str(error))
 
def sendMention4(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker4.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker4.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention5(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker5.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker5.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention6(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker6.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker6.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention7(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker7.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker7.sendMessage(to, "[ INFO ] Error :\n" + str(error))
 
def sendMention8(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker8.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker8.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention9(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker9.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker9.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention10(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker10.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker10.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention11(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker11.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker11.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention12(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker12.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker12.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention13(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker13.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker13.sendMessage(to, "[ INFO ] Error :\n" + str(error))
 
def sendMention14(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker14.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker14.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention15(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker15.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker15.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention16(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker16.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker16.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention17(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker17.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker17.sendMessage(to, "[ INFO ] Error :\n" + str(error))
 
def sendMention18(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker18.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker18.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention19(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker19.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker19.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention20(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kicker20.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kicker20.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def cloneProfile(myMid):
    contact = line.getContact(myMid)
    if contact.videoProfile == None:
        line.cloneContactProfilev2(myMid)
    else:
        profile = line.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        line.updateProfile(profile)
        pict = line.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = line.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = line.getProfileDetail(myMid)['result']['objectId']
    line.updateProfileCoverById(coverId)

def backupProfile():
    profile = line.getContact(myMid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = line.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)

def sendTemplate(to, data):
    line = LiffChatContext(to)
    ratedit = LiffContext(chat=line)
    view = LiffViewRequest('1602687308-GXq4Vvk9', ratedit)
    token = line.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    	
def restoreProfile():
    profile = line.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = line.downloadFileURL("http://dl.profile.line-cdn.net/{}".format(settings["myProfile"]["pictureStatus"]), saveAs="tmp/backupPicture.bin")
        line.updateProfilePicture(profile.pictureStatus)
        line.updateProfile(profile)
    else:
        line.updateProfile(profile)
        pict = line.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = line.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    line.updateProfileCoverById(coverId)
def time_converter(time):
    converted_time = datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time

def url_builder(city_id):
    user_api = '6975b23cef6c84e7f26062ef1c913c0d'  # Obtain yours form: http://openweathermap.org/
    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    api = 'http://api.openweathermap.org/data/2.5/weather?id='     # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz
    full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url


def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict


def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
        sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
        wind=raw_api_dict.get('wind').get('speed'),
        wind_deg=raw_api_dict.get('deg'),
        dt=time_converter(raw_api_dict.get('dt')),
        cloudiness=raw_api_dict.get('clouds').get('all')
    )
    return data

def data_output(to,data,prov):
    m_symbol = ' °C'
    if prov == 1:
        line.sendMessage(to,"สภาพอากาศ: เชียงใหม่\nอุณหภูมิ: "+str(data['temp'])+m_symbol+"\n(มากสุด: "+str(data['temp_max'])+m_symbol+", น้อยสุด: "+str(data['temp_max'])+m_symbol+")\n\nแรงลม: "+str(data['wind'])+"\nความชื้น: "+str(data['humidity'])+"\nเมฆ: "+str(data['cloudiness'])+"%\nความดัน: "+str(data['pressure'])+"\nดวงอาทิตย์ขึ้น: "+str(data['sunrise'])+"\nดวงอาทิตย์ตก: "+str(data['sunset'])+"\n\nอัพเดทล่าสุด: "+str(data['dt']))
    elif prov == 2:
        line.sendMessage(to,"สภาพอากาศ: อุบลราชธานี\nอุณหภูมิ: "+str(data['temp'])+m_symbol+"\n(มากสุด: "+str(data['temp_max'])+m_symbol+", น้อยสุด: "+str(data['temp_max'])+m_symbol+")\n\nแรงลม: "+str(data['wind'])+"\nความชื้น: "+str(data['humidity'])+"\nเมฆ: "+str(data['cloudiness'])+"%\nความดัน: "+str(data['pressure'])+"\nดวงอาทิตย์ขึ้น: "+str(data['sunrise'])+"\nดวงอาทิตย์ตก: "+str(data['sunset'])+"\n\nอัพเดทล่าสุด: "+str(data['dt']))
    elif prov == 3:
        line.sendMessage(to,"สภาพอากาศ: กรุงเทพมหานคร\nอุณหภูมิ: "+str(data['temp'])+m_symbol+"\n(มากสุด: "+str(data['temp_max'])+m_symbol+", น้อยสุด: "+str(data['temp_max'])+m_symbol+")\n\nแรงลม: "+str(data['wind'])+"\nความชื้น: "+str(data['humidity'])+"\nเมฆ: "+str(data['cloudiness'])+"%\nความดัน: "+str(data['pressure'])+"\nดวงอาทิตย์ขึ้น: "+str(data['sunrise'])+"\nดวงอาทิตย์ตก: "+str(data['sunset'])+"\n\nอัพเดทล่าสุด: "+str(data['dt']))
    elif prov == 4:
        line.sendMessage(to,"สภาพอากาศ: เพชรบูรณ์\nอุณหภูมิ: "+str(data['temp'])+m_symbol+"\n(มากสุด: "+str(data['temp_max'])+m_symbol+", น้อยสุด: "+str(data['temp_max'])+m_symbol+")\n\nแรงลม: "+str(data['wind'])+"\nความชื้น: "+str(data['humidity'])+"\nเมฆ: "+str(data['cloudiness'])+"%\nความดัน: "+str(data['pressure'])+"\nดวงอาทิตย์ขึ้น: "+str(data['sunrise'])+"\nดวงอาทิตย์ตก: "+str(data['sunset'])+"\n\nอัพเดทล่าสุด: "+str(data['dt']))
    elif prov == 5:
        line.sendMessage(to,"สภาพอากาศ: ขอนแก่น\nอุณหภูมิ: "+str(data['temp'])+m_symbol+"\n(มากสุด: "+str(data['temp_max'])+m_symbol+", น้อยสุด: "+str(data['temp_max'])+m_symbol+")\n\nแรงลม: "+str(data['wind'])+"\nความชื้น: "+str(data['humidity'])+"\nเมฆ: "+str(data['cloudiness'])+"%\nความดัน: "+str(data['pressure'])+"\nดวงอาทิตย์ขึ้น: "+str(data['sunrise'])+"\nดวงอาทิตย์ตก: "+str(data['sunset'])+"\n\nอัพเดทล่าสุด: "+str(data['dt']))
    elif prov == 6:
        line.sendMessage(to,"สภาพอากาศ: อยุธยา\nอุณหภูมิ: "+str(data['temp'])+m_symbol+"\n(มากสุด: "+str(data['temp_max'])+m_symbol+", น้อยสุด: "+str(data['temp_max'])+m_symbol+")\n\nแรงลม: "+str(data['wind'])+"\nความชื้น: "+str(data['humidity'])+"\nเมฆ: "+str(data['cloudiness'])+"%\nความดัน: "+str(data['pressure'])+"\nดวงอาทิตย์ขึ้น: "+str(data['sunrise'])+"\nดวงอาทิตย์ตก: "+str(data['sunset'])+"\n\nอัพเดทล่าสุด: "+str(data['dt']))

def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    if cmd == 'logoutbot':
        line.sendMessage(to, 'Bot will logged out')
        sys.exit('##----- PROGRAM STOPPED -----##')
    elif cmd == 'logoutdevicee':
        line.sendMessage(to, 'Bot will logged outdevicee')        
        line.logout()
        sys.exit('##----- line LOGOUT -----##')
    elif cmd == 'รีบอท':
        line.sendMessage(to, 'กำลังรี😘♪')
        restartProgram()
    elif cmd == 'help':
        line.sendReplyMessage(msg_id,to,help(),{'AGENT_LINK': 'line://ti/p/~jamekillover','AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(myMid).pictureStatus,'AGENT_NAME': 'รัตน์'})
    elif text.lower() == 'resetlogin':
        os.system('clear')
        line.sendReplyMessage(msg_id,to," 「 Reset Login 」\nType: Reset Login\nระบบกำลังประมวลผล...",{'AGENT_LINK': 'line://ti/p/~jamekillover','AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(myMid).pictureStatus,'AGENT_NAME': 'รัตน์'})
        python = sys.executable
        os.execl(python, python, * sys.argv)                
    elif cmd == 'helpbot':
        kicker.sendReplyMessage(msg_id, to, helpbot(),contentMetadata={"MSG_SENDER_NAME":"188c17d367a9455e4b60f809f280003d867d4df7188c17d367a9455e7d4df7188c17d367a9455e188c17d367a9455e4b60f809f280003d867d4df7188c17d367a9455e7d4df7188c17d367a9455e5ee8776c4c58a0367a9455e4b60f80358c204u21d04f683a70e","MSG_SENDER_ICON":"https://media.giphy.com/media/T9qJa0lfRjXsQ/source.gif"})
    elif cmd == 'speed':
        start = time.time()
        sendMentionxd(msg.to, sender, "「ความเร็วของคุณคือ...」 ", "")
        elapsed_time = time.time() - start
        line.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
    elif text.lower() == 'myspeed':
        time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=1000)
        str1 = str(time0)
        start = time.time()
        line.sendMessage(to,'ความเร็วในการประมวลผล\n' + str1 + 'วินาที')
        elapsed_time = time.time() - start
        line.sendMessage(to,'การตอบสนองต่อคำสั่ง\n' + format(str(elapsed_time)) + 'วินาที')        
    elif cmd == 'me':
        key1 = myMid
        line.sendReplyMessage(msg_id, to, None, contentMetadata={"MSG_SENDER_NAME":"188c17d367a9455e4b60f809f280003d867d4df","MSG_SENDER_ICON":"https://media.giphy.com/media/T9qJa0lfRjXsQ/source.gif",'mid': key1}, contentType=13)
    elif cmd == "me2":
        line.sendReplyMessage(msg_id,to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'https://media.giphy.com/media/T9qJa0lfRjXsQ/source.gif', 'i-installUrl': 'line://app/1602687308-GXq4Vvk9?type=profile', 'type': 'mt', 'subText': "", 'a-installUrl': 'line://app/1602687308-GXq4Vvk9?type=profile', 'a-installUrl': ' line://app/1602687308-GXq4Vvk9?type=profile', 'a-packageName': 'line://app/1602687308-GXq4Vvk9?type=profile', 'countryCode': 'line://app/1602687308-GXq4Vvk9?type=profileID', 'a-linkUri': 'line://app/1602687308-GXq4Vvk9?type=profile', 'i-linkUri': 'line://app/1602687308-GXq4Vvk9?type=profile', 'id': 'line://app/1602687308-GXq4Vvk9?type=profile', 'text': 'รัตน์ไง', 'linkUri': 'line://app/1602687308-GXq4Vvk9?type=profile'}, contentType=19)
    elif cmd == 'ออน':
        runtime = time.time() - programStart
        line.sendMessage(to,format_timespan(runtime))
    elif cmd == 'author':
        line.sendMessage(to, 'Author is linepy')
    elif cmd == 'me3':
        line.sendReplyMessage(msg_id, to,"Fn",contentMetadata={'vCard': 'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:ANDROID 8.13.3 Android OS 4.4.4\r\nFN:\\'+line.getContact(sender).displayName+'\nTEL;TYPE=mobile:'+line.getContact(sender).statusMessage+'\r\nN:?;\\,\r\nEND:VCARD\r\n', 'displayName': line.getContact(sender).displayName},contentType=13)
    elif cmd == 'about':
        try:
            arr = []
            owner = "ucccca2ada2b522c6d59e6640f29aafd0"
            creator = line.getContact(owner)
            contact = line.getContact(myMid)
            grouplist = line.getGroupIdsJoined()
            contactlist = line.getAllContactIds()
            blockedlist = line.getBlockedContactIds()
            ret_ = "____________________________\n❨✪❩ Impormation Selfbot ❨✪❩\n____________________________"
            ret_ += "\n┃❨✪❩ Line Name : {}".format(contact.displayName)
            ret_ += "\n┃❨✪❩ Groups : {}".format(str(len(grouplist)))
            ret_ += "\n┃❨✪❩ Friends : {}".format(str(len(contactlist)))
            ret_ += "\n┃❨✪❩ Blocked : {}".format(str(len(blockedlist)))
            ret_ += "\n┃❨✪❩ Version1 : Python3 Update"
            ret_ += "\n┃❨✪❩ Version2 : Premium server"
            ret_ += "\n┃❨✪❩ Server : Ubuntu 18.04.1 LTS (GNU/Linux 4.15.0-33-generic x86_64)"
            ret_ += "\n┃❨✪❩ Edit : 14-11-2018"
            ret_ += "\n┃❨✪❩ Creator : {}".format(creator.displayName)
            ret_ += "\n____________________________"
            line.sendMessage(to, str(ret_))
        except Exception as e:
            line.sendMessage(msg.to, str(e))        
    elif cmd == 'status':
        res = '╭───「 Status 」'
        res += '\n├ Auto Add : ' + bool_dict[settings['autoAdd']['status']][1]
        res += '\n├ Auto Join : ' + bool_dict[settings['autoJoin']['status']][1]
        res += '\n├ Auto Respond : ' + bool_dict[settings['autoRespond']['status']][1]
        res += '\n├ Auto Respond Mention : ' + bool_dict[settings['autoRespondMention']['status']][1]
        res += '\n├ Auto Read : ' + bool_dict[settings['autoRead']][1]
        res += '\n├ Setting Key : ' + bool_dict[settings['setKey']['status']][1]
        res += '\n├ Mimic : ' + bool_dict[settings['mimic']['status']][1]
        res += '\n├ Greetings Join : ' + bool_dict[settings['greet']['join']['status']][1]
        res += '\n├ Greetings Leave : ' + bool_dict[settings['greet']['leave']['status']][1]
        res += '\n├ Check Contact : ' + bool_dict[settings['checkContact']][1]
        res += '\n├ Check Post : ' + bool_dict[settings['checkPost']][1]
        res += '\n├ Check Sticker : ' + bool_dict[settings['checkSticker']][1]
        res += '\n╰───「SelfBot ProtectV2.2」'
        line.sendMessage(to, parsingRes(res))
    elif cmd == 'abort':
        aborted = False
        if to in settings['changeGroupPicture']:
            settings['changeGroupPicture'].remove(to)
            line.sendMessage(to, 'ยกเลิกเปลี่ยนรูปภาพกลุ่มเรียบร้อย')
            aborted = True
        if settings['changePictureProfile']:
            settings['changePictureProfile'] = False
            line.sendMessage(to, 'ยกเลิกเปลี่ยนรูปภาพโปรไฟล์เรียบร้อย')
            aborted = True
        if settings['changeCoverProfile']:
            settings['changeCoverProfile'] = False
            line.sendMessage(to, 'ยกเลิกเปลี่ยนรูปปกเรียบร้อย')
            aborted = True
        if not aborted:
            line.sendMessage(to, 'ไม่สามารถยกเลิกได้\nไม่มีอะไรไห้ยกเลิก')
    elif cmd.startswith("midcopy "):
        target = removeCmd("midcopy", text)
        if target is not None:
            cloneProfile(target)
            line.sendContact(to,myMid)
            line.sendMessage(to,"คัดลอกบัญชีเรียบร้อยแล้ว")								
    elif cmd.startswith("copy "):
        if sender in myMid:
            if 'MENTION' in msg.contentMetadata.keys()!= None:
                names = re.findall(r'@(\w+)', text)
                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                mentionees = mention['MENTIONEES']
                lists = []
                for mention in mentionees:
                    if mention["M"] not in lists:
                        lists.append(mention["M"])
                if len(lists) != []:
                    ls = random.choice(lists)
                    cloneProfile(ls)
                    line.sendMessage(to,"คัดลอกบัญชีเรียบร้อยแล้ว")										
    elif cmd == "load":
        if sender in myMid:
            try:
                restoreProfile()
                line.sendMessage(to, "เรียกคืนสถานะบัญชีสำเร็จโปรดรอสักครู่จนกว่าโปรไฟล์จะเปลี่ยน")
            except Exception as e:
                line.sendMessage(to, "ไม่สามารถเรียกคืนสถานะบัญชีได้")
                line.sendMessage(msg.to, str(e))
    elif cmd == "save":
        if sender in myMid:
            try:
                backupProfile()
                line.sendMessage(to, "บันทึกสถานะบัญชีเรียบร้อยแล้ว")
            except Exception as e:
                line.sendMessage(to, "ไม่สามารถบันทึกสถานะบัญชีได้")
                line.sendMessage(msg.to, str(e))

    elif cmd == 'speed2':
        start = time.time()
        sendMentionxd(msg.to, sender, "「Your Test Speed Bot」 ", "")
        elapse = time.time() - start
        line.sendMessage(to, ' %s seconds' % str(elapse),{'AGENT_ICON': 'https://i.imgur.com/GSE9LLM.gif','AGENT_NAME': 'รัตน์','AGENT_LINK': 'line://app/1608998163-Xxzr1PmV'})
        
    elif cmd == 'infome':
        arr = []
        mention = "@x\n"
        text = msg.text[len("infome"):].strip()
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':myMid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,7,25)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = line.getAllContactIds()
        gid = line.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)    
        h = line.getContact(myMid)                 
        line.reissueUserTicket()
        My_Id = line.profile.displayName + "\nMy id Line: http://line.me/ti/p/" + line.getUserTicket().id
        text += mention+"TIME : "+datetime.strftime(timeNow,'%H:%M:%S')+" Thailand\nMy Group : "+str(len(gid))+"\nMy Friend: "+str(len(teman))+"\nMy Mid : "+h.mid+"\nMy Name : "+My_Id
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

    elif text.lower() == 'เปลี่ยนวีดีโอ':
      if wait["selfbot"] == True:		
        if msg._from in admin:						  
            line.sendMessage(to, "กรุณารอ20-30นาที")							
            picture = line.downloadFileURL("https://i.imgur.com/83Z5C2f.png", saveAs="image.png")
            video = line.downloadFileURL("https://www.saveoffline.com/get/?i=eAQRQWRnY9Rs3RTdn3jZUV6sNVQkzqsJ&u=qQaKnkcoKrbhu8sr0CiqKlFxpiiOvHUX", saveAs="video.mp4")
            changeVideoAndPictureProfile(picture, video)
            line.sendMessage(to, "เปลี่ยนเรียบร้อย")
    elif cmd == 'test':
        line.sendTextWithFooter(to, "Footer message", footerIconURL="https://os.line.naver.jp/os/p/" + line.profile.mid, footerText="Footer", footerURL="https://line.me/ti/p/wprfnIo55O")
        line.sendMessage(to, 'Your Test',{'AGENT_LINK': 'line://app/1608998163-Xxzr1PmV','AGENT_ICON': 'https://i.imgur.com/GSE9LLM.gif','AGENT_NAME': 'รัตน์'})               

    elif cmd == "เชคบอท":
      if wait["selfbot"] == True:
        if msg._from in admin:            
            sendMention1(msg.to, sender, "「Ready」 ", "")
            sendMention2(msg.to, sender, "「Ready」 ", "")
            sendMention3(msg.to, sender, "「Ready」 ", "")
            sendMention4(msg.to, sender, "「Ready」 ", "")
            sendMention5(msg.to, sender, "「Ready」 ", "")
            sendMention6(msg.to, sender, "「Ready」 ", "")
            sendMention7(msg.to, sender, "「Ready」 ", "")
            sendMention8(msg.to, sender, "「Ready」 ", "")
            sendMention9(msg.to, sender, "「Ready」 ", "")
            sendMention10(msg.to, sender, "「Ready」 ", "")
            sendMention11(msg.to, sender, "「Ready」 ", "")
            sendMention12(msg.to, sender, "「Ready」 ", "")
            sendMention13(msg.to, sender, "「Ready」 ", "")
            sendMention14(msg.to, sender, "「Ready」 ", "")
            sendMention15(msg.to, sender, "「Ready」 ", "")
            sendMention16(msg.to, sender, "「Ready」 ", "")
            sendMention17(msg.to, sender, "「Ready」 ", "")
            sendMention18(msg.to, sender, "「Ready」 ", "")
            sendMention19(msg.to, sender, "「Ready」 ", "")
            sendMention20(msg.to, sender, "「Ready」 ", "")            
    elif cmd == "ceklogin":
      if wait["selfbot"] == True:
        if msg._from in admin:
            try: 
                sendMention1(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention2(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention3(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention4(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention5(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention6(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention7(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention8(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention9(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention10(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention11(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention12(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention13(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention14(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention15(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention16(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention17(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention18(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention19(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")
                sendMention20(msg.to, sender, "「Ready」 ", "NOT LOG_OUT")                
            except Exception as e:
                line.sendMessage(msg.to,"เกิดข้อผิดพลาด\n" +str(e))                                                	
    elif cmd == "responname":
      if wait["selfbot"] == True:
        if msg._from in admin:
            try: 
                kicker.sendMessage(msg.to,responsename1)
                kicker2.sendMessage(msg.to,responsename2)
                kicker3.sendMessage(msg.to,responsename3)
                kicker4.sendMessage(msg.to,responsename4)	
                kicker5.sendMessage(msg.to,responsename5)
                kicker6.sendMessage(msg.to,responsename6)
                kicker7.sendMessage(msg.to,responsename7)
                kicker8.sendMessage(msg.to,responsename8)
                kicker9.sendMessage(msg.to,responsename9)	
                kicker10.sendMessage(msg.to,responsename10) 
                kicker11.sendMessage(msg.to,responsename11)
                kicker12.sendMessage(msg.to,responsename12)
                kicker13.sendMessage(msg.to,responsename13)
                kicker14.sendMessage(msg.to,responsename14)	
                kicker15.sendMessage(msg.to,responsename15)
                kicker16.sendMessage(msg.to,responsename16)
                kicker17.sendMessage(msg.to,responsename17)
                kicker18.sendMessage(msg.to,responsename18)
                kicker19.sendMessage(msg.to,responsename19)	
                kicker20.sendMessage(msg.to,responsename20)                                
            except Exception as e:
                line.sendMessage(msg.to,"เกิดข้อผิดพลาด\n" +str(e))
               
    elif cmd == "inv":
      if wait["selfbot"] == True:   
        if msg._from in admin:
            try:
                anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid]                                    
                line.inviteIntoGroup(msg.to, anggota)
                kicker.acceptGroupInvitation(msg.to)
                kicker2.acceptGroupInvitation(msg.to)
                kicker3.acceptGroupInvitation(msg.to)
                kicker4.acceptGroupInvitation(msg.to)								
                kicker5.acceptGroupInvitation(msg.to)
                kicker6.acceptGroupInvitation(msg.to)
                kicker7.acceptGroupInvitation(msg.to)
                kicker8.acceptGroupInvitation(msg.to)
                kicker9.acceptGroupInvitation(msg.to)								
                kicker10.acceptGroupInvitation(msg.to)
                kicker11.acceptGroupInvitation(msg.to)
                kicker12.acceptGroupInvitation(msg.to)
                kicker13.acceptGroupInvitation(msg.to)
                kicker14.acceptGroupInvitation(msg.to)								
                kicker15.acceptGroupInvitation(msg.to)
                kicker16.acceptGroupInvitation(msg.to)
                kicker17.acceptGroupInvitation(msg.to)
                kicker18.acceptGroupInvitation(msg.to)
                kicker19.acceptGroupInvitation(msg.to)								
                kicker20.acceptGroupInvitation(msg.to)                	                								
            except Exception as e:
                line.sendMessage(msg.to,"เกิดข้อผิดพลาด\n" +str(e))               
              
    elif cmd == "antijs stay":
      if wait["selfbot"] == True:
        if msg._from in admin:
            try:
                ginfo = line.getGroup(msg.to)
                line.inviteIntoGroup(msg.to, [g1MID])
                line.sendMessage(msg.to,"Group 「"+str(ginfo.name)+"」 ทำการเปิดใช้งานโหมดป้องกันJS")
            except Exception as e:
                line.sendMessage(msg.to,"เกิดข้อผิดพลาด\n" +str(e))
    elif cmd == "~~":
      if wait["selfbot"] == True:
        if msg._from in admin:
            G = line.getGroup(msg.to)
            kicker.leaveGroup(msg.to)
            kicker2.leaveGroup(msg.to)
            kicker3.leaveGroup(msg.to)
            kicker4.leaveGroup(msg.to)
            kicker5.leaveGroup(msg.to)
            kicker6.leaveGroup(msg.to)
            kicker7.leaveGroup(msg.to)
            kicker8.leaveGroup(msg.to)
            kicker9.leaveGroup(msg.to)
            kicker10.leaveGroup(msg.to)	
            kicker11.leaveGroup(msg.to)
            kicker12.leaveGroup(msg.to)
            kicker13.leaveGroup(msg.to)
            kicker14.leaveGroup(msg.to)
            kicker15.leaveGroup(msg.to)
            kicker16.leaveGroup(msg.to)
            kicker17.leaveGroup(msg.to)
            kicker18.leaveGroup(msg.to)
            kicker19.leaveGroup(msg.to)
            kicker20.leaveGroup(msg.to)	                        		
    elif cmd == "kicker join":
        if msg._from in admin:
            G = line.getGroup(msg.to)
            ginfo = line.getGroup(msg.to)
            G.preventedJoinByTicket = False
            line.updateGroup(G)
            invsend = 0
            Ticket = line.reissueGroupTicket(msg.to)
            g1.acceptGroupInvitationByTicket(msg.to,Ticket)
            G = g1.getGroup(msg.to)
            G.preventedJoinByTicket = True
            g1.updateGroup(G)

    elif cmd == "kicker bye":
        if msg._from in admin:
            G = line.getGroup(msg.to)
            g1.leaveGroup(msg.to)
    elif cmd == "/k:speed":
      if wait["selfbot"] == True:
        if msg._from in admin:
            start = time.time()
            kicker.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start
            kicker.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker2.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start            
            kicker2.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker3.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start                 
            kicker3.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker4.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start            
            kicker4.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker5.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start                
            kicker5.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker6.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start              
            kicker6.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker7.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start            
            kicker7.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker8.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start                   
            kicker8.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker9.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start            
            kicker9.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker10.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start                
            kicker10.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()            
            kicker11.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start
            kicker11.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker12.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start            
            kicker12.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker13.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start                 
            kicker13.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker14.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start            
            kicker14.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker15.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start                
            kicker15.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker16.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start              
            kicker16.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker17.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start            
            kicker17.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker18.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start                   
            kicker18.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker19.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start            
            kicker19.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
            start = time.time()
            kicker20.sendMessage("u21d04f683a70ee8776c4c58a0358c204", ".")
            elapsed_time = time.time() - start                
            kicker20.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")            
    elif "spamcall" in msg.text.lower():
        if msg.toType == 2:
            sep = msg.text.split(" ")
            resp = msg.text.replace(sep[0] + " ","")
            num = int(resp)
            try:
                sendMention1(msg.to, sender, "「SpamCall Ready」 ", "")
            except:
                pass
            while range(1):
                group = kicker.getGroup(to)
                members = [mem.mid for mem in group.members]
                for var in range(num):
                    kicker.acquireGroupCallRoute(to)
                    kicker.inviteIntoGroupCall(to, contactIds=members)
                    kicker2.acquireGroupCallRoute(to)
                    kicker2.inviteIntoGroupCall(to, contactIds=members)
                    kicker3.acquireGroupCallRoute(to)
                    kicker3.inviteIntoGroupCall(to, contactIds=members)
                    kicker4.acquireGroupCallRoute(to)
                    kicker4.inviteIntoGroupCall(to, contactIds=members)
                    kicker5.acquireGroupCallRoute(to)
                    kicker5.inviteIntoGroupCall(to, contactIds=members)
                    kicker6.acquireGroupCallRoute(to)
                    kicker6.inviteIntoGroupCall(to, contactIds=members)
                    kicker7.acquireGroupCallRoute(to)
                    kicker7.inviteIntoGroupCall(to, contactIds=members)  
                    kicker8.acquireGroupCallRoute(to)
                    kicker8.inviteIntoGroupCall(to, contactIds=members)
                    kicker9.acquireGroupCallRoute(to)
                    kicker9.inviteIntoGroupCall(to, contactIds=members)
                    kicker10.acquireGroupCallRoute(to)
                    kicker10.inviteIntoGroupCall(to, contactIds=members) 
                    kicker11.acquireGroupCallRoute(to)
                    kicker11.inviteIntoGroupCall(to, contactIds=members)
                    kicker12.acquireGroupCallRoute(to)
                    kicker12.inviteIntoGroupCall(to, contactIds=members)
                    kicker13.acquireGroupCallRoute(to)
                    kicker13.inviteIntoGroupCall(to, contactIds=members)
                    kicker14.acquireGroupCallRoute(to)
                    kicker14.inviteIntoGroupCall(to, contactIds=members)
                    kicker15.acquireGroupCallRoute(to)
                    kicker15.inviteIntoGroupCall(to, contactIds=members)
                    kicker16.acquireGroupCallRoute(to)
                    kicker16.inviteIntoGroupCall(to, contactIds=members)
                    kicker17.acquireGroupCallRoute(to)
                    kicker17.inviteIntoGroupCall(to, contactIds=members)  
                    kicker18.acquireGroupCallRoute(to)
                    kicker18.inviteIntoGroupCall(to, contactIds=members)
                    kicker19.acquireGroupCallRoute(to)
                    kicker19.inviteIntoGroupCall(to, contactIds=members)
                    kicker20.acquireGroupCallRoute(to)
                    kicker20.inviteIntoGroupCall(to, contactIds=members)                                                                                                                                                                                       
                sendMention1(msg.to, sender, "「SpamCall End」 ", "")
                break
        else:
            kicker.sendMessage(to,"คำสั่งนี้สามารถใช้ได้เฉพาะกลุ่ม")          

    elif 'Set autolike ' in msg.text:
       if msg._from in admin:
          spl = msg.text.replace('Set autolike ','')
          if spl in [""," ","\n",None]:
              line.sendMessage(msg.to, "เกิดข้อผิดพลาดร้ายแรง")
          else:
              wait["comment"] = spl
              line.sendMessage(msg.to, "「Autolike」\nเปลี่ยนคอมเม้นเป็น\n「{}」".format(str(spl)))

    elif text.lower() == "cek autolike":
        if msg._from in admin:
           line.sendMessage(msg.to, "「AutoLike」\nคอมเม้นของคุณคือ!\n「 " + str(wait["comment"]) + " 」")

    elif cmd.startswith('like '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if wait['autoLike']:
                line.sendMessage(to, "「AutoLike on」")
            else:
                wait['autoLike'] = True
                line.sendMessage(to, "「AutoLike on」")
        elif texttl == 'off':
            if not wait['autoLike']:
                line.sendMessage(to, "「AutoLike off」")
            else:
                wait['autoLike'] = False
                line.sendMessage(to, "「AutoLike off」")
#===========Protection============#
    elif 'Po1 ' in msg.text:
       if msg._from in admin:
          spl = msg.text.replace('Po1 ','')
          if spl == 'on':
              if msg.to in protectqr:
                   msgs = "URL Protect Start"
              else:
                   protectqr.append(msg.to)
                   ginfo = line.getGroup(msg.to)
                   msgs = "URL Protect Start\nIn Group : " +str(ginfo.name)
              line.sendMessage(msg.to, "「STATUS PROTECT URL」\n" + msgs)
          elif spl == 'off':
                if msg.to in protectqr:
                     protectqr.remove(msg.to)
                     ginfo = line.getGroup(msg.to)
                     msgs = "URL Protect Trun off\nIn Group : " +str(ginfo.name)
                else:
                     msgs = "URL Protect Trun off"
                line.sendMessage(msg.to, "「STATUS PROTECT URL」\n" + msgs)

    elif 'Po2 ' in msg.text:
       if msg._from in admin:
          spl = msg.text.replace('Po2 ','')
          if spl == 'on':
              if msg.to in protectkick:
                   msgs = "Kick Member Protect Start"
              else:
                   protectkick.append(msg.to)
                   ginfo = line.getGroup(msg.to)
                   msgs = "Kick Member Protect Start\nIn Group : " +str(ginfo.name)
              line.sendMessage(msg.to, "「STATUS PROTECT KICK」\n" + msgs)
          elif spl == 'off':
                if msg.to in protectkick:
                     protectkick.remove(msg.to)
                     ginfo = line.getGroup(msg.to)
                     msgs = "Kick Member Protect Trun off\nIn Group : " +str(ginfo.name)
                else:
                     msgs = "Kick Member Protect Trun off"
                line.sendMessage(msg.to, "「STATUS PROTECT KICK」\n" + msgs)

    elif 'Po3 ' in msg.text:
       if msg._from in admin: 
          spl = msg.text.replace('Po3 ','')
          if spl == 'on':
              if msg.to in protecARoin:
                   msgs = "Joinkick Start"
              else:
                   protecARoin.append(msg.to)
                   ginfo = line.getGroup(msg.to)
                   msgs = "Joinkick Start\nIn Group : " +str(ginfo.name)
              line.sendMessage(msg.to, "「STATUS PROTECT JOIN」\n" + msgs)
          elif spl == 'off':
                if msg.to in protecARoin:
                     protecARoin.remove(msg.to)
                     ginfo = line.getGroup(msg.to)
                     msgs = "Joinkick Trun off\nIn Group : " +str(ginfo.name)
                else:
                     msgs = "Joinkick Trun off"
                line.sendMessage(msg.to, "「STATUS PROTECT JOIN」\n" + msgs)

    elif 'Protectcanceljs ' in msg.text:
       if msg._from in admin:
          spl = msg.text.replace('Protectcanceljs ','')
          if spl == 'on':
              if msg.to in protectcanceljs:
                   msgs = "ป้องกันยกเลิกเชิญบอทเปิดใช้งาน"
              else:
                   protectcanceljs[msg.to] = True
                   f=codecs.open('protectcanceljs.json','w','utf-8')
                   json.dump(protectcanceljs, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                   ginfo = line.getGroup(msg.to)
                   msgs = "ป้องกันยกเลิกเชิญบอทเปิดใช้งาน\nIn Group : " +str(ginfo.name)
              line.sendMessage(msg.to, "「STATUS PROTECT CANCEL」\n" + msgs)
          elif spl == 'off':
                if msg.to in protectcanceljs:
                     del protectcanceljs[msg.to]
                     f=codecs.open('protectcanceljs.json','w','utf-8')
                     json.dump(protectcanceljs, f, sort_keys=True, indent=4,ensure_ascii=False)										 
                     ginfo = line.getGroup(msg.to)
                     msgs = "ป้องกันยกเลิกเชิญบอทปิดใช้งาน\nIn Group : " +str(ginfo.name)
                else:
                     msgs = "ป้องกันยกเลิกเชิญบอทปิดใช้งาน"
                line.sendMessage(msg.to, "「STATUS PROTECT CANCEL」\n" + msgs)
 
    elif 'Protectcancel ' in msg.text:
       if msg._from in admin:
          spl = msg.text.replace('Protectcancel ','')
          if spl == 'on':
              if msg.to in protectcancel:
                   msgs = "ป้องกันยกเลิกเชิญถูกเปิดใช้งานอยู่แล้ว"
              else:
                   protectcancel[msg.to] = True
                   f=codecs.open('protectcancel.json','w','utf-8')
                   json.dump(protectcancel, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                   ginfo = line.getGroup(msg.to)
                   msgs = "ป้องกันยกเลิกเชิญเปิดใช้งาน\nIn Group : " +str(ginfo.name)
              line.sendMessage(msg.to, "「STATUS PROTECT CANCEL」\n" + msgs)
          elif spl == 'off':
                if msg.to in protectcancel:
                     del protectcancel[msg.to]
                     f=codecs.open('protectcancel.json','w','utf-8')
                     json.dump(protectcancel, f, sort_keys=True, indent=4,ensure_ascii=False)										 
                     ginfo = line.getGroup(msg.to)
                     msgs = "ป้องกันยกเลิกเชิญปิดใช้งาน\nIn Group : " +str(ginfo.name)
                else:
                     msgs = "ป้องกันยกเลิกเชิญถูกปิดใช้งานอยู่แล้ว"
                line.sendMessage(msg.to, "「STATUS PROTECT CANCEL」\n" + msgs)
        
    elif 'Po4 ' in msg.text:
       if msg._from in admin:
          spl = msg.text.replace('Po4 ','')
          if spl == 'on':
              if msg.to in protectinvite:
                   msgs = "InviteProtect Start"
              else:
                   protectinvite[msg.to] = True
                   f=codecs.open('protectinvite.json','w','utf-8')
                   json.dump(protectinvite, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                   ginfo = line.getGroup(msg.to)
                   msgs = "InviteProtect Start\nIn Group : " +str(ginfo.name)
              line.sendMessage(msg.to, "「STATUS PROTECT CANCEL」\n" + msgs)
          elif spl == 'off':
                if msg.to in protectinvite:
                     del protectinvite[msg.to]
                     f=codecs.open('protectinvite.json','w','utf-8')
                     json.dump(protectinvite, f, sort_keys=True, indent=4,ensure_ascii=False)										 
                     ginfo = line.getGroup(msg.to)
                     msgs = "InviteProtect Trun off\nIn Group : " +str(ginfo.name)
                else:
                     msgs = "InviteProtect Trun off"
                line.sendMessage(msg.to, "「STATUS PROTECT CANCEL」\n" + msgs)

    elif 'Antijs ' in msg.text:
       if msg._from in admin:
          spl = msg.text.replace('Antijs ','')
          if spl == 'on':
              if msg.to in protectantijs:
                   msgs = "ป้องกันJSถูกเปิดใช้งานอยู่แล้ว"
              else:
                   protectantijs[msg.to] = True
                   f=codecs.open('protectantijs.json','w','utf-8')
                   json.dump(protectantijs, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                   ginfo = line.getGroup(msg.to)
                   msgs = "ป้องกันJSเปิดใช้งาน\nIn Group : " +str(ginfo.name)
              line.sendMessage(msg.to, "「STATUS PROTECT JS」\n" + msgs)
          elif spl == 'off':
                if msg.to in protectantijs:
                     del protectantijs[msg.to]
                     f=codecs.open('protectantijs.json','w','utf-8')
                     json.dump(protectantijs, f, sort_keys=True, indent=4,ensure_ascii=False)												 
                     ginfo = line.getGroup(msg.to)
                     msgs = "ป้องกันJSปิดใช้งาน\nIn Group : " +str(ginfo.name)
                else:
                     msgs = "ป้องกันJSถูกปิดใช้งานอยู่แล้ว"
                line.sendMessage(msg.to, "「STATUS PROTECT JS」\n" + msgs)
    elif "whois " in msg.text.lower():
        spl = re.split("whois ",msg.text,flags=re.IGNORECASE)
        if spl[0] == "":
            msg.contentType = 13
            msg.text = None
            msg.contentMetadata = {"mid":spl[1]}
            line.sendMessage(msg.to,text = None,contentMetadata = {"mid":spl[1]},contentType = 13)
                
    elif 'Ghost ' in msg.text:
       if msg._from in admin:
          spl = msg.text.replace('Ghost ','')
          if spl == 'on':
              if msg.to in ghost:
                   msgs = "เปิดใช้งานโหมด Ghost"
              else:
                   ghost[msg.to] = True
                   f=codecs.open('ghost.json','w','utf-8')
                   json.dump(ghost, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                   ginfo = line.getGroup(msg.to)
                   msgs = "เปิดใช้งานโหมด Ghost\nIn Group : " +str(ginfo.name)
              line.sendMessage(msg.to, "「STATUS PROTECT JS」\n" + msgs)
          elif spl == 'off':
                if msg.to in ghost:
                     del ghost[msg.to]
                     f=codecs.open('ghost.json','w','utf-8')
                     json.dump(ghost, f, sort_keys=True, indent=4,ensure_ascii=False)												 
                     ginfo = line.getGroup(msg.to)
                     msgs = "ปิดใช้งานโหมด Ghost\nIn Group : " +str(ginfo.name)
                else:
                     msgs = "ปิดใช้งานโหมด Ghost"
                line.sendMessage(msg.to, "「STATUS PROTECT JS」\n" + msgs)

    elif ("ส่อง " in msg.text):
      if wait["selfbot"] == True:
        if msg._from in admin:
           key = eval(msg.contentMetadata["MENTION"])
           key1 = key["MENTIONEES"][0]["M"]
           mi = line.getContact(key1)
           line.sendMessage(msg.to, "ชื่อ : "+str(mi.displayName)+"\nMID : " +key1)
           line.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

    elif ("Ban " in msg.text):
      if wait["selfbot"] == True:
        if msg._from in admin:
           key = eval(msg.contentMetadata["MENTION"])
           key["MENTIONEES"][0]["M"]
           targets = []
           for x in key["MENTIONEES"]:
                targets.append(x["M"])
           for target in targets:
                   try:
                       wait["blacklist"][target] = True
                       line.sendMessage(msg.to,"เพิ่มบัญชีดำสำเร็จแล้ว")
                   except:
                       pass

    elif ("Unban " in msg.text):
      if wait["selfbot"] == True:
        if msg._from in admin:
           key = eval(msg.contentMetadata["MENTION"])
           key["MENTIONEES"][0]["M"]
           targets = []
           for x in key["MENTIONEES"]:
                targets.append(x["M"])
           for target in targets:
                   try:
                       del wait["blacklist"][target]
                       line.sendMessage(msg.to,"ลบบัญชีดำสำเร็จแล้ว")
                   except:
                       pass

    elif cmd == "ban":
      if wait["selfbot"] == True:
        if msg._from in admin:
            wait["wblacklist"] = True
            line.sendMessage(to,"Send contact you will be blacklist")

    elif cmd == "unban":
      if wait["selfbot"] == True:
        if msg._from in admin:
            wait["dblacklist"] = True
            line.sendMessage(to,"Send contact you will be whitelist")

    elif cmd == "bc":
      if wait["selfbot"] == True:
        if msg._from in admin:
          if wait["blacklist"] == {}:
                line.sendMessage(msg.to,"ไม่พบคนติดดำ")
          else:
                ma = ""
                for i in wait["blacklist"]:
                    ma = line.getContact(i)
                    line.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
    elif cmd == "cb":
      if wait["selfbot"] == True:
        if msg._from in admin:
          wait["blacklist"] = {}
          ragets = line.getContacts(wait["blacklist"])
          mc = "「%i」User Blacklist" % len(ragets)
          line.sendMessage(to,"ปลดแบนสมาชิกแล้ว~ " +mc)
          kicker.sendMessage(to,"ปลดแบนสมาชิกแล้ว~ " +mc)
          kicker2.sendMessage(to,"ปลดแบนสมาชิกแล้ว~ " +mc)
          kicker3.sendMessage(to,"ปลดแบนสมาชิกแล้ว~ " +mc)
          kicker4.sendMessage(to,"ปลดแบนสมาชิกแล้ว~ " +mc)
          kicker5.sendMessage(to,"ปลดแบนสมาชิกแล้ว~ " +mc)
          kicker6.sendMessage(to,"ปลดแบนสมาชิกแล้ว~ " +mc)
          kicker7.sendMessage(to,"ปลดแบนสมาชิกแล้ว~ " +mc)
          kicker8.sendMessage(to,"ปลดแบนสมาชิกแล้ว~ " +mc)
          kicker9.sendMessage(to,"ปลดแบนสมาชิกแล้ว~ " +mc)
          kicker10.sendMessage(to,"ปลดแบนสมาชิกแล้ว~ " +mc)                   
    elif cmd.startswith('error'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Error 」'
        res += '\n├ Usage : '
        res += '\n│ • {key}Error'
        res += '\n│ • {key}Error Logs'
        res += '\n│ • {key}Error Reset'
        res += '\n│ • {key}Error Detail <errid>'
        res += '\n╰───「SelfBot ProtectV2.2」'
        if cmd == 'error':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == 'logs':
            try:
                filee = open('errorLog.txt', 'r')
            except FileNotFoundError:
                return line.sendMessage(to, 'ไม่สามารถแสดงบันทึกข้อผิดพลาดได้\nไม่พบไฟล์')
            errors = [err.strip() for err in filee.readlines()]
            filee.close()
            if not errors: return line.sendMessage(to, 'ไม่สามารถแสดงบันทึกข้อผิดพลาดได้\nบันทึกข้อผิดพลาดว่างเปล่า')
            res = '╭───「 Error Logs 」'
            res += '\n├ List :'
            parsed_len = len(errors)//200+1
            no = 0
            for point in range(parsed_len):
                for error in errors[point*200:(point+1)*200]:
                    if not error: continue
                    no += 1
                    res += '\n│ %i. %s' % (no, error)
                    if error == errors[-1]:
                        res += '\n╰───「SelfBot ProtectV2.2」'
                if res:
                    if res.startswith('\n'): res = res[1:]
                    line.sendMessage(to, res)
                res = ''
        elif cond[0].lower() == 'reset':
            filee = open('errorLog.txt', 'w')
            filee.write('')
            filee.close()
            shutil.rmtree('tmp/errors/', ignore_errors=True)
            os.system('mkdir tmp/errors')
            line.sendMessage(to, 'Success reset error logs')
        elif cond[0].lower() == 'detail':
            if len(cond) < 2:
                return line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            errid = cond[1]
            if os.path.exists('tmp/errors/%s.txt' % errid):
                with open('tmp/errors/%s.txt' % errid, 'r') as f:
                    line.sendMessage(to, f.read())
            else:
                return line.sendMessage(to, 'Failed display details error, errorid not valid')
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif txt.startswith('setkey'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Setting Key 」'
        res += '\n├ Status : ' + bool_dict[settings['setKey']['status']][1]
        res += '\n├ Key : ' + settings['setKey']['key'].title()
        res += '\n├ Usage : '
        res += '\n│ • Setkey'
        res += '\n│ • Setkey <on/off>'
        res += '\n│ • Setkey <key>'
        res += '\n╰───「SelfBot ProtectV2.2」'
        if txt == 'setkey':
            line.sendMessage(to, parsingRes(res))
        elif texttl == 'on':
            if settings['setKey']['status']:
                line.sendMessage(to, 'Failed activate setkey, setkey already active')
            else:
                settings['setKey']['status'] = True
                line.sendMessage(to, 'Success activated setkey')
        elif texttl == 'off':
            if not settings['setKey']['status']:
                line.sendMessage(to, 'Failed deactivate setkey, setkey already deactive')
            else:
                settings['setKey']['status'] = False
                line.sendMessage(to, 'Success deactivated setkey')
        else:
            settings['setKey']['key'] = texttl
            line.sendMessage(to, 'Success change set key to (%s)' % textt)
    elif cmd.startswith('autoadd'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Auto Add 」'
        res += '\n├ Status : ' + bool_dict[settings['autoAdd']['status']][1]
        res += '\n├ Reply : ' + bool_dict[settings['autoAdd']['reply']][0]
        res += '\n├ Reply Message : ' + settings['autoAdd']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}AutoAdd'
        res += '\n│ • {key}AutoAdd <on/off>'
        res += '\n│ • {key}AutoAdd Reply <on/off>'
        res += '\n│ • {key}AutoAdd <message>'
        res += '\n╰───「SelfBot ProtectV2.2」'
        if cmd == 'autoadd':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoAdd']['status']:
                line.sendMessage(to, 'เปิดรับแอดออโต้')
            else:
                settings['autoAdd']['status'] = True
                line.sendMessage(to, 'เปิดรับแอดออโต้')
        elif texttl == 'off':
            if not settings['autoAdd']['status']:
                line.sendMessage(to, 'ปิดรับแอดออโต้')
            else:
                settings['autoAdd']['status'] = False
                line.sendMessage(to, 'ปิดรับแอดออโต้')
        elif cond[0].lower() == 'reply':
            if len(cond) < 2:
                return line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoAdd']['reply']:
                    line.sendMessage(to, 'เปิดข้อความทักคนแอด')
                else:
                    settings['autoAdd']['reply'] = True
                    line.sendMessage(to, 'เปิดข้อความทักคนแอด')
            elif cond[1].lower() == 'off':
                if not settings['autoAdd']['reply']:
                    line.sendMessage(to, 'ปิดข้อความทักคนแอด')
                else:
                    settings['autoAdd']['reply'] = False
                    line.sendMessage(to, 'ปิดข้อความทักคนแอด')
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            settings['autoAdd']['message'] = textt
            line.sendMessage(to, 'เปลี่ยนข้อความออโต้แอดเป็น `%s`' % textt)
    elif cmd.startswith('autojoin'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Auto Join 」'
        res += '\n├ Status : ' + bool_dict[settings['autoJoin']['status']][1]
        res += '\n├ Reply : ' + bool_dict[settings['autoJoin']['reply']][0]
        res += '\n├ Reply Message : ' + settings['autoJoin']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}AutoJoin'
        res += '\n│ • {key}AutoJoin <on/off>'
        res += '\n│ • {key}AutoJoin Ticket <on/off>'
        res += '\n│ • {key}AutoJoin Reply <on/off>'
        res += '\n│ • {key}AutoJoin <message>'
        res += '\n╰───「SelfBot ProtectV2.2」'
        if cmd == 'autojoin':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoJoin']['status']:
                line.sendMessage(to, 'เปิดเข้าร่วมกลุ่มออโต้')
            else:
                settings['autoJoin']['status'] = True
                line.sendMessage(to, 'เปิดเข้าร่วมกลุ่มออโต้')
        elif texttl == 'off':
            if not settings['autoJoin']['status']:
                line.sendMessage(to, 'ปิดเข้าร่วมกลุ่มออโต้')
            else:
                settings['autoJoin']['status'] = False
                line.sendMessage(to, 'ปิดเข้าร่วมกลุ่มออโต้')
        elif cond[0].lower() == 'reply':
            if len(cond) < 2:
                return line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoJoin']['reply']:
                    line.sendMessage(to, 'เปิดความทักคนเชิญเข้ากลุ่ม')
                else:
                    settings['autoJoin']['reply'] = True
                    line.sendMessage(to, 'เปิดความทักคนเชิญเข้ากลุ่ม')
            elif cond[1].lower() == 'off':
                if not settings['autoJoin']['reply']:
                    line.sendMessage(to, 'ปิดความทักคนเชิญเข้ากลุ่ม')
                else:
                    settings['autoJoin']['reply'] = False
                    line.sendMessage(to, 'ปิดความทักคนเชิญเข้ากลุ่ม')
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == 'ticket':
            if len(cond) < 2:
                return line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoJoin']['ticket']:
                    line.sendMessage(to, 'เปิดเข้ากลุ่มออโต้ด้วยลิ้ง')
                else:
                    settings['autoJoin']['ticket'] = True
                    line.sendMessage(to, 'เปิดเข้ากลุ่มออโต้ด้วยลิ้ง')
            elif cond[1].lower() == 'off':
                if not settings['autoJoin']['ticket']:
                    line.sendMessage(to, 'ปิดเข้ากลุ่มออโต้ด้วยลิ้ง')
                else:
                    settings['autoJoin']['ticket'] = False
                    line.sendMessage(to, 'ปิดเข้ากลุ่มออโต้ด้วยลิ้ง')
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            settings['autoJoin']['message'] = textt
            line.sendMessage(to, 'ข้อความทักคนเชิญเข้ากลุ่มเปลี่ยนเป็น `%s`' % textt)
    elif cmd.startswith('autorespondmention'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Auto Respond 」'
        res += '\n├ Status : ' + bool_dict[settings['autoRespondMention']['status']][1]
        res += '\n├ Reply Message : ' + settings['autoRespondMention']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}AutoRespondMention'
        res += '\n│ • {key}AutoRespondMention <on/off>'
        res += '\n│ • {key}AutoRespondMention <message>'
        res += '\n╰───「SelfBot ProtectV2.2」'     
        if cmd == 'autorespondmention':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoRespondMention']['status']:
                line.sendMessage(to, 'เปิดตอบกลับคนแทค')
            else:
                settings['autoRespondMention']['status'] = True
                line.sendMessage(to, 'เปิดตอบกลับคนแทค')
        elif texttl == 'off':
            if not settings['autoRespondMention']['status']:
                line.sendMessage(to, 'ปิดตอบกลับคนแทค')
            else:
                settings['autoRespondMention']['status'] = False
                line.sendMessage(to, 'ปิดตอบกลับคนแทค')
        else:
            settings['autoRespondMention']['message'] = textt
            line.sendMessage(to, 'ข้อความตอบกลับคนแทคเปลี่ยนเป็น `%s`' % textt)
    elif cmd.startswith('autorespond'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Auto Respond 」'
        res += '\n├ Status : ' + bool_dict[settings['autoRespond']['status']][1]
        res += '\n├ Reply Message : ' + settings['autoRespond']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}AutoRespond'
        res += '\n│ • {key}AutoRespond <on/off>'
        res += '\n│ • {key}AutoRespond <message>'
        res += '\n╰───「SelfBot ProtectV2.2」'
        if cmd == 'autorespond':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoRespond']['status']:
                line.sendMessage(to, 'เปิดตอบกลับอัตโนมัติ')
            else:
                settings['autoRespond']['status'] = True
                line.sendMessage(to, 'เปิดตอบกลับอัตโนมัติ')
        elif texttl == 'off':
            if not settings['autoRespond']['status']:
                line.sendMessage(to, 'ปิดตอบกลับอัตโนมัติ')
            else:
                settings['autoRespond']['status'] = False
                line.sendMessage(to, 'ปิดตอบกลับอัตโนมัติ')
        else:
            settings['autoRespond']['message'] = textt
            line.sendMessage(to, 'ข้อความเปิดตอบกลับอัตโนมัติถูกเปลี่ยนเป็น `%s`' % textt)
    elif cmd.startswith('autoread '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['autoRead']:
                line.sendMessage(to, 'เปิดอ่านออโต้')
            else:
                settings['autoRead'] = True
                line.sendMessage(to, 'เปิดอ่านออโต้')
        elif texttl == 'off':
            if not settings['autoRead']:
                line.sendMessage(to, 'ปิดอ่านออโต้')
            else:
                settings['autoRead'] = False
                line.sendMessage(to, 'ปิดอ่านออโต้')
    elif cmd.startswith('checkcontact '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkContact']:
                line.sendMessage(to, 'เปิดเช็คคท')
            else:
                settings['checkContact'] = True
                line.sendMessage(to, 'เปิดเช็คคท')
        elif texttl == 'off':
            if not settings['checkContact']:
                line.sendMessage(to, 'ปิดเช็คคท')
            else:
                settings['checkContact'] = False
                line.sendMessage(to, 'ปิดเช็คคท')
    elif cmd.startswith('checkpost '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkPost']:
                line.sendMessage(to, 'เปิดเช็คโพส')
            else:
                settings['checkPost'] = True
                line.sendMessage(to, 'เปิดเช็คโพส')
        elif texttl == 'off':
            if not settings['checkPost']:
                line.sendMessage(to, 'ปิดเช็คโพส')
            else:
                settings['checkPost'] = False
                line.sendMessage(to, 'ปิดเช็คโพส')
    elif cmd.startswith('checksticker '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkSticker']:
                line.sendMessage(to, 'เปิดเช็คสติ๊กเกอร์')
            else:
                settings['checkSticker'] = True
                line.sendMessage(to, 'เปิดเช็คสติ๊กเกอร์')
        elif texttl == 'off':
            if not settings['checkSticker']:
                line.sendMessage(to, 'ปิดเช็คสติ๊กเกอร์')
            else:
                settings['checkSticker'] = False
                line.sendMessage(to, 'ปิดเช็คสติ๊กเกอร์')
    elif cmd.startswith('myprofile'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        profile = line.getProfile()
        res = '╭───「 My Profile 」'
        res += '\n├ MID : ' + profile.mid
        res += '\n├ Display Name : ' + str(profile.displayName)
        res += '\n├ Usage : '
        res += '\n│ • {key}MyProfile'
        res += '\n│ • {key}MyProfile MID'
        res += '\n│ • {key}MyProfile Name'
        res += '\n│ • {key}MyProfile Bio'
        res += '\n│ • {key}MyProfile Pict'
        res += '\n│ • {key}MyProfile Cover'
        res += '\n│ • {key}MyProfile Change Name <name>'
        res += '\n│ • {key}MyProfile Change Bio <bio>'
        res += '\n│ • {key}MyProfile Change Pict'
        res += '\n│ • {key}MyProfile Change Cover'
        res += '\n╰───「SelfBot ProtectV2.2」'
        if texttl == 'mid':
            line.sendMessage(to, '「 MID 」\n' + str(profile.mid))
        elif texttl == 'name':
            line.sendMessage(to, '「 Display Name 」\n' + str(profile.displayName))
        elif texttl == 'bio':
            line.sendMessage(to, '「 Status Message 」\n' + str(profile.statusMessage))
        elif texttl == 'pict':
            if profile.pictureStatus:
                path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                line.sendImageWithURL(to, path)
                line.sendMessage(to, '「 Picture Status 」\n' + path)
            else:
                line.sendMessage(to, 'ไม่สามารถแสดงรูปได้เนื่องจากผู้ใช้นี้ไม่ได้ใส่รูป')
        elif texttl == 'cover':
            cover = line.getProfileCoverURL(profile.mid)
            line.sendImageWithURL(to, str(cover))
            line.sendMessage(to, '「 Cover Picture 」\n' + str(cover))
        elif texttl.startswith('change '):
            texts = textt[7:]
            textsl = texts.lower()
            if textsl.startswith('name '):
                name = texts[5:]
                if len(name) <= 20:
                    profile.displayName = name
                    line.updateProfile(profile)
                    line.sendMessage(to, 'เปลี่ยนชื่อสำเร็จ\nเปลี่ยนชื่อเป็น`%s`' % name)
                else:
                    line.sendMessage(to, 'ไม่สามารถเปลี่ยนชื่อได้\nความยาวของชื่อต้องไม่เกิน 20')
            elif textsl.startswith('bio '):
                bio = texts[4:]
                if len(bio) <= 3000:
                    profile.statusMessage = bio
                    line.updateProfile(profile)
                    line.sendMessage(to, 'เปลี่ยนสถานะเรียบร้อย\nเปลี่ยนสถนานะเป็น `%s`' % bio)
                else:
                    line.sendMessage(to, 'ไม่สามารถเปลี่ยนสถานะได้\nความยาวของข้อความสถานะต้องไม่เกิน3000')
            elif textsl == 'pict':
                settings['changePictureProfile'] = True
                line.sendMessage(to, 'กรุณาส่งภาพเพื่อเปลี่ยนรูปโปรไฟล์, พิม `{key}Abort` ถ้าต้องการยกเลิก\nคำเตือน:การดาวน์โหลดภาพจะล้มเหลวหากอัพโหลดภาพนานเกินไป'.format(key=setKey.title()))
            elif textsl == 'cover':
                settings['changeCoverProfile'] = True
                line.sendMessage(to, 'กรุณาส่งภาพเพื่อเปลี่ยนรูปปก, พิม `{key}Abort` ถ้าต้องการยกเลิก\nคำเตือน:การดาวน์โหลดภาพจะล้มเหลวหากอัพโหลดภาพนานเกินไป'.format(key=setKey.title()))
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('profile'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        profile = line.getContact(to) if msg.toType == 0 else None
        res = '╭───「 My Profile 」'
        if profile:
            res += '\n├ MID : ' + profile.mid
            res += '\n├ Display Name : ' + str(profile.displayName)
            if profile.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(profile.displayNameOverridden)
            res += '\n├ Status Message : ' + str(profile.statusMessage)
        res += '\n├ Usage : '
        res += '\n│ • {key}Profile'
        res += '\n│ • {key}Profile Mid'
        res += '\n│ • {key}Profile Name'
        res += '\n│ • {key}Profile Bio'
        res += '\n│ • {key}Profile Pict'
        res += '\n│ • {key}Profile Cover'
        res += '\n│ • {key}Profile Steal Profile <mention>'
        res += '\n│ • {key}Profile Steal Mid <mention>'
        res += '\n│ • {key}Profile Steal Name <mention>'
        res += '\n│ • {key}Profile Steal Bio <mention>'
        res += '\n│ • {key}Profile Steal Pict <mention>'
        res += '\n│ • {key}Profile Steal Cover <mention>'
        res += '\n╰───「SelfBot ProtectV2.2」'
        if texttl == 'mid':
            if msg.toType != 0: return line.sendMessage(to, 'คำสั่งนี้ใช้ได้ในแชทส่วนตัวเท่านั้น')
            line.sendMessage(to, '「 MID 」\n' + str(profile.mid))
        elif texttl == 'name':
            if msg.toType != 0: return line.sendMessage(to, 'คำสั่งนี้ใช้ได้ในแชทส่วนตัวเท่านั้น')
            line.sendMessage(to, '「 Display Name 」\n' + str(profile.displayName))
        elif texttl == 'bio':
            if msg.toType != 0: return line.sendMessage(to, 'คำสั่งนี้ใช้ได้ในแชทส่วนตัวเท่านั้น')
            line.sendMessage(to, '「 Status Message 」\n' + str(profile.statusMessage))
        elif texttl == 'pict':
            if msg.toType != 0: return line.sendMessage(to, 'คำสั่งนี้ใช้ได้ในแชทส่วนตัวเท่านั้น')
            if profile.pictureStatus:
                path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                line.sendImageWithURL(to, path)
                line.sendMessage(to, '「 Picture Status 」\n' + path)
            else:
                line.sendMessage(to, 'ไม่สามารถแสดงรูปได้เนื่องจากผู้ใช้นี้ไม่ได้ใส่รูป')
        elif texttl == 'cover':
            if msg.toType != 0: return line.sendMessage(to, 'คำสั่งนี้ใช้ได้ในแชทส่วนตัวเท่านั้น')
            cover = line.getProfileCoverURL(profile.mid)
            line.sendImageWithURL(to, str(cover))
            line.sendMessage(to, '「 Cover Picture 」\n' + str(cover))
        elif texttl.startswith('steal '):
            texts = textt[6:]
            textsl = texts.lower()
            if textsl.startswith('profile '):
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        profile = line.getContact(mention['M'])
                        if profile.pictureStatus:
                            line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
                        cover = line.getProfileCoverURL(profile.mid)
                        line.sendImageWithURL(to, str(cover))
                        res = '╭───「 Profile 」'
                        res += '\n├ MID : ' + profile.mid
                        res += '\n├ Display Name : ' + str(profile.displayName)
                        if profile.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(profile.displayNameOverridden)
                        res += '\n├ Status Message : ' + str(profile.statusMessage)
                        res += '\n╰───「SelfBot ProtectV2.2」'
                        line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'ไม่สามารถดึงรูปโปรไฟล์ได้, กรุณาแทคผู้ใช้ด้วย')
            elif textsl.startswith('mid '):
                res = '╭───「 MID 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        mid = mentions['MENTIONEES'][0]['M']
                        return line.sendMessage(to, '「 MID 」\n' + mid)
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        no += 1
                        res += '\n│ %i. %s' % (no, mid)
                    res += '\n╰───「SelfBot ProtectV2.2」'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'ไม่สามารถดึงmidได้, กรุณาแทคผู้ใช้ด้วย')
            elif textsl.startswith('name '):
                res = '╭───「 Display Name 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        return line.sendMessage(to, '「 Display Name 」\n' + str(profile.displayName))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        res += '\n│ %i. %s' % (no, profile.displayName)
                    res += '\n╰───「SelfBot ProtectV2.2」'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'ไม่สามารถดึงชื่อได้, กรุณาแทคผู้ใช้ด้วย')
            elif textsl.startswith('bio '):
                res = '╭───「 Status Message 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        return line.sendMessage(to, '「 Status Message 」\n' + str(profile.statusMessage))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        res += '\n│ %i. %s' % (no, profile.statusMessage)
                    res += '\n╰───「SelfBot ProtectV2.2」'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'ไม่สามารถดึงสถานะได้, กรุณาแทคผู้ใช้ด้วย')
            elif textsl.startswith('pict '):
                res = '╭───「 Picture Status 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        if profile.pictureStatus:
                            path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                            line.sendImageWithURL(to, path)
                            return line.sendMessage(to, '「 Picture Status 」\n' + path)
                        else:
                            return line.sendMessage(to, 'ไม่สามารถดึงรูปได้, บุคคนนี้ `%s` doesn\'ไม่ได้ใส่รูปภาพโปรไฟล์' % profile.displayName)
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        if profile.pictureStatus:
                            path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                            line.sendImageWithURL(to, path)
                            res += '\n│ %i. %s' % (no, path)
                        else:
                            res += '\n│ %i. Not Found' % no
                    res += '\n╰───「SelfBot ProtectV2.2」'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'ไม่สามารถดึงรูปได้, กรุณาแทคผู้ใช้ด้วย')
            elif textsl.startswith('cover '):
                res = '╭───「 Cover Picture 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        mid = mentions['MENTIONEES'][0]['M']
                        cover = line.getProfileCoverURL(mid)
                        line.sendImageWithURL(to, str(cover))
                        line.sendMessage(to, '「 Cover Picture 」\n' + str(cover))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        no += 1
                        cover = line.getProfileCoverURL(mid)
                        line.sendImageWithURL(to, str(cover))
                        res += '\n│ %i. %s' % (no, cover)
                    res += '\n╰───「SelfBot ProtectV2.2」'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'ไม่สามารถดึงปกได้, กรุณาแทคผู้ใช้ด้วย')
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('mimic'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        targets = ''
        if settings['mimic']['target']:
            no = 0
            for target, status in settings['mimic']['target'].items():
                no += 1
                try:
                    name = line.getContact(target).displayName
                except TalkException:
                    name = 'Unknown'
                targets += '\n│ %i. %s//%s' % (no, name, bool_dict[status][1])
        else:
            targets += '\n│ Nothing'
        res = '╭───「 Mimic 」'
        res += '\n├ Status : ' + bool_dict[settings['mimic']['status']][1]
        res += '\n├ List :'
        res += targets
        res += '\n├ Usage : '
        res += '\n│ • {key}Mimic'
        res += '\n│ • {key}Mimic <on/off>'
        res += '\n│ • {key}Mimic Reset'
        res += '\n│ • {key}Mimic Add <mention>'
        res += '\n│ • {key}Mimic Del <mention>'
        res += '\n╰───「SelfBot ProtectV2.2」'
        if cmd == 'mimic':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['mimic']['status']:
                line.sendMessage(to, 'เริ่มการล้อเลียน')
            else:
                settings['mimic']['status'] = True
                line.sendMessage(to, 'เริ่มการล้อเลียน')
        elif texttl == 'off':
            if not settings['mimic']['status']:
                line.sendMessage(to, 'ยกเลิกการล้อเลียน')
            else:
                settings['mimic']['status'] = False
                line.sendMessage(to, 'ยกเลิกการล้อเลียน')
        elif texttl == 'reset':
            settings['mimic']['target'] = {}
            line.sendMessage(to, 'รีเช็ตรายชื่อที่จะล้อเลี่ยนเรียบร้อย')
        elif texttl.startswith('add '):
            res = '╭───「 Mimic 」'
            res += '\n├ Status : Add Target'
            res += '\n├ Added :'
            no = 0
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    settings['mimic']['target'][mid] = True
                    no += 1
                    try:
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───「SelfBot ProtectV2.2」'
                line.sendMessage(to, res)
            else:
                line.sendMessage(to, 'ไม่สามารถเพื่มรายชื่อได้, กรุณาแทคผู้ใช้ด้วย')
        elif texttl.startswith('del '):
            res = '╭───「 Mimic 」'
            res += '\n├ Status : Del Target'
            res += '\n├ Deleted :'
            no = 0
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in settings['mimic']['target']:
                        settings['mimic']['target'][mid] = False
                    no += 1
                    try:
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───「SelfBot ProtectV2.2」'
                line.sendMessage(to, res)
            else:
                line.sendMessage(to, 'ไม่สามารถลบรายชื่อได้, กรุณาแทคผู้ใช้ด้วย')
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('broadcast'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Broadcast 」'
        res += '\n├ Broadcast Type : '
        res += '\n│ 1 : Friends'
        res += '\n│ 2 : Groups'
        res += '\n│ 0 : All'
        res += '\n├ Usage : '
        res += '\n│ • {key}Broadcast'
        res += '\n│ • {key}Broadcast <type> <message>'
        res += '\n╰───「SelfBot ProtectV2.2」'
        if cmd == 'broadcast':
            line.sendMessage(to, parsingRes(res).format(key=setKey.title()))
        elif cond[0] == '1':
            if len(cond) < 2:
                return line.sendMessage(to, 'ไม่สามารถประกาศได้, ไม่พบข้อความ')
            res = '「 Broadcast 」\n'
            res += textt[2:]
            res += '\n\n「SelfBot ProtectV2.2」'
            targets = line.getAllContactIds()
            for target in targets:
                try:
                    line.sendMessage(target, res)
                except TalkException:
                    targets.remove(target)
                    continue
                time.sleep(0.8)
            line.sendMessage(to, 'ประกาศเรียบร้อย, จำนวน %i คน' % len(targets))
        elif cond[0] == '2':
            if len(cond) < 2:
                return line.sendMessage(to, 'ไม่สามารถประกาศได้, ไม่พบข้อความ')
            res = '「 Broadcast 」\n'
            res += textt[2:]
            res += '\n\n「SelfBot ProtectV2.2」'
            targets = line.getGroupIdsJoined()
            for target in targets:
                try:
                    line.sendMessage(target, res)
                except TalkException:
                    targets.remove(target)
                    continue
                time.sleep(0.8)
            line.sendMessage(to, 'ประกาศเรียบร้อย, จำนวน %i กลุ่ม' % len(targets))
        elif cond[0] == '0':
            if len(cond) < 2:
                return line.sendMessage(to, 'ไม่สามารถประกาศได้, ไม่พบข้อความ')
            res = '「 Broadcast 」\n'
            res += textt[2:]
            res += '\n\n「SelfBot ProtectV2.2」'
            targets = line.getGroupIdsJoined() + line.getAllContactIds()
            for target in targets:
                try:
                    line.sendMessage(target, res)
                except TalkException:
                    targets.remove(target)
                    continue
                time.sleep(0.8)
            line.sendMessage(to, 'ประกาศเรียบร้อย, จำนวน %i ' % len(targets))
        else:
            line.sendMessage(to, parsingRes(res).format(key=setKey.title()))
    elif cmd.startswith('friendlist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cids = line.getAllContactIds()
        cids.sort()
        cnames = []
        ress = []
        res = '╭───「 Friend List 」'
        res += '\n├ List:'
        if cids:
            contacts = []
            no = 0
            if len(cids) > 200:
                parsed_len = len(cids)//200+1
                for point in range(parsed_len):
                    for cid in cids[point*200:(point+1)*200]:
                        try:
                            contact = line.getContact(cid)
                            contacts.append(contact)
                        except TalkException:
                            cids.remove(cid)
                            continue
                        no += 1
                        res += '\n│ %i. %s' % (no, contact.displayName)
                        cnames.append(contact.displayName)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for cid in cids:
                    try:
                        contact = line.getContact(cid)
                        contacts.append(contact)
                    except TalkException:
                        cids.remove(cid)
                        continue
                    no += 1
                    res += '\n│ %i. %s' % (no, contact.displayName)
                    cnames.append(contact.displayName)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}FriendList'
        res += '\n│ • {key}FriendList Info <num/name>'
        res += '\n│ • {key}FriendList Add <mention>'
        res += '\n│ • {key}FriendList Del <mention/num/name/all>'
        res += '\n╰───「SelfBot ProtectV2.2」'
        ress.append(res)
        if cmd == 'friendlist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('info '):
            texts = textt[5:].split(', ')
            if not cids:
                return line.sendMessage(to, 'แสดงข้อมูลเพื่อนล้มเหลว, ไม่พบเพื่อน')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(contact.mid)
                    line.sendImageWithURL(to, str(cover))
                    res = '╭───「 Contact Info 」'
                    res += '\n├ MID : ' + contact.mid
                    res += '\n├ Display Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\n├ Status Message : ' + str(contact.statusMessage)
                    res += '\n╰───「SelfBot ProtectV2.2」'
                    line.sendMessage(to, parsingRes(res))
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.pictureStatus:
                            line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                        cover = line.getProfileCoverURL(contact.mid)
                        line.sendImageWithURL(to, str(cover))
                        res = '╭───「 Contact Info 」'
                        res += '\n├ MID : ' + contact.mid
                        res += '\n├ Display Name : ' + str(contact.displayName)
                        if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                        res += '\n├ Status Message : ' + str(contact.statusMessage)
                        res += '\n╰───「SelfBot ProtectV2.2」'
                        line.sendMessage(to, parsingRes(res))
        elif texttl.startswith('add '):
            res = '╭───「 Friend List 」'
            res += '\n├ Status : Add Friend'
            res += '\n├ Added :'
            no = 0
            added = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in cids or mid in added:
                        continue
                    no += 1
                    try:
                        line.findAndAddContactsByMid(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    added.append(mid)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───「SelfBot ProtectV2.2」'
                line.sendMessage(to, res)
            else:
                line.sendMessage(to, 'ไม่สามารถแอดเพื่อนได้, กรุณาแทคผู้ใช้ด้วย')
        elif texttl.startswith('del '):
            texts = textt[4:].split(', ')
            if not cids:
                return line.sendMessage(to, 'เปิดข้อผิดพลาดที่ไม่แน่ชัด')
            res = '╭───「 Friend List 」'
            res += '\n├ Status : Del Friend'
            res += '\n├ Deleted :'
            no = 0
            deleted = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid not in cids or mid in deleted:
                        continue
                    no += 1
                    try:
                        line.deleteContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(mid)
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.mid not in cids and contact.mid in deleted:
                        continue
                    no += 1
                    try:
                        line.deleteContact(contact.mid)
                        name = contact.displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(contact.mid)
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.mid not in cids and contact.mid in deleted:
                            continue
                        no += 1
                        try:
                            line.deleteContact(contact.mid)
                            name = contact.displayName
                        except TalkException:
                            name = 'Unknown'
                        res += '\n│ %i. %s' % (no, name)
                        deleted.append(contact.mid)
                    elif name.lower() == 'all':
                        for contact in contacts:
                            if contact.mid not in cids and contact.mid in deleted:
                                continue
                            no += 1
                            try:
                                line.deleteContact(contact.mid)
                                name = contact.displayName
                            except TalkException:
                                name = 'Unknown'
                            res += '\n│ %i. %s' % (no, name)
                            deleted.append(contact.mid)
                            time.sleep(0.8)
                    else:
                        line.sendMessage(to, 'Failed del friend with name `%s`, ไม่พบชื่อกลุ่มนี้ ♪' % name)
            if no == 0: res += '\n│ Nothing'
            res += '\n╰───「SelfBot ProtectV2.2」'
            line.sendMessage(to, res)
        else:
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('blocklist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cids = line.getBlockedContactIds()
        cids.sort()
        cnames = []
        ress = []
        res = '╭───「 Block List 」'
        res += '\n├ List:'
        if cids:
            contacts = []
            no = 0
            if len(cids) > 200:
                parsed_len = len(cids)//200+1
                for point in range(parsed_len):
                    for cid in cids[point*200:(point+1)*200]:
                        try:
                            contact = line.getContact(cid)
                            contacts.append(contact)
                        except TalkException:
                            cids.remove(cid)
                            continue
                        no += 1
                        res += '\n│ %i. %s' % (no, contact.displayName)
                        cnames.append(contact.displayName)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for cid in cids:
                    try:
                        contact = line.getContact(cid)
                        contacts.append(contact)
                    except TalkException:
                        cids.remove(cid)
                        continue
                    no += 1
                    res += '\n│ %i. %s' % (no, contact.displayName)
                    cnames.append(contact.displayName)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}BlockList'
        res += '\n│ • {key}BlockList Info <num/name>'
        res += '\n│ • {key}BlockList Add <mention>'
        res += '\n│ • {key}BlockList Del <mention/num/name/all>'
        res += '\n╰───「SelfBot ProtectV2.2」'
        ress.append(res)
        if cmd == 'blocklist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('info '):
            texts = textt[5:].split(', ')
            if not cids:
                return line.sendMessage(to, 'แสดงข้อมูลผู้ใช้ที่ถูกบล็อกล้มเหลว, ไม่มีผู้ใช้ในรายการ')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(contact.mid)
                    line.sendImageWithURL(to, str(cover))
                    res = '╭───「 Contact Info 」'
                    res += '\n├ MID : ' + contact.mid
                    res += '\n├ Display Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\n├ Status Message : ' + str(contact.statusMessage)
                    res += '\n╰───「SelfBot ProtectV2.2」'
                    line.sendMessage(to, parsingRes(res))
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.pictureStatus:
                            line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                        cover = line.getProfileCoverURL(contact.mid)
                        line.sendImageWithURL(to, str(cover))
                        res = '╭───「 Contact Info 」'
                        res += '\n├ MID : ' + contact.mid
                        res += '\n├ Display Name : ' + str(contact.displayName)
                        if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                        res += '\n├ Status Message : ' + str(contact.statusMessage)
                        res += '\n╰───「SelfBot ProtectV2.2」'
                        line.sendMessage(to, parsingRes(res))
        elif texttl.startswith('add '):
            res = '╭───「 Block List 」'
            res += '\n├ Status : Add Block'
            res += '\n├ Added :'
            no = 0
            added = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in cids or mid in added:
                        continue
                    no += 1
                    try:
                        line.blockContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    added.append(mid)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───「SelfBot ProtectV2.2」'
                line.sendMessage(to, res)
            else:
                line.sendMessage(to, 'Failed block contact, กรุณาแทคผู้ใช้ด้วย')
        elif texttl.startswith('del '):
            texts = textt[4:].split(', ')
            if not cids:
                return line.sendMessage(to, 'ไม่สามาถปลกบล็อคได้, ไม่มีผู้ใช้ในรายการ')
            res = '╭───「 Block List 」'
            res += '\n├ Status : Del Block'
            res += '\n├ Deleted :'
            no = 0
            deleted = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid not in cids or mid in deleted:
                        continue
                    no += 1
                    try:
                        line.unblockContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(mid)
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.mid not in cids and contact.mid in deleted:
                        continue
                    no += 1
                    try:
                        line.unblockContact(contact.mid)
                        name = contact.displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(contact.mid)
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.mid not in cids and contact.mid in deleted:
                            continue
                        no += 1
                        try:
                            line.unblockContact(contact.mid)
                            name = contact.displayName
                        except TalkException:
                            name = 'Unknown'
                        res += '\n│ %i. %s' % (no, name)
                        deleted.append(contact.mid)
                    elif name.lower() == 'all':
                        for contact in contacts:
                            if contact.mid not in cids and contact.mid in deleted:
                                continue
                            no += 1
                            try:
                                line.unblockContact(contact.mid)
                                name = contact.displayName
                            except TalkException:
                                name = 'Unknown'
                            res += '\n│ %i. %s' % (no, name)
                            deleted.append(contact.mid)
                            time.sleep(0.8)
                    else:
                        line.sendMessage(to, 'ไม่สามารถปลดบล็อกรายชื่อนี้ได้ `%s`, ชื่อไม่อยู่ในรายการ ♪' % name)
            if no == 0: res += '\n│ Nothing'
            res += '\n╰───「SelfBot ProtectV2.2」'
            line.sendMessage(to, res)
        else:
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))

    elif msg.text.lower() == ".getjoined":
        line.sendMessage(to,"กรุณารอสักครู่ ใจเย็นๆ")
        all = line.getGroupIdsJoined()
        text = ""
        cnt = 0
        for i in all:
            text += line.getGroup(i).name + "\n" + i + "\n\n"
            cnt += 1
            if cnt == 10:
                line.sendMessage(to,text[:-2])
                text = ""
                cnt = 0
        line.sendMessage(to,text[:-2])
        cnt = 0
    elif "kickejoinid " in msg.text.lower():
        spl = re.split("kickejoinid ",msg.text,flags=re.IGNORECASE)
        if spl[0] == "":
            gid = spl[1]
            x = line.getGroup(gid)
            if Amid not in [i.mid for i in x.members]:
                if x.preventedJoinByTicket == False:
                    ticket = line.reissueGroupTicket(gid)
                    kicker.acceptGroupInvitationByTicket(gid,ticket)
                    kicker2.acceptGroupInvitationByTicket(gid,ticket)
                    kicker3.acceptGroupInvitationByTicket(gid,ticket)
                    kicker4.acceptGroupInvitationByTicket(gid,ticket)
                    kicker5.acceptGroupInvitationByTicket(gid,ticket)
                    kicker6.acceptGroupInvitationByTicket(gid,ticket)
                    kicker7.acceptGroupInvitationByTicket(gid,ticket)
                    kicker8.acceptGroupInvitationByTicket(gid,ticket)
                    kicker9.acceptGroupInvitationByTicket(gid,ticket)
                    kicker10.acceptGroupInvitationByTicket(gid,ticket)
                else:
                    sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                    if sirilist == []:
                        x.preventedJoinByTicket = False
                        line.updateGroup(x)
                        ticket = line.reissueGroupTicket(gid)
                        kicker.acceptGroupInvitationByTicket(gid,ticket)
                        kicker2.acceptGroupInvitationByTicket(gid,ticket)
                        kicker3.acceptGroupInvitationByTicket(gid,ticket)
                        kicker4.acceptGroupInvitationByTicket(gid,ticket)
                        kicker5.acceptGroupInvitationByTicket(gid,ticket)
                        kicker6.acceptGroupInvitationByTicket(gid,ticket)
                        kicker7.acceptGroupInvitationByTicket(gid,ticket)
                        kicker8.acceptGroupInvitationByTicket(gid,ticket)  
                        kicker9.acceptGroupInvitationByTicket(gid,ticket)
                        kicker10.acceptGroupInvitationByTicket(gid,ticket)
                        kicker.sendMessage(gid,"โหมดคุ้มกันแอดมินทำงาน (｀・ω・´)")                               
                    else:
                        line.inviteIntoGroup(gid,[Amid])
                        x.preventedJoinByTicket = True
                        line.updateGroup(x)
                    kicker.sendMessage(gid,"โหมดคุ้มกันแอดมินทำงาน (｀・ω・´)")                        
            else:
                line.sendMessage(to,"kicker อยู่ในกลุ่มอยู่แล้ว")
    elif cmd == "^^":
        if wait["selfbot"] == True:
            if msg._from in admin:        
                if msg.toType == 2:
                    x = line.getGroup(msg.to)
                    if x.preventedJoinByTicket:
                        x.preventedJoinByTicket = False
                        line.updateGroup(x)
                    Ticket = line.reissueGroupTicket(msg.to)
                    kicker.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker5.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker6.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker7.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker8.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker9.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker10.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker11.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker12.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker13.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker14.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker15.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker16.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker17.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker18.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker19.acceptGroupInvitationByTicket(msg.to,Ticket)
                    kicker20.acceptGroupInvitationByTicket(msg.to,Ticket) 
                    G = kicker.getGroup(msg.to)                   
                    G.preventedJoinByTicket = True                  
                    random.choice(ABC).updateGroup(G) 
                    kicker.sendMessage(msg.to,"โหมดคุ้มกันแอดมินทำงาน (｀・ω・´)")
    elif "kickerleave " in msg.text.lower():
        spl = re.split("kickerleave ",msg.text,flags=re.IGNORECASE)
        if spl[0] == "":
            try:
                kicker.leaveGroup(spl[1])
                kicker2.leaveGroup(spl[1])
                kicker3.leaveGroup(spl[1])
                kicker4.leaveGroup(spl[1])
                kicker5.leaveGroup(spl[1])
                kicker6.leaveGroup(spl[1])
                kicker7.leaveGroup(spl[1])
                kicker8.leaveGroup(spl[1])
                kicker9.leaveGroup(spl[1])   
                kicker10.leaveGroup(spl[1])                                                                         
            except Exception as e:
                line.sendMessage(to,str(e))
#===========BOT UPDATE============#
    elif msg.text.lower().startswith("mentionall"):
      if msg._from in admin:						
        data = msg.text[len("mentionall"):].strip()
        if data == "":
            group = line.getGroup(msg.to)
            nama = [contact.mid for contact in group.members if contact.mid != zxcvzx]
            cb = ""
            cb2 = ""
            count = 1
            strt = len(str(count)) + 2
            akh = int(0)
            cnt = 0
            for md in nama:
                akh = akh + len(str(count)) + 2 + 5
                cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                strt = strt + len(str(count+1)) + 2 + 6
                akh = akh + 1
                cb2 += str(count)+". @name\n"
                cnt = cnt + 1
                if cnt == 20:
                            cb = (cb[:int(len(cb)-1)])
                            cb2 = cb2[:-1]
                            msg.contentType = 0
                            msg.text = cb2
                            msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                            try:
                                line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                            except:
                                line.sendMessage(msg.to,"[[NO MENTION]]")
                            cb = ""
                            cb2 = ""
                            strt = len(str(count)) + 2
                            akh = int(0)
                            cnt = 0
                count += 1
            cb = (cb[:int(len(cb)-1)])
            cb2 = cb2[:-1]
            msg.contentType = 0
            msg.text = cb2
            msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
            try:
                line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
            except:
                line.sendMessage(msg.to,"[[NO MENTION]]")
        elif data[0] == "<":
            mentargs = int(data[1:].strip())
            group = line.getGroup(msg.to)
            nama = [contact.mid for contact in group.members if contact.mid != zxcvzx]
            cb = ""
            cb2 = ""
            count = 1
            strt = len(str(count)) + 2
            akh = int(0)
            cnt = 0
            for md in nama:
                if count > mentargs:
                            break
                akh = akh + len(str(count)) + 2 + 5
                cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                strt = strt + len(str(count+1)) + 2 + 6
                akh = akh + 1
                cb2 += str(count)+". @name\n"
                cnt = cnt + 1
                if cnt == 20:
                            cb = (cb[:int(len(cb)-1)])
                            cb2 = cb2[:-1]
                            msg.contentType = 0
                            msg.text = cb2
                            msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                            try:
                                line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                            except:
                                line.sendMessage(msg.to,"[[NO MENTION]]")
                            cb = ""
                            cb2 = ""
                            strt = len(str(count)) + 2
                            akh = int(0)
                            cnt = 0
                count += 1
            cb = (cb[:int(len(cb)-1)])
            cb2 = cb2[:-1]
            msg.contentType = 0
            msg.text = cb2
            msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
            try:
                line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
            except:
                line.sendMessage(msg.to,"[[NO MENTION]]")
        elif data[0] == ">":
            mentargs = int(data[1:].strip())
            group = line.getGroup(msg.to)
            nama = [contact.mid for contact in group.members if contact.mid != zxcvzx]
            cb = ""
            cb2 = ""
            count = 1
            if mentargs >= 0:
                strt = len(str(mentargs)) + 2
            else:
                strt = len(str(count)) + 2
            akh = int(0)
            cnt = 0
            for md in nama:
                if count < mentargs:
                            count += 1
                            continue
                akh = akh + len(str(count)) + 2 + 5
                cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                strt = strt + len(str(count+1)) + 2 + 6
                akh = akh + 1
                cb2 += str(count)+". @name\n"
                cnt = cnt + 1
                if cnt == 20:
                            cb = (cb[:int(len(cb)-1)])
                            cb2 = cb2[:-1]
                            msg.contentType = 0
                            msg.text = cb2
                            msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                            try:
                                line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                            except:
                                line.sendMessage(msg.to,"[[NO MENTION]]")
                            cb = ""
                            cb2 = ""
                            strt = len(str(count)) + 2
                            akh = int(0)
                            cnt = 0
                count += 1
            cb = (cb[:int(len(cb)-1)])
            cb2 = cb2[:-1]
            msg.contentType = 0
            msg.text = cb2
            msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
            try:
                line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
            except:
                line.sendMessage(msg.to,"[[NO MENTION]]")
        elif data[0] == "=":
            mentargs = int(data[1:].strip())
            group = line.getGroup(msg.to)
            nama = [contact.mid for contact in group.members if contact.mid != zxcvzx]
            cb = ""
            cb2 = ""
            count = 1
            akh = int(0)
            cnt = 0
            for md in nama:
                if count != mentargs:
                            count += 1
                            continue
                akh = akh + len(str(count)) + 2 + 5
                strt = len(str(count)) + 2
                cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                strt = strt + len(str(count+1)) + 2 + 6
                akh = akh + 1
                cb2 += str(count)+". @name\n"
                cnt = cnt + 1
                if cnt == 20:
                            cb = (cb[:int(len(cb)-1)])
                            cb2 = cb2[:-1]
                            msg.contentType = 0
                            msg.text = cb2
                            msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                            try:
                                line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                            except:
                                line.sendMessage(msg.to,"[[NO MENTION]]")
                            cb = ""
                            cb2 = ""
                            strt = len(str(count)) + 2
                            akh = int(0)
                            cnt = 0
                count += 1
            cb = (cb[:int(len(cb)-1)])
            cb2 = cb2[:-1]
            msg.contentType = 0
            msg.text = cb2
            msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
            try:
                line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
            except:
                line.sendMessage(msg.to,"[[NO MENTION]]")
    elif cmd == 'groupinfo':
        if msg.toType != 2: return line.sendMessage(to, 'ไม่สามารถดูข้อมูลกลุ่มได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        group = line.getGroup(to)
        try:
            ccreator = group.creator.mid
            gcreator = group.creator.displayName
        except:
            ccreator = None
            gcreator = 'Not found'
        if not group.invitee:
            pendings = 0
        else:
            pendings = len(group.invitee)
        qr = 'Close' if group.preventedJoinByTicket else 'Open'
        if group.preventedJoinByTicket:
            ticket = 'Not found'
        else:
            ticket = 'https://line.me/R/ti/g/' + str(line.reissueGroupTicket(group.id))
        created = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(group.createdTime) / 1000))
        path = 'http://dl.profile.line-cdn.net/' + group.pictureStatus
        res = '╭───「 Group Info 」'
        res += '\n├ ID : ' + group.id
        res += '\n├ Name : ' + group.name
        res += '\n├ Creator : ' + gcreator
        res += '\n├ Created Time : ' + created
        res += '\n├ Member Count : ' + str(len(group.members))
        res += '\n├ Pending Count : ' + str(pendings)
        res += '\n├ QR Status : ' + qr
        res += '\n├ Ticket : ' + ticket
        res += '\n╰───「SelfBot ProtectV2.2」'
        line.sendImageWithURL(to, path)
        if ccreator:
            line.sendContact(to, ccreator)
        line.sendMessage(to, res)
    elif cmd.startswith('grouplist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        gids = line.getGroupIdsJoined()
        gnames = []
        ress = []
        res = '╭───「 Group List 」'
        res += '\n├ List:'
        if gids:
            groups = line.getGroups(gids)
            no = 0
            if len(groups) > 200:
                parsed_len = len(groups)//200+1
                for point in range(parsed_len):
                    for group in groups[point*200:(point+1)*200]:
                        no += 1
                        res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                        gnames.append(group.name)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for group in groups:
                    no += 1
                    res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                    gnames.append(group.name)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}GroupList'
        res += '\n│ • {key}GroupList Leave <num/name/all>'
        res += '\n╰───「SelfBot ProtectV2.2」'
        ress.append(res)
        if cmd == 'grouplist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('leave '):
            texts = textt[6:].split(', ')
            leaved = []
            if not gids:
                return line.sendMessage(to, 'ไม่สามารถออกลุ่มได้\nไม่พบชื่อกลุ่มนี้')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in leaved:
                            line.sendMessage(to, 'ออกจากลุ่มเรียบร้อย %s' % group.name)
                            continue
                        kicker.leaveGroup(group.id)
                        leaved.append(group.id)
                        if to not in leaved:
                            line.sendMessage(to, 'ออกจากลุ่มเรียบร้อย %s' % group.name)
                    else:
                        line.sendMessage(to, 'Failed leave group number %i, เลขเกิน!' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in leaved:
                            line.sendMessage(to, 'ออกจากลุ่มเรียบร้อย %s' % group.name)
                            continue
                        kicker.leaveGroup(group.id)
                        leaved.append(group.id)
                        if to not in leaved:
                            line.sendMessage(to, 'ออกจากลุ่มเรียบร้อย %s' % group.name)
                    elif name.lower() == 'all':
                        for gid in gids:
                            if gid in leaved:
                                continue
                            kicker.leaveGroup(gid)
                            kicker2.leaveGroup(gid)
                            kicker3.leaveGroup(gid)
                            kicker4.leaveGroup(gid)
                            kicker5.leaveGroup(gid)
                            kicker6.leaveGroup(gid)
                            kicker7.leaveGroup(gid)
                            kicker8.leaveGroup(gid)
                            kicker9.leaveGroup(gid)
                            kicker10.leaveGroup(gid)                            
                            leaved.append(gid)
                            #time.sleep(0.8)
                        if to not in leaved:
                            line.sendMessage(to, 'ออกทุกกลุ่มเรียบร้อย ♪')
                    else:
                        line.sendMessage(to, 'ไม่สามารถออกกลุ่มชื่อ `%s`นี้ได้\nไม่พบชื่อกลุ่มนี้ ♪' % name)
        else:
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('invitationlist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        gids = line.getGroupIdsInvited()
        gnames = []
        ress = []
        res = '╭───「 Invitation List 」'
        res += '\n├ List:'
        if gids:
            groups = line.getGroups(gids)
            no = 0
            if len(groups) > 200:
                parsed_len = len(groups)//200+1
                for point in range(parsed_len):
                    for group in groups[point*200:(point+1)*200]:
                        no += 1
                        res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                        gnames.append(group.name)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for group in groups:
                    no += 1
                    res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                    gnames.append(group.name)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}InvitationList'
        res += '\n│ • {key}InvitationList Accept <num/name/all>'
        res += '\n│ • {key}InvitationList Reject <num/name/all>'
        res += '\n╰───「SelfBot ProtectV2.2」'
        ress.append(res)
        if cmd == 'invitationlist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('accept '):
            texts = textt[7:].split(', ')
            accepted = []
            if not gids:
                return line.sendMessage(to, 'ไม่สามารถเข้าร่วมกลุ่มได้\nไม่มีคำเชิญเข้ากลุ่ม')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in accepted:
                            line.sendMessage(to, 'ทำการเข้าร่วมกลุ่ม %s' % group.name)
                            continue
                        line.acceptGroupInvitation(group.id)
                        accepted.append(group.id)
                        line.sendMessage(to, 'ทำการเข้าร่วมกลุ่ม %s' % group.name)
                    else:
                        line.sendMessage(to, 'ไม่สามารถเข้าร่วมกลุ่มได้ เนื่องจากมายเลข %i นี้มากว่าคำเชิญที่คุณมี' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in accepted:
                            line.sendMessage(to, 'ทำการเข้าร่วมกลุ่ม %s' % group.name)
                            continue
                        line.acceptGroupInvitation(group.id)
                        accepted.append(group.id)
                        line.sendMessage(to, 'ทำการเข้าร่วมกลุ่ม %s' % group.name)
                    elif name.lower() == 'all':
                        for gid in gids:
                            if gid in accepted:
                                continue
                            line.acceptGroupInvitation(gid)
                            accepted.append(gid)
                            time.sleep(0.8)
                        line.sendMessage(to, 'ทำการเข้าร่วมกลุ่มทั้งหมดแล้ว ♪')
                    else:
                        line.sendMessage(to, 'ไม่สามารถเข้าร่วมกลุ่มได้ `%s`, ไม่พบชื่อกลุ่มนี้ ♪' % name)
        elif texttl.startswith('reject '):
            texts = textt[7:].split(', ')
            rejected = []
            if not gids:
                return line.sendMessage(to, 'ไม่สามารถคำเชิญเข้าร่วมกลุ่มได้\nไม่มีคำเชิญเข้าร่วมกลุ่ม')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in rejected:
                            line.sendMessage(to, 'ทำการยกเลิกค้างเชิญ %s' % group.name)
                            continue
                        line.rejectGroupInvitation(group.id)
                        rejected.append(group.id)
                        line.sendMessage(to, 'ทำการยกเลิกค้างเชิญ %s' % group.name)
                    else:
                        line.sendMessage(to, 'ไม่สามายกเลิกค้างเชิญหมายเลข %iนี้ได้เนื่องจากเลขเกิน!' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in rejected:
                            line.sendMessage(to, 'ทำการยกเลิกค้างเชิญ %s' % group.name)
                            continue
                        line.rejectGroupInvitation(group.id)
                        rejected.append(group.id)
                        line.sendMessage(to, 'ทำการยกเลิกค้างเชิญ %s' % group.name)
                    elif name.lower() == 'all':
                        for gid in gids:
                            if gid in rejected:
                                continue
                            line.rejectGroupInvitation(gid)
                            rejected.append(gid)
                            time.sleep(0.8)
                        line.sendMessage(to, 'ยกเลิกคำเชิญเข้าร่วมกลุ่มทั้งหมดแล้ว ♪')
                    else:
                        line.sendMessage(to, 'ไม่สามารถยกเลิกคำเชิญเข้าร่วมกลุ่มชื่อ`%s`นี้ได้เนื่องจากไม่พบชื่อกลุ่มนี้ ♪' % name)
        else:
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd == 'memberlist':
        if msg.toType == 1:
            room = line.getRoom(to)
            members = room.contacts
        elif msg.toType == 2:
            group = line.getGroup(to)
            members = group.members
        else:
            return line.sendMessage(to, 'ไม่สามารถแสดงจำนวนสมาชิกในกลุ่มได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        if not members:
            return line.sendMessage(to, 'ไม่สามารถแสดงจำนวนสมาชิกในกลุ่มได้\nไม่มีสมาชิกในกลุ่ม')
        res = '╭───「 Member List 」'
        parsed_len = len(members)//200+1
        no = 0
        for point in range(parsed_len):
            for member in members[point*200:(point+1)*200]:
                no += 1
                res += '\n│ %i. %s' % (no, member.displayName)
                if member == members[-1]:
                    res += '\n╰───「SelfBot ProtectV2.2」'
            if res:
                if res.startswith('\n'): res = res[1:]
                line.sendMessage(to, res)
            res = ''
    elif cmd == 'pendinglist':
        if msg.toType != 2: return line.sendMessage(to, 'ไม่สามารถแสดงจำนวนค้างเชิญในกลุ่มได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        group = line.getGroup(to)
        members = group.invitee
        if not members:
            return line.sendMessage(to, 'ไม่สามารถแสดงจำนวนค้างเชิญในกลุ่มได้\nไม่พบค้างเชิญ')
        res = '╭───「 Pending List 」'
        parsed_len = len(members)//200+1
        no = 0
        for point in range(parsed_len):
            for member in members[point*200:(point+1)*200]:
                no += 1
                res += '\n│ %i. %s' % (no, member.displayName)
                if member == members[-1]:
                    res += '\n╰───「SelfBot ProtectV2.2」'
            if res:
                if res.startswith('\n'): res = res[1:]
                line.sendMessage(to, res)
            res = ''
    elif cmd == 'openqr':
        if msg.toType != 2: return line.sendMessage(to, 'ไม่สามารถเปิดลิ้งกลุ่มได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        group = line.getGroup(to)
        group.preventedJoinByTicket = False
        line.updateGroup(group)
        line.sendMessage(to, 'เปิดลิ้งกลุ่มแล้ว')
    elif "im " in msg.text.lower():
        query = msg.text.replace("im ","")
        r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
        data=r.text
        data=json.loads(r.text)
        if data != []:
            for food in data:
                line.sendImageWithURL(msg.to, str(food["url"]))                
    elif msg.text.lower() == "/gift":
        msg.contentType = 9
        msg.contentMetadata={'PRDID': '','PRDTYPE': 'THEME','MSGTPL': '1'}
        msg.text = None
        line.sendMessage(msg.to,text = None,contentMetadata={'PRDID': themeid,'PRDTYPE': 'THEME','MSGTPL': '1'},contentType = 9)
    elif "/gift " in msg.text.lower():
        red = re.compile(re.escape('.gift '),re.IGNORECASE)
        themeid = red.sub('',msg.text)
        msg.contentType = 9
        msg.contentMetadata={'PRDID': themeid,'PRDTYPE': 'THEME','MSGTPL': '1'}
        msg.text = None
        line.sendMessage(msg.to,text = None,contentMetadata={'PRDID': themeid,'PRDTYPE': 'THEME','MSGTPL': '1'},contentType = 9)
    elif msg.text.lower() == "weather:chiangmai":
        if msg.toType != 0:
            data_output(msg.to,data_organizer(data_fetch(url_builder(1153670))),1)
        else:
            data_output(msg.from_,data_organizer(data_fetch(url_builder(1153670))),1)
    elif msg.text.lower() == "weather:ubonratchathani":
        if msg.toType != 0:
            data_output(msg.to,data_organizer(data_fetch(url_builder(1605245))),2)
        else:
            data_output(msg.from_,data_organizer(data_fetch(url_builder(1605245))),2)
    elif msg.text.lower() == "weather:bangkok":
        if msg.toType != 0:
            data_output(msg.to,data_organizer(data_fetch(url_builder(1609350))),3)
        else:
            data_output(msg.from_,data_organizer(data_fetch(url_builder(1609350))),3)
    elif msg.text.lower() == "weather:phetchabun":
        if msg.toType != 0:
            data_output(msg.to,data_organizer(data_fetch(url_builder(1607737))),4)
        else:
            data_output(msg.from_,data_organizer(data_fetch(url_builder(1607737))),4)
    elif msg.text.lower() == "weather:khon kaen":
        if msg.toType != 0:
            data_output(msg.to,data_organizer(data_fetch(url_builder(1609776))),5)
        else:
            data_output(msg.from_,data_organizer(data_fetch(url_builder(1609776))),5)  
    elif msg.text.lower() == "weather:ayutthaya":
        if msg.toType != 0:
            data_output(msg.to,data_organizer(data_fetch(url_builder(1607532))),6)
        else:
            data_output(msg.from_,data_organizer(data_fetch(url_builder(1607532))),6)                                                                      
    elif msg.text.lower() in ["weather"]:
        if msg.toType != 0:
            line.sendMessage(msg.to,"สภาพอากาศในแต่ละจังหวัด\n- chiangmai\n- ubonratchathani\n- bangkok\n- phetchabun\n-khon kaen\n-ayutthaya\nพิมพ์ \"weather:[ชื่อจังหวัด]\" เพื่อดูข้อมูลสภาพอากาศ")
        else:
            line.sendMessage(msg.to,"สภาพอากาศในแต่ละจังหวัด\n- chiangmai\n- ubonratchathani\n- bangkok\n- phetchabun\n-khon kaen\n-ayutthaya\nพิมพ์ \"weather:[ชื่อจังหวัด]\" เพื่อดูข้อมูลสภาพอากาศ")

#-----------------------------------------------------------

    elif msg.text.lower().startswith(".recall"):
        if msg.toType == 2:
            reps = int(msg.text.split(" ")[1])
            asup = [g1.adityasplittext(msg.text,'s').replace('{} '.format(reps),'')]*reps
            if 'MENTION' in msg.contentMetadata.keys()!=None:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                nama = [key1]
                g1.sendMessage(to,"กำลังดำเนินการ...")
                babu = [g1.call.inviteIntoGroupCall(to,nama,mediaType=2) for babu in asup] ; g1.sendMessage(to,"เชิญคอลสำเร็จแล้ว!")
            else:
                g1.sendMessage(to,"กำลังดำเนินการ...")
                group = g1.getGroup(to);nama = [contact.mid for contact in group.members]; babu = [g1.call.inviteIntoGroupCall(to,nama,mediaType=2) for babu in asup] ; g1.sendMessage(to,"เชิญคอลสำเร็จแล้ว!")
        else:
            g1.sendMessage(to,"คำสั่งนี้สามารถใช้ได้เฉพาะกลุ่ม")

    elif cmd.startswith("spaminv "):
        aa = cmd.replace("spaminv ","")						
        bb = aa.split("-")
        count = int(bb[0])
        name = str(bb[1])
        target = bb[2]
        grup = kicker.groups
        try:
            kicker.findAndAddContactsByMid(target)
        except:
            pass
        for anu in range(count):
            kicker.createGroup(name, [target])
            for i in grup:
                group = kicker.getGroup(i)
                if group.name == name:
                    kicker.inviteIntoGroup(group.id, [target])
            print("Inviting to group %s"%anu)
        print("Sukses mank")
        line.sendMessage(msg.to, "Success invite %s\nGroup : %s\nCount : %s"%(kicker.getContact(target).displayName, name, count))

    elif cmd.startswith("spaminv2 "):
        aa = cmd.replace("spaminv2 ","")						
        bb = aa.split("-")
        count = int(bb[0])
        name = str(bb[1])
        target = bb[2]
        grup = kicker2.groups
        try:
            kicker2.findAndAddContactsByMid(target)
        except:
            pass
        for anu in range(count):
            kicker2.createGroup(name, [target])
            for i in grup:
                group = kicker2.getGroup(i)
                if group.name == name:
                    kicker2.inviteIntoGroup(group.id, [target])
            print("Inviting to group %s"%anu)
        print("Sukses mank")
        line.sendMessage(msg.to, "Success invite %s\nGroup : %s\nCount : %s"%(kicker2.getContact(target).displayName, name, count))

    elif cmd.startswith("spaminv3 "):
        aa = cmd.replace("spaminv3 ","")						
        bb = aa.split("-")
        count = int(bb[0])
        name = str(bb[1])
        target = bb[2]
        grup = kicker3.groups
        try:
            kicker3.findAndAddContactsByMid(target)
        except:
            pass
        for anu in range(count):
            kicker3.createGroup(name, [target])
            for i in grup:
                group = kicker3.getGroup(i)
                if group.name == name:
                    kicker3.inviteIntoGroup(group.id, [target])
            print("Inviting to group %s"%anu)
        print("Sukses mank")
        line.sendMessage(msg.to, "Success invite %s\nGroup : %s\nCount : %s"%(kicker3.getContact(target).displayName, name, count))

    elif cmd.startswith("spaminv4 "):
        aa = cmd.replace("spaminv4 ","")						
        bb = aa.split("-")
        count = int(bb[0])
        name = str(bb[1])
        target = bb[2]
        grup = kicker4.groups
        try:
            kicker4.findAndAddContactsByMid(target)
        except:
            pass
        for anu in range(count):
            kicker4.createGroup(name, [target])
            for i in grup:
                group = kicker4.getGroup(i)
                if group.name == name:
                    kicker4.inviteIntoGroup(group.id, [target])
            print("Inviting to group %s"%anu)
        print("Sukses mank")
        line.sendMessage(msg.to, "Success invite %s\nGroup : %s\nCount : %s"%(kicker4.getContact(target).displayName, name, count))


    elif cmd.startswith("spaminv5 "):
        aa = cmd.replace("spaminv5 ","")						
        bb = aa.split("-")
        count = int(bb[0])
        name = str(bb[1])
        target = bb[2]
        grup = kicker5.groups
        try:
            kicker5.findAndAddContactsByMid(target)
        except:
            pass
        for anu in range(count):
            kicker5.createGroup(name, [target])
            for i in grup:
                group = kicker5.getGroup(i)
                if group.name == name:
                    kicker5.inviteIntoGroup(group.id, [target])
            print("Inviting to group %s"%anu)
        print("Sukses mank")
        line.sendMessage(msg.to, "Success invite %s\nGroup : %s\nCount : %s"%(kicker5.getContact(target).displayName, name, count))

    elif cmd.startswith("spaminv6 "):
        aa = cmd.replace("spaminv6 ","")						
        bb = aa.split("-")
        count = int(bb[0])
        name = str(bb[1])
        target = bb[2]
        grup = kicker6.groups
        try:
            kicker6.findAndAddContactsByMid(target)
        except:
            pass
        for anu in range(count):
            kicker6.createGroup(name, [target])
            for i in grup:
                group = kicker6.getGroup(i)
                if group.name == name:
                    kicker6.inviteIntoGroup(group.id, [target])
            print("Inviting to group %s"%anu)
        print("Sukses mank")
        line.sendMessage(msg.to, "Success invite %s\nGroup : %s\nCount : %s"%(kicker6.getContact(target).displayName, name, count))

    elif cmd.startswith("spaminv7 "):
        aa = cmd.replace("spaminv7 ","")						
        bb = aa.split("-")
        count = int(bb[0])
        name = str(bb[1])
        target = bb[2]
        grup = kicker7.groups
        try:
            kicker7.findAndAddContactsByMid(target)
        except:
            pass
        for anu in range(count):
            kicker8.createGroup(name, [target])
            for i in grup:
                group = kicker8.getGroup(i)
                if group.name == name:
                    kicker8.inviteIntoGroup(group.id, [target])
            print("Inviting to group %s"%anu)
        print("Sukses mank")
        line.sendMessage(msg.to, "Success invite %s\nGroup : %s\nCount : %s"%(kicker7.getContact(target).displayName, name, count))

    elif cmd.startswith("spaminv8 "):
        aa = cmd.replace("spaminv8 ","")						
        bb = aa.split("-")
        count = int(bb[0])
        name = str(bb[1])
        target = bb[2]
        grup = kicker9.groups
        try:
            kicker9.findAndAddContactsByMid(target)
        except:
            pass
        for anu in range(count):
            kicker9.createGroup(name, [target])
            for i in grup:
                group = kicker9.getGroup(i)
                if group.name == name:
                    kicker9.inviteIntoGroup(group.id, [target])
            print("Inviting to group %s"%anu)
        print("Sukses mank")
        line.sendMessage(msg.to, "Success invite %s\nGroup : %s\nCount : %s"%(kicker9.getContact(target).displayName, name, count))

    elif cmd.startswith("spaminv9 "):
        aa = cmd.replace("spaminv9 ","")						
        bb = aa.split("-")
        count = int(bb[0])
        name = str(bb[1])
        target = bb[2]
        grup = kicker10.groups
        try:
            kicker10.findAndAddContactsByMid(target)
        except:
            pass
        for anu in range(count):
            kicker10.createGroup(name, [target])
            for i in grup:
                group = kicker10.getGroup(i)
                if group.name == name:
                    kicker10.inviteIntoGroup(group.id, [target])
            print("Inviting to group %s"%anu)
        print("Sukses mank")
        line.sendMessage(msg.to, "Success invite %s\nGroup : %s\nCount : %s"%(kicker10.getContact(target).displayName, name, count))

    elif cmd.startswith("spaminv10 "):
        aa = cmd.replace("spaminv10 ","")						
        bb = aa.split("-")
        count = int(bb[0])
        name = str(bb[1])
        target = bb[2]
        grup = g1.groups
        try:
            g1.findAndAddContactsByMid(target)
        except:
            pass
        for anu in range(count):
            g1.createGroup(name, [target])
            for i in grup:
                group = g1.getGroup(i)
                if group.name == name:
                    g1.inviteIntoGroup(group.id, [target])
            print("Inviting to group %s"%anu)
        print("Sukses mank")
        line.sendMessage(msg.to, "Success invite %s\nGroup : %s\nCount : %s"%(g1.getContact(target).displayName, name, count))                                


    elif cmd.startswith("spaminv11 "):
        aa = cmd.replace("spaminv11 ","")						
        bb = aa.split("-")
        count = int(bb[0])
        name = str(bb[1])
        target = bb[2]
        grup = kicker7.groups
        try:
            kicker7.findAndAddContactsByMid(target)
        except:
            pass
        for anu in range(count):
            kicker7.createGroup(name, [target])
            for i in grup:
                group = kicker7.getGroup(i)
                if group.name == name:
                    kicker7.inviteIntoGroup(group.id, [target])
            print("Inviting to group %s"%anu)
        print("Sukses mank")
        line.sendMessage(msg.to, "Success invite %s\nGroup : %s\nCount : %s"%(kicker7.getContact(target).displayName, name, count))        

    elif cmd.startswith("lifftest"):
            sep = text.split(" ")
            search = text.replace(sep[0] + " ","")
            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
            data = r.text
            a = json.loads(data)
            if a["items"] != []:
                ret_ = []
                yt = []
                for music in a["items"]:
                    ret_.append({"thumbnailImageUrl": 'https://i.ytimg.com/vi/{}/maxresdefault.jpg'.format(music['id']['videoId']),"imageSize": "contain","imageAspectRatio": "square","title": '{}'.format(str(music['snippet']['title'][:40])),"text": '{}'.format(str(music['snippet']['channelTitle'][:15])),"actions": [{"type": "uri","label": "Go Page","uri": 'https://www.youtube.com/watch?v=' +music['id']['videoId']}]})
                    yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                k = len(ret_)//10
                for aa in range(k+1):
                    data = {"type": "template","altText": "Youtube","template": {"type": "carousel","columns": ret_[aa*10 : (aa+1)*10]}}
                    sendflex(to, data) 
    elif ".s " in msg.text.lower():
        spl = re.split(".s ",msg.text,flags=re.IGNORECASE)
        if spl[0] == "":
            try:
                line.sendMessage(to,subprocess.getoutput(spl[1]))
            except:
                pass                    
    elif cmd == 'closeqr':
        if msg.toType != 2: return line.sendMessage(to, 'ไม่สามารถเปิดลิ้งกลุ่มได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        group = line.getGroup(to)
        group.preventedJoinByTicket = True
        line.updateGroup(group)
        line.sendMessage(to, 'ปิดลิ้งกลุ่มแล้ว')
    elif cmd.startswith('changegroupname '):
        if msg.toType != 2: return line.sendMessage(to, 'ไม่สามารถเปลี่ยนชื่อกลุ่มได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        group = line.getGroup(to)
        gname = removeCmd(text, setKey)
        if len(gname) > 50:
            return line.sendMessage(to, 'ไม่สามารถเปลี่ยนชื่อกลุ่มได้\nชื่อกลุ่มต้องไม่เกิน 50')
        group.name = gname
        line.updateGroup(group)
        line.sendMessage(to, 'เปลี่ยนชื่อกลุ่มเป็น `%s`' % gname)
    elif cmd == 'changegrouppict':
        if msg.toType != 2: return line.sendMessage(to, 'ไม่สามารถเปลี่ยนรุปกลุ่มได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        if to not in settings['changeGroupPicture']:
            settings['changeGroupPicture'].append(to)
            line.sendMessage(to, 'กรุณาส่งภาพ, พิม `{key}Abort` ถ้าต้องการยกเลิก\nคำเตือน:การดาวน์โหลดภาพจะล้มเหลวหากอัพโหลดภาพนานเกินไป'.format(key=setKey.title()))
        else:
            line.sendMessage(to, 'คำสั่งนี้ถูกงานอยู่แล้ว, กรุณาส่งภาพ หรือ พิม `{key}Abort` ถ้าต้องการยกเลิก\nคำเตือน:การดาวน์โหลดภาพจะล้มเหลวหากอัพโหลดภาพนานเกินไป'.format(key=setKey.title()))
    elif cmd == 'kickall':
        if msg.toType != 2: return line.sendMessage(to, 'ไม่สามารถเตะสมาชิกทั้งหมดได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        group = line.getGroup(to)
        if not group.members:
            return line.sendMessage(to, 'ไม่สามารถเตะสมาชิกทั้งหมดได้\nไม่มีคนไห้เตะ')
        for member in group.members:
            if member.mid == myMid:
                continue
            try:
                line.kickoutFromGroup(to, [member.mid])
            except TalkException as talk_error:
                return line.sendMessage(to, 'ไม่สามารถเตะสมาชิกทั้งหมดได้เนื่องจาก `%s`' % talk_error.reason)
            time.sleep(0.8)
        line.sendMessage(to, 'เตะสมาชิกทั้งหมด, จำนวน %i คน' % len(group.members))
    elif cmd == 'cancelall':
        if msg.toType != 2: return line.sendMessage(to, 'ไม่สามารถยกเลิกค้างเชิญได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        group = line.getGroup(to)
        if not group.invitee:
            return line.sendMessage(to, 'ไม่สามารถยกเลิกค้างเชิญได้\nไม่มีสมาชิกค้างเชิญ')
        for member in group.invitee:
            if member.mid == myMid:
                continue
            try:
                line.cancelGroupInvitation(to, [member.mid])
            except TalkException as talk_error:
                return line.sendMessage(to, 'ไม่สามารถยกเลิกค้างเชิญได้เนื่องจาก `%s`' % talk_error.reason)
            time.sleep(0.8)
        line.sendMessage(to, 'ยกเลิกค้างเชิญทั้งหมดแล้ว\nจำนวน %i คน' % len(group.invitee))
    elif cmd.startswith('lurk'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if msg.toType in [1, 2] and to not in lurking:
            lurking[to] = {
                'status': False,
                'time': None,
                'members': [],
                'reply': {
                    'status': False,
                    'message': settings['defaultReplyReader']
                }
            }
        res = '╭───「 Lurking 」'
        if msg.toType in [1, 2]: res += '\n├ Status : ' + bool_dict[lurking[to]['status']][1]
        if msg.toType in [1, 2]: res += '\n├ Reply Reader : ' + bool_dict[lurking[to]['reply']['status']][1]
        if msg.toType in [1, 2]: res += '\n├ Reply Reader Message : ' + lurking[to]['reply']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}Lurk'
        res += '\n│ • {key}Lurk <on/off>'
        res += '\n│ • {key}Lurk Result'
        res += '\n│ • {key}Lurk Reset'
        res += '\n│ • {key}Lurk ReplyReader <on/off>'
        res += '\n│ • {key}Lurk ReplyReader <message>'
        res += '\n╰───「SelfBot ProtectV2.2」'
        if cmd == 'lurk':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif msg.toType not in [1, 2]:
            return line.sendMessage(to, 'ไม่สามารถใช้คำสั่งนี้ได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        elif texttl == 'on':
            if lurking[to]['status']:
                line.sendMessage(to, 'เปิดโหมดตรวจจับคนอ่าน')
            else:
                lurking[to].update({
                    'status': True,
                    'time': datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S'),
                    'members': []
                })
                line.sendMessage(to, 'เปิดแล้ว')
        elif texttl == 'off':
            if not lurking[to]['status']:
                line.sendMessage(to, 'ปิดโหมดตรวจจับคนอ่าน')
            else:
                lurking[to].update({
                    'status': False,
                    'time': None,
                    'members': []
                })
                line.sendMessage(to, 'ปิดแล้ว')
        elif texttl == 'result':
            if not lurking[to]['status']:
                line.sendMessage(to, 'รีเช็ตคนอ่านเรียบร้อย')
            else:
                if not lurking[to]['members']:
                    line.sendMessage(to, 'ไม่สามารถรีเช็ตคนอ่านได้\nเนื่องจากไม่พบคนอ่าน')
                else:
                    members = lurking[to]['members']
                    res = '╭───「 Lurking 」'
                    if msg.toType == 2: res += '\n├ Group Name : ' + line.getGroup(to).name
                    parsed_len = len(members)//200+1
                    no = 0
                    for point in range(parsed_len):
                        for member in members[point*200:(point+1)*200]:
                            no += 1
                            try:
                                name = line.getContact(member).displayName
                            except TalkException:
                                name = 'Unknown'
                            res += '\n│ %i. %s' % (no, name)
                            if member == members[-1]:
                                res += '\n│'
                                res += '\n├ Time Set : ' + lurking[to]['time']
                                res += '\n╰───「SelfBot ProtectV2.2」'
                        if res:
                            if res.startswith('\n'): res = res[1:]
                            line.sendMessage(to, res)
                        res = ''
        elif texttl == 'reset':
            if not lurking[to]['status']:
                line.sendMessage(to, 'ไม่สามารถรีเช็ตคนอ่านได้\nยังไม่ได้เปิดโหมดตรวจจับคนอ่าน')
            else:
                lurking[to].update({
                    'status': True,
                    'time': datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S'),
                    'members': []
                })
                line.sendMessage(to, 'รีเช็ตเรียบร้อย')
        elif texttl.startswith('replyreader '):
            texts = textt[12:]
            if texts == 'on':
                if lurking[to]['reply']['status']:
                    line.sendMessage(to, 'ข้อความทักคนอ่านเปิดใช้งานอยู่แล้ว')
                else:
                    lurking[to]['reply']['status'] = True
                    line.sendMessage(to, 'เปิดข้อความทักคนอ่าน')
            elif texts == 'off':
                if not lurking[to]['reply']['status']:
                    line.sendMessage(to, 'ข้อความทักคนอ่านถุกปิดใช้งานอยู่แล้ว')
                else:
                    lurking[to]['reply']['status'] = False
                    line.sendMessage(to, 'ปิดข้อความทักคนอ่าน')
            else:
                lurking[to]['reply']['message'] = texts
                line.sendMessage(to, 'เปลี่ยนข้อความทักคนอ่านเป็น `%s`' % texts)
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('greet'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Greet Message 」'
        res += '\n├ Greetings Join Status : ' + bool_dict[settings['greet']['join']['status']][1]
        res += '\n├ Greetings Join Message : ' + settings['greet']['join']['message']
        res += '\n├ Greetings Leave Status : ' + bool_dict[settings['greet']['leave']['status']][0]
        res += '\n├ Greetings Join Message : ' + settings['greet']['leave']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}Greet'
        res += '\n│ • {key}Greet Join <on/off>'
        res += '\n│ • {key}Greet Join <message>'
        res += '\n│ • {key}Greet Leave <on/off>'
        res += '\n│ • {key}Greet Leave <message>'
        res += '\n╰───「SelfBot ProtectV2.2」'
        if cmd == 'greet':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('join '):
            texts = textt[5:]
            textsl = texts.lower()
            if textsl == 'on':
                if settings['greet']['join']['status']:
                    line.sendMessage(to, 'ข้อความทักคนเข้ากลุ่มถูกเปิดใช้งานอยู่แล้ว')
                else:
                    settings['greet']['join']['status'] = True
                    line.sendMessage(to, 'เปิดข้อความทักคนเข้ากลุ่ม')
            elif textsl == 'off':
                if not settings['greet']['join']['status']:
                    line.sendMessage(to, 'ข้อความทักคนเข้ากลุ่มถูกปิดใช้งานอยู่แล้ว')
                else:
                    settings['greet']['join']['status'] = False
                    line.sendMessage(to, 'ปิดข้อความทักคนเข้ากลุ่ม')
            else:
                settings['greet']['join']['message'] = texts
                line.sendMessage(to, 'เปลี่ยนข้อความทักคนเข้ากลุ่มเป็น `%s`' % texts)
        elif texttl.startswith('leave '):
            texts = textt[6:]
            textsl = texts.lower()
            if textsl == 'on':
                if settings['greet']['leave']['status']:
                    line.sendMessage(to, 'ข้อความทักคนออกกลุ่มถุกเปิดใช้งานอยู่แล้ว')
                else:
                    settings['greet']['leave']['status'] = True
                    line.sendMessage(to, 'เปิดข้อความทักคนออกกลุ่ม')
            elif textsl == 'off':
                if not settings['greet']['leave']['status']:
                    line.sendMessage(to, 'ข้อความทักคนออกกลุ่มถูกปิดใช้งานอยู่แล้ว')
                else:
                    settings['greet']['leave']['status'] = False
                    line.sendMessage(to, 'ปิดข้อความทักคนออกกลุ่ม')
            else:
                settings['greet']['leave']['message'] = texts
                line.sendMessage(to, 'เปลี่ยนข้อความทักคนออกกลุ่มเป็น `%s`' % texts)
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('kick '):
        if msg.toType != 2: return line.sendMessage(to, 'คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น')
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                mid = mention['M']
                if mid == myMid:
                    continue
                try:
                    kicker5.kickoutFromGroup(to, [mid])
                except TalkException as talk_error:
                    return kicker5.sendMessage(to, 'ไม่สามารถเตะสมาชิกได้\nเนื่องจาก `%s`' % talk_error.reason)
                time.sleep(0.8)
            kicker5.sendMessage(to, 'เตะสมาชิกเรียบร้อย\nจำนวน %i คน' % len(mentions['MENTIONEES']))
        else:
            kicker5.sendMessage(to, 'ไม่สามารถเตะสมาชิกได้\nกรุณาแท็กคนที่จะเตะ')
    elif cmd.startswith('vkick '):
        if msg.toType != 2: return line.sendMessage(to, 'คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น')
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                mid = mention['M']
                if mid == myMid:
                    continue
                try:
                    line.kickoutFromGroup(to, [mid])
                    line.findAndAddContactsByMid(mid)
                    line.inviteIntoGroup(to, [mid])
                    line.cancelGroupInvitation(to, [mid])
                except TalkException as talk_error:
                    return line.sendMessage(to, 'ไม่สามารถเตะสมาชิกได้\nเนื่องจาก `%s`' % talk_error.reason)
                time.sleep(0.8)
            line.sendMessage(to, 'เตะสมาชิกเรียบร้อย\nจำนวน %i คน' % len(mentions['MENTIONEES']))
        else:
            line.sendMessage(to, 'ไม่สามารถเตะสมาชิกได้\nกรุณาแท็กคนที่จะเตะ')

def executeOp(op):
    try:
        print ('[* %i ] %s' % (op.type, OpType._VALUES_TO_NAMES[op.type].replace('_', ' ')))
        if op.type == 5:
            if settings['autoAdd']['status']:
                line.findAndAddContactsByMid(op.param1)
            if settings['autoAdd']['reply']:
                if '@!' not in settings['autoAdd']['message']:
                    line.sendMessage(op.param1, settings['autoAdd']['message'])
                else:
                    line.sendMentionV2(op.param1, settings['autoAdd']['message'], [op.param1])
        if op.type == 13:
            if settings['autoJoin']['status'] and myMid in op.param3:
                line.acceptGroupInvitation(op.param1)
                if settings['autoJoin']['reply']:
                    if '@!' not in settings['autoJoin']['message']:
                        line.sendMessage(op.param1, settings['autoJoin']['message'])
                    else:
                        line.sendMentionV2(op.param1, settings['autoJoin']['message'], [op.param2])                        
        if op.type == 15:
            if settings['greet']['leave']['status']:
                if '@!' not in settings['greet']['leave']['message']:
                    line.sendMessage(op.param1, settings['greet']['leave']['message'].format(name=line.getGroup(op.param1).name))
                else:
                    line.sendMentionV2(op.param1, settings['greet']['leave']['message'].format(name=line.getGroup(op.param1).name), [op.param2])
        if op.type == 17:
            if settings['greet']['join']['status']:
                if '@!' not in settings['greet']['join']['message']:
                    line.sendMessage(op.param1, settings['greet']['join']['message'].format(name=line.getGroup(op.param1).name))
                else:
                    line.sendMentionV2(op.param1, settings['greet']['join']['message'].format(name=line.getGroup(op.param1).name), [op.param2])
        if op.type == 11:
            if op.param1 in protectqr:
                    try:
                        if line.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                random.choice(ABC).reissueGroupTicket(op.param1)
                                X = line.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                random.choice(ABC).updateGroup(X)
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        invitor = op.param2
                        gotinvite = []
                        if "\x1e" in op.param3:
                            gotinvite = op.param3.split("\x1e")
                        else:
                            gotinvite.append(op.param3)                        
                        for u in gotinvite:
                            wait["blacklist"][op.param2] = True
                            kicker.cancelGroupInvitation(op.param1,[op.param3])
                            kicker.kickoutFromGroup(op.param1,[op.param2])                              
                    except:
                        try:
                            kicker2.cancelGroupInvitation(op.param1,[op.param3])
                            kicker2.kickoutFromGroup(op.param1,[op.param2]) 
                        except:
                            try:
                                kicker3.cancelGroupInvitation(op.param1,[op.param3])
                                kicker3.kickoutFromGroup(op.param1,[op.param2])     
                            except:
                                try:
                                    kicker4.cancelGroupInvitation(op.param1,[op.param3])
                                    kicker4.kickoutFromGroup(op.param1,[op.param2])     
                                except:
                                    try:
                                        kicker5.cancelGroupInvitation(op.param1,[op.param3])
                                        kicker5.kickoutFromGroup(op.param1,[op.param2])     
                                    except:
                                        try:
                                            kicker6.cancelGroupInvitation(op.param1,[op.param3])
                                            kicker6.kickoutFromGroup(op.param1,[op.param2])     
                                        except:
                                            try:
                                                kicker7.cancelGroupInvitation(op.param1,[op.param3])
                                                kicker7.kickoutFromGroup(op.param1,[op.param2])  
                                            except:
                                                try:
                                                    kicker8.cancelGroupInvitation(op.param1,[op.param3])
                                                    kicker8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kicker9.cancelGroupInvitation(op.param1,[op.param3])
                                                        kicker9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kicker10.cancelGroupInvitation(op.param1,[op.param3])
                                                            kicker10.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            pass         
        if op.type == 13:
            if op.param3 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    random.choice(ABC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    G = line.getGroup(op.param1)	
                    G.preventedJoinByTicket = True		
                    random.choice(ABC).updateGroup(G)

        if op.type == 32:
            if op.param1 in protectcanceljs:
                if op.param3 in Bots:    
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        wait["blacklist"][op.param2] = True
                        try:
                            if op.param3 not in wait["blacklist"]:
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                line.inviteIntoGroup(op.param1,[g1MID])		
                                G.preventedJoinByTicket = True
                                random.choice(ABC).updateGroup(G)
                        except:
                            pass
                    return
        if op.type == 32:
            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                pass
            if op.param1 in protectcancel:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                kicker.findAndAddContactsByMid(op.param3)
                kicker.inviteIntoGroup(op.param1,[op.param3])
                wait["blacklist"][op.param2] = True

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    G = line.getGroup(op.param1)	
                    G.preventedJoinByTicket = True		
                    random.choice(ABC).updateGroup(G)	
        if op.type == 17:
            if op.param1 in protecARoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                return
#================================================================================
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass            
        if op.type == 19:
            if op.param1 in ghost:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    G = line.getGroup(op.param1)                    
                    G.preventedJoinByTicket = False                     
                    random.choice(ABC).updateGroup(G)
                    invsend = 0
                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                    g1.acceptGroupInvitationByTicket(op.param1,Ticket)                    
                    g1.kickoutFromGroup(op.param1,[op.param2])                                    
                X = line.getGroup(op.param1)             
                X.preventedJoinByTicket = True
                random.choice(ABC).updateGroup(X)
        if op.type == 19:
            if op.param1 in protectantijs:
                if myMid in op.param3:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        try:
                            g1.acceptGroupInvitation(op.param1)         
                            g1.inviteIntoGroup(op.param1,[myMid])
                            g1.kickoutFromGroup(op.param1,[op.param2])
                            line.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                            g1.leaveGroup(op.param1)
                            line.inviteIntoGroup(op.param1,[Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,ga1,ga2,ga3,ga4,ga5,ga6,ga7,ga8,ga9,ga10,g1MID])
                        except:
                            pass
        if op.type == 19:
            if myMid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        kicker.inviteIntoGroup(op.param1,[op.param3])
                        line.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker2.kickoutFromGroup(op.param1,[op.param2])
                            kicker2.inviteIntoGroup(op.param1,[op.param3])
                            line.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker3.kickoutFromGroup(op.param1,[op.param2])
                                kicker3.inviteIntoGroup(op.param1,[op.param3])
                                line.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker4.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker4.kickoutFromGroup(op.param1,[op.param2])
                                    kicker4.updateGroup(G)
                                    Ticket = kicker4.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker4.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker4.updateGroup(G)
                                    Ticket = kicker4.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker5.kickoutFromGroup(op.param1,[op.param2])
                                        kicker5.inviteIntoGroup(op.param1,[op.param3])
                                        line.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker6.kickoutFromGroup(op.param1,[op.param2])
                                            kicker6.inviteIntoGroup(op.param1,[op.param3])
                                            line.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker7.kickoutFromGroup(op.param1,[op.param2])
                                                kicker7.inviteIntoGroup(op.param1,[op.param3])
                                                line.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker8.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker8.inviteIntoGroup(op.param1,[op.param3])
                                                    line.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker9.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker9.inviteIntoGroup(op.param1,[op.param3])
                                                        line.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker10.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker10.inviteIntoGroup(op.param1,[op.param3])
                                                            line.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker11.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker11.inviteIntoGroup(op.param1,[op.param3])
                                                                line.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker12.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker12.inviteIntoGroup(op.param1,[op.param3])
                                                                    line.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker13.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker13.inviteIntoGroup(op.param1,[op.param3])
                                                                        line.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker14.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker14.inviteIntoGroup(op.param1,[op.param3])
                                                                            line.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker15.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker15.inviteIntoGroup(op.param1,[op.param3])
                                                                                line.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker16.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker16.inviteIntoGroup(op.param1,[op.param3])
                                                                                    line.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker17.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker17.inviteIntoGroup(op.param1,[op.param3])
                                                                                        line.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker18.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker18.inviteIntoGroup(op.param1,[op.param3])
                                                                                            line.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            try:
                                                                                                kicker19.kickoutFromGroup(op.param1,[op.param2])
                                                                                                kicker20.kickoutFromGroup(op.param1,[op.param2])
                                                                                                kicker20.inviteIntoGroup(op.param1,[op.param3])
                                                                                                line.acceptGroupInvitation(op.param1)
                                                                                            except:
                                                                                                pass                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker2.kickoutFromGroup(op.param1,[op.param2])
                        kicker2.inviteIntoGroup(op.param1,[op.param3])
                        kicker.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker3.kickoutFromGroup(op.param1,[op.param2])
                            kicker3.inviteIntoGroup(op.param1,[op.param3])
                            kicker.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker4.kickoutFromGroup(op.param1,[op.param2])
                                kicker4.inviteIntoGroup(op.param1,[op.param3])
                                kicker.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker5.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker5.kickoutFromGroup(op.param1,[op.param2])
                                    kicker5.updateGroup(G)
                                    Ticket = kicker5.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker5.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker5.updateGroup(G)
                                    Ticket = kicker5.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker6.kickoutFromGroup(op.param1,[op.param2])
                                        kicker6.inviteIntoGroup(op.param1,[op.param3])
                                        kicker.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker7.kickoutFromGroup(op.param1,[op.param2])
                                            kicker7.inviteIntoGroup(op.param1,[op.param3])
                                            kicker.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker8.kickoutFromGroup(op.param1,[op.param2])
                                                kicker8.inviteIntoGroup(op.param1,[op.param3])
                                                kicker.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker9.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker9.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker10.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker10.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker11.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker11.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker12.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker12.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker13.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker13.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker14.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker14.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker15.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker15.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker16.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker16.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker17.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker17.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker18.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker18.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker20.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker19.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker19.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker3.kickoutFromGroup(op.param1,[op.param2])
                        kicker3.inviteIntoGroup(op.param1,[op.param3])
                        kicker2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker4.kickoutFromGroup(op.param1,[op.param2])
                            kicker4.inviteIntoGroup(op.param1,[op.param3])
                            kicker2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker5.kickoutFromGroup(op.param1,[op.param2])
                                kicker5.inviteIntoGroup(op.param1,[op.param3])
                                kicker2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker6.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker6.kickoutFromGroup(op.param1,[op.param2])
                                    kicker6.updateGroup(G)
                                    Ticket = kicker6.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker6.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker6.updateGroup(G)
                                    Ticket = kicker6.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker7.kickoutFromGroup(op.param1,[op.param2])
                                        kicker7.inviteIntoGroup(op.param1,[op.param3])
                                        kicker2.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker8.kickoutFromGroup(op.param1,[op.param2])
                                            kicker8.inviteIntoGroup(op.param1,[op.param3])
                                            kicker2.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker9.kickoutFromGroup(op.param1,[op.param2])
                                                kicker9.inviteIntoGroup(op.param1,[op.param3])
                                                kicker2.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker10.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker10.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker2.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker11.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker12.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker2.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker13.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker13.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker2.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker14.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker14.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker2.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker15.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker15.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker2.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker16.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker16.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker2.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker17.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker17.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker2.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker18.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker18.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker2.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker19.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker19.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker2.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker20.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker20.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker2.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker3.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker4.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker5.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker2.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker2.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return


            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker4.kickoutFromGroup(op.param1,[op.param2])
                        kicker4.inviteIntoGroup(op.param1,[op.param3])
                        kicker3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker5.kickoutFromGroup(op.param1,[op.param2])
                            kicker5.inviteIntoGroup(op.param1,[op.param3])
                            kicker3.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker6.kickoutFromGroup(op.param1,[op.param2])
                                kicker6.inviteIntoGroup(op.param1,[op.param3])
                                kicker3.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker7.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker7.kickoutFromGroup(op.param1,[op.param2])
                                    kicker7.updateGroup(G)
                                    Ticket = kicker7.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker7.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker7.updateGroup(G)
                                    Ticket = kicker7.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker8.kickoutFromGroup(op.param1,[op.param2])
                                        kicker8.inviteIntoGroup(op.param1,[op.param3])
                                        kicker3.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker9.kickoutFromGroup(op.param1,[op.param2])
                                            kicker9.inviteIntoGroup(op.param1,[op.param3])
                                            kicker3.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker10.kickoutFromGroup(op.param1,[op.param2])
                                                kicker10.inviteIntoGroup(op.param1,[op.param3])
                                                kicker3.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker11.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker11.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker3.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker12.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker13.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker3.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker14.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker14.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker3.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker15.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker15.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker3.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker16.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker16.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker3.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker17.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker17.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker3.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker18.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker18.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker3.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker19.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker19.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker3.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker20.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker20.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker3.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker3.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker2.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker5.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker6.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker3.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker3.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return

            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker5.kickoutFromGroup(op.param1,[op.param2])
                        kicker5.inviteIntoGroup(op.param1,[op.param3])
                        kicker4.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker6.kickoutFromGroup(op.param1,[op.param2])
                            kicker6.inviteIntoGroup(op.param1,[op.param3])
                            kicker4.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker7.kickoutFromGroup(op.param1,[op.param2])
                                kicker7.inviteIntoGroup(op.param1,[op.param3])
                                kicker4.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker8.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker8.kickoutFromGroup(op.param1,[op.param2])
                                    kicker8.updateGroup(G)
                                    Ticket = kicker8.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker8.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker8.updateGroup(G)
                                    Ticket = kicker8.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker9.kickoutFromGroup(op.param1,[op.param2])
                                        kicker9.inviteIntoGroup(op.param1,[op.param3])
                                        kicker4.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker10.kickoutFromGroup(op.param1,[op.param2])
                                            kicker10.inviteIntoGroup(op.param1,[op.param3])
                                            kicker4.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker11.kickoutFromGroup(op.param1,[op.param2])
                                                kicker11.inviteIntoGroup(op.param1,[op.param3])
                                                kicker4.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker12.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker12.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker4.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker13.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker13.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker4.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker14.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker14.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker4.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker15.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker15.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker4.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker16.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker16.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker4.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker17.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker17.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker4.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker18.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker18.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker4.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker19.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker19.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker4.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker20.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker20.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker4.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker4.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker2.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker3.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker3.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker4.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker4.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return
            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker6.kickoutFromGroup(op.param1,[op.param2])
                        kicker6.inviteIntoGroup(op.param1,[op.param3])
                        kicker5.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker7.kickoutFromGroup(op.param1,[op.param2])
                            kicker7.inviteIntoGroup(op.param1,[op.param3])
                            kicker5.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker8.kickoutFromGroup(op.param1,[op.param2])
                                kicker8.inviteIntoGroup(op.param1,[op.param3])
                                kicker5.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker9.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker9.kickoutFromGroup(op.param1,[op.param2])
                                    kicker9.updateGroup(G)
                                    Ticket = kicker9.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker9.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker9.updateGroup(G)
                                    Ticket = kicker9.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker10.kickoutFromGroup(op.param1,[op.param2])
                                        kicker10.inviteIntoGroup(op.param1,[op.param3])
                                        kicker5.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker11.kickoutFromGroup(op.param1,[op.param2])
                                            kicker11.inviteIntoGroup(op.param1,[op.param3])
                                            kicker5.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker12.kickoutFromGroup(op.param1,[op.param2])
                                                kicker12.inviteIntoGroup(op.param1,[op.param3])
                                                kicker5.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker13.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker13.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker5.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker14.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker14.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker5.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker15.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker15.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker5.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker16.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker16.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker5.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker17.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker17.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker5.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker18.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker18.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker5.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker19.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker19.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker5.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker20.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker20.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker5.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker5.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker2.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker2.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker5.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker3.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker4.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker4.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker5.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker5.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return

            if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker7.kickoutFromGroup(op.param1,[op.param2])
                        kicker7.inviteIntoGroup(op.param1,[op.param3])
                        kicker6.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker8.kickoutFromGroup(op.param1,[op.param2])
                            kicker8.inviteIntoGroup(op.param1,[op.param3])
                            kicker6.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker9.kickoutFromGroup(op.param1,[op.param2])
                                kicker9.inviteIntoGroup(op.param1,[op.param3])
                                kicker6.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker10.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker10.kickoutFromGroup(op.param1,[op.param2])
                                    kicker10.updateGroup(G)
                                    Ticket = kicker10.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker10.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker10.updateGroup(G)
                                    Ticket = kicker10.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker11.kickoutFromGroup(op.param1,[op.param2])
                                        kicker11.inviteIntoGroup(op.param1,[op.param3])
                                        kicker6.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker12.kickoutFromGroup(op.param1,[op.param2])
                                            kicker12.inviteIntoGroup(op.param1,[op.param3])
                                            kicker6.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker13.kickoutFromGroup(op.param1,[op.param2])
                                                kicker13.inviteIntoGroup(op.param1,[op.param3])
                                                kicker6.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker14.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker14.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker6.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker15.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker15.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker6.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker16.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker16.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker6.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker17.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker17.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker6.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker18.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker18.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker6.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker19.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker19.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker6.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker20.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker20.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker6.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker6.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker2.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker2.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker6.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker3.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker3.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker6.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker4.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker5.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker5.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker6.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker6.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return

            if Gmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker8.kickoutFromGroup(op.param1,[op.param2])
                        kicker8.inviteIntoGroup(op.param1,[op.param3])
                        kicker7.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker9.kickoutFromGroup(op.param1,[op.param2])
                            kicker9.inviteIntoGroup(op.param1,[op.param3])
                            kicker7.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker10.kickoutFromGroup(op.param1,[op.param2])
                                kicker10.inviteIntoGroup(op.param1,[op.param3])
                                kicker7.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker11.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker11.kickoutFromGroup(op.param1,[op.param2])
                                    kicker11.updateGroup(G)
                                    Ticket = kicker11.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker11.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker11.updateGroup(G)
                                    Ticket = kicker11.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker12.kickoutFromGroup(op.param1,[op.param2])
                                        kicker12.inviteIntoGroup(op.param1,[op.param3])
                                        kicker7.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker13.kickoutFromGroup(op.param1,[op.param2])
                                            kicker13.inviteIntoGroup(op.param1,[op.param3])
                                            kicker7.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker14.kickoutFromGroup(op.param1,[op.param2])
                                                kicker14.inviteIntoGroup(op.param1,[op.param3])
                                                kicker7.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker15.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker15.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker7.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker16.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker16.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker7.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker17.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker17.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker7.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker18.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker18.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker7.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker19.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker19.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker7.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker20.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker20.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker7.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker7.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker2.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker2.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker7.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker3.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker3.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker7.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker4.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker4.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker7.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker5.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker6.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker6.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker7.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker7.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return

            if Hmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker9.kickoutFromGroup(op.param1,[op.param2])
                        kicker9.inviteIntoGroup(op.param1,[op.param3])
                        kicker8.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker10.kickoutFromGroup(op.param1,[op.param2])
                            kicker10.inviteIntoGroup(op.param1,[op.param3])
                            kicker8.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker11.kickoutFromGroup(op.param1,[op.param2])
                                kicker11.inviteIntoGroup(op.param1,[op.param3])
                                kicker8.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker12.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker12.kickoutFromGroup(op.param1,[op.param2])
                                    kicker12.updateGroup(G)
                                    Ticket = kicker12.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker12.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker12.updateGroup(G)
                                    Ticket = kicker12.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker13.kickoutFromGroup(op.param1,[op.param2])
                                        kicker13.inviteIntoGroup(op.param1,[op.param3])
                                        kicker8.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker14.kickoutFromGroup(op.param1,[op.param2])
                                            kicker14.inviteIntoGroup(op.param1,[op.param3])
                                            kicker8.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker15.kickoutFromGroup(op.param1,[op.param2])
                                                kicker15.inviteIntoGroup(op.param1,[op.param3])
                                                kicker8.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker16.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker16.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker8.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker17.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker17.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker8.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker18.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker18.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker8.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker19.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker19.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker8.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker20.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker20.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker8.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker8.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker2.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker2.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker8.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker3.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker3.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker8.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker4.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker4.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker8.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker5.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker5.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker8.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker6.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker7.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker7.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker8.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker8.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return

            if Imid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker10.kickoutFromGroup(op.param1,[op.param2])
                        kicker10.inviteIntoGroup(op.param1,[op.param3])
                        kicker9.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker11.kickoutFromGroup(op.param1,[op.param2])
                            kicker11.inviteIntoGroup(op.param1,[op.param3])
                            kicker9.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker12.kickoutFromGroup(op.param1,[op.param2])
                                kicker12.inviteIntoGroup(op.param1,[op.param3])
                                kicker9.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker13.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker13.kickoutFromGroup(op.param1,[op.param2])
                                    kicker13.updateGroup(G)
                                    Ticket = kicker13.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker13.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker13.updateGroup(G)
                                    Ticket = kicker13.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker14.kickoutFromGroup(op.param1,[op.param2])
                                        kicker14.inviteIntoGroup(op.param1,[op.param3])
                                        kicker9.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker15.kickoutFromGroup(op.param1,[op.param2])
                                            kicker15.inviteIntoGroup(op.param1,[op.param3])
                                            kicker9.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker16.kickoutFromGroup(op.param1,[op.param2])
                                                kicker16.inviteIntoGroup(op.param1,[op.param3])
                                                kicker9.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker17.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker17.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker9.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker18.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker18.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker9.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker19.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker19.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker9.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker20.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker20.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker9.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker9.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker2.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker2.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker9.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker3.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker3.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker9.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker4.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker4.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker9.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker5.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker5.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker9.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker6.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker6.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker9.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker7.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker8.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker7.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker9.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker9.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return

            if Jmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker11.kickoutFromGroup(op.param1,[op.param2])
                        kicker11.inviteIntoGroup(op.param1,[op.param3])
                        kicker10.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker12.kickoutFromGroup(op.param1,[op.param2])
                            kicker12.inviteIntoGroup(op.param1,[op.param3])
                            kicker10.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker13.kickoutFromGroup(op.param1,[op.param2])
                                kicker13.inviteIntoGroup(op.param1,[op.param3])
                                kicker10.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker14.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker14.kickoutFromGroup(op.param1,[op.param2])
                                    kicker14.updateGroup(G)
                                    Ticket = kicker14.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker14.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker14.updateGroup(G)
                                    Ticket = kicker14.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker15.kickoutFromGroup(op.param1,[op.param2])
                                        kicker15.inviteIntoGroup(op.param1,[op.param3])
                                        kicker10.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker16.kickoutFromGroup(op.param1,[op.param2])
                                            kicker16.inviteIntoGroup(op.param1,[op.param3])
                                            kicker10.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker17.kickoutFromGroup(op.param1,[op.param2])
                                                kicker17.inviteIntoGroup(op.param1,[op.param3])
                                                kicker10.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker18.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker18.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker10.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker19.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker19.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker10.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker20.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker20.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker10.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker10.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker2.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker2.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker10.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker3.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker3.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker10.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker4.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker4.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker10.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker5.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker5.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker10.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker6.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker6.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker10.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker7.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker7.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker10.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker8.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker9.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker9.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker10.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker10.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return

            if ga1 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker12.kickoutFromGroup(op.param1,[op.param2])
                        kicker12.inviteIntoGroup(op.param1,[op.param3])
                        kicker11.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker13.kickoutFromGroup(op.param1,[op.param2])
                            kicker13.inviteIntoGroup(op.param1,[op.param3])
                            kicker11.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker14.kickoutFromGroup(op.param1,[op.param2])
                                kicker14.inviteIntoGroup(op.param1,[op.param3])
                                kicker11.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker15.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker15.kickoutFromGroup(op.param1,[op.param2])
                                    kicker15.updateGroup(G)
                                    Ticket = kicker15.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker15.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker15.updateGroup(G)
                                    Ticket = kicker15.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker16.kickoutFromGroup(op.param1,[op.param2])
                                        kicker16.inviteIntoGroup(op.param1,[op.param3])
                                        kicker11.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker17.kickoutFromGroup(op.param1,[op.param2])
                                            kicker17.inviteIntoGroup(op.param1,[op.param3])
                                            kicker11.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker18.kickoutFromGroup(op.param1,[op.param2])
                                                kicker18.inviteIntoGroup(op.param1,[op.param3])
                                                kicker11.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker19.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker19.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker11.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker20.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker20.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker11.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker11.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker2.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker2.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker11.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker3.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker3.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker11.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker4.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker4.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker11.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker5.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker5.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker11.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker6.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker6.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker11.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker7.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker11.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker8.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker8.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker11.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker9.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker10.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker10.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker11.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker11.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return

            if ga2 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker13.kickoutFromGroup(op.param1,[op.param2])
                        kicker13.inviteIntoGroup(op.param1,[op.param3])
                        kicker12.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker14.kickoutFromGroup(op.param1,[op.param2])
                            kicker14.inviteIntoGroup(op.param1,[op.param3])
                            kicker12.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker15.kickoutFromGroup(op.param1,[op.param2])
                                kicker15.inviteIntoGroup(op.param1,[op.param3])
                                kicker12.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker16.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker16.kickoutFromGroup(op.param1,[op.param2])
                                    kicker16.updateGroup(G)
                                    Ticket = kicker16.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker16.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker16.updateGroup(G)
                                    Ticket = kicker16.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker17.kickoutFromGroup(op.param1,[op.param2])
                                        kicker17.inviteIntoGroup(op.param1,[op.param3])
                                        kicker12.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker18.kickoutFromGroup(op.param1,[op.param2])
                                            kicker18.inviteIntoGroup(op.param1,[op.param3])
                                            kicker12.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker19.kickoutFromGroup(op.param1,[op.param2])
                                                kicker19.inviteIntoGroup(op.param1,[op.param3])
                                                kicker12.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker20.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker20.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker12.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker12.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker2.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker2.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker12.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker3.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker3.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker12.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker4.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker4.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker12.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker5.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker5.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker12.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker6.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker6.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker12.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker7.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker7.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker12.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker8.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker8.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker12.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker9.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker9.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker12.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker10.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker11.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker10.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker12.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker12.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return

            if ga3 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker14.kickoutFromGroup(op.param1,[op.param2])
                        kicker14.inviteIntoGroup(op.param1,[op.param3])
                        kicker13.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker15.kickoutFromGroup(op.param1,[op.param2])
                            kicker15.inviteIntoGroup(op.param1,[op.param3])
                            kicker13.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker16.kickoutFromGroup(op.param1,[op.param2])
                                kicker16.inviteIntoGroup(op.param1,[op.param3])
                                kicker13.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker17.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker17.kickoutFromGroup(op.param1,[op.param2])
                                    kicker17.updateGroup(G)
                                    Ticket = kicker17.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker17.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker17.updateGroup(G)
                                    Ticket = kicker17.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker17.kickoutFromGroup(op.param1,[op.param2])
                                        kicker17.inviteIntoGroup(op.param1,[op.param3])
                                        kicker13.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker18.kickoutFromGroup(op.param1,[op.param2])
                                            kicker18.inviteIntoGroup(op.param1,[op.param3])
                                            kicker13.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker19.kickoutFromGroup(op.param1,[op.param2])
                                                kicker19.inviteIntoGroup(op.param1,[op.param3])
                                                kicker13.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker20.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker20.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker13.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker13.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker2.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker2.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker13.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker3.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker3.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker13.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker4.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker4.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker13.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker5.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker5.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker13.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker6.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker6.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker13.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker7.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker7.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker13.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker8.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker8.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker13.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker9.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker9.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker13.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker10.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker11.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker12.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker13.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker13.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return

            if ga4 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker15.kickoutFromGroup(op.param1,[op.param2])
                        kicker15.inviteIntoGroup(op.param1,[op.param3])
                        kicker14.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker16.kickoutFromGroup(op.param1,[op.param2])
                            kicker16.inviteIntoGroup(op.param1,[op.param3])
                            kicker14.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker17.kickoutFromGroup(op.param1,[op.param2])
                                kicker17.inviteIntoGroup(op.param1,[op.param3])
                                kicker14.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker18.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker18.kickoutFromGroup(op.param1,[op.param2])
                                    kicker18.updateGroup(G)
                                    Ticket = kicker18.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker18.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker18.updateGroup(G)
                                    Ticket = kicker18.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker19.kickoutFromGroup(op.param1,[op.param2])
                                        kicker19.inviteIntoGroup(op.param1,[op.param3])
                                        kicker14.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker20.kickoutFromGroup(op.param1,[op.param2])
                                            kicker20.inviteIntoGroup(op.param1,[op.param3])
                                            kicker14.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker.kickoutFromGroup(op.param1,[op.param2])
                                                kicker.inviteIntoGroup(op.param1,[op.param3])
                                                kicker14.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker2.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker2.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker14.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker3.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker3.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker14.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker4.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker4.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker14.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker5.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker5.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker14.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker6.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker6.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker14.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker7.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker7.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker14.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker8.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker8.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker14.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker9.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker9.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker14.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker10.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker10.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker14.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker11.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker11.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker14.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker12.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker13.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker13.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker14.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker14.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return

            if ga5 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker16.kickoutFromGroup(op.param1,[op.param2])
                        kicker16.inviteIntoGroup(op.param1,[op.param3])
                        kicker15.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker17.kickoutFromGroup(op.param1,[op.param2])
                            kicker17.inviteIntoGroup(op.param1,[op.param3])
                            kicker15.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker18.kickoutFromGroup(op.param1,[op.param2])
                                kicker18.inviteIntoGroup(op.param1,[op.param3])
                                kicker15.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker19.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker19.kickoutFromGroup(op.param1,[op.param2])
                                    kicker19.updateGroup(G)
                                    Ticket = kicker19.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker19.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker19.updateGroup(G)
                                    Ticket = kicker19.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker20.kickoutFromGroup(op.param1,[op.param2])
                                        kicker20.inviteIntoGroup(op.param1,[op.param3])
                                        kicker15.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker.kickoutFromGroup(op.param1,[op.param2])
                                            kicker.inviteIntoGroup(op.param1,[op.param3])
                                            kicker15.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker2.kickoutFromGroup(op.param1,[op.param2])
                                                kicker2.inviteIntoGroup(op.param1,[op.param3])
                                                kicker15.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker3.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker3.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker15.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker4.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker4.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker15.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker5.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker5.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker15.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker6.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker6.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker15.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker7.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker7.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker15.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker8.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker8.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker15.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker9.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker9.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker15.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker10.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker10.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker15.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker11.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker11.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker15.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker12.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker12.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker15.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker13.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker14.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker13.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker15.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker15.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return

            if ga6 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker17.kickoutFromGroup(op.param1,[op.param2])
                        kicker17.inviteIntoGroup(op.param1,[op.param3])
                        kicker16.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker18.kickoutFromGroup(op.param1,[op.param2])
                            kicker18.inviteIntoGroup(op.param1,[op.param3])
                            kicker16.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker19.kickoutFromGroup(op.param1,[op.param2])
                                kicker19.inviteIntoGroup(op.param1,[op.param3])
                                kicker16.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker20.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker20.kickoutFromGroup(op.param1,[op.param2])
                                    kicker20.updateGroup(G)
                                    Ticket = kicker20.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker20.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker20.updateGroup(G)
                                    Ticket = kicker20.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker.kickoutFromGroup(op.param1,[op.param2])
                                        kicker.inviteIntoGroup(op.param1,[op.param3])
                                        kicker16.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker2.kickoutFromGroup(op.param1,[op.param2])
                                            kicker2.inviteIntoGroup(op.param1,[op.param3])
                                            kicker16.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker3.kickoutFromGroup(op.param1,[op.param2])
                                                kicker3.inviteIntoGroup(op.param1,[op.param3])
                                                kicker16.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker4.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker4.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker16.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker5.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker5.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker16.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker6.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker6.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker16.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker7.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker7.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker16.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker8.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker8.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker16.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker9.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker9.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker16.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker10.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker10.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker16.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker11.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker11.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker16.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker12.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker12.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker16.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker13.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker13.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker16.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker14.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker15.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker15.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker16.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker16.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return

            if ga7 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker18.kickoutFromGroup(op.param1,[op.param2])
                        kicker18.inviteIntoGroup(op.param1,[op.param3])
                        kicker17.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker19.kickoutFromGroup(op.param1,[op.param2])
                            kicker19.inviteIntoGroup(op.param1,[op.param3])
                            kicker17.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker20.kickoutFromGroup(op.param1,[op.param2])
                                kicker20.inviteIntoGroup(op.param1,[op.param3])
                                kicker17.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker.kickoutFromGroup(op.param1,[op.param2])
                                    kicker.updateGroup(G)
                                    Ticket = kicker.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker.updateGroup(G)
                                    Ticket = kicker.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker2.kickoutFromGroup(op.param1,[op.param2])
                                        kicker2.inviteIntoGroup(op.param1,[op.param3])
                                        kicker17.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker3.kickoutFromGroup(op.param1,[op.param2])
                                            kicker3.inviteIntoGroup(op.param1,[op.param3])
                                            kicker17.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker4.kickoutFromGroup(op.param1,[op.param2])
                                                kicker4.inviteIntoGroup(op.param1,[op.param3])
                                                kicker17.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker5.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker5.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker17.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker6.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker6.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker17.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker7.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker7.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker17.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker8.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker8.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker17.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker9.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker9.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker17.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker10.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker10.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker17.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker11.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker11.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker17.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker12.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker12.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker17.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker13.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker13.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker17.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker14.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker14.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker17.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker15.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker16.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker15.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker17.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker17.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return

            if ga8 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker19.kickoutFromGroup(op.param1,[op.param2])
                        kicker19.inviteIntoGroup(op.param1,[op.param3])
                        kicker18.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker20.kickoutFromGroup(op.param1,[op.param2])
                            kicker20.inviteIntoGroup(op.param1,[op.param3])
                            kicker18.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker.kickoutFromGroup(op.param1,[op.param2])
                                kicker.inviteIntoGroup(op.param1,[op.param3])
                                kicker18.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker2.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker2.kickoutFromGroup(op.param1,[op.param2])
                                    kicker2.updateGroup(G)
                                    Ticket = kicker.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker2.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker2.updateGroup(G)
                                    Ticket = kicker2.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker3.kickoutFromGroup(op.param1,[op.param2])
                                        kicker3.inviteIntoGroup(op.param1,[op.param3])
                                        kicker18.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker4.kickoutFromGroup(op.param1,[op.param2])
                                            kicker4.inviteIntoGroup(op.param1,[op.param3])
                                            kicker18.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker5.kickoutFromGroup(op.param1,[op.param2])
                                                kicker5.inviteIntoGroup(op.param1,[op.param3])
                                                kicker18.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker6.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker6.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker18.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker7.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker7.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker18.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker8.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker8.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker18.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker9.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker9.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker18.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker10.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker10.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker18.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker11.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker11.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker18.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker12.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker12.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker18.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker13.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker13.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker18.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker14.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker14.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker18.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker15.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker15.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker18.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker16.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker17.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker17.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker18.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker18.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return

            if ga9 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker20.kickoutFromGroup(op.param1,[op.param2])
                        kicker20.inviteIntoGroup(op.param1,[op.param3])
                        kicker19.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker.kickoutFromGroup(op.param1,[op.param2])
                            kicker.inviteIntoGroup(op.param1,[op.param3])
                            kicker19.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker2.kickoutFromGroup(op.param1,[op.param2])
                                kicker2.inviteIntoGroup(op.param1,[op.param3])
                                kicker19.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker3.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker3.kickoutFromGroup(op.param1,[op.param2])
                                    kicker3.updateGroup(G)
                                    Ticket = kicker.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker3.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker3.updateGroup(G)
                                    Ticket = kicker3.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker4.kickoutFromGroup(op.param1,[op.param2])
                                        kicker4.inviteIntoGroup(op.param1,[op.param3])
                                        kicker19.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker5.kickoutFromGroup(op.param1,[op.param2])
                                            kicker5.inviteIntoGroup(op.param1,[op.param3])
                                            kicker19.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker6.kickoutFromGroup(op.param1,[op.param2])
                                                kicker6.inviteIntoGroup(op.param1,[op.param3])
                                                kicker19.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker7.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker7.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker19.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker8.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker8.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker19.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker9.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker9.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker19.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker10.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker10.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker19.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker11.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker11.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker19.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker12.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker12.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker19.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker13.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker13.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker19.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker14.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker14.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker19.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker15.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker15.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker19.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker16.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker16.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker19.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker17.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker18.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker18.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker19.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker19.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return

            if ga10 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        kicker.inviteIntoGroup(op.param1,[op.param3])
                        kicker20.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker2.kickoutFromGroup(op.param1,[op.param2])
                            kicker2.inviteIntoGroup(op.param1,[op.param3])
                            kicker20.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker3.kickoutFromGroup(op.param1,[op.param2])
                                kicker3.inviteIntoGroup(op.param1,[op.param3])
                                kicker20.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker4.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker4.kickoutFromGroup(op.param1,[op.param2])
                                    kicker4.updateGroup(G)
                                    Ticket = kicker.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker20.acceptGroupInvitationByTicket(op.param1,Ticket)                                    
                                    G = kicker4.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker4.updateGroup(G)
                                    Ticket = kicker4.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker5.kickoutFromGroup(op.param1,[op.param2])
                                        kicker5.inviteIntoGroup(op.param1,[op.param3])
                                        kicker20.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker6.kickoutFromGroup(op.param1,[op.param2])
                                            kicker6.inviteIntoGroup(op.param1,[op.param3])
                                            kicker20.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kicker7.kickoutFromGroup(op.param1,[op.param2])
                                                kicker7.inviteIntoGroup(op.param1,[op.param3])
                                                kicker20.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kicker8.kickoutFromGroup(op.param1,[op.param2])
                                                    kicker8.inviteIntoGroup(op.param1,[op.param3])
                                                    kicker20.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kicker9.kickoutFromGroup(op.param1,[op.param2])
                                                        kicker9.inviteIntoGroup(op.param1,[op.param3])
                                                        kicker20.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kicker10.kickoutFromGroup(op.param1,[op.param2])
                                                            kicker10.inviteIntoGroup(op.param1,[op.param3])
                                                            kicker20.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                kicker11.kickoutFromGroup(op.param1,[op.param2])
                                                                kicker11.inviteIntoGroup(op.param1,[op.param3])
                                                                kicker20.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kicker12.kickoutFromGroup(op.param1,[op.param2])
                                                                    kicker12.inviteIntoGroup(op.param1,[op.param3])
                                                                    kicker20.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kicker13.kickoutFromGroup(op.param1,[op.param2])
                                                                        kicker13.inviteIntoGroup(op.param1,[op.param3])
                                                                        kicker20.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kicker14.kickoutFromGroup(op.param1,[op.param2])
                                                                            kicker14.inviteIntoGroup(op.param1,[op.param3])
                                                                            kicker20.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kicker15.kickoutFromGroup(op.param1,[op.param2])
                                                                                kicker15.inviteIntoGroup(op.param1,[op.param3])
                                                                                kicker20.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kicker16.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kicker16.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kicker20.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kicker17.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kicker17.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kicker20.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kicker18.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker19.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kicker19.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kicker20.acceptGroupInvitation(op.param1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                        except:
                                                                                            try:
                                                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kicker20.acceptGroupInvitation(op.param1)                                                                                                                                                                                                    
                                                                                            except:
                                                                                                pass
                return
                                                                                                                                             
#==============================================================================================================
#==============================================[OP TYPE 22 24 JOIN]============================================
#==============================================================================================================
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:            	
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    G = line.getGroup(op.param1)	
                    G.preventedJoinByTicket = True		
                    random.choice(ABC).updateGroup(G)	
        if op.type == 25:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            to       = sender if not msg.toType and sender != myMid else receiver
            txt      = text.lower()
            cmd      = command(text)
            setKey   = settings['setKey']['key'] if settings['setKey']['status'] else ''
            if text in tmp_text:
                return tmp_text.remove(text)
            if msg.contentType == 0: # Content type is text
                if '/ti/g/' in text and settings['autoJoin']['ticket']:
                    regex = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = regex.findall(text)
                    tickets = []
                    gids = line.getGroupIdsJoined()
                    for link in links:
                        if link not in tickets:
                            tickets.append(link)
                    for ticket in tickets:
                        try:
                            group = line.findGroupByTicket(ticket)
                        except:
                            continue
                        if group.id in gids:
                            line.sendMessage(to, 'เข้าร่วมกลุ่ม' + group.name)
                            continue
                        line.acceptGroupInvitationByTicket(group.id, ticket)
                        if settings['autoJoin']['reply']:
                            if '@!' not in settings['autoJoin']['message']:
                                line.sendMessage(to, settings['autoJoin']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoJoin']['message'], [sender])
                        line.sendMessage(to, 'เข้าร่วมกลุ่ม' + group.name)
                try:
                    executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey)
                except TalkException as talk_error:
                    logError(talk_error)
                    if talk_error.code in [7, 8, 20]:
                        sys.exit(1)
                    line.sendMessage(to, 'เกิดข้อผิดพลาด\n' + str(talk_error))
                    time.sleep(3)
                except Exception as error:
                    logError(error)
                    line.sendMessage(to, 'เกิดข้อผิดพลาด\n' + str(error))
                    time.sleep(3)
            elif msg.contentType == 1: # Content type is image
                if settings['changePictureProfile']:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/picture.jpg')
                    line.updateProfilePicture(path)
                    line.sendMessage(to, 'เปลี่ยนรูปโปรไฟล์เรียบร้อย')
                    settings['changePictureProfile'] = False
                elif settings['changeCoverProfile']:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/cover.jpg')
                    line.updateProfileCover(path)
                    line.sendMessage(to, 'เปลี่ยนรูปปกเรียบร้อย')
                    settings['changeCoverProfile'] = False
                elif to in settings['changeGroupPicture'] and msg.toType == 2:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/grouppicture.jpg')
                    line.updateGroupPicture(to, path)
                    line.sendMessage(to, 'เปลี่ยนรูปกลุ่มแล้ว')
                    settings['changeGroupPicture'].remove(to)
            elif msg.contentType == 7: # Content type is sticker
                if settings['checkSticker']:
                    res = '╭───「 Sticker Info 」'
                    res += '\n├ Sticker ID : ' + msg.contentMetadata['STKID']
                    res += '\n├ Sticker Packages ID : ' + msg.contentMetadata['STKPKGID']
                    res += '\n├ Sticker Version : ' + msg.contentMetadata['STKVER']
                    res += '\n├ Sticker Link : line://shop/detail/' + msg.contentMetadata['STKPKGID']
                    res += '\n╰───「SelfBot ProtectV2.2」'
                    line.sendMessage(to, parsingRes(res))
            elif msg.contentType == 13: # Content type is contact
                if settings['checkContact']:
                    mid = msg.contentMetadata['mid']
                    try:
                        contact = line.getContact(mid)
                    except:
                        return line.sendMessage(to, 'เกิดข้ผิดพลาดเฉียบพลัน ' + mid)
                    res = '╭───「 Details Contact 」'
                    res += '\n├ MID : ' + mid
                    res += '\n├ Display Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\n├ Status Message : ' + str(contact.statusMessage)
                    res += '\n╰───「SelfBot ProtectV2.2」'
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(mid)
                    line.sendImageWithURL(to, str(cover))
                    line.sendMessage(to, parsingRes(res))
            elif msg.contentType == 16: # Content type is album/note
                if settings['checkPost']:
                    if msg.contentMetadata['serviceType'] in ['GB', 'NT', 'MH']:
                        if msg.contentMetadata['serviceType'] in ['GB', 'NT']:
                            contact = line.getContact(sender)
                            author = contact.displayName
                        else:
                            author = msg.contentMetadata['serviceName']
                        posturl = msg.contentMetadata['postEndUrl']
                        res = '╭───「 Details Post 」'
                        res += '\n├ Creator : ' + author
                        res += '\n├ Post Link : ' + posturl
                        res += '\n╰───「SelfBot ProtectV2.2」'                  
        elif op.type == 26:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            to       = sender if not msg.toType and sender != myMid else receiver
            txt      = text.lower()
            if settings['autoRead']:
                kicker.sendChatChecked(to, msg_id)
                kicker2.sendChatChecked(to, msg_id)
                kicker3.sendChatChecked(to, msg_id)
                kicker4.sendChatChecked(to, msg_id)
                kicker5.sendChatChecked(to, msg_id)
                kicker6.sendChatChecked(to, msg_id)
                kicker7.sendChatChecked(to, msg_id)
                kicker8.sendChatChecked(to, msg_id)
                kicker9.sendChatChecked(to, msg_id)
                kicker10.sendChatChecked(to, msg_id)
                kicker11.sendChatChecked(to, msg_id)
                kicker12.sendChatChecked(to, msg_id)
                kicker13.sendChatChecked(to, msg_id)
                kicker14.sendChatChecked(to, msg_id)
                kicker15.sendChatChecked(to, msg_id)
                kicker16.sendChatChecked(to, msg_id)
                kicker17.sendChatChecked(to, msg_id)
                kicker18.sendChatChecked(to, msg_id)
                kicker19.sendChatChecked(to, msg_id)
                kicker20.sendChatChecked(to, msg_id)                                    
                g1.sendChatChecked(to, msg_id)
            if msg.contentType == 0: # Content type is text
                if '/ti/g/' in text and settings['autoJoin']['ticket']:
                    regex = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = regex.findall(text)
                    tickets = []
                    gids = line.getGroupIdsJoined()
                    for link in links:
                        if link not in tickets:
                            tickets.append(link)
                    for ticket in tickets:
                        try:
                            group = line.findGroupByTicket(ticket)
                        except:
                            continue
                        if group.id in gids:
                            line.sendMessage(to, 'I\'m aleady on group ' + group.name)
                            continue
                        line.acceptGroupInvitationByTicket(group.id, ticket)
                        if settings['autoJoin']['reply']:
                            if '@!' not in settings['autoJoin']['message']:
                                line.sendMessage(to, settings['autoJoin']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoJoin']['message'], [sender])
                        line.sendMessage(to, 'Success join to group ' + group.name)
                if settings['mimic']['status']:
                    if sender in settings['mimic']['target'] and settings['mimic']['target'][sender]:
                        try:
                            line.sendMessage(to, text, msg.contentMetadata)
                            tmp_text.append(text)
                        except:
                            pass
                if settings['autoRespondMention']['status']:
                    if msg.toType in [1, 2] and 'MENTION' in msg.contentMetadata.keys() and sender != myMid and msg.contentType not in [6, 7, 9]:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = [mention['M'] for mention in mentions['MENTIONEES']]
                        if myMid in mentionees:
                            if line.getProfile().displayName in text:
                                if '@!' not in settings['autoRespondMention']['message']:
                                    line.sendMessage(to, settings['autoRespondMention']['message'])
                                else:
                                    line.sendMentionV2(to, settings['autoRespondMention']['message'], [sender])
                if settings['autoRespond']['status']:
                    if msg.toType == 0:
                        contact = line.getContact(sender)
                        if contact.attributes != 32 and 'MENTION' not in msg.contentMetadata.keys():
                            if '@!' not in settings['autoRespond']['message']:
                                line.sendMessage(to, settings['autoRespond']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoRespond']['message'], [sender])             
        if op.type == 55:
            if op.param1 in lurking:
                if lurking[op.param1]['status'] and op.param2 not in lurking[op.param1]['members']:
                    lurking[op.param1]['members'].append(op.param2)
                    if lurking[op.param1]['reply']['status']:
                        if '@!' not in lurking[op.param1]['reply']['message']:
                            line.sendMessage(op.param1, lurking[op.param1]['reply']['message'])
                        else:
                            line.sendMentionV2(op.param1, lurking[op.param1]['reply']['message'], [op.param2])
    except TalkException as talk_error:
        logError(talk_error)
        if talk_error.code in [7, 8, 20]:
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit('##---- KEYBOARD INTERRUPT -----##')
    except Exception as error:
        logError(error)

while True:
    try:
        ops = oepoll.singleTrace(count=80)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread1 = threading.Thread(target=executeOp, args=(op,))
                thread1.daemon = True
                thread1.start()
    except Exception as e:
        pass
