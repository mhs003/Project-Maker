Project Template Manager
=========================
**Project Template Manager** is a template manager that helps to create project from a template

## install

in **Linux**/**Termux**:

clone the repo:
```bash
git clone https://github.com/mhs003/Template-Manager.git
cd Template-Manager 
```

install requirements:
```bash
sudo apt install python3
# or in Termux
pkg install python
```

change installer file's permission:
```bash
chmod +x install.bash
```

install:
```bash
bash install.bash
```

## import your own templates

1. Prepare your template first.
2. Create a `info` file under root directory of the template and write some information about your template in it.
3. Then place your template folder in `$HOME/.local/share/mkproj/Templates` directory.

Your template should be ready to use now.

## usage

Syntax:
```
mkproj [TEMPLATE_NAME] [NEW_PROJECT_NAME]
```

Create basic website project:
```bash
mkproj basic-web MySimpleWebsite
```

View help document:
```bash
mkproj -h
```
