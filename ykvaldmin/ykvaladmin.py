import _mysql #http://mysql-python.sourceforge.net/MySQLdb.html
import string
import sys
import datetime
import getpass

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
	nk_id = raw_input("ID: [\"\"]")

	nk_secret = raw_input("Secret: [\"\"] ")

	nk_email = raw_input("Email: [\"\"]")
	
	nk_notes = raw_input("Notes: [\"\"]")

	nk_otp = raw_input("OTP: [\"\"]")
	
	now = datetime.datetime.now()
	fmtime = now.strftime('%Y-%m-%d')
	nk_hw = 1
	nk_created = fmtime

	db.query("INSERT INTO clients (`id`,`active`,`created`,`secret`,`email`,`notes`,`otp`) VALUES ('"+nk_id+"','"+nk_act+"','"+nk_created+"','"+nk_secret+"','"+nk_email+"','"+nk_notes+"','"+nk_otp+"');")
	main()

def delete():
	dk_id = raw_input("ID of client to delete:")
	if dk_id == '':
		error("ID required to delete item from clients table")
		delete()
	db.query("DELETE FROM clients WHERE id='"+dk_id+"'")
	main()


def activate():
	aord = raw_input("[A]ctivate or [D]eactivate key?")
	if aord == '':
		error("Please choose activate or deactivate")
		activate()
	ak_id = raw_input("ID of client: ")
	if ak_ser == '':
		error("Please enter id of client to modify")
		activate()
	aord = string.upper(aord)
	if aord == 'A':
		db.query("UPDATE clients SET ACTIVE = 1 WHERE id='"+ak_id+"'")
		main()
	if aord == 'D':
		db.query("UPDATE clients SET ACTIVE = 0 WHERE id='"+ak_id+"'")
		main()

def getkeys():
	# id | active | created | secret | email | notes | otp  |
	db.query("""SELECT * FROM clients""")
	r=db.store_result()
	rs = r.fetch_row(maxrows=0,how=2)
	for res in rs:
		print "ID: "+res['clients.id'] \
		+"| Active: "+res['clients.active'] \
		+"| Created: "+res['clients.created'] \
		+"| Secret: "+res['clients.secret'] \
		+"| Email: "+res['clients.email'] \
		+"| Notes: "+res['clients.notes'] \
		+"| OTP: "+res['clients.otp']

def error(msg):
	print "\n=====\nERROR\n=====\n"+msg+"\n=====\n"

def definedb():
	db_host=raw_input("DB host:")
	db_username=raw_input("DB Username:")
	db_pw = getpass.getpass("DB Password:")
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
	next = raw_input("What would you like to do?\nNew client?[n] Delete client?[d] Deactivate/Activate client?[a] Show clients?[s] Exit?[x]")
	keyaction(next)


if __name__ == "__main__":
	main()
#end of file
