import Convert


def check_elements(links, rechts, index = 0):

    if Convert.convert(links[index]) < Convert.convert(rechts[index]):
        return False

    if links.lower() == rechts.lower():
        if ord(links[0]) > ord(rechts[0]):
            return True
        elif ord(links[0]) < ord(rechts[0]):
            return False

    try:
        if Convert.convert(links[index]) == Convert.convert(rechts[index]):
            return check_elements(links, rechts, index + 1)

    except IndexError:
        if len(links) > len(rechts):
            return True

        else:
            return False

    return True
