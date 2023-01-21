Project Maker
==============
Project Maker or `mkproj` helps to create project from a template

## install

in **Linux**/**Termux**:

clone the repo:
```bash
git clone https://github.com/mhs003/Project-Maker.git
cd Project-Maker 
```

install requirements:
```bash
sudo apt install python3
# in Termux
pkg install python
```

change installer file's permission:
```bash
chmod +x install.bash
```

install `mkproj`:
```bash
bash install.bash
```

## Import your custom templates

1. Prepare your own template first.
2. Create a `info` file and write some information about your template in it.
3. Then place your template folder in `$HOME/.local/share/mkproj/Templates` directory.

Your template should be ready to use now.

## usage

Create basic website project:
```bash
mkproj basic-web MySimpleWebsite
```

use the command in terminal to view help document:
```bash
mkproj -h
```