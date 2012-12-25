# coding=utf8

from flask import Flask, request
from subprocess import call
import ujson
import pyzmail

app = Flask(__name__)

f = open("miao.json", 'r')
conf = ujson.loads(f.read())
f.close()

if conf['email_notify']:
    for r in conf['repos']:
        if "specify_recipients" in r:
            r['recipients'] = r['specify_recipients']
        else:
            r['recipients'] = conf['email_settings']['default_recipients']

git_pull = '" && git reset --hard {} && git pull'
hg_pull = '" && hg update -C && hg pull'

def do_pull(repo, c):
    if repo['type'] == 'git':
        call(['cd "' + repo['path'] + git_pull.format(repo['branch']) + ' && ' + repo['command']], shell=True)
    else:
        call(['cd "' + repo['path'] + hg_pull + ' && ' + repo['command']], shell=True)
    if conf['email_notify']:
        sender = (conf['email_settings']['sender_name'], conf['email_settings']['sender_email'])
        recipients = repo['recipients']
        subject=u'｢喵｣ triggered on '+c['name']+':'+repo['branch']
        text_content='\n'.join([u'Miaopull was triggered by the commit', u"｢喵噗哦｣被以下提交觸發:", 'Message: '+c['msg'], 'ID: '+c['id']])
        prefered_encoding='utf-8'
        text_encoding='utf-8'

        payload, mail_from, rcpt_to, msg_id = pyzmail.compose_mail(sender, recipients, subject, prefered_encoding, (text_content, text_encoding), html=None)

        ret=pyzmail.send_mail(payload, mail_from, rcpt_to, conf['email_settings']['host'], smtp_port=conf['email_settings']['port'], smtp_mode=conf['email_settings']['mode'], smtp_login=conf['email_settings']['login'], smtp_password=conf['email_settings']['password'])

        if isinstance(ret, dict):
            if ret:
                print '[email notify] failed recipients:', ', '.join(ret.keys())
            else:
                print '[email notify] success'
        else:
            print '[email notify] error:', ret

@app.route("/welcome")
def welcome():
    return u"Miaopull｢喵噗哦｣"

@app.route('/miao', methods=['POST'])
def miaopull():
    payload = ujson.loads(request.form['payload'])
    c = {}
    if 'canon_url' in payload:
        ptype = 'bitbucket'
        pbranch = payload['commits'][0]['branch']
        c['name'] = payload['repository']['name']
        c['msg'] = payload['commits'][0]['message']
        c['id'] = payload['commits'][0]['raw_node']
    else:
        ptype = 'github'
        pbranch = payload['ref'].split('/')[-1]
        c['name'] = payload['repository']['name']
        c['msg'] = payload['commits'][0]['message']
        c['id'] = payload['commits'][0]['id']

    for r in conf['repos']:
        rpath = r['path']
        rbranch = r['branch']
        if rbranch == pbranch:
            rcommands = r['commands']
            r['command'] = ' && '.join(rcommands)
            if ptype == 'bitbucket':
                r['type'] = payload['repository']['scm']
            else:
                r['type'] = 'git'
            do_pull(r, c)
    return u"｢喵｣"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=conf['port'])