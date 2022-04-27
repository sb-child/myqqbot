reaction = {
    "thinking": "\U0001F914",
    "nya": "\U0001F63A",
    "cat": "\U0001F408",
    "happy": "\U0001F642",
    "sad": "\U0001F625",
    "lgbt": "\U0001F3F3\U0000FE0F\U0000200D\U0001F308",
    "transgender": "\U0001F3F3\U0000FE0F\U0000200D\U000026A7\U0000FE0F",
    "transsymbol": "\U000026A7",
}

def find_reaction(query: str):
    for i, j in reaction.items():
        if i.startswith(query):
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
        
    if len(g) == 0:
        return "没有匹配到表情"
    return "".join(g)


if __name__ == "__main__":
    print(parse_sub_cmd("sad2lg2transg3ny12t"))
