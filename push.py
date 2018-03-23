#!/usr/bin/env python
#-*- coding: utf-8 -*-

import json
import requests

def main():
    """ PUSH通知
    """
    payload = {
        "priority": "high",
        "content_available": True,
        "notification": {
            "title": "",
            "body":  "",
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": ""
        "project_id": ""
    }

    r = requests.post('https://fcm.googleapis.com/fcm/send', data=json.dumps(payload), headers=headers)

    print(r.content)
    

if __name__ == "__main__":
    """
    """
    main()
