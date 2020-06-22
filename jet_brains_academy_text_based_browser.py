import os
import sys
from enum import Enum

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


class Websites(Enum):
    BLOOMBERG = 'bloomberg.com'
    NYTIMES = 'nytimes.com'
    BLOOMBERG_SHORT = 'bloomberg'
    NYTIMES_SHORT = 'nytimes'


def save_website_to_file(filename, text):
    with open(f'{user_save_path}/{filename}', 'w') as f:
        f.write(text)
    pages_viewed_by_user.append(filename)
    print(text)
    print(f'File {filename} saved')


def display_website(url_):
    stripped_url = url_.strip('.com')
    if stripped_url in pages_viewed_by_user:
        read_file(stripped_url)
        pages_viewed_by_user.append(stripped_url)
    else:
        if url.lower() == Websites.BLOOMBERG.value:
            save_website_to_file(Websites.BLOOMBERG_SHORT.value, bloomberg_com)
            save_history(pages_viewed_by_user)
        elif url.lower() == Websites.NYTIMES.value:
            save_website_to_file(Websites.NYTIMES_SHORT.value, nytimes_com)
            save_history(pages_viewed_by_user)
        elif url.lower() == 'exit':
            exit('Goodbye')
        else:
            print('Error check Your address')


def read_file(filename):
    with open(f'{user_save_path}/{filename}', 'r') as f:
        print(f.read())


def load_history():
    with open(f'{history_file_path}{history_file_name}') as f:
        list_ = f.read().splitlines()
        print(list_)
        return list_


def save_history(history):
    with open(f'{history_file_path}{history_file_name}', 'w') as f:
        for h in history:
            f.write(h)
            f.write('\n')

#
# def display_previous_website():


args = sys.argv
current_path = os.getcwd()  # retrieves current directory user is working in
user_save_path = os.path.join(current_path, args[1])  # creates a save path for visited pages
history_file_path = current_path + '/' + args[1] + '/'
history_file_name = 'history'

if os.path.exists(user_save_path):
    pass
else:
    os.mkdir(user_save_path)

pages_viewed_by_user = []
if os.path.isfile(f'{history_file_path}{history_file_name}'):
    pages_viewed_by_user = load_history()
    print(pages_viewed_by_user)

url = ''
while url.lower() != 'exit':
    print(pages_viewed_by_user)
    url = input('Type url ')
    if url.__contains__('.'):
        display_website(url)

    elif not url.__contains__('.') or pages_viewed_by_user.__len__() > 0:
        if url.lower() == Websites.BLOOMBERG_SHORT.value and Websites.BLOOMBERG_SHORT.value in pages_viewed_by_user:
            read_file(Websites.BLOOMBERG_SHORT.value)
            pages_viewed_by_user.append(Websites.BLOOMBERG_SHORT.value)
            
        elif url.lower() == Websites.NYTIMES_SHORT.value and Websites.NYTIMES_SHORT.value in pages_viewed_by_user:
            read_file(Websites.NYTIMES_SHORT.value)
            pages_viewed_by_user.append(Websites.NYTIMES_SHORT.value)
        elif url == 'back':
            read_file(pages_viewed_by_user[pages_viewed_by_user.__len__() - 2])
            pages_viewed_by_user.pop(pages_viewed_by_user.__len__() - 2)
        elif url.lower() == 'exit':
            break
        else:
            print('Error no page in history')
    elif url.lower() == 'exit':
        break
    else:
        print('Error')
