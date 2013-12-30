from Registry import Registry
import codecs

def getPlugin(reg_nt, reg_sys='', reg_soft=''):

    print ("\n" + ("=" * 51) + "\nUSER ASSIST\n" + ("=" * 51))

    try:
        userassist = reg_nt.open("Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\UserAssist")

        for items in userassist.subkeys():
            k = reg_nt.open("Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\UserAssist\\%s" % (items.name()))
            for ua_keys in k.subkeys():
                for ua_values in ua_keys.values():
                    print codecs.decode(ua_values.name(), 'rot_13')

    except Registry.RegistryKeyNotFoundException as e:
        pass