from Registry import Registry
from get_controlset import getControlSet

def getPlugin(reg_soft, reg_nt, reg_sys):

    print ("\n" + ("=" * 51) + "\nTRADITIONAL \"RUN\" KEYS\n" + ("=" * 51))

    hklm_run_list = ["Microsoft\\Windows\\CurrentVersion\\Run",
                     "Microsoft\\Windows\\CurrentVersion\\RunOnce",
                     "Microsoft\\Windows\\CurrentVersion\\RunOnceEx",
                     "Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run",
                     "Microsoft\\Active Setup\\Installed Components",
                     # "Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad",
                     # "Microsoft\\Windows\\CurrentVersion\\Authentication\\Credential Providers",
                     "Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run",
                     "Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\RunOnce",
                     "Wow6432Node\\Microsoft\\Active Setup\\Installed Components",
                     "Microsoft\\Windows\\CurrentVersion\\Explorer\\SharedTaskScheduler",
                     "Classes\\Protocols\\Handler",
                     "Classes\\*\\ShellEx\\ContextMenuHandlers"]

    ntuser_run_list = ["Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                       "Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce",
                       "Software\\Microsoft\\Windows\\CurrentVersion\\RunServicesOnce",
                       "Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows",
                       #"Software\\Wow6432Node\\Microsoft\\Active Setup\\InstalledComponents",
                       "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run"]

    try:

        for k in hklm_run_list:
            key = reg_soft.open(k)
            for v in key.values():
                if v.value_type() == Registry.RegSZ or v.value_type() == Registry.RegExpandSZ or v.value_type() == Registry.RegMultiSZ:
                    print 'Key: %s\nValue: %s\nRegPath: %s\n' % (v.name().encode('ascii', 'ignore'), v.value().encode('ascii', 'ignore'), k)

        for k in hklm_run_list:
            print k
            key = reg_sys.open(k)
            for v in key.values():
                if v.value_type() == Registry.RegSZ or v.value_type() == Registry.RegExpandSZ or v.value_type() == Registry.RegMultiSZ:
                    print 'Key: %s\nValue: %s\nRegPath: %s\n' % (v.name().encode('ascii', 'ignore'), v.value().encode('ascii', 'ignore'), k)

        for k in ntuser_run_list:
            key = reg_nt.open(k)
            for v in key.values():
                if v.value_type() == Registry.RegSZ or v.value_type() == Registry.RegExpandSZ or v.value_type() == Registry.RegMultiSZ:
                    print 'Key: %s\nValue: %s\nRegPath: %s\n' % (v.name().encode('ascii', 'ignore'), v.value().encode('ascii', 'ignore'), k)

    except Registry.RegistryKeyNotFoundException as e:
        pass

def getAppInitDLLs(reg_soft):

    print ("\n" + ("=" * 51) + "\nAppInit_DLLs\n" + ("=" * 51))

    appinit_dlls = ["Microsoft\\Windows NT\\CurrentVersion\\Windows",
                    "Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Windows"]

    try:
        for k in appinit_dlls:
            key = reg_soft.open(k)
            for v in key.values():
                matchObj = re.match(r"AppInit_DLLs", v.name())
                path = k + "\\" + v.name()
                if matchObj:
                    if v.value_type() == Registry.RegSZ or v.value_type() == Registry.RegExpandSZ or v.value_type() == Registry.RegMultiSZ:
                        print 'Key: %s\nValue: %s\nRegPath: %s\n' % (v.name().encode('ascii', 'ignore'), v.value().encode('ascii', 'ignore'), path)
                else:
                    pass

    except Registry.RegistryKeyNotFoundException as e:
        pass

def getWinlogon(reg_soft):

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
                            #print 'Key: %s\nValue: %s\nRegPath: %s\n' % (winlogon_values.name(), winlogon_path)
                        else:
                            pass
                else:
                    pass

    except Registry.RegistryKeyNotFoundException as e:
        pass