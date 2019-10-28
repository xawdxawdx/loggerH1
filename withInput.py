import json, requests, os.path

http_proxy  = "http://127.0.0.1:8080"
https_proxy = "https://127.0.0.1:8080"

proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy
            }

headers = {'Content-Type' : 'application/json'}

programName = input()

for filename in os.listdir("/root/tools/loggerH1/programs/"):
  if filename.endswith(".json"):
    jsonRequest = {"query":"query Team_year_thanks_page($first_0:Int!,$year_1:Int!,$size_2:ProfilePictureSizes!,$size_3:ProfilePictureSizes!) {query {id,...F2}} fragment F0 on ParticipantWithReputationEdge {rank,reputation,node {id,username,_profile_picture2rz4nb:profile_picture(size:$size_3)}} fragment F1 on Team {_participants113VYv:participants(first:$first_0,year:$year_1) {year_range,edges {node {id,_id,username,_profile_picture1Fh783:profile_picture(size:$size_2)},rank,cursor,...F0},pageInfo {hasNextPage,hasPreviousPage}},id} fragment F2 on Query {_teamVmULt:team(handle:\"" + programName + "\") {id,...F1},id}","variables":{"first_0":100,"year_1":2019,"size_2":"medium","size_3":"large"}}
    r = requests.post('https://hackerone.com/graphql?', json = jsonRequest, headers=headers, verify=False)
    
    parsed_string2 = json.loads(r.text)
    
    if os.path.exists("programs/" + filename) == False:
      with open("programs/" + filename, 'w') as json_file:
        json.dump(parsed_string2, json_file)
    
    with open("programs/" + filename, 'r') as f:
      parsed_string = json.load(f)
    
    l = open(programName + "_log.txt", "a+") # make a logfile for bb program
    
    for node in parsed_string["data"]["query"]["_teamVmULt"]["_participants113VYv"]["edges"]:
      for node2 in parsed_string2["data"]["query"]["_teamVmULt"]["_participants113VYv"]["edges"]:
        if node["node"]["username"] == node2["node"]["username"]: # Go throuth users
          if node2["reputation"] > node["reputation"]: # If user got more reputation, than the past
             if node2["reputation"] - node["reputation"] == 7: # TRIAGED
                print(node["node"]["username"] + " got triaged")
                l.write(node["node"]["username"] + " got triaged")
             else:
               if node2["reputation"] - node["reputation"] == 2: # Correct duplicate
                   print(node["node"]["username"] + " got correct duplicate")
                   l.write(node["node"]["username"] + " got correct duplicate")
             else:
               if node2["reputation"] - node["reputation"] == 15: # bounty received
                   print(node["node"]["username"] + " got a little bounty")
                   l.write(node["node"]["username"] + " got a little bounty\n")
             else:
               if node2["reputation"] - node["reputation"] == 25: # 1000+ $ received
                   print(node["node"]["username"] + " got a medium bounty")
                   l.write(node["node"]["username"] + " got a medium bounty\n")
             else:
               if node2["reputation"] - node["reputation"] == 50: # 1500+ $ received
                   print(node["node"]["username"] + " got a huge bounty")
                   l.write(node["node"]["username"] + " got a huge bounty\n")
          else:
             if node["reputation"] - node2["reputation"] == 5: # Got N/A :()
               print(node["node"]["username"] + " got N/A")
                l.write(node["node"]["username"] + " got correct duplicate")
             else:
               if node["reputation"] - node2["reputation"] == 7: # Need more info :/
                 print("Mail.ru needs more information from " + node["node"]["username"])
                   l.write("Mail.ru needs more information from " + node["node"]["username"])
                  
    with open("programs/" + filename, 'w') as json_file:
       json.dump(parsed_string2, json_file)