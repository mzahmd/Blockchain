from hashlib import md5

found = False
num = 0

while not found:
    hash_str = "A" + str(num)
    result = md5(hash_str.encode()).hexdigest()
    nonce = result[:4]
    # print(nonce)
    if nonce == "0000":
        found = True
        print("My number: " + str(num))
        print(result)
    num = num + 1

