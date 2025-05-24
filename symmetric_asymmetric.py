from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import base64

app = FastAPI()

# The setup for symmetric key
sym_key = Fernet.generate_key()
fern = Fernet(sym_key)

# Setup for asymmetric key
pv_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
pub_key = pv_key.public_key()

class Theplaintext(BaseModel):
  paragraph: str

class Encryptionprocess(BaseModel):
  encrypted: str


# symmetric function
@app.post("/symmetric/encryption")
def symmetric_encryption(input: Theplaintext):
  encrypted = fern.encrypt(input.paragraph.encode())
  return {"Encrypted process": encrypted.decode()}

@app.post("/symmetric/decryption")
def symmetric_decryption(input: Encryptionprocess):
  try:
    decrypted = fern.decrypt(input.encrypted.encode())
    return {"Decrypted process": decrypted.decode()}
  except Exception:
    raise HTTPException(status_code=400, detail="The encrypted text is invalid")

# asymmetric function
@app.post("/asymmetric/encryption")
def asymmetric_encryption(input: Theplaintext):
  encrypted = pub_key.encrypt(
      input.paragraph.encode(),
      padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                   algorithm = hashes. SHA256(),
                   label = None)
  )
  coded = base64.b64encode(encrypted).decode()
  return {"Asymmetric encryption process": coded}

@app.post("/asymmetric/decryption")
def asymmetric_decryption(input: Encryptionprocess):
  try:
    encryptedb = base64.b64decode(input.encrypted.encode())
    decrypted = pv_key.decrypt(
        encryptedb,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(),
                     label=None)
    )
    return {"Asymmetric decryption process": decrypted.decode()}
  except Exception:
    raise HTTPException(status_code=400, detail="The decrypted text is invalid")
