__all__ = (
    'id_value_generator',
)


def id_value_generator(data, data_):
    l = [index for index, value in enumerate(data)]
    l_ = [index for index, value in enumerate(data_)]

    for i in l:
        if i in l_:
            yield data[i].strip('\n'), data_[i].strip('\n')
        else:
            yield data[i].strip('\n'), 'None'
