from Registry import Registry

def getPlugin(reg_soft, reg_nt='', reg_sys=''):

    print ("\n" + ("=" * 51) + "\nWINDOWS LOGON\n" + ("=" * 51))

    winlogon_list = ["Microsoft\\Windows NT\\CurrentVersion",
                     "Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\Notify"]

    try:
        for k in winlogon_list:
            key = reg_soft.open(k)
            winlogon_subkeys = key.subkeys()
            for subK in winlogon_subkeys:
                if subK.name() == "Winlogon":
                    winlogon_path = "Microsoft\\Windows NT\\CurrentVersion\Winlogon"
                    for winlogon_values in subK.values():
                        if winlogon_values.name() == "Shell":
                            print 'Key: %s\nValue: %s\nRegPath: %s\n' % (subK.name(), subK.value("Shell").value(), winlogon_path)
                        else:
                            pass
                        if winlogon_values.name() == "Userinit":
                            print 'Key: %s\nValue: %s\nRegPath: %s\n' % (subK.name(), subK.value("Userinit").value(), winlogon_path)
                        else:
                            pass
                        if winlogon_values.name() == "Taskman":
                            print 'Key: %s\nValue: %s\nRegPath: %s\n' % (winlogon_values.name() == "Taskman", winlogon_path)
                        else:
                            pass
                else:
                    pass

    except Registry.RegistryKeyNotFoundException as e:
        pass