import sys
import ConfigParser
import re
import requests

from lxml import etree

from git.repo.base import Repo

config = ConfigParser.SafeConfigParser()
config.read('.cbconfig')

AUTH_USERNAME = config.get('auth', 'username')
AUTH_TOKEN = config.get('auth', 'token')
AUTH_CREDENTIALS = (AUTH_USERNAME, AUTH_TOKEN,)

PROJECT_NAME = config.get('project', 'name')

API_URL = 'http://api3.codebasehq.com/%s/' % PROJECT_NAME


class Commander(object):

    def __init__(self):
        self.function_map = {}

    def command(self, *args):
        key = args

        def wrapper(func):
            self.function_map[key] = func
            return func

        return wrapper


commander = Commander()
repo = Repo()


@commander.command('ticket')
def ticket(number):
    '''Links to the supplied ticket number for any subsequent commands.'''
    pass


@commander.command('status')
def status(ticket_number=None):
    '''Gets the status of the current ticket.'''
    branch_name = repo.active_branch.name
    if not ticket_number:
        ticket_no = re.match('^(?:ticket-)?([0-9]+)', branch_name).groups()[0]
    else:
        ticket_no = ticket_number

    res = requests.get('%stickets/%s' % (API_URL, ticket_no), auth=AUTH_CREDENTIALS)
    content = res.content
    root = etree.fromstring(content)
    print root.xpath('/ticket/status/name')[0].text


@commander.command('status', 'update')
def status_update(new_status=''):
    '''Sets the status of the ticket.'''
    pass


@commander.command('assigned')
def assigned():
    '''Gets the currently assigned user.'''
    pass


@commander.command('assigned', 'update')
def assigned_update(user):
    '''Sets the assigned user.'''
    pass


@commander.command('comments')
def comments(user=''):
    '''Gets a log of the comments.'''
    pass


@commander.command('comment', 'update')
def comments_update(message=''):
    '''Creates a comment.'''
    pass


if __name__ == "__main__":
    command_found = False
    command_end = len(sys.argv)
    command = tuple(sys.argv[1:])
    arguments = tuple(sys.argv[command_end:])
    while not command_found and command:
        try:
            func = commander.function_map[command]
        except KeyError:
            command_end = command_end - 1
            command = tuple(sys.argv[1:command_end])
            arguments = tuple(sys.argv[command_end:])
        else:
            command_found = True
            try:
                func(*arguments)
            except TypeError:
                print 'Too many arguments'
    if not command_found:
        print 'Command not found'
