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
############################ Main Gui ##########################################

import hashlib
import os
import getpass

from gi.repository import Gtk, Gdk

class MyApp(Gtk.Window):
	"""
	Main 
	"""
	def __init__(self):
		"""
		initialize
		"""
		Gtk.Window.__init__(self, title="GenHash v0.1")
		self.set_size_request(550,200)
		self.connect("destroy", Gtk.main_quit)
		# Fenêtre non modifiable
		self.set_resizable(False)
		self.set_position(Gtk.WindowPosition.CENTER)
		self.set_icon_from_file("img/icon.png")

		vbox = Gtk.VBox()
		self.add(vbox)

		table = Gtk.Table(2,5)

		info = Gtk.Label("Veuillez saisir le chemin du fichier")
		choose = Gtk.Button("Choisir fichier")
		choose.connect("clicked", self.choix_destination)
		button = Gtk.Button("Calculer")
		hashage = Gtk.Label("Choisir Algorithme")
		button.connect("clicked", self.hash_calc)
		self.entry = Gtk.Entry()
		user = getpass.getuser()
		self.entry.set_text("/home/"+user)
		self.view = Gtk.TextView()
		# TextView non éditable
		self.view.set_editable(False)
		# Wrap mode : Retourner à la ligne
		self.view.set_wrap_mode(1)

		# Liste des algorithmes supportés
		# Les autres algorithmes ne sont pas récommandés
		algo = [[1,"sha1"], [2,"md5"], [4,"sha256"], [5,"sha384"], [6,"sha512"], [7,"OpenSSL : ripemd160"]]
		liste = Gtk.ListStore(int,str)

		for i in range(6):
			liste.append(algo[i])
		self.combo = Gtk.ComboBox.new_with_model_and_entry(liste)
		self.combo.set_entry_text_column(1)

		table.attach(info, 0, 2, 0, 1)
		table.attach(choose, 0, 1, 1, 2,Gtk.AttachOptions.SHRINK,Gtk.AttachOptions.SHRINK)
		table.attach(self.entry, 1, 2, 1, 2)
		table.attach(button, 1, 2, 3, 4,Gtk.AttachOptions.FILL,Gtk.AttachOptions.SHRINK)
		table.attach(hashage, 0,1,2, 3)
		table.attach(self.combo,1,2,2,3)
		
		vbox.pack_start(table, True, True, 10)
		vbox.pack_start(self.view,True, True,0)
		author = Gtk.Label("Chiheb NeXus | http://nexus-coding.blogspot.com")
		vbox.pack_end(author,True, True, 0)
		
		self.show_all()

	def hash_calc(self, widget):
		"""
		block_size : taille de block de hashage en octet
		"""
		path = self.entry.get_text()
		alg_hash = self.combo.get_active()

		try:
			with open(path,'rb') as file_open :
				block_size = 65536
				contenu = file_open.read(block_size)

				if alg_hash == 0:
					hash_object = hashlib.sha1(str(contenu).encode())
				if alg_hash == 1:
					hash_object = hashlib.md5(str(contenu).encode())
				if alg_hash == 2:
					hash_object = hashlib.sha256(str(contenu).encode())
				if alg_hash == 3:
					hash_object = hashlib.sha384(str(contenu).encode())
				if alg_hash == 4:
					hash_object = hashlib.sha512(str(contenu).encode())
				if alg_hash == 5:
					hash_object = hashlib.new('ripemd160')
					hash_object.update(str(contenu).encode())
					
				hex_dig = hash_object.hexdigest()
				txt = str(hex_dig)
			buffe = Gtk.TextBuffer()
			buffe.set_text(txt)
			self.view.set_buffer(buffe)
		except:
			self.error_msg()

	def choix_destination(self, widget):
		"""
		Choisir un fichier
		"""
		dialog = Gtk.FileChooserDialog("Choisir Fichier", self,Gtk.FileChooserAction.OPEN,(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Validate", Gtk.ResponseType.OK))
		dialog.set_default_size(800, 400)
		response = dialog.run()
		if response == Gtk.ResponseType.OK:
			self.entry.set_text(dialog.get_filename())
			dialog.destroy()
		if response == Gtk.ResponseType.CANCEL:
			dialog.destroy()

	def error_msg(self):
		"""
		Erreur d'une mauvaise saisie d'un fichier
		Ou faux type d'algorithme
		"""
		msg = ""
		if self.combo.get_active() == -1:
			msg = "choisir un algorithme"
		if self.entry.get_text() =="":
			msg = "choisir un fichier"
		if os.path.isfile(self.entry.get_text()) == False:
			msg = "indiquer un chemin d'un fichier valide"

		info = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Avant de procéder aux calculs, veuillez "+msg)
		info.run()
		info.destroy()

####### Test #######
if __name__ == '__main__':
	win = MyApp()
	Gtk.main()

