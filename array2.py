import json


class ComponentObject:
    artifactId = ""
    groupId = ""
    version = ""
    
    def __init__(self,artifactId,groupId,version):
        self.artifactId = artifactId
        self.groupId = groupId
        self.version = version

def getComponentObjects():
    
    componentobjectslist = []
    with open('allE3Comps.json') as json_data:
        d = json.load(json_data)
    for component in d:
        if component['displayName'] is not None:
            group=""
            artifact=""
            version=""
            for part in component['displayName']['parts']:
                if 'field' in part:
                    if part['field'] == "Group":
                        group = part['value']
                    if part['field'] == "Artifact":
                        artifact = part['value']
                    if part['field'] == "Version":
                        version = part['value']
            compObj = ComponentObject(group,artifact,version)
            componentobjectslist.append(compObj)
    return componentobjectslist;
       
componentobjectslist2 = getComponentObjects();

for cm in componentobjectslist2:
    print(cm.artifactId,cm.version,cm.groupId)
	
