from cryptography.fernet import Fernet
import os
import glob
homeDir = os.path.expanduser("~")
print(homeDir)

files = glob.glob(f'{homeDir}\\creds\\**\\*.*', recursive=True)


with open("key.key", "rb") as KeyFile:
    key = KeyFile.read()

fernet = Fernet(key)

for file in files: 
    try:
        with open(file, "rb") as tf:
            tf_bytes = tf.read()
    except:
        pass
    try:
        tf_bytes_Decrypt = fernet.decrypt(tf_bytes)
    except:
        print("Error Decrypting the Files ")
        

    with open(file, "wb") as tf:
        tf.write(tf_bytes_Decrypt)

    