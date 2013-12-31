from Registry import Registry

def getPlugin(reg_nt, reg_sys='', reg_soft=''):

    print ("\n" + ("=" * 51) + "\nSYSINTERNAL TOOLS THAT HAVE BEEN RUN \n" + ("=" * 51))

    sysinternal = ["Software\\Sysinternals"]

    try:
        for k in sysinternal:
            key = reg_nt.open(k)
            sysinternal_keys = key.subkeys()
            for sysKeys in sysinternal_keys:
                for v in sysKeys.values():
                    if "EulaAccepted" in v.name():
                        if v.value() == 1:
                            print 'Key: %s\nLast Write: %s\n' % (sysKeys.name(), sysKeys.timestamp())
                        else:
                            pass
                    else:
                        pass
    except Registry.RegistryKeyNotFoundException as e:
        pass