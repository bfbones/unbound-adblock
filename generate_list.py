###
#   This small script generates couple of config
#   entries for unbound local-zones.
#   The server list is based on 'yoyo.org's adserverlist
#   http://pgl.yoyo.org/as/serverlist.php
###

##
# open list of adservers

adservers = open('adblocklist')


##
# every domain is redirected to localhost
# you may want to adjust that
# possible zone types are:
#   deny refuse static transparent redirect nodefault

zonetype = 'redirect'
destination = "A 127.0.0.1"

##
# generate unbound config entry for each server

for line in adservers:
  line = line.replace('\n', '')

  print('local-zone: "' + line + '" ' + zonetype)
  print('local-data: "' + line + ' ' + destination + '"')
