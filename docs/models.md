# MCServerData
- server_id[int] - unique server identifier
- name[string] - meaningful name of the server
- description[string] - description of the server
- client_json_url[string] - url of the client.json file
- client_json_size[int] - size of client.json in bytes
- modded[boolean] - if the server contains mods


# MCModPackData
- modpack_id[int] - unique modpack identifier
- server_id[int] - unique server identifier this modpack belongs to
- name[string] - meaningful name of the modpack
- description[string] - description of the modpack
- required[boolean] - if this modpack required to enter the server
- url[string] - url from where to download the modpack
- size[int] - size of this modpack in bytes
