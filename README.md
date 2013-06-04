# codebase-cli

## Install

    $ pip install codebase-cli
 
## Usage

### Initialise

#### Automatic discovery

For automatic discovery the name of the branch is important as it will map to the ticket. Either ticket-xxx- or xxx- are valid.

    $ cd ticket-1234-my-awesome-code
    
#### Explicit project

For explicitly linking with a project.

    $ cb project foo-bar
    
#### Explicit ticket

For explicity linking with a ticket.

    $ cb ticket xxx
    
### Status

To get the current status.

    $ cb status
    
To set the status via interface.

    $ cb status update
    
Explicitly set status straight away.

    $ cb status update new-status

### Assigning

To get the currently assigned user.

    $ cb assign[ed]
    
To set the assigned user via interface.

    $ cb assign[ed] update
    
To set the user straight away.

    $ cb assign[ed] update user
    
### Comments

To get a log of comments.

    $ cb comment[s]
    
To create a comment via interface.

    $ cb comment[s] update
    
To create a comment straight away.

    $ cb comment[s] update 'This is my new comment that I would like to make'
