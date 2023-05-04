import secrets

for i in range(10):
    crypto = secrets.token_hex(32)
    # crypto = hex(secrets.randbits(256))
    print(crypto)

