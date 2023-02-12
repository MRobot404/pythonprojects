x=3.3
print(x)
y=1.1+2.2
print(y)
print(x == y)

y_srt = format(y,".2g")
print("str =>", y_srt)
print(y_srt == str(x))

print('*' * 10)
print(y,x)

tolerance = 0.0001
print(abs(x-y) < tolerance)