#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals
import json
import requests
import warnings
import json
import time
import uuid
import sys
import time
from thehive4py.api import TheHiveApi
from thehive4py.models import Case, CustomFieldHelper, CaseTask, CaseObservable

file_id='count.txt'
qradar_url = 'https://sec-qradar.hq.bc/api/siem/offenses?fields=id%2Cstatus%2Cdescription%2Coffense_type%2Coffense_source%2Cmagnitude%2Csource_network%2Cdestination_networks%2Cassigned_to%2Cstart_time%2Cevent_count'
warnings.filterwarnings('ignore')

def OffenseRequest():
    response_qradar = requests.get(qradar_url,headers=headers,verify=False)
    if (response_qradar.status_code)==200:
        data = response_qradar.json()
        print(data)
        new_id = (int(data[0]['id']))
        
    else:
        print(response_qradar.status.code)

    for i in range(0,new_id):
        offenseId = int(data[i]['id'])
        print('OFFENSE info ID:'+str(type(offenseId)), offenseId)
        offenseDescription = str(data[i]['description'])
        print('OFFENSE info DESCRIPTION:'+str(type(offenseDescription)), offenseDescription)
        offenseSource = str(data[i]['offense_source'])#string???
        print('OFFENSE info SOURCE :'+str(type(offenseSource)), offenseSource)
        offenseMagnitude = int(data[i]['magnitude'])#1-10
        print('OFFENSE info MAGN:'+str(type(offenseMagnitude)), offenseMagnitude)
        offenseSourceNetwork = str(data[i]['source_network'])
        print('OFFENSE info SN:'+str(type(offenseSourceNetwork)), offenseSourceNetwork)
        offenseDestinationNetworks = str(data[i]['destination_networks'])
        print('OFFENSE info DN:'+str(type(offenseDestinationNetworks)), offenseDestinationNetworks)
        offenseEventCount = int(data[i]['event_count'])
        print('OFFENSE info COUNT:'+str(type(offenseEventCount)), offenseEventCount)
        offenseType = int(data[i]['offense_type'])
        print('OFFENSE info TYPE:'+str(type(offenseType)), offenseType)
        

while True:
    OffenseRequest()
