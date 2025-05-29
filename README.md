# 【钉钉打卡自动化】

1. 定时发邮件，影刀每隔一分钟检测收件箱。
2. 检测到【钉钉打卡】的主题或内容，执行abd脚本触发钉钉打卡，adb自动化打卡脚本如下：

```shell
@echo off
setlocal enabledelayedexpansion

adb kill-server && adb start-server

adb reconnect offline

set "displayState=OFF"
for /f "tokens=*" %%a in ('adb -s d77c234 shell dumpsys power ^| findstr /c:"Display Power: state=" /m') do (
    set "line=%%a"
    echo !line!
    if "!line!"=="Display Power: state=ON" (
        set "displayState=ON"
    )
)

echo Display state is: !displayState!

cd D:\env\platform-tools-latest-windows\platform-tools
D:

if "!displayState!"=="OFF" (
    adb -s d77c234 shell input keyevent 26
    timeout /t 3
)

adb -s d77c234 shell am start -n com.alibaba.android.rimet/com.alibaba.android.rimet.biz.LaunchHomeActivity
timeout /t 15
adb -s d77c234 shell am force-stop com.alibaba.android.rimet
timeout /t 5
adb -s d77c234 shell input keyevent 3
timeout /t 5
adb -s d77c234 shell input keyevent 26

endlocal
```
