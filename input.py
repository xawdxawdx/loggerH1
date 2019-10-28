import json, requests, os.path

http_proxy  = "http://127.0.0.1:8080"
https_proxy = "https://127.0.0.1:8080"

proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy
            }

headers = {'Content-Type' : 'application/json'}

programName = input()

jsonRequest = {"query":"query Team_year_thanks_page($first_0:Int!,$year_1:Int!,$size_2:ProfilePictureSizes!,$size_3:ProfilePictureSizes!) {query {id,...F2}} fragment F0 on ParticipantWithReputationEdge {rank,reputation,node {id,username,_profile_picture2rz4nb:profile_picture(size:$size_3)}} fragment F1 on Team {_participants113VYv:participants(first:$first_0,year:$year_1) {year_range,edges {node {id,_id,username,_profile_picture1Fh783:profile_picture(size:$size_2)},rank,cursor,...F0},pageInfo {hasNextPage,hasPreviousPage}},id} fragment F2 on Query {_teamVmULt:team(handle:\"" + programName + "\") {id,...F1},id}","variables":{"first_0":100,"year_1":2019,"size_2":"medium","size_3":"large"}}
r = requests.post('https://hackerone.com/graphql?', json = jsonRequest, headers=headers, verify=False)

parsed_string2 = json.loads(r.text)

if os.path.exists("programs/" + programName + '.json') == False:
  with open("programs/" + programName + '.json', 'w') as json_file:
    json.dump(parsed_string2, json_file)