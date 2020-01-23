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
    
    session_id  - session id (uuid), primary key 
    name        - short description (text)
    created     - creation (datetime)
    updated     - last update (datetime)
    deleted     - deletion (datetime)
    status      - session status (open/locked)
    description - user description/notes (text)
    exception   - system generated exceptions (text)  

### files

    file_id    - file id (uuid), primary key 
    session_id - session id (uuid) references session table
    status     - file status (char)
    name       - file name (char)
    path       - file path (char)
    ctime      - creation time 
    mtime      - modification time 
    mimetype   - type (char)
    size       - file size bytes (int)
    description = TextField(null=True)
