import re
from Registry import Registry

def getPlugin(reg_soft, reg_nt='', reg_sys=''):

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
                    #if v.value_type() == Registry.RegSZ or v.value_type() == Registry.RegExpandSZ or v.value_type() == Registry.RegMultiSZ:
                    if v.value() == '':
                        print 'Key: %s\nValue: No Value to report\n' % (v.name().encode('ascii', 'ignore'))
                    else:
                        print 'Key: %s\nValue: %s\n' % (v.name().encode('ascii', 'ignore'), v.value().encode('ascii', 'ignore'))
                else:
                    pass

    except Registry.RegistryKeyNotFoundException as e:
        pass