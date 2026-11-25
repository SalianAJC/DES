#Implementation of a DES encryptor

plaintxt= "La caca fresca es rica"
key= ("601e172827684484")

hexed= plaintxt.encode("utf-8").hex()

print ((hexed))

def hex2bin(s):
	mp = {'0': "0000",
		'1': "0001",
		'2': "0010",
		'3': "0011",
		'4': "0100",
		'5': "0101",
		'6': "0110",
		'7': "0111",
		'8': "1000",
		'9': "1001",
		'A': "1010",
		'B': "1011",
		'C': "1100",
		'D': "1101",
		'E': "1110",
		'F': "1111"}
	bin = ""
	for i in range(len(s)):
		bin = bin + mp[s[i]]
	return bin


def bin2hex(s):
	mp = {"0000": '0',
		"0001": '1',
		"0010": '2',
		"0011": '3',
		"0100": '4',
		"0101": '5',
		"0110": '6',
		"0111": '7',
		"1000": '8',
		"1001": '9',
		"1010": 'A',
		"1011": 'B',
		"1100": 'C',
		"1101": 'D',
		"1110": 'E',
		"1111": 'F'}
	hex = ""
	for i in range(0, len(s), 4):
		ch = ""
		ch = ch + s[i]
		ch = ch + s[i + 1]
		ch = ch + s[i + 2]
		ch = ch + s[i + 3]
		hex = hex + mp[ch]

	return hex


def bin2dec(binary):

	binary1 = binary
	decimal, i, n = 0, 0, 0
	while(binary != 0):
		dec = binary % 10
		decimal = decimal + dec * pow(2, i)
		binary = binary//10
		i += 1
	return decimal

def dec2bin(num):
	res = bin(num).replace("0b", "")
	if(len(res) % 4 != 0):
		div = len(res) / 4
		div = int(div)
		counter = (4 * (div + 1)) - len(res)
		for i in range(0, counter):
			res = '0' + res
	return res

#permutation

def permute (k, arr, n):
    perm=""
    for i in range(0,n):
        perm=perm+k[arr[i]-1]
    return perm

def permuted_choice_2(k,contr):
    
    def contract(k):
        n = len (k)
        
        target = n-1
        res=k.copy()
        
        posit= res.index(target)
        res[posit]=res[target]
        return res[:-1]
    
    def iterated(k, contr): #Apply (contr) sequential contractions to the permutation
        
        res = k.copy()
        
        for z in range (contr):
            res = contract(res)
            
        return res  
    
    return(iterated(k,contr))
    
    

#Left shift by n shifts

def leftie(k,finalshift):
    
    storage="" #Empty string for storage
    for i in range(finalshift): #shifting by amount of given shifts
        for j in range (1,len(k)):#for every letter in string k
            storage = storage+k[j] #Add the current letter to what storage already has
        storage=storage + k[0] #Inverse initial perm
        k=storage #set the current string to the one we made
        storage = "" #Reset storage
        
    return k #Return current 


        
            
            
