#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# GenHash PyGtk Gui
# 
# Copyright 2014 Chiheb Nexus
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#  
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#  
################################################################################ 
################################# À propos #####################################

from gi.repository import Gtk 

def about (self):
	"""
	À propos de GenHash
	"""
	image = Gtk.Image()
	image.set_from_file("img/icon.png")
	label = Gtk.Label()
	label.set_text("GenHash est un petit logiciel qui permet de générer des hashs\n"+
	"de vos fichier de faibles volumes comme les plus volumineux en utilisant\n"+
	"le module hashlib de python 3 et PyGI")
	link_blog = Gtk.LinkButton("http://p.pw/baemSL","Blog")
	link_github = Gtk.LinkButton("http://p.pw/baec4B","GitHub")
	label_link = Gtk.Label("Liens : ")

	hbox = Gtk.HBox()
	hbox.set_homogeneous(True)
	hbox.pack_start(label_link, False, False, 0)
	hbox.pack_start(link_blog, False, False, 0)
	hbox.pack_start(link_github, False, False, 0)

	box = Gtk.VBox()

	box.pack_start(image, True, True, 0)
	box.pack_start(label, True, True, 0)
	box.pack_start(hbox, True, True, 0)

	return box
