import json 

def RetrieveJSONFromFile(filename):
    with open(filename) as f:
        data = json.load(f)

        return data
    
def RetrieveTextFromFile(filename):
    with open(filename) as f:
        data = f.read()
        
        return data