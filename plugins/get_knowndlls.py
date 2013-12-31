from Registry import Registry
from get_controlset import getControlSet

def getPlugin(reg_sys, reg_nt='', reg_soft=''):

    current = getControlSet(reg_sys)
    knowndlls = reg_sys.open('%s\\Control\\Session Manager\\KnownDLLs' % (current))

    print ("\n" + ("=" * 51) + "\nKNOWN DLLs\n" + ("=" * 51))
    print '\nKnown DLLs LastWrite: %s\n' % (knowndlls.timestamp())

    try:
        for v in knowndlls.values():
            print 'Name: %s\nDLL: %s\n' % (v.name(), v.value())

    except Registry.RegistryKeyNotFoundException as e:
        pass