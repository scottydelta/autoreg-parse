'''
Author: Patrick Olsen
Twitter: @patrickrolsen
Email: patrickolsen@sysforensics.org
Blog: www.sysforensics.org

The MIT License (MIT)

Copyright (c) 2013 Patrick R. Olsen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import sys
import argparse
from Registry import Registry


parser = argparse.ArgumentParser(description='Parse the Windows registry for malware-ish related artifacts.')
parser.add_argument('-nt', '--ntuser', help='Path to the NTUSER.DAT hive you want parsed')
parser.add_argument('-sys', '--system', help='Path to the SYSTEM hive you want parsed')
parser.add_argument('-soft', '--software', help='Path to the SOFTWARE hive you want parsed')
parser.add_argument('-p', '--plugin', nargs='+', help='Specify plugin your plugin name')

def main():
    args = parser.parse_args()
    reg_nt = Registry.Registry(args.ntuser) if args.ntuser else ""
    reg_soft = Registry.Registry(args.software) if args.software else ""
    reg_sys = Registry.Registry(args.system) if args.system else ""
    #if not args.plugin:
    #    print parser.usage
    #    exit(0)
    try:
        plugin_filename = 'get_' + args.plugin[0]
        sys.path.insert(0, 'plugins')
        module = __import__(plugin_filename)
        module.getPlugin(reg_nt=reg_nt, reg_soft=reg_soft, reg_sys=reg_sys)
    except Exception as e:
        print e
        print "No Plugin Found."
if __name__ == "__main__":
    main()
