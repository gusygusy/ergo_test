__all__ = (
    'email_name_stacker',
)


def email_name_stacker(row):
    final = []
    temp = []
    for r in row:
        for item in r:
            item = item.split(',')
            if item[0] not in temp:
                temp.append(item[0])
            else:
                final = list(final)
                final.append(tuple(temp))
                final = tuple(final)
                temp = []
                temp.append(item[0])

    final = final + tuple(temp)
    return final



