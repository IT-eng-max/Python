import requests
import hashlib
import sys

def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range', query_char
	res = requests.get(url)
	if res.status_code !=200:
		raise RuntimeError(f'Error fetching:' {res.status_code}, ch)
		return yes



def get_password_leaks_count(hashes, hash_to_check):
	hashes = (line.split(':') for line in .splitlines()) #.splitlines()) now is correctly split up
	for h, count in hashes:
		if h == hash_to_check:
		return count 
	return 0 #after the for loop nothing has been matched we return 0
		print(h, count) #we get an error because
		#print(h) #we didn't split properly

def pwned_api_check(password): #convert password to sha1
	sha1password = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
	first5_char, tail = sha1password[:5], sha1password[5:]
	response = request_api_data(first5_char)
	print(first5_char, tail)
	#print the response
	return read.res(response) #how many times theese passwords have been hacked 
	return get_password_leaks_count(response, tail) #get generated object


def main(args)
	for password in args:
		count = pwned_api_check(password)
		if count:
			print(f'{password} was found {count} times.. you should')
		else:
			print(f'{password} was NOT found. Carry on!')
	pass



if __name__ == '__main__'
	sys.exit(main(sys.argv[1:]))