TEMPLATE_DIR=$HOME/.local/share/mkproj/Templates
BIN="$(dirname $(which which))"

if [ ! -d $TEMPLATE_DIR ];
then
    mkdir -p $TEMPLATE_DIR
fi

echo "Installing mkproj..."
haspy=0
for py in $BIN/python $BIN/python3
do
    if [ -x $py ];
    then
        haspy=1
        dpy=$py
    fi
done

if (( $haspy == 0 ));
then
    echo -e "\e[1;31mPython not found!"
    echo -e "Exitting installation.\e[0m"
    exit 1
else
    echo -e "#!$dpy\n" >> new_mkproj && cat mkproj.py >> new_mkproj
fi

if [ "$(uname -o)" == "Android" ];
then
    if [ -f $BIN/mkproj ];
    then
        rm $BIN/mkproj
    fi
    cp new_mkproj $BIN/mkproj
    chmod +x $BIN/mkproj
else
    if [ -f $BIN/mkproj ];
    then
        sudo rm $BIN/mkproj
    fi
    sudo cp new_mkproj $BIN/mkproj
    sudo chmod +x $BIN/mkproj
fi
rm new_mkproj
echo -e "\e[1;32mInstallation completed!\e[0m\n"

echo "Copying templates..."
cp -rf Basic-Templates/* $TEMPLATE_DIR
echo -e "\e[1;32mDone!\e[0m"

