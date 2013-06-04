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


@commander.command('ticket')
def ticket(number):
    '''Links to the supplied ticket number for any subsequent commands.'''
    pass


@commander.command('status')
def status():
    '''Gets the status of the current ticket.'''
    pass


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
