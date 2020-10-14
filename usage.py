from nested import parse

data = {"rows":[{"elements":[{"distance":{"text":"227 mi","value":365468},"duration":{"text":"3 hours 54 mins","value":14064},"status":"OK"},{"distance":{"text":"94.6 mi","value":152193},"duration":{"text":"1 hour 44 mins","value":6227},"status":"OK"}]}]}
parsed_data = parse(data, 'text') #Replace "text" with the key that you are trying to parse
print(parsed_data)
