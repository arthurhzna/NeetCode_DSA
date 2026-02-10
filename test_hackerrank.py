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