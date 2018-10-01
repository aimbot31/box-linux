# coding: utf-8

from __future__ import print_function, unicode_literals
import os
from boxsdk import Client
from boxsdk.exception import BoxAPIException
from auth import authenticate

def run_user_example(client):
    # 'me' is a handy value to get info on the current authenticated user.
    me = client.user(user_id='me').get(fields=['login'])
    print('The email of the user is: {0}'.format(me['login']))


def run_folder_examples(client):
    root_folder = client.folder(folder_id='0').get()
    print('The root folder is owned by: {0}'.format(root_folder.owned_by['login']))

    items = root_folder.get_items(limit=100, offset=0)
    print('This is the first 100 items in the root folder:')
    print(items)
    print(type(items))
    for item in items:
        print(item)
        print(type(item))
        print("   " + item.name)

def upload_file(client):
    root_folder = client.folder(folder_id='0')
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'example.api')
    a_file = root_folder.upload(file_path, file_name='example.api')
    try:
        print('{0} uploaded: '.format(a_file.get()['name']))
    finally:
        print("ok")
    #    print('Delete i-am-a-file.txt succeeded: {0}'.format(a_file.delete()))

def run_examples(oauth):
    client = Client(oauth)

    run_folder_examples(client)
    #upload_file(client)

def main():
    oauth, access_token, refresh_token = authenticate()
    print(oauth)
    oauth._store_tokens(access_token, refresh_token)
    run_examples(oauth)
    os._exit(0)

if __name__ == '__main__':
    main()