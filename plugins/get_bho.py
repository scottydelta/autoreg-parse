from Registry import Registry

def getPlugin(reg_soft, reg_nt='', reg_sys=''):

    bho_keys = ["Microsoft\\Windows\\CurrentVersion\\Explorer\\Browser Helper Objects",
                "Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Browser Helper Objects"]

    BHO_list = []

    print ("\n" + ("=" * 51) + "\nBROWSER HELPER OBJECTS\n" + ("=" * 51))

    try:
        for b in bho_keys:
            k = reg_soft.open(b)
            for v in k.subkeys():
                BHO_list.append(v.name())

        for clsids in BHO_list:
            ke = reg_soft.open("Classes\\CLSID\\%s" % (clsids))
            print "Key Name: %s\nPath %s\nKey Last Write: %s\n" % (ke.name(), ke.subkey("InProcServer32").value('').value(), ke.timestamp())

    except Registry.RegistryKeyNotFoundException as e:
        pass