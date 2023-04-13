
# todo

COMMAND_SUCCESS = "[AI服务]\n命令成功完成"
COMMAND_FAILED = "[AI服务]\n执行失败:\n"

def ai_help():
    s = "[AI服务帮助]"
    for i in commands.items():
        s += f"\n{i[0]}: {i[1][0]}"
    return s

def ai_attach():
    return COMMAND_SUCCESS

def ai_detach():
    return COMMAND_SUCCESS

def ai_enable():
    return COMMAND_SUCCESS

def ai_disable():
    return COMMAND_SUCCESS

def ai_timeout():
    return COMMAND_SUCCESS

def ai_up():
    return COMMAND_SUCCESS

def ai_down():
    return COMMAND_SUCCESS

def ai_status():
    return COMMAND_SUCCESS

def ai_mask():
    return COMMAND_SUCCESS

def ai_unmask():
    return COMMAND_SUCCESS

commands = {
    "help": ["查看帮助", ai_help],
    "attach": ["立即启动AI服务并接管当前会话", ai_attach],
    "detach": ["取回AI会话权", ai_detach],
    "enable": ["允许自动启动AI服务并接管当前会话", ai_enable],
    "disable": ["禁止AI服务接管当前会话", ai_disable],
    "timeout": ["设置AI服务自动接管当前会话的等待时间", ai_timeout],
    "up": ["立即启动AI服务", ai_up],
    "down": ["立即停止AI服务", ai_down],
    "status": ["获取AI服务状态", ai_status],
    "mask": ["立即停止AI服务并全局禁止接管会话", ai_mask],
    "unmask": ["全局启用接管会话", ai_unmask],
}

# print(ai_help())
# print(commands["enable"][1]())

def execute(s: str) -> str:
    c = s.split(" ")
    if len(c) <= 0:
        return COMMAND_FAILED + "请输入子命令"
    if c[0] not in commands:
        return COMMAND_FAILED + "找不到命令，请输入 .ai help 查看帮助"
    return commands[c[0]][1]()
