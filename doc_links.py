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

from gi.repository import Gtk 

def links(self):
	"""
	Documentations + liens externes
	Ouvrir lien dans votre navigateur par défaut 
	"""
	sha1 = Gtk.LinkButton("http://en.wikipedia.org/wiki/SHA-1", "SHA1")
	sha256 = Gtk.LinkButton("http://en.wikipedia.org/wiki/SHA-2", "SHA256")
	sha384 = Gtk.LinkButton("http://en.wikipedia.org/wiki/SHA-2", "SHA384")
	sha512 = Gtk.LinkButton("http://en.wikipedia.org/wiki/SHA-", "SHA512")
	md5 = Gtk.LinkButton("http://en.wikipedia.org/wiki/MD5", "MD5")
	ripmed = Gtk.LinkButton("http://en.wikipedia.org/wiki/RIPEMD", "RIPED")
	dsa = Gtk.LinkButton("http://en.wikipedia.org/wiki/DSA", "DSA")
	md4 = Gtk.LinkButton("http://en.wikipedia.org/wiki/MD4", "MD4")
	base64 = Gtk.LinkButton("http://en.wikipedia.org/wiki/Base64", "BASE64")
	adler = Gtk.LinkButton("http://en.wikipedia.org/wiki/Adler-32", "ADLER-32")
	crc = Gtk.LinkButton("http://en.wikipedia.org/wiki/Cyclic_redundancy_check", "CRC32")
	crypto = Gtk.LinkButton("http://en.wikipedia.org/wiki/Cryptography", "Cryptography")

	table = Gtk.Table(3,4, False)
	table.attach(sha1,0,1,0,1)
	table.attach(sha256,1,2,0,1)
	table.attach(sha512,2,3,0,1)
	table.attach(sha384,0,1,1,2)
	table.attach(md5,1,2,1,2)
	table.attach(md4,2,3,1,2)
	table.attach(ripmed,0,1,2,3)
	table.attach(dsa,1,2,2,3)
	table.attach(base64,2,3,2,3)
	table.attach(adler,0,1,3,4)
	table.attach(crc,1,2,3,4)
	table.attach(crypto,2,3,3,4)

	return table
