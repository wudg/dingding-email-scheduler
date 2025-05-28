import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime
import pytz

def send_email(subject, content, to_email):
    # 从环境变量获取邮箱配置
    qq_email = os.environ['QQ_EMAIL']
    auth_code = os.environ['QQ_AUTH_CODE']
    
    # 创建邮件内容
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = Header(f'自动邮件系统 <{qq_email}>', 'utf-8')
    msg['To'] = Header(to_email, 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    
    try:
        # 连接 QQ 邮件服务器
        smtp = smtplib.SMTP_SSL('smtp.qq.com', 465)
        smtp.login(qq_email, auth_code)
        smtp.sendmail(qq_email, [to_email], msg.as_string())
        smtp.quit()
        print("邮件发送成功")
        return True
    except Exception as e:
        print(f"邮件发送失败: {str(e)}")
        return False

def get_email_content():
    """生成邮件内容"""
    # 获取北京时间
    tz = pytz.timezone('Asia/Shanghai')
    now = datetime.datetime.now(tz)
    date_str = now.strftime("%Y年%m月%d日")
    time_str = now.strftime("%H:%M")
    
    # 根据时间生成不同内容
    if now.hour == 8 and now.minute >= 30:
        content = f"早上好！\n\n现在是北京时间 {time_str}，新的一天开始了！\n\n"
        content += "今日提醒：\n1. 检查工作计划\n2. 完成晨会准备\n3. 处理紧急邮件"
        subject = f"【早安提醒】{date_str}"
    elif now.hour == 18 and now.minute >= 30:
        content = f"下午好！\n\n现在是北京时间 {time_str}，工作即将结束。\n\n"
        content += "今日总结：\n1. 回顾今日完成事项\n2. 准备明日计划\n3. 放松休息"
        subject = f"【晚间提醒】{date_str}"
    else:
        content = f"测试邮件\n发送时间：{date_str} {time_str}"
        subject = f"【测试邮件】{date_str}"
    
    return subject, content

if __name__ == "__main__":
    # 收件人邮箱（替换为你的QQ邮箱）
    to_email = "your-qq-email@qq.com"
    
    subject, content = get_email_content()
    print(f"准备发送邮件:\n主题: {subject}\n内容: {content}")
    
    if send_email(subject, content, to_email):
        print("邮件发送任务完成")
    else:
        print("邮件发送任务失败")
