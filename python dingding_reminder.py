import requests
import json
import time

# 钉钉机器人 WebHook 地址（你提供的）
DINGDING_WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=fb4678afbd31d2edace2e750562ae81fb3ccc980da7054910c2ec6473120e2d5"

def send_smoking_reminder():
    """
    是时候调整广告了（包含必过安检关键词：机器人提醒）
    """
    # 请求头
    headers = {"Content-Type": "application/json"}
    
    # 消息内容（必含关键词：机器人提醒）
    message = {
        "msgtype": "text",
        "text": {
            "content": "机器人提醒：是时候调整广告了！"
        }
    }

    try:
        # 发送请求到钉钉机器人
        response = requests.post(
            url=DINGDING_WEBHOOK,
            headers=headers,
            data=json.dumps(message)
        )
        result = response.json()
        if result.get("errcode") == 0:
            print("✅ 提醒发送成功")
        else:
            print(f"❌ 发送失败：{result}")
    except Exception as e:
        print(f"⚠️  请求异常：{e}")

if __name__ == "__main__":
    # 群内有消息时触发（这里模拟触发，可对接真实群消息监听）
    print("🔔 群内有新消息，开始发送提醒...")
    send_smoking_reminder()
