from Registry import Registry
from get_controlset import getControlSet
from collections import defaultdict
from itertools import izip

def getPlugin(reg_sys, reg_nt='', reg_soft=''):
    current = getControlSet(reg_sys)
    servicesnames = reg_sys.open('%s\\Services' % (current))

    service_list = []
    autostart_list = []
    loadondemand_list = []
    bootloader_list = []
    autostart_dict = defaultdict(list)
    loadondemand_dict = defaultdict(list)
    bootloader_dict = defaultdict(list)
    
    service_baseline = []
    baseline = open("plugins/service_baseline.txt", 'r').read()
    service_baseline.append(baseline.rstrip('\n').lower())    

    for service in servicesnames .subkeys():
        service_list.append(service.name().lower())
    for service_name in service_list:
        k = reg_sys.open('%s\\Services\\%s' % (current, service_name))
        for v in k.values():
            if v.name() == "Start":
                start_methods = v.value()
                for service_start_code in str(start_methods):
                    # 0x2 (Auto Load) = SCM - Loaded or started automatically for all start ups.
                    if service_start_code == "2": 
                        autostart_list.append(k.name())
                        try:
                            display_name = k.value("DisplayName").value()
                            image_path = k.value("ImagePath").value()
                        except:
                            display_name = "???"
                            image_path = "No Image Path Found!"
                        autostart_dict['ServiceName'].append(k.name().lower())
                        autostart_dict['WriteTime'].append(k.timestamp())
                        autostart_dict['ImagePath'].append(image_path.lower())
                        autostart_dict['DisplayName'].append(display_name)
                    # 0x3 (Load on demand) = SCM - Not start until the user starts it.
                    elif service_start_code == "3": 
                        try:
                            display_name = k.value("DisplayName").value()
                            image_path = k.value("ImagePath").value()
                        except:
                            display_name = "???"
                            image_path = "No Image Path Found!"
                        loadondemand_dict['ServiceName'].append(k.name().lower())
                        loadondemand_dict['WriteTime'].append(k.timestamp())
                        loadondemand_dict['ImagePath'].append(image_path.lower())
                        loadondemand_dict['DisplayName'].append(display_name)
                    # 0x0 (Boot) = Kernel Loader
                    elif service_start_code == "0": 
                        bootloader_list.append(k.name())
                        try:
                            display_name = k.value("DisplayName").value()
                            image_path = k.value("ImagePath").value()
                        except:
                            display_name = "???"
                            image_path = "No Image Path Found!"
                        bootloader_dict['ServiceName'].append(k.name().lower())
                        bootloader_dict['WriteTime'].append(k.timestamp())
                        bootloader_dict['ImagePath'].append(image_path.lower())
                        bootloader_dict['DisplayName'].append(display_name)             
            else:
                pass

    print ("\n" + ("=" * 51) + "\nUNKNOWN/NON-BASELINED TYPE 2 SERVICES)\n" + ("=" * 51))
    for sname, ltime, ipath, dispname in izip(autostart_dict['ServiceName'], autostart_dict['WriteTime'], autostart_dict['ImagePath'], autostart_dict['DisplayName']):
        for name in service_baseline:
            if sname.lower() in name.lower():
                pass
            else:
                print 'Disp: {0:<10}\nName: {1:<10}\nPath: {2:<10}\nTime: {3}\n'.format(dispname, sname, ipath.encode('ascii', 'ignore'), ltime)

    print ("\n" + ("=" * 51) + "\nTYPE 2 SERVICES NOT IN SYSTEM32\n" + ("=" * 51))
    for sname, ltime, ipath, dispname in izip(autostart_dict['ServiceName'], autostart_dict['WriteTime'], autostart_dict['ImagePath'], autostart_dict['DisplayName']):
        if "system32" not in ipath.lower():
            print 'Disp: {0:<10}\nName: {1:<10}\nPath: {2:<10}\nTime: {3}\n'.format(dispname, sname, ipath.encode('ascii', 'ignore'), ltime)
        else:
            pass

    print ("\n" + ("=" * 51) + "\nALL TYPE 2 SERVICES\n" + ("=" * 51))
    for sname, ltime, ipath, dispname in izip(autostart_dict['ServiceName'], autostart_dict['WriteTime'], autostart_dict['ImagePath'], autostart_dict['DisplayName']):   
        print 'Disp: {0:<10}\nName: {1:<10}\nPath: {2:<10}\nTime: {3}\n'.format(dispname, sname, ipath.encode('ascii', 'ignore'), ltime)

    
    print ("\n" + ("=" * 51) + "\nALL TYPE 3 SERVICES\n" + ("=" * 51))
    for sname, ltime, ipath, dispname in izip(loadondemand_dict['ServiceName'], loadondemand_dict['WriteTime'], loadondemand_dict['ImagePath'], loadondemand_dict['DisplayName']):   
        print 'Disp: {0:<10}\nName: {1:<10}\nPath: {2:<10}\nTime: {3}\n'.format(dispname, sname, ipath.encode('ascii', 'ignore'), ltime)

    
    print ("\n" + ("=" * 51) + "\nALL TYPE 0 SERVICES\n" + ("=" * 51))
    for sname, ltime, ipath, dispname in izip(bootloader_dict['ServiceName'], bootloader_dict['WriteTime'], bootloader_dict['ImagePath'], bootloader_dict['DisplayName']):   
        print 'Disp: {0:<10}\nName: {1:<10}\nPath: {2:<10}\nTime: {3}\n'.format(dispname, sname, ipath.encode('ascii', 'ignore'), ltime)

