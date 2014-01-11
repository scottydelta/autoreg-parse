import re
from Registry import Registry
from collections import defaultdict
from itertools import izip

moz_ver = ["mozilla.org\\Mozilla"]
moz_plugins = ["MozillaPlugins"]
ff_extensions = ["Mozilla\\Firefox\\extensions"]


version_dict = defaultdict(list)
plugin_dict = defaultdict(list)
extension_dict = defaultdict(list)


def getPlugin(reg_soft, reg_nt='', reg_sys=''):
    for k in moz_ver:
        key = reg_soft.open(k)
        for v in key.values():
        	version_dict['MozVer'].append(v.value())
    print ("\n" + ("=" * 51) + "\nVERSION\n" + ("=" * 51))

    print 'LastWrite: %s\n' % (key.timestamp())

    for ver in version_dict['MozVer']:
    	print 'Version: {0:<10}\n'.format(ver)

    print ("\n" + ("=" * 51) + "\nINSTALLED PLUGIN(s)\n" + ("=" * 51))

    for k in moz_plugins:
        key = reg_soft.open(k)

        for keys in key.subkeys():
            for v in keys.values():
            	if "path" in v.name().lower():
            		plugin_dict['Timestamp'].append(keys.timestamp())
            		plugin_dict['Path'].append(v.value())
            	elif "description" in v.name().lower():
            		plugin_dict['Description'].append(v.value())
            	else:
            		pass

    for path, desc, time in izip(plugin_dict['Path'], plugin_dict['Description'], plugin_dict['Timestamp']):
    	print 'Description: {0:<10}\nPath: {1:<10}\nLastWrite: {2:<10}\n'.format(desc, path, str(time))


    print ("\n" + ("=" * 51) + "\nFIREFOX EXTENSION(s)\n" + ("=" * 51))

    for k in ff_extensions:
        key = reg_soft.open(k)
        print 'LastWrite: %s\n' % (key.timestamp())	
        for v in key.values():
	    	print 'Extension: {0:<10}\nPath: {1:<10}\n'.format(v.name(), v.value())