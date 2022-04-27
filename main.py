import websocket
import time
import rel
import json
import requests


def send_msg(t: str, target: int, m: str):
    print("> ", requests.post("http://127.0.0.1:5700/send_msg", data={
        "message_type": t,
        "user_id": target,
        "group_id": target,
        "message": "> " + m,
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
    rm = m["raw_message"]
    # process
    if rm == ".ping":
        send_msg(m["message_type"], reply, "机器人已收到消息!")
    elif rm == ".r t":
        send_msg(m["message_type"], reply, "🤔")
    elif rm == ".r tt":
        send_msg(m["message_type"], reply, "🤔🤔")
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
