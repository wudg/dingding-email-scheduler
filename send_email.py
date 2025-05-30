import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(subject, content, to_email):
    # 从环境变量获取邮箱配置
    qq_email = os.environ['QQ_EMAIL']
    auth_code = os.environ['QQ_AUTH_CODE']
    
    # 创建邮件内容
    msg = MIMEText(content, 'plain', 'utf-8')
    
    msg['From'] = qq_email
    
    # 设置 To 和 Subject 标头
    msg['To'] = to_email
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
    content = "钉钉打卡-Github"
    subject = "钉钉打卡-Github"
    return subject, content

if __name__ == "__main__":
    # 收件人邮箱（替换为你的QQ邮箱）
    to_email = "321073229@qq.com"
    
    subject, content = get_email_content()
    print(f"准备发送邮件:\n主题: {subject}\n内容: {content}")
    
    if send_email(subject, content, to_email):
        print("邮件发送任务完成")
    else:
        print("邮件发送任务失败")
