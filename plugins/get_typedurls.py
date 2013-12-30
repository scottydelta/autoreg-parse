from Registry import Registry

def getPlugin(reg_nt, reg_sys='', reg_soft=''):

    print ("\n" + ("=" * 51) + "\nTYPED URLS\n" + ("=" * 51))

    TypedURL = []

    try:
        typedURLs = reg_nt.open("Software\\Microsoft\\Internet Explorer\\TypedURLs")
        for url in typedURLs.values():
            print url.value()

    except Registry.RegistryKeyNotFoundException as e:
        pass