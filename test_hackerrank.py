def getMatchingProducts(products, queries):
    parsed = []
    year_map = {}

    for name, price, year in products:
        price = int(price)
        year = int(year)

        parsed.append((name, price, year))

        if year not in year_map:
            year_map[year] = []
        year_map[year].append(name)

    result = []

    for qtype, value in queries:
        value = int(value)
        matches = []

        if qtype == "Type1":
            matches = year_map.get(value, [])

        elif qtype == "Type2":
            for name, price, year in parsed:
                if price < value:
                    matches.append(name)

        elif qtype == "Type3":
            for name, price, year in parsed:
                if price > value:
                    matches.append(name)

        result.append(matches)

    return result

def getMaxLength(s):
    left = 0
    seen = set()
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

def smallestString(substrings):
    n = len(substrings)

    for i in range(1, n):
        key = substrings[i]
        j = i - 1

        while j >= 0 and key + substrings[j] < substrings[j] + key: #When the value at the current index is greater than the value before it, it compares with the previous index and replaces it if the key is greater.
            substrings[j + 1] = substrings[j]
            j -= 1

        substrings[j + 1] = key

    return ''.join(substrings)