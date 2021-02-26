# removes password and saves a copy
# requires https://sourceforge.net/projects/qpdf/files/
import os
password = ''
for i in os.listdir('.'):
	if i.endswith('.pdf'):
		cmd = "qpdf --decrypt --password='" + password + "' "+i+" U"+i
		os.system(cmd)
