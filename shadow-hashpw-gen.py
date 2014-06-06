#!/usr/bin/python
# Description: Hash Generator
# Written by iarly selbir <iarlyy@gmail.com>
# Thanks to Jack Neely <jjneely@ncsu.edu> [http://linuxczar.net/code/hashpw.py]
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

# This script depends on the GNU extensions to the crypt() glibc
# function call.  So, stick to Linux, alright?

from crypt import crypt
from getpass import getpass
import random
import string
import sys



def salt(prefix=""):
	chars = string.ascii_letters + string.digits + "./"
#    if prefix in ["$0$", ""]:
#        return ''.join(random.choice(chars) for x in range(2))
#    else:
	return prefix + ''.join(random.choice(chars) for x in range(8))

def main():
	p = getpass("Password: ")
	print "SHADOW HASH -> " + crypt(p, salt("$6$"))

if __name__ == "__main__":
	main()

