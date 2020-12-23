import json
import boto3
import sys
import re
from fulfillment import *
from conn_handler import *

def list_clusters(event, region, state):
    emr = get_client(event, region)
    resp = emr.list_clusters()
    result = []
    print("result")
    if state == '' or state == 'all':
        for i in resp['Clusters']:
            cid=i['Id']
            cname=i['Name']
            cst=i['Status']
            result.append(cid + "  " + cname + "  " + cst)
    else:
        for i in resp['Clusters']:
            cst=i['Status']
            if cst == state.upper():
                cid=i['Id']
                cname=i['Name']
                result.append(cid + "  " + cname + "  " + cst)
        
    if len(result) == 0:
        return get_fulfillment('No EMR Clusters Found in '+ region)
    else:
        return get_fulfillment(state.title() + " Clusters are: \n" + str(result))
        
def list_instances(region, ins_state, clusterid):
    emr = get_client(event, region)
    
    result = []
    
    if ins_state == '' or ins_state == 'all':
        resp = emr.list_instances(ClusterId = clusterid)
        for i in resp['Instances']:
            iid=i['Id']
            iec2id=i['Ec2InstanceId']
            itype=i['InstanceType']
            ist=i['Status']['State']
            result.append(iid + "  " + iec2id + "  " + itype + "  " + ist)
    else:
        resp = emr.list_instances(ClusterId = clusterid, InstanceStates=[ins_state.upper()])
        for i in resp['Instances']:
            iid=i['Id']
            iec2id=i['Ec2InstanceId']
            itype=i['InstanceType']
            ist=i['Status']['State']
            result.append(iid + "  " + iec2id + "  " + itype + "  " + ist)
        
    if len(result) == 0:
        return get_fulfillment("No EMR Instances found for Cluster " + clusterid + " in "+ region)
    else:
        return get_fulfillment(ins_state.title() + " Instances in Cluster " + clusterid + " are: \n" + str(result))
        
def list_steps(region, stp_state, clusterid):
    emr = get_client(event, region)
    
    result = []
    
    if stp_state == '' or stp_state == 'all':
        resp = emr.list_steps(ClusterId = clusterid)
        print(clusterid)
        for i in resp['Steps']:
            sid=i['Id']
            sname=i['Name']
            sst=i['Status']['State']
            result.append(sid + "  " + sname + "  " + sst)
    else:
        resp = emr.list_steps(ClusterId = clusterid, StepStates=[stp_state.upper()])
        for i in resp['Steps']:
            sid=i['Id']
            sname=i['Name']
            sst=i['Status']['State']
            result.append(sid + "  " + sname + "  " + sst)
        
    if len(result) == 0:
        return get_fulfillment("No EMR Steps found for Cluster " + clusterid + " in "+ region)
    else:
        return get_fulfillment(stp_state.title() + " Steps in Cluster " + clusterid + " are: \n" + str(result))

