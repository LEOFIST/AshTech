encChar = "mmZ\dxZmx]Zpgy"

for Key in range(100):

    decrptMsg = ""
    

    for c in encChar:

        if (c - Key > 126):
            EncryptedChar = ((ord (c) - Key) + 127 - 32)
            decrptMsg = Msg+chr(EncryptedChar)
        else:
            EncryptedChar = (ord(c) + Key)
            decrptMsg = Msg+chr(EncryptedChar)                  
        
                   
            

    print(key," = ",decrptMsg)     
         
