from Registry import Registry
from get_controlset import getControlSet

def getPlugin(reg_sys, reg_nt='', reg_soft=''):

    print ("\n" + ("=" * 51) + "\nSESSION MANAGER INFORMATION\n" + ("=" * 51))

    current = getControlSet(reg_sys)       
    
    controlSetSubkeys = reg_sys.open('%s\\Control' % (current))

    session_manager_list = [('%s\\' % (current)) + controlSetSubkeys.name() + "\\Session Manager"]

    try:
        for k in session_manager_list:
            key = reg_sys.open(k)
            for v in key.values():
                if v.value_type() == Registry.RegSZ or v.value_type() == Registry.RegExpandSZ or v.value_type() == Registry.RegMultiSZ:
                    if v.name() == "PendingFileRenameOperations" or v.name() == "BootExecute":
                        for emptySpaces in v.value():
                            if emptySpaces == '':
                                pass
                            else:
                                print 'Key: %s\nValue: %s\n' % (str(v.name()).encode('ascii', 'ignore'), str(emptySpaces).encode('ascii', 'ignore'))
                    else:
                        pass

    except Registry.RegistryKeyNotFoundException as e:
        pass