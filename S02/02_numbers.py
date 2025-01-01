x = 10
print(bin(x))
print(oct(x))
print(hex(x))

# Casting
x = float(x)
print(x)

x = int(x)
print(x)

x = complex(x)
print(x)

f = 2_000_000_000_000.0
print(f)

f = 2e+12
print(f)

f = 2e+500 # inf
print(f)

c = 1 +3j
print(c.real)
print(c.imag)
print(c.conjugate())

d = 2 + 4j
print(c+d)
print(c-d)
print(c*d)
print(c/d)

c = -3.142154
print(round(c, 2))
print(abs(c))
print(pow(c, 2))