from Registry import Registry
from get_controlset import getControlSet
from collections import defaultdict
from itertools import izip

def getPlugin(reg_sys, reg_nt='', reg_soft=''):
    current = getControlSet(reg_sys)
    servicesnames = reg_sys.open('%s\\Services' % (current))

    service_list = []
    autostart_list = []
    autostart_dict = defaultdict(list)
    loadondemand_dict = defaultdict(list)
    
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
                            image_path = k.value("ImagePath").value()
                        except:
                            image_path = "No Image Path Found!"
                        autostart_dict['ServiceName'].append(k.name().lower())
                        autostart_dict['ImagePath'].append(image_path.lower())
                    # 0x3 (Load on demand) = SCM - Not start until the user starts it.
                    elif service_start_code == "3": 
                        autostart_list.append(k.name())
                        try:
                            image_path = k.value("ImagePath").value()
                        except:
                            image_path = "No Image Path Found!"
                        
                        loadondemand_dict['ServiceName'].append(k.name().lower())
                        loadondemand_dict['ImagePath'].append(image_path.lower())
                        pass
                    
            else:
                pass

    print ("\n" + ("=" * 51) + "\nUNKNOWN/NON-BASELINED TYPE 2 SERVICES)\n" + ("=" * 51))
    
    for sname, ipath  in izip(autostart_dict['ServiceName'], autostart_dict['ImagePath']):
        for name in service_baseline:
            if sname.lower() in name.lower():
                pass
            else:
                print 'Service Name: %s\nImage Path: %s\n' % (sname, ipath.encode('ascii', 'ignore'))
      
    print ("\n" + ("=" * 51) + "\nTYPE 2 SERVICES NOT IN SYSTEM32\n" + ("=" * 51))
    
    for sname, ipath  in izip(autostart_dict['ServiceName'], autostart_dict['ImagePath']):
        if "system32" not in ipath.lower():
            print "Service Name: %s\nImage Path: %s\n" % (sname, ipath.encode('ascii', 'ignore'))
        else:
            pass