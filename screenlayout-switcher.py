#!/usr/bin/env python2
# screen-layout-switcher.py - load ~/.screenlayout
#    Copyright (C) 2014 Eugene Miller <theerm@gmail.com>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

import gtk
import os
import sys
from subprocess import Popen, PIPE

def on_activate(item, script_path, **kwargs):
    print "on_activate:", script_path
    Popen([script_path])
    # Popen([sys.path[0]+"/lib/listeners_list.py"])


def quit(*args, **kwargs):
    gtk.main_quit()


def on_button_press(icon, event, **kwargs):
    print "on_button_press"
    popup_menu = gtk.Menu()
    for root, dirs, files in os.walk(os.path.expanduser("~/.screenlayout")):
        for f in files:
            filename = os.path.join(root, f)
            if not os.access(filename, os.X_OK):
                continue
            item = gtk.ImageMenuItem(gtk.STOCK_FULLSCREEN)
            item.set_label("%s" % f)
            item.connect("activate", on_activate, os.path.join(root, f))
            popup_menu.append(item)

    item = gtk.ImageMenuItem(gtk.STOCK_QUIT)
    item.connect("activate", quit )
    popup_menu.append(item)
    popup_menu.show_all()
    popup_menu.popup(None, None, None, event.button, event.get_time())

image_path = ""
if os.path.exists(sys.path[0]+"/images/angry-square.jpg"):
    image_path = sys.path[0]+"/images/"

tray_icon = gtk.StatusIcon()
tray_icon.set_name("screenlayout-switcher")
tray_icon.set_title("screenlayout-switcher")
tray_icon.connect("button-press-event", on_button_press)
# gtk.STOCK_FULLSCREEN
# rating_icon.set_from_file(+"rate.6.svg.png")
# tray_icon.connect("scroll-event", on_tray_scroll)
tray_icon.set_from_stock(gtk.STOCK_FULLSCREEN)

if __name__ == "__main__":
    gtk.main()
