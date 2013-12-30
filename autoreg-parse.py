'''
Author: Patrick Olsen
Email: patrickolsen@sysforensics.org
Twitter: @patrickrolsen
'''
import sys
import argparse
from Registry import Registry


parser = argparse.ArgumentParser(description='Parse the Windows registry for malware-ish related artifacts.')
parser.add_argument('-nt', '--ntuser', help='Path to the NTUSER.DAT hive you want parsed')
parser.add_argument('-sys', '--system', help='Path to the SYSTEM hive you want parsed')
parser.add_argument('-soft', '--software', help='Path to the SOFTWARE hive you want parsed')
parser.add_argument('-p', '--plugin', nargs='+', help='Specify plugin your plugin name')

args = parser.parse_args()

if args.ntuser:
    reg_nt = Registry.Registry(args.ntuser)
else:
    reg_nt = ''
    pass
if args.software:
    reg_soft = Registry.Registry(args.software)
else:
    reg_soft = ''
    pass
if args.system:
    reg_sys = Registry.Registry(args.system)
else:
    reg_sys = ''
    pass

if not args.plugin:
    print parser.usage
    exit(0)

def main():
    for plugin_name in args.plugin:
        plugin_filename = 'get_' + plugin_name
    try:
        sys.path.insert(0, 'plugins')
        module = __import__(plugin_filename)
        module.getPlugin(reg_nt=reg_nt, reg_soft=reg_soft, reg_sys=reg_sys)
    except:
        print "No Plugin Found."
if __name__ == "__main__":
    main()