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
from doc_links import *
from compare import *
from gi.repository import Gtk, GLib, GObject

class GenHash(Gtk.Window):
	"""
	Main 
	"""
	def __init__(self):
		"""
		initialize
		"""
		Gtk.Window.__init__(self, title="GenHash v0.4")
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
		self.button = Gtk.Button()
		self.button.set_label("Calculer")
		hashage = Gtk.Label("Choisir Algorithme")
		self.button.connect("clicked", self.hash_calc,"main")
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

		# Spinner
		self.spin = Gtk.Spinner()
		# Effacer log
		log = Gtk.Button("Effacer log")
		log.connect("clicked", self.effacer_log)

		table.attach(info, 0, 2, 0, 1)
		table.attach(choose, 0, 1, 1, 2,Gtk.AttachOptions.SHRINK,Gtk.AttachOptions.SHRINK)
		table.attach(self.entry, 1, 2, 1, 2)
		table.attach(self.button, 1, 2, 3, 4,Gtk.AttachOptions.FILL,Gtk.AttachOptions.SHRINK)
		table.attach(hashage, 0,1,2, 3)
		table.attach(self.combo,1,2,2,3)
		table.attach(self.spin, 0, 1, 3, 4)
		
		notebook = Gtk.Notebook()
		notebook.append_page(table, Gtk.Label("Generate"))
		notebook.insert_page(comparer(self), Gtk.Label("Comparaison"), 2)
		notebook.insert_page(links(self), Gtk.Label("Documentations"), 3)

		vbox.pack_start(notebook, True, True, 10)
		vbox.pack_start(log, False, False,0)
		vbox.pack_start(scroll,True, True,0)
		author = Gtk.Label("Chiheb NeXus | http://nexus-coding.blogspot.com")
		vbox.pack_end(author,True, True, 0)
		
		self.show_all()

	def effacer_log(self, widget):
		""" 
		Effacer le log de TextView
		"""
		buf = Gtk.TextBuffer()
		txt = ""
		buf.set_text(txt)
		self.view.set_buffer(buf)


	def hash_calc(self, widget, data):
		"""
		block_size : taille de block de lecture du fichier en octet
		Gtk.events_pending() : Function returns True if
		       any events are pending. This can be used to update
		       the user interface and invoke timeouts etc. 
		        while doing some time intensive computation.
		Gtk.main_iteration() : Function runs a single iteration 
		        of the mainloop. If no events are waiting to be 
		        processed PyGTK will block until the next event 
		        is noticed if block is True. This function is identical
		         to the gtk.main_iteration_do() function.
		"""
		path = self.entry.get_text()
		if data == "main":
			alg_hash = self.combo.get_active()
		if data == "comparer":
			alg_hash = comparer.combo2.get_active()

		try:
			with open(path,'rb') as file_open :
				block_size = 65536 
				
				if data == "main" and path !="" and alg_hash != -1:
					self.spin.start()
					self.button.set_label("Chargement")
				if data == "comparer" and path !="" and alg_hash != -1:
					comparer.spin.start()
					comparer.compar.set_label("Loading")

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
					# Ne pas bloquer la GUI lors de l'ouverture du fichier
					# La lecture du fichier passe en démon et la GUI reste active
					while Gtk.events_pending():
						Gtk.main_iteration()
					if not contenu:
						if data == "main":
							self.spin.stop()
							self.button.set_label("Calculer")
						if data == "comparer":
							comparer.spin.stop()
							comparer.compar.set_label("Comparer")
						break
					if alg_hash == 8 or alg_hash == 9 or alg_hash == 10:
						hex_dig = mhash(contenu)
					else:
						mhash.update(contenu)
						hex_dig = mhash.hexdigest()

			if data == "main":
				txt = str(hex_dig)
				buffe = Gtk.TextBuffer()
				buffe.set_text(txt)
				self.view.set_buffer(buffe)
			if data == "comparer":
				if str(hex_dig) == comparer.entrer_hash.get_text():
					buffe = Gtk.TextBuffer()
					txt = "Égaux"
					buffe.set_text(txt)
					self.view.set_buffer(buffe)
				else:
					buffe = Gtk.TextBuffer()
					txt = "Non égaux"
					buffe.set_text(txt)
					self.view.set_buffer(buffe)

		except:
			self.error_msg(data)

	def choix_destination(self, widget):
		"""
		Choisir un fichier
		"""
		dialog = Gtk.FileChooserDialog("Choisir Fichier", self,Gtk.FileChooserAction.OPEN,(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Validate", Gtk.ResponseType.OK))
		dialog.set_default_size(800, 400)
		response = dialog.run()
		if response == Gtk.ResponseType.OK:
			self.entry.set_text(dialog.get_filename())
			comparer.entry_hash.set_text(dialog.get_filename())
			dialog.destroy()
		if response == Gtk.ResponseType.CANCEL:
			dialog.destroy()

	def error_msg(self, data):
		"""
		Erreur lors d'une mauvaise saisie d'un fichier
		Ou faux type d'algorithme
		"""
		msg = ""
		if data == "main":
			if self.combo.get_active() == -1:
				msg = "choisir un algorithme"
			if self.entry.get_text() =="":
				msg = "choisir un fichier"
			if os.path.isfile(self.entry.get_text()) == False:
				msg = "indiquer un chemin d'un fichier valide"
		if data == "comparer":
			if comparer.combo2.get_active() == -1:
				msg = "choisir un algorithme"
			if comparer.entry_hash.get_text() =="":
				msg = "choisir un fichier"
			if os.path.isfile(comparer.entry_hash.get_text()) == False:
				msg = "choisir un fichier"

		info = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Avant de procéder aux calculs, veuillez "+msg)
		info.run()
		info.destroy()

####### Test #######
if __name__ == '__main__':
	win = GenHash()
	Gtk.main()


