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

class GenHash(Gtk.Window):
	"""
	Main 
	"""
	def __init__(self):
		"""
		initialize
		"""
		Gtk.Window.__init__(self, title="GenHash v0.2")
		self.set_size_request(550,250)
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

		# Scrollable TextView
		scroll = Gtk.ScrolledWindow()
		scroll.set_border_width(5)
		scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
		scroll.add(self.view)

		# Liste des algorithmes supportés
		# Les autres algorithmes ne sont pas récommandés
		algo = [[1,"sha1"], [2,"md5"], [3,"sha256"], [4,"sha384"], [5,"sha512"], [6,"OpenSSL : ripemd160"], [7, "Open SSL : DSA"],
		[8, "Open SSL : MD4"],[9, 'base64'],[10,'Zlib : adler32'], [11, 'Zlib : crc32']]

		liste = Gtk.ListStore(int,str)
		for i in range(11):
			liste.append(algo[i])
		self.combo = Gtk.ComboBox.new_with_model_and_entry(liste)
		self.combo.set_entry_text_column(1)

		table.attach(info, 0, 2, 0, 1)
		table.attach(choose, 0, 1, 1, 2,Gtk.AttachOptions.SHRINK,Gtk.AttachOptions.SHRINK)
		table.attach(self.entry, 1, 2, 1, 2)
		table.attach(button, 1, 2, 3, 4,Gtk.AttachOptions.FILL,Gtk.AttachOptions.SHRINK)
		table.attach(hashage, 0,1,2, 3)
		table.attach(self.combo,1,2,2,3)
		
		notebook = Gtk.Notebook()
		notebook.append_page(table, Gtk.Label("Generate"))
		vbox.pack_start(notebook, True, True, 10)
		vbox.pack_start(scroll,True, True,0)
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

				if alg_hash == 0:
					mhash = hashlib.sha1()
				if alg_hash == 1:
					mhash = hashlib.md5()
				if alg_hash == 2:
					mhash = hashlib.sha256()
				if alg_hash == 3:
					mhash = hashlib.sha384()
				if alg_hash == 4:
					mhash = hashlib.sha512()
				if alg_hash == 5:
					mhash = hashlib.new('ripemd160')
				if alg_hash == 6:
					mhash = hashlib.new('DSA')
				if alg_hash == 7:
					mhash = hashlib.new('MD4')
				if alg_hash == 8:
					import base64
					mhash = base64.b64encode
				if alg_hash == 9:
					import zlib
					mhash = zlib.adler32
				if alg_hash == 10:
					import zlib
					mhash = zlib.crc32

				while True:
					contenu = file_open.read(block_size)
					if not contenu:
						break
					if alg_hash == 8 or alg_hash == 9 or alg_hash == 10:
						hex_dig = mhash(contenu)
					else:
						mhash.update(contenu)

				if alg_hash != 8 and alg_hash != 9 and alg_hash !=10:
					hex_dig = mhash.hexdigest()

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
		Erreur lors d'une mauvaise saisie d'un fichier
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
	win = GenHash()
	Gtk.main()

