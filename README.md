screen-layout-switcher
======================

Reads the contents of `~/.screenlayout` and puts them in a menu.  By default
`arandr` saves the scripts there.  In theory you can put any script in ~/.screenlayout 
and as long as it's +x it'll run. (doesn't do .desktop files.)



## Sample `~/.config/autostart/screenlayout-switcher.desktop`

```
[Desktop Entry]
Encoding=UTF-8
Version=0.9.4
Type=Application
Name=screenlayout-switcher
Comment=
Exec=/home/erm/git/screen-layout-switcher/screenlayout-switcher.py
OnlyShowIn=XFCE;
StartupNotify=false
Terminal=false
Hidden=false

```



