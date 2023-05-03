import secrets

for i in range(10):
    crypto = secrets.token_hex(256)
    print(crypto)

