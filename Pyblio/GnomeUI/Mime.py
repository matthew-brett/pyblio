# This file is part of pybliographer
# 
# Copyright (C) 1998-2003 Frederic GOBRY
# Email : gobry@idiap.ch
# 	   
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2 
# of the License, or (at your option) any later version.
#   
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details. 
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
# 
# $Id: Mime.py,v 1.1.2.6 2003/10/10 13:15:37 fredgo Exp $


""" Symbol Definitions for Drag and Drop, Copy / Paste """

# Manipulate data as strings
STRING = 0
# Manipulate pickled keys
KEY    = 1
# Manipulate pickled entries
ENTRY  = 2

# Related string definitions
SYM_STRING = 'STRING'
SYM_KEY    = 'application/x-pyblio-key'
SYM_ENTRY  = 'application/x-pyblio-entry'
SYM_APP    = 'application/x-pybliographic'
