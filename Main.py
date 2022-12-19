import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while(1): 
  
  direction = input("Type encode to encrypt, decode to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  def caesar(new_direction,plain_text,shift_amount):
    
    def encrypt(plain_text, shift_amount):
      cipher_text = ""
      for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
      print(f"The encoded text is {cipher_text}")
  
    def decrypt(cipher_text, shift_amount):
      plain_text = ""
      for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
      print(f"The decoded text is {plain_text}")

    if direction == "encode":
      encrypt(plain_text,shift_amount )
    elif direction == "decode":
      decrypt(plain_text, shift_amount)
    
  caesar(new_direction = direction, plain_text=text,shift_amount=shift)
  res=input("Would you like to continue Y(yes) or N(no):\n")
  if res == ("Y" or "y"):
    continue
  else:
    break
     
