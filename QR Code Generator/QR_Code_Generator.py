import os
def is_package_installed(pkg_name):
    return os.system(f"dpkg -l {pkg_name} > /dev/null 2>&1") == 0
def main():
    print("\nWelcome to QR Code app. Please select a option below....")
    while True:
        print("1. Read QR Code\n2. Create QR Code\n3. Exit App")
        n=input("Enter your choice...").strip() or "a"
        if n=='1':
            read_qr()
            break   
        elif n=='2':
            write_qr()
            break
        elif n=='3':
            break
        else:
            print("\nChoose a valid option...")
        # Get image file path from user input
def read_qr():
    try:
        from pyzbar.pyzbar import decode
    except ImportError:
        print("Scaning QR code required pyzbar python library which is not install. Install it by 'pip install pyzbar' and try again")
        return
    try:
        from PIL import Image
    except ImportError:
        print("Scaning QR code required Pillow python library which is not install. Install it by 'pip install pillow' and try again")
        return

    while True:
        try:
            print("\nEnter a correct QR code image path below. Type 'X' for exit.")
            image_path = input("Image path: ").strip() or "result.png"
            if image_path == "X":
                return
            # Open the image using Pillow
            image = Image.open(image_path)
            break
        except FileNotFoundError:
            print("No such file or directory.")

    # Decode the QR code
    decoded_objects = decode(image)

    # Check if any QR codes were found
    if decoded_objects:
        for obj in decoded_objects:
            print("QR Code Data:\n", obj.data.decode("utf-8"))
    else:
        print("No QR code found in the image.")
        
def write_qr():
    try:
        import segno
    except ImportError:
        print("\nCreating QR code required segno python library which is not installed. Please install it by 'pip install segno' and try again.")
        return

    data = input("Enter the data for the QR code: ")
    
    # Get user input for the file name
    file_name = input("Enter the file name (without extension): ") or "result"
    
    # Get user input for the size (scale)
    while True:
        try:
            scale = int(input("Enter the scale (recommended 1-20, default 10): ") or 10)
            if scale > 0:
                break
            else:
                print("Scale must be a positive integer.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    # Get user input for colors
    fg_color = input("Enter the foreground color (default 'black'): ") or "black"
    bg_color = input("Enter the background color (default 'white'): ") or "white"
    
    # Create the QR code
    qr = segno.make(data, micro=False)
    
    # Save the QR code with user-defined properties
    qr.save(f"{file_name}.png", scale=scale, dark=fg_color, light=bg_color)
    
    print(f"QR Code saved as {file_name}.png")
    if is_package_installed("termimage"):
        print("\nQR Code Preview:")
        os.system("termimage "+file_name+".png")
main()