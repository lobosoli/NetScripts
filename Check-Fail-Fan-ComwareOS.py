from netmiko import ConnectHandler
from datetime import datetime

A5120_9 = {
    'device_type':'hp_comware',
    'ip':'192.168.99.9',
    'username':'admin',
    'password':'admin',
}

device = [A5120_9]

fail_list = []
normal_list = []
for x in device:
    try:
        net_connect = ConnectHandler(**x)
        output = net_connect.send_command("screen-length disable",read_timeout=30)
        output = net_connect.send_command("display fan", read_timeout=30)
        name = net_connect.find_prompt() + x['ip']
        if "Fault" in output:
            fail_list.append(x['ip'])
        elif "Normal" in output:
            normal_list.append(x['ip'])
    except Exception as e:
        print (x['ip'])
        print (e)
        continue
print (end_time)

if fail_list != []:
    print ("\nThese devices failed:")
    print (fail_list)
if normal_list != []:
    print ("\n\nThese devices OK:")
    print(normal_list)
else:
    print ("\n\nAll devices OK")
