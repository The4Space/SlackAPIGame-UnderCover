#!/usr/bin/python
# coding=utf-8

from _core import worker_base
import json
import subprocess
import yaml
import random

import os

config_path = os.path.join( os.path.dirname(os.path.abspath(__file__)), "config.yml")

config = {}
with open( config_path, 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

slack_url = config['slack_url']


def send_slack_message( message, user = '' ):
    reply = {}
    reply['text'] = message
    if user != '':
        reply['channel'] = "@{id}".format(id=user)
    payload = 'payload=' + json.dumps(reply)
    subprocess.check_output( [ 'curl', '-X', 'POST', '--data-urlencode', payload, slack_url ] )

def attend_player( player ):
    member.append(player)
    members = ''.join(member)
    send_slack_message(members)


class API_Worker( worker_base.API_Worker_Base ):

    def do_GET( self ):
        self.reply( 'Hello World', 'text/html', 200 )

    def do_POST( self ):
        data = self.post_data
        print data
        print type(data)

        data_text = data['text'][0][1:]
        player_name = data['user_name'][0]
        hey_rita_response = [
            ":hearts::hearts::hearts: Love you :hearts::hearts::hearts:",
            "怎麼了嗎? :hearts:",
            "Hedy: 那我呢?",
            "Hi~~有你的包裹唷＾＾",
            "公共場合的垃圾要自己帶走喔~ :hearts::hearts::hearts:",
            "請大家將沒吃完的食物倒在廚餘回收桶裡面，不要倒在水槽～"
        ]

        if data_text == 'SPY':
            send_slack_message( 'Game Start !', player_name  )
        elif data_text == '+1':
            send_slack_message( 'Welcome ! ' + player_name, "" )
        elif data_text == 'Time up':
            attend_player( 'Attend player have: ' +  player_name, "" )
        elif data_text == 'Hey Siri':
            send_slack_message( 'Honey~ :heart::heart::heart::heart::heart:', player_name )
        elif data_text == 'Hey NPC':
            send_slack_message( "What's up honey?" )
        elif data_text == 'Hey Ted':
            send_slack_message( "I'm Tim!!!!" )
        elif data_text == 'Hey Rita':
            if player_name == 'dogtim':
                send_slack_message( "Honey~ Happy Birthday :revolving_hearts::heart::heart::heart:")
            elif player_name == 'nan':
                send_slack_message( "Nan GOGOGO")
            else:
                send_slack_message( random.choice(hey_rita_response) )
        elif data_text == 'OK. GO!':
            if player_name == 'nan':
                send_slack_message( ":heart::heart::heart:")

        self.reply( '', 'text/html', 200 )
