def decode(text):
    before_char = 'abcdefghijklmnopqrstuvwxyz'
    after_char = 'pvwdgazxubqfsnrhocitlkeymj'
    length_of_text = len(text);
    new_text = ''
    for text_char in text:
        if text_char in after_char:
            new_text += before_char[after_char.find(text_char)];
        else:
            new_text += text_char
    return new_text


encodedtext = '''Wxgcg txgcg ui p ixgff, txgcg ui p epm. I gyhgwt mrl lig txg ixgff wrsspnd tr irfkg txui \
hcrvfgs, nre, hfgpig tcm liunz txg crt13 ra "ixgff" tr gntgc ngyt fgkgf.'''.lower()
print decode(encodedtext)
