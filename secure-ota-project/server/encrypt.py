from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

KEY = b"1234567890ABCDEF"   # MUST MATCH ESP

with open("firmware.bin", "rb") as f:
    firmware = f.read()

iv = get_random_bytes(16)

cipher = AES.new(KEY, AES.MODE_CBC, iv)

pad_len = 16 - (len(firmware) % 16)
firmware += bytes([pad_len]) * pad_len

encrypted = iv + cipher.encrypt(firmware)

with open("encrypted.bin", "wb") as f:
    f.write(encrypted)

sha = SHA256.new(firmware)
with open("checksum.txt", "w") as f:
    f.write(sha.hexdigest())

print("Encryption Done ✔")
