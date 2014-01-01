'''
Todo:
[ ] Sort the numbered values so they are easier to read.
'''

from Registry import Registry

def getPlugin(reg_nt, reg_sys='', reg_soft=''):

    print ("\n" + ("=" * 51) + "\nRECENT DOCUMENTS\n" + ("=" * 51))

    try:
        recentdocs = reg_nt.open("Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RecentDocs")

        for docs in sorted(recentdocs.values()):
        	if docs.name().lower() == "viewstream" or docs.name().lower() == "mrulistex":
        		pass
        	else:
        		print '{0:<10} {1:<5} {2:>20}'.format(recentdocs.name(), docs.name(), docs.value())
       		
        for sk in sorted(recentdocs.subkeys()):
        	for v in sorted(sk.values()):
        		if "mrulistex" in v.name().lower():
        			pass
        		else:
        			print '{0:<10} {1:<5} {2:>20}'.format(sk.name(), v.name(), v.value())

    except Registry.RegistryKeyNotFoundException as e:
        pass