def getPlugin(reg_soft, reg_sys='', reg_nt=''):

    print ("\n" + ("=" * 51) + "\nACTIVE SETUP - INSTALLED COMPONENTS \n" + ("=" * 51))

    active_setup = ["Microsoft\\Active Setup\\Installed Components",
                    "Wow6432Node\\Microsoft\\Active Setup\\Installed Components"]

    active_setup_list = []
    try:
        for m in active_setup:
            k = reg_soft.open(m)
            for v in k.subkeys():
                active_setup_list.append(v.name())

            for keys in active_setup_list:
                k = reg_soft.open(m + "\\%s" % (keys))
                for activesets in k.values():
                    if activesets.name() == "StubPath":
                        if activesets.value() == '':
                            pass
                        else:
                            print 'Key: %s\nValue: %s\n' % (k.name().encode('ascii', 'ignore'), activesets.value().encode('ascii', 'ignore'))
                    else:
                        pass

    except Registry.RegistryKeyNotFoundException as e:
        pass