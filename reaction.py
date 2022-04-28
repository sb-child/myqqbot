reaction = {
    "thinking,思考": "\U0001F914",
    "nya,喵": "\U0001F63A",
    "cat,猫": "\U0001F408",
    "happy,开心,高兴": "\U0001F642",
    "sad,伤心": "\U0001F625",
    "lgbt,rainbowflag,彩虹旗": "\U0001F3F3\U0000FE0F\U0000200D\U0001F308",
    "transgender,蓝粉白,跨性别旗": "\U0001F3F3\U0000FE0F\U0000200D\U000026A7\U0000FE0F",
    "transsymbol,跨性别符号": "\U000026A7",
    # sticker
    "ckbz,choukebuzi,progynova,抽颗补子": "[CQ:image,file=42289bd1d2ee01b57d20188eb6945aea.image]",
    "nzmysyn,nizenmoyeshiyaoniang,你怎么也是药娘": "[CQ:image,file=85bc5aef397a5acae9fd5ed2429a8a84.image]",
    "myzmdsyn,mayezenmodoushiyaoniang,zmdsyn,zenmodoushiyaoniang,怎么都是药娘,妈耶怎么都是药娘": "[CQ:image,file=30be9c53363b71697dcaef1f23e3f967.image]",
    "wzmybclyn,wozenmoyebianchengleyaoniang,我怎么也变成了药娘": "[CQ:image,file=9ad80e62b88adef61e29c0a7b2608cb2.image]",
    "yncxrcrxxl,yaoniangchuxianrenchuanrenxianxiangle,药娘出现人传人现象了": "[CQ:image,file=d9867355752b44da8766105a25fc38c6.image]",
}


def find_reaction(query: str):
    for i, j in reaction.items():
        match = i.split(",")
        for k in match:
            if k.startswith(query):
                return j
    return ""


def parse_sub_cmd(cmd: str):
    g = []
    if len(cmd) == 0:
        return "请输入表情短语"
    if not cmd[-1].isdigit():
        cmd += "1"
    last_word = ""
    last_number = ""
    # sad1lg4transg
    # sad * 1 + lgbt * 4 + transgender * 1
    # ca
    # cat * 1
    # cat10s52
    # cat * 10 + sad * 52
    print(cmd)
    for i in range(len(cmd)):
        if last_number == last_word == "":
            # first
            if cmd[i].isdigit():
                # first char cannot be a digit
                break
            # fill the first char
            last_word += cmd[i]
            continue
        elif last_word != "" and last_number == "":
            # at least 1 char in buffer
            if cmd[i].isdigit():
                # this char is a digit
                last_number += cmd[i]
                continue
            last_word += cmd[i]
            continue
        elif last_word != "" and last_number != "":
            # fill number
            if cmd[i].isdigit():
                last_number += cmd[i]
                continue
            # next begin
        else:
            break
        for _ in range(int(last_number)):
            g.append(find_reaction(last_word))
        last_word = last_number = ""
        last_word += cmd[i]
    if last_number != "" and last_word != "":
        for _ in range(int(last_number)):
            g.append(find_reaction(last_word))

    r = "".join(g).strip()
    if len(r) == 0:
        return "没有匹配到表情"
    return r


if __name__ == "__main__":
    print(parse_sub_cmd("sad2lg2transg3ny12t1抽2"))
