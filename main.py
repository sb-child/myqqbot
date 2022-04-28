import websocket
import time
import rel
import json
import requests
import reaction
import re

cq_re = re.compile(r"(\[CQ:.*])?(.*)")
cq_re_replys = re.compile(r"(\[CQ:reply,id=)(-?\d+)(.*?)]")


def send_msg(t: str, target: int, m: str, reply=""):
    msg = ""
    if reply != "":
        msg += "[CQ:reply,id=" + reply + ",qq=" + str(target) + "]"
    msg += ("> " + m) if m.find("[CQ:") == -1 else m
    print("> send:", msg)
    print("> ", requests.post("http://127.0.0.1:5700/send_msg", data={
        "message_type": t,
        "user_id": target,
        "group_id": target,
        "message": msg,
        "auto_escape": False,
    }).json())


def delete_msg(target: int):
    print("> ", requests.post("http://127.0.0.1:5700/delete_msg", data={
        "message_id": target,
    }).json())


def on_message(ws, message):
    m = dict(json.loads(message))
    print(m)
    if not ("post_type" in m and (m["post_type"] == "message" or m["post_type"] == "message_sent")):
        print("- not message")
        return
    if "self_id" not in m or "user_id" not in m:
        print("- bad type")
        return
    if m["self_id"] != m["user_id"]:
        print("- not me")
        return
    reply = ""
    if m["message_type"] == "group":
        reply = m["group_id"]
    elif m["message_type"] == "private":
        reply = m["target_id"]
    else:
        print("- other type")
        return
    rm_raw = cq_re.findall(m["raw_message"])
    if len(rm_raw) == 0 or len(rm_raw[0]) != 2:
        print("- not command")
        return
    print("- regex: ", rm_raw)
    rm: str = rm_raw[0][1].strip()
    rm_cq_reply = cq_re_replys.findall(rm_raw[0][0])
    print("- reply regex: ", rm_cq_reply)
    if len(rm_cq_reply) == 0 or len(rm_cq_reply[0]) != 3:
        print("? not reply")
        rm_cq_reply = ""
    else:
        rm_cq_reply = rm_cq_reply[0][1]
    # process
    if rm == ".ping":
        send_msg(m["message_type"], reply, "机器人已收到消息!", rm_cq_reply)
    elif rm.startswith(".r "):
        send_msg(m["message_type"], reply, reaction.parse_sub_cmd(rm[3:]), rm_cq_reply)
    else:
        return
    # delete
    delete_msg(m["message_id"])


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    print("Opened connection")


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:5701/",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()
