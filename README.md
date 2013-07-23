# Codebase-CLI

Codebase-CLI is a command line interface for codebasehq.com.

## Usage

### Initialise

Initialisation will run the first time a command is used. You will be asked a set of questions pertaining to your codebasehq.com setup.

#### Automatic discovery

For automatic discovery the name of the branch is important as it will map to the ticket that you are working on. Either ticket-xxx- or xxx- are valid.

    $ cd ticket-1234-my-awesome-code

#### Manually set ticket

If you are not working on a branch that can be used for automatic discovery you can manually set the ticket that you are working on.

    $ cb ticket set 1234

Automatic discovery always trumps a manually set ticket.

### Status

To get the status of the current ticket.

    $ cb status

To get the status of a ticket explicitly.

    $ cb status 1234

To set the status via interface.

    $ cb status update

Explicitly set status straight away.

    $ cb status update 1

The id for the statuses can be retrieved via.

    $ cb statuses

### Assigning

To get the currently assigned user.

    $ cb assigned

To set the assigned user via interface.

    $ cb assigned update

### Comments

To get a log of comments.

    $ cb comments

To create a comment via interface.

    $ cb comment update

To create a comment straight away.

    $ cb comment update 'This is my new comment that I would like to make'

### Description

To get the description of the current ticket.

    $ cb description

### Open

To open the current ticket in a browser window.

    $ cb open

### Review

To checkout a branch and mark a ticket as "In Review". This will try to autodiscover the ticket you want to work on but will let you choose if it is ambiguous.

    $ cb review 1234

### Update multiple values

To update multiple values at once (notes, status, assignee).

    $ cb ticket update

### To view the ticket number cb is working against.

    $ cb ticket number
