import _mysql #http://mysql-python.sourceforge.net/MySQLdb.html
import string
import sys
import datetime

now = datetime.datetime.now()
fmtime = now.strftime('%Y-%m-%d')

def keyaction(next):
	next = string.upper(next)
	if next == 'N':
		new()
	if next == 'D':
		delete()
	if next == 'A':
		activate()
	if next == 'S':
		main()
	if next == 'X':
		bye()

def new():
	print "\nPlease enter the key info\nNote: [<value>] indicates default\n"
	nk_act = raw_input("Active: [1]/0")
	if nk_act == '':
		nk_act = '1'
	nk_pub = raw_input("Public name: ")
	if nk_pub == '':
		error("Public name required")
		new()
	nk_int = raw_input("Internal Name: ")
	if nk_int == '':
		error("Internal name required")
		new()
	nk_aes = raw_input("AES key: ")
	if nk_aes == '':
		error("AES key required")
		new()
	nk_ser = raw_input("Serial: ")
	if nk_ser == '':
		error("Serial Number required")
		new()
	nk_lock = raw_input("Lock code:[000000000000]")
	if nk_lock == '':
		nk_lock = '000000000000'

	nk_hw = 1
	nk_created = fmtime

	db.query("INSERT INTO yubikeys (`created`,`active`,`creator`,`publicname`,`hardware`,`internalname`,`aeskey`,`serialnr`,`lockcode`) VALUES ('"+nk_created+"','"+nk_act+"','ykadminpy','"+nk_pub+"','1','"+nk_int+"','"+nk_aes+"','"+nk_ser+"','"+nk_lock+"');")
	main()

def delete():
	dk_ser = raw_input("Serial number of key to delete:")
	if dk_ser == '':
		error("Serial number required to delete key")
	delete()
	db.query("DELETE FROM yubikeys WHERE serialnr='"+dk_ser+"'")
	main()


def activate():
	aord = raw_input("[A]ctivate or [D]eactivate key?")
	if aord == '':
		error("Please choose activate or deactivate")
		activate()
	ak_ser = raw_input("Serial number of key: ")
	if ak_ser == '':
		error("Please enter serial number of key to modify")
		activate()
	aord = string.upper(aord)
	if aord == 'A':
		db.query("UPDATE yubikeys SET ACTIVE = 1 WHERE serialnr='"+ak_ser+"'")
		main()
	if aord == 'D':
		db.query("UPDATE yubikeys SET ACTIVE = 0 WHERE serialnr='"+ak_ser+"'")
		main()

def getkeys():
	db.query("""SELECT * FROM yubikeys""")
	r=db.store_result()
	rs = r.fetch_row(maxrows=0,how=2)
	for res in rs:
		print "Created: "+res['yubikeys.created'] \
		+"| Active: "+res['yubikeys.active'] \
		+"| Creator: "+res['yubikeys.creator'] \
		+"| Publicname: "+res['yubikeys.publicname'] \
		+"| Hardware: "+res['yubikeys.hardware'] \
		+"| InternalName: "+res['yubikeys.internalname'] \
		+"| aesKey: "+res['yubikeys.aeskey'] \
		+"| Serial: "+res['yubikeys.serialnr'] \
		+"| Lockcode: "+res['yubikeys.lockcode']

def error(msg):
	print "\n=====\nERROR\n=====\n"+msg+"\n=====\n"

def definedb():
	db_host=raw_input("DB host:")
	db_username=raw_input("DB Username:")
	db_pw = raw_input("DB Password:")
	db_database = raw_input("Database:")
	global db
	db = _mysql.connect(db_host,db_username,db_pw,db_database)

def bye():
	sys.exit(1)

def main():
	try:
		db
	except NameError:
		definedb()
	getkeys()
	next = raw_input("What would you like to do?\nNew key?[n] Delete key?[d] Deactivate/Activate key?[a] Show keys?[s] Exit?[x]")
	keyaction(next)


if __name__ == "__main__":
	main()
#end of file
