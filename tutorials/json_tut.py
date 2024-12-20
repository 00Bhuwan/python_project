import json
from importlib.metadata import metadata

from IPython.utils.coloransi import value
from pywin32_testutil import non_admin_error_codes

'''
1) Import Json
2) Parse The Json into Python Dict
3) Access the FamilyProduct Key from Root Key
4) Then Access the metakeywords key From FamilyProduct then
5) There should be lang and content and the content consist of list string
6) return the new array where the string starts from m or M
'''
with open('text.json', 'r') as json_file:
    loaded_data = json.load(json_file)
    # print(loaded_data)

pydict = dict(loaded_data)

# dict2 = pydict['Root']
# key = dict2.keys()

family = pydict['Root']['FamilyProducts']
print(family)

meta = pydict['Root']['FamilyProducts'][0]['metaKeywords']
print(meta)

key_req = pydict['Root']['FamilyProducts'][0]['metaKeywords'][0].keys()
print(key_req)

content = pydict['Root']['FamilyProducts'][0]['metaKeywords'][0]['content']
print(content)

sorted_with_m = []
for m in content:
    if (m[0][0] == 'm') or (m[0][0] == 'M'):
        sorted_with_m.append(m)
print((sorted_with_m))