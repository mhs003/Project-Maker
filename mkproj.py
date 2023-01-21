import sys
import os
import shutil
import subprocess as sp


version = 'v1.0'
buildOpts = ['-h', '-v', '-l', '-i', '--help', '--version']

# Functions


def parseOpt(opt):
    if not opt.startswith('--') and opt.startswith('-') and len(opt) > 2:
        return ['-'+x for x in opt[1:]]
    else:
        return opt


def printHelp():
    print(f"""
Usage: mkproj [options] | [template name] [project name]

  Create a project from a template.

Options:
  -l                 List available project templates
  -i template_name   Information about a template
  -v, --version      Print program version
  -h, --help         Print this help page

Default Templates:
  basic-web     Basic html, css, js website
  php-web       Basic dynamic website using php
  react-app     A native react website
  
How to create my own template?
  Place your template folder in \033[1;32m{sp.getoutput('echo $HOME')}/.local/share/mkproj/Templates\033[0m directory. Create a \033[1;93minfo\033[0m file in your template's root directory and write some information about your template in the file. And you are all done! The template should be ready to use.
  
Version: {version}
  """.strip())
    exit()

# Main Program


argvs = sys.argv
HOME_DIR = sp.getoutput('echo $HOME')
WORKING_DIR = sp.getoutput('pwd') + '/'
TEMPLATES_DIR = HOME_DIR + '/.local/share/mkproj/Templates/'

opts = [opt for opt in argvs[1:] if opt.startswith("-")]
args = [arg for arg in argvs[1:] if not arg.startswith("-")]

# controller

if '-h' in opts or '--help' in opts:
    printHelp()
elif '-v' in opts or '--version' in opts:
    print(version)
    exit()
elif '-i' in opts:
    if len(argvs) > argvs.index('-i') + 1 and argvs[argvs.index('-i') + 1] in args:
        if os.path.isdir(TEMPLATES_DIR + argvs[argvs.index('-i') + 1]):
            if os.path.isfile(TEMPLATES_DIR + argvs[argvs.index('-i') + 1] + '/info'):
                fop = open(TEMPLATES_DIR + argvs[argvs.index('-i') + 1] + '/info', 'r')
                print(fop.read(), end="")
                fop.close()
                exit()
            else:
                print('No information available for ' + argvs[argvs.index('-i') + 1])
                exit()
        else:
            print('Template not found!')
            exit()
    else:
        print('Broken command! see --help')
        exit()
elif '-l' in opts:
    if os.path.isdir(TEMPLATES_DIR):
        ls = os.listdir(TEMPLATES_DIR)
        for l in ls:
            if os.path.isdir(TEMPLATES_DIR + '/' + l):
                print(f"\033[1;34m{l}\033[0m", end="" if l == ls[len(ls) - 1] else "    ")
        else:
            print()
        exit()
                    
    else:
        print('No templates are available. See --help')
        exit()
elif len(opts) > 0:
    print(f'Unknown option {opts[0]}')
    printHelp()

    
if len(args) > 1:
    if os.path.isdir(TEMPLATES_DIR):
        if os.path.isdir(TEMPLATES_DIR + args[0]):
            print('Making the project...')
            shutil.copytree(TEMPLATES_DIR + args[0], WORKING_DIR + args[1])
            if os.path.isfile(WORKING_DIR + args[1] + '/info'):
                os.unlink(WORKING_DIR + args[1] + '/info')
            print(f'\033[1;32mProject {args[1]} was made successfully!\033[0m')
        else:
            print(f'Template \'{args[0]}\' not available. see --help')
    else:
        print('No templates are available. See --help')
else:
    print(f"Requires two arguments! Only {len(args)} argument{'s are' if len(args) == 0 else ' has been'} passed")
    printHelp()
