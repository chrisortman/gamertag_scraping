import re

pattern = re.compile(r"^n.+007,76\d\d\d$")
values = open("extracted.csv")
for line in values:
   if pattern.match(line):
      print(line)
