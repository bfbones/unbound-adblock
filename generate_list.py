#!/usr/bin/env python3
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

sZonetype = 'static'

##
# generate unbound config entry for each server

for sServer in adservers:
  sServer = sServer.replace('\n', '')

# generate a empty static zone, so unbound answers with NXDOMAIN
  print('local-zone: "' + sServer + '" ' + sZonetype)
