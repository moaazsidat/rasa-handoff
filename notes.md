# human-in-the-loop api

functions as the chat layer for human <> human interaction within rasa

## Implementation

### backend side (api)
- rasa chat sends the sender id
- api looks up sender id, checks to see if state is paused or unpaused
  ```
  if paused
    wait on a reply from a human (post on the sender id in the api)
    as soon as reply received, send that over to the rasa chat
  if unpaused
    do nothing/send message back stating unpaused
  ```

- could have an api dedicated to pause/unpause and another to listen for messages

### rasa side (chat)
- rasa chat sends the sender id
- poll until response of unpause is received
  ```
  while message != '/unpause':
    # get/wait on message from api 
    # pass message to chat context
  
  # message == unpause
  # unpause conversation
  ```

