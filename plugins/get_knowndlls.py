from Registry import Registry

def getPlugin(reg_sys, reg_nt='', reg_soft=''):

    selectCurrent = reg_sys.open("Select")
    selectCurrentNumber = selectCurrent.value("Current").value()
    controlSetSubkeys = reg_sys.open('ControlSet00%d\\Control' % (selectCurrentNumber))

    known_DLLs_list = [('ControlSet00%d\\' % (selectCurrentNumber)) + controlSetSubkeys.name() + "\\Session Manager\\KnownDLLs"]

    print ("\n" + ("=" * 51) + "\nKNOWN DLLs\n" + ("=" * 51))

    try:
        for k in known_DLLs_list:
            key = reg_sys.open(k)
            for v in key.values():
                if v.value_type() == Registry.RegSZ or v.value_type() == Registry.RegExpandSZ or v.value_type() == Registry.RegMultiSZ:
                    print 'Key: %s\nValue: %s\n' % (str(v.name()).encode('ascii', 'ignore'), str(v.value()).encode('ascii', 'ignore'))

                else:
                    pass

    except Registry.RegistryKeyNotFoundException as e:
        pass