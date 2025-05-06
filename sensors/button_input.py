import grovepi

# Button connected to port D5
button_port = 5
grovepi.pinMode(button_port, "INPUT")

def read_button_state():
    try:
        button_state = grovepi.digitalRead(button_port)
        return "pressed" if button_state == 1 else "released"
    except IOError as e:
        print(f"❌ Error reading button state: {e}")
        return "error"
