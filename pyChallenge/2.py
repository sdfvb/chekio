def leteer(l1, l2):
    print(ord(l1), ' ', ord(l2), end='\t')
    print(ord(l1) - ord(l2), end='\n')


# leteer('K', 'M')
# leteer('O', 'Q')
# leteer('E', 'G')


def translater(text: str) -> str:
    """

    :param text:
    :return:
    """
    result_list = [chr(ord(x) + 2) for x in text if x.isalpha() else x]

    return ''.join(result_list)

if __name__ == '__main__':
    print(translater(
        """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""))
