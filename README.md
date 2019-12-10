#Proposed API

##END POINTS

### /sessions

    Collection of sessions
    
    GET  - list active sessions
    POST - create new session
    
### /sessions/uuid
    GET    - dump current session
    PUT    - update session
                - add additional data
                - change status (e.g. locked)
    DELETE - delete session 
    
### /sessions/uuid/files
    TBD
    
### /sessions/metadata
    TBD

## DATA MODEL

### sessions
    
    uuid    - primary uuid session id
    status  - session status (open/locked) 
    created - creation datetime
    updated - last update datetime  
    
