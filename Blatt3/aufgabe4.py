from hashlib import md5

a_str = "A"
found = False
num = 0
while not found:
    hash_str = a_str + str(num)
    result = md5(hash_str.encode()).hexdigest()
    nonce = result[:4]
    num = num + 1
    # print(nonce)
    if nonce == "0000":
        found = True
        print("My number: " + str(num))
        print(result)

