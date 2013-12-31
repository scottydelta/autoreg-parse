from Registry import Registry

def getPlugin(reg_nt, reg_soft='', reg_sys=''):

    print ("\n" + ("=" * 51) + "\nARCHIVE LOCATIONS (WinZip, WinRAR, and 7zip)\n" + ("=" * 51))
    #archivedFiles = []

    try:
        print ("WINZIP: Software\\Nico Mak Computing\\WinZip\\filemenu")
        winzip = reg_nt.open("Software\\Nico Mak Computing\\WinZip")
        print winzip
        for wz_archives in winzip.subkeys():
            if wz_archives.name() == 'filemenu':
                print 'LastWrite Time: %s\n' % (winzip.timestamp())
                for wz_v in wz_archives.values():
                    print '%s -> %s' % (wz_v.name(), wz_v.value())
            else:
                pass

        print ("\n""WINZIP: Software\\Nico Mak Computing\\WinZip\\WIZDIR")
        for wz_archives in winzip.subkeys():
            if wz_archives.name() == 'WIZDIR':
                print 'LastWrite Time: %s\n' % (winzip.timestamp())
                for wz_v in wz_archives.values():
                    print '%s -> %s' % (wz_v.name(), wz_v.value())
            else:
                pass

    except Registry.RegistryKeyNotFoundException as e:
        pass
