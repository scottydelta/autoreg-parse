from Registry import Registry

def getPlugin(reg_soft, reg_nt='', reg_sys=''):

    print ("\n" + ("=" * 51) + "\nWINDOWS LOGON\n" + ("=" * 51))

    winlogon_list = ["Microsoft\\Windows NT\\CurrentVersion\\Winlogon"]
    white_list = ["explorer.exe", "c:\windows\system32\userinit.exe,"]

    try:
        for k in winlogon_list:
            key = reg_soft.open(k)

            for v in key.values():
                if v.name().lower() == "shell":
                    if v.value().lower() != white_list[0]:
                        print 'ALERT!!!\nKey Name: %s\nValue: %s\nLastWrite: %s\n' % (v.name(), v.value(), key.timestamp())
                    else:
                        print 'Key Name: %s\nValue: %s\nLastWrite: %s\n' % (v.name(), v.value(), key.timestamp())
                
                elif v.name().lower() == "userinit":
                    if v.value().lower() != white_list[1]:
                        print 'ALERT!!!\nKey Name: %s\nValue: %s\nLastWrite: %s\n' % (v.name(), v.value(), key.timestamp())
                    else:
                        print 'Key Name: %s\nValue: %s\nLastWrite: %s\n' % (v.name(), v.value(), key.timestamp())
                
                elif v.name().lower() == "taskman":
                    print 'Key Name: %s\nValue: %s\nLastWrite: %s\n' % (v.name(), v.value(), key.timestamp())
                else:
                    pass

    except Registry.RegistryKeyNotFoundException as e:
        pass