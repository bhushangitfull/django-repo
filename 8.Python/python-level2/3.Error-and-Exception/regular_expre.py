import re

patterns = ['term1','term2']

text = 'with the term1, not'

for pattern in patterns:
    print("I'm searching for: "+pattern)

match = re.search('term1', text)

print(match.start())

print(re.findall('match', 'test match phrase match in match'))

def multi_re_find(pattern,phrase):

    for pat in pattern:
        print("searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print("\n")
    

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dsssss.sdddd'
test_patterns = ['sd*']

multi_re_find(test_patterns, test_phrase)