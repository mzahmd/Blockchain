from hashlib import sha256

a_str = "Die Blockchain ist die Loesung all unserer Probleme"
b_str = "Die Blockchain ist die Loesung all unserer Probleme!"


hashStr = sha256(a_str.encode()).hexdigest()
print(hashStr)

hashStr = sha256(b_str.encode()).hexdigest()
print(hashStr)
