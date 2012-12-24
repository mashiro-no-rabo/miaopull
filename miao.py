# coding=utf8

from flask import Flask, request
from subprocess import call
import ujson

app = Flask(__name__)

f = open("miao.json", 'r')
conf = ujson.loads(f.read())
f.close()

git_pull = '" && git reset --hard {} && git pull'
hg_pull = '" && hg update -C && hg pull'

def do_pull(type, path, branch):
    if type == 'git':
        call(['cd "' + path + git_pull.format(branch)], shell=True)
    else:
        call(['cd "' + path + hg_pull], shell=True)

@app.route("/welcome")
def welcome():
    return u"｢喵噗哦｣"

@app.route('/miao', methods=['POST'])
def miaopull():
    payload = ujson.loads(request.form['payload'])
    if 'canon_url' in payload:
        ptype = 'bitbucket'
        pbranch = payload['commits'][0]['branch']
    else:
        ptype = 'github'
        pbranch = payload['ref'].split('/')[-1]

    for r in conf['repos']:
        rpath = r['path']
        rwatch = r['watch']
        for b in rwatch:
            if b == pbranch:
                if ptype == 'bitbucket':
                    do_pull(payload['repository']['scm'], rpath, b)
                else:
                    do_pull('git', rpath, b)
    return u"｢喵｣"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=conf['port'])