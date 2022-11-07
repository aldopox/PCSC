import base64
from cryptography.fernet import Fernet
import hashlib

def compute_camera_id(email, password):
    h = hashlib.md5(password.encode())
    fernet = Fernet(base64.urlsafe_b64encode(h.hexdigest().encode()))
    encMessage = fernet.encrypt(email.encode())
    h = hashlib.md5(encMessage)
    return h.hexdigest()

email, password = "pappo@gmail.com", "papo"
camera_id = compute_camera_id(email, password)
print(camera_id)

#decMessage = fernet.decrypt(encMessage).decode()
#print("decrypted string: ", decMessage)