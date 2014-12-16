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
############################### Docs + Links ###################################

import getpass
from gi.repository import Gtk 

def comparer(self):
	"""
	Comparer deux hash et retourner égaux ou différents comme valeur de retour
	"""

	choisir = Gtk.Button("Choisir fichier")
	choisir.connect("clicked", self.choix_destination)
	comparer.entry_hash = Gtk.Entry ()
	user = getpass.getuser()
	comparer.entry_hash.set_text("/home/"+user)
	label_hash = Gtk.Label("Choisir Algorithme")
	comparer.compar = Gtk.Button("Comparer")
	comparer.compar.connect("clicked", self.hash_calc,"comparer")
	comparer.spin = Gtk.Spinner()

	algo = [[1,"sha1"], [2,"md5"], [3,"sha256"], [4,"sha384"], [5,"sha512"], [6,"OpenSSL : ripemd160"], [7, "Open SSL : DSA"],
		[8, "Open SSL : MD4"],[9, 'base64'],[10,'Zlib : adler32'], [11, 'Zlib : crc32']]

	liste = Gtk.ListStore(int,str)
	for i in range(11):
		liste.append(algo[i])
	comparer.combo2 = Gtk.ComboBox.new_with_model_and_entry(liste)
	comparer.combo2.set_entry_text_column(1)

	comparer.entrer_hash = Gtk.Entry()
	label_entry_hash = Gtk.Label("Entrer votre Hash")



	table = Gtk.Table(4,5, False)

	table.attach(choisir, 0,1,0,1,Gtk.AttachOptions.SHRINK,Gtk.AttachOptions.SHRINK)
	table.attach(comparer.entry_hash, 1,2,0,1)
	table.attach(label_entry_hash,0,1,1,2)
	table.attach(comparer.entrer_hash,1,2,1,2)
	table.attach(label_hash, 0,1,2,3)
	table.attach(comparer.combo2, 1,2,2,3)
	table.attach(comparer.spin,0,1,3,4)
	table.attach(comparer.compar,1,2,3,4,Gtk.AttachOptions.FILL,Gtk.AttachOptions.SHRINK)

	return table

