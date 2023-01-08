import pyqrcode
import png

def generate_qr(url):
  # Generate QR code
  qr = pyqrcode.create(url)
 
  # Save QR code as PNG file
  qr.png('qr.png', scale=8)
 
  # Print QR code to console
  print(qr.terminal(quiet_zone=1))
 
# Prompt user for web address
url = input("Enter web address: ")
 
# Generate QR code
generate_qr(url)
