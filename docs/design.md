# What is this project
Server53 Index is an API for fetching/updating data about minecraft servers (and maybe other things related our server).

# Minecraft functionality (General functionality of version 0.1)
- Store / update / fetch list of minecraft servers available (as [MCServerData][m1])
- Store / update / fetch list of modpacks available for any server by server_id (as [MCModPackData][m2])
- Store / update / download files linked to by url links from [MCServerData][m1] & [MCModPackData][m2]

## Outline of required modules:
### ServersProvider
> Uses FileStore
Allows to:
    fetch list of servers,
    add new servers,
    patch existing servers,
    deprecate old servers.

### ModPackProvider
> Uses FileStore
Allows to:
    fetch list of modpacks,
    add new modpacks,
    patch existing modpacks,
    deprecate old modpacks.

### FileStorage
Somehow persists files, allows to
    add new files,
    download persisted files, 
    delete unneded files.
(Maybe should move deleted files to special storage instead of deleting)


[m1]: models.md#mcserverdata 
[m2]: models.md#mcmodpackdata 