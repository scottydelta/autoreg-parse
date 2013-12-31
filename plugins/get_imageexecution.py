from Registry import Registry

def getPlugin(reg_soft, reg_nt='', reg_sys=''):

    ifeo = reg_soft.open("Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options")

    print ("\n" + ("=" * 51) + "\nIMAGE FILE EXECUTION OPTIONS\n" + ("=" * 51))

    try:
        for subkey in ifeo.subkeys():
            for v in subkey.values():
            	if v.name().lower() == "debugger":
            		if v.value_type() == Registry.RegSZ or \
            		v.value_type() == Registry.RegExpandSZ:
            			print 'Key Name: %s\nValue: %s\nLastWrite: %s\n' % (subkey.name(), v.value(), subkey.timestamp())
            		else:
            			pass

    except Registry.RegistryKeyNotFoundException as e:
        pass