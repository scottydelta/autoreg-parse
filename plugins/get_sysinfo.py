from Registry import Registry
from get_controlset import getControlSet
import time

def getPlugin(reg_soft, reg_sys, reg_nt=''):

    os_dict = {}

    k = reg_soft.open("Microsoft\\Windows NT\\CurrentVersion")

    try:
        for v in k.values():
            if v.name() == "ProductName":
                os_dict['ProductName'] = v.value()
            if v.name() == "EditionID":
                os_dict['EditionID'] = v.value()
            if v.name() == "CurrentBuild":
                os_dict['CurrentBuild'] = v.value()
            if v.name() == "CurrentVersion":
                os_dict['CurrentVersion'] = v.value()
            if v.name() == "InstallDate":
                os_dict['InstallDate'] = time.strftime('%a %b %d %H:%M:%S %Y (UTC)', time.gmtime(v.value()))
            else:
                pass

    except Registry.RegistryKeyNotFoundException as e:
        pass

    current = getControlSet(reg_sys)
    computerName = reg_sys.open("%s\\Control\\ComputerName\\ComputerName" % (current))

    try:
        for v in computerName.values():
            if v.name() == "ComputerName":
                os_dict["ComputerName"] = v.value()
            else:
                pass

    except Registry.RegistryKeyNotFoundException as e:
        pass

    print ("\n" + ("=" * 51) + "\nOS INFORMATION\n" + ("=" * 51))
    print "Computer Name: " + os_dict['ComputerName']
    print "Operating System: " + os_dict['ProductName'], os_dict['CurrentVersion'], os_dict['CurrentBuild']
    print "Install Date: " + os_dict['InstallDate']