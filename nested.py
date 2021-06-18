def parse(data, key):
    results = []
    items = [data]

    while items:
        current = items.pop(0)

        if isinstance(current, dict):
            if key in current:
                results.append(current[key])
                
            items.extend(current.values())

        elif isinstance(current, list):
            items.extend(current)

    return results
