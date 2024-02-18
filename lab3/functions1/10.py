def uniq(input):
    unique = []
    for el in input:
        if el not in unique:
            unique.append(el)
    return unique

