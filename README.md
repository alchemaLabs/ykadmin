ykadmin -> ksmadmin
=======

This tool is designed to make my life easier by creating an interface other than mysql interpreter 
to add keys to my yubico ksm. It is horribly coded as python is hard. 

Please do not use it. If you do use it, please
do not sql inject yourself because it is very possible to do so. 


License
---

There is no license.

Usage
---

Download the file. 

Run `python ksmadmin.py` and answer the questions.

Prerequisites
---

[Python 2.6](http://www.python.org/download/releases/2.6/)   
<> 2.6 may work; didn't test. >= 3.0 may work if you change `raw_input` to `input`

[PyMySQLdb](http://mysql-python.sourceforge.net/MySQLdb.html)

[Yubico Validation Server](https://github.com/Yubico/yubikey-val)

[Yubico KSM](https://github.com/Yubico/yubikey-ksm)

MySQL administrator credentials
