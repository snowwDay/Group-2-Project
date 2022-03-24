import random

class utils:
    
	def gen_token(length):
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join((random.choice(letters_and_digits) for i in range(length)))