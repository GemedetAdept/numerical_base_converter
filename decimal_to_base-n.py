import string
import math

val_in = 273
base_out = 12
decimal_prec = 5
val_out = []

alphabet = list(string.ascii_uppercase)

if isinstance(val_in, int):
	decimal_in = val_in - int(val_in)


while val_in != 0:
	rem = val_in % base_out

	if rem - 9 > 0:
		base_alph = rem - 9
		rem = alphabet[base_alph-1]

	val_out.append(rem)

	val_in = int(math.floor(val_in / base_out))

val_out.reverse()
output = "".join(map(str, val_out))
print(output)
