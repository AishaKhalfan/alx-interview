'''ACCESS_LOG_PATTERN = '^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*(\S+)\s*" (\d{3}) (\S+)'

logLine='127.0.0.1 - - [01/Jul/1995:00:00:01 -0400] "GET /images/launch-logo.gif HTTP/1.0" 200 1839'

match = re.search(APACHE_ACCESS_LOG_PATTERN, logLine)
    host          = match.group(1)

    client_identd = match.group(2)

    user_id       = match.group(3)

    date_time     = match.group(4)

    method        = match.group(5)

    endpoint      = match.group(6)

    protocol      = match.group(7)

    response_code = int(match.group(8))

    content_size  = match.group(9)

    7

You need to make your group 7 optional by adding a ?. Use the following regex:

"^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] (\S+) (\S+)\s*(\S+)?\s* (\d{3}) (\S+)"

# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility
'''

import re

regex = r"^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] (\S+) (\S+)\s*(\S+)?\s* (\d{3}) (\S+)"

test_str = ("127.0.0.1 - - [01/Jul/1995:00:00:01 -0400] \"GET /images/launch-logo.gif HTTP/1.0\" 200 1839\n"
	"127.0.0.1 - - [01/Jul/1995:00:00:01 -0400] \"GET /\" 200 1839\n\n"
	"127.0.0.1 - - [01/Jul/1995:00:00:01 -0400] \"GET / \" 200 1839")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.

