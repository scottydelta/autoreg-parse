from Registry import Registry

def getPlugin(reg_sys, reg_nt, reg_soft=''):

    print ("\n" + ("=" * 65) + "\nMOUNTPOINTS2 and NETWORK MRUs (XP) -> POSSIBLE LATERAL MOVEMENT\n" + ("=" * 65))

    mDevices = []
    mPoints2 = []

    try:
        mounteddevices = reg_sys.open("MountedDevices")
        mountpoints = reg_nt.open("Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MountPoints2")
        networkmru = reg_nt.open("Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Map Network Drive MRU")

        for mount in mounteddevices.values():
            mDevices.append(mount.name())

        for mps in mountpoints.subkeys():
            mPoints2.append(mps.name())

            if "#" in mps.name():
                print 'MountPoints2 Share: %s\nLast Write: %s\n' % (mps.name(), mps.timestamp())
            else:
                pass

        for mrus in networkmru.values():
            if mrus.name() == "MRUList":
                pass
            else:
                print 'Network MRU: %s\nShare: %s\nLast Write: %s\n' % (mrus.name(), mrus.value(), networkmru.timestamp())

    except Registry.RegistryKeyNotFoundException as e:
        pass