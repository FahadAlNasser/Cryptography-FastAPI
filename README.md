As you may have seen in my previous projects, I have been practicing with a few packages. You may have also noticed that I have been practicing with FastAPI. From my understanding, FastAPI is created to assist developers build web APIs (Application Programming Interfaces) sufficiently and simplified. 

In this practice, the code works to encrypt and decrypt data using both symmetric and asymmetric encryption with key generated automatically to simplify the implementation. For better security, it is essential to use API keys or authentication techniques in python to prevent unauthorized access. 

### Output Example: 

POST
/symmetric/encryption
Symmetric Encryption

Request body

{
  "paragraph": "test1"
}

{
  "Encrypted process": "gAAAAABoMbc434hcrwSBQLTDRORqYY3GqffEWeGdQep_v-L_I8-SHj_06maIVsoPn8wxVmwMYJmMGZMV9yfjeH3vpVYQl_vd9A=="
}


POST
/symmetric/decryption
Symmetric Decryption

Request body

{
  "encrypted": "gAAAAABoMbc434hcrwSBQLTDRORqYY3GqffEWeGdQep_v-L_I8-SHj_06maIVsoPn8wxVmwMYJmMGZMV9yfjeH3vpVYQl_vd9A=="
}

{
  "Decrypted process": "test1"
}


POST
/asymmetric/encryption
Asymmetric Encryption

Request body

{
  "paragraph": "pfhtest`883"
}

POST
/asymmetric/decryption
Asymmetric Decryption

Request body

{
  "encrypted": "H1rP5cumWah/RSquwl6Y9Uq+TOJA5fbc7AkofShgF6siyJ0njh1tjwQmHU8QA8qvWRf12f+7C6iyS2Xx+yVPen4eiQI+iAsafZa9E80P9PyNKbjrLetD1Md/oDicF/GLr+y7KMZcGg0ChIh4kYyt3msMT7tzvZiT7QZs07wjx80Uzn27lZZeiNOmWkxaoRkCizCweHT4sWH6eScZ3oXtssFcK1VsQGfeXIaVlsdLbAHKHaSV/i+3YsQL4ME4aQZykazaCjPoFzAksbwUBlRNM1IR/A9tB7Ws08MdyRzSGo4DeWcpCaF45gwFmiz2XPgucNEHON4BPcnsauIObBqxxg=="
}

{
  "Asymmetric decryption process": "pfhtest`883"
}

### Disclaimer

I am learning, experimenting, and practicing with coding. I am exploring different tools, techniques, and programming languages to enhance my skills. This is code is experimental and intended for educational purposes only.
