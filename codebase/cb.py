def command(fn, *args):
    return fn


@command('ticket')
def ticket(number):
    '''Links to the supplied ticket number for any subsequent commands.'''
    pass


@command('status')
def status():
    '''Gets the status of the current ticket.'''
    pass


@command('status', 'update')
def status_update(new_status=''):
    '''Sets the status of the ticket.'''
    pass


@command('assign')
@command('assigned')
def assigned():
    '''Gets the currently assigned user.'''
    pass


@command('assign', 'update')
@command('assigned', 'update')
def assigned_update(user):
    '''Sets the assigned user.'''
    pass


@command('comment')
@command('comments')
def comments(user=''):
    '''Gets a log of the comments.'''
    pass


@command('comment', 'update')
@command('comments', 'update')
def comments_update(message=''):
    '''Creates a comment.'''
    pass

