from inputs import devices
from inputs import get_gamepad
import simpleaudio as sa

# for device in devices.gamepads:
#     print(device)

BUTTON_LIST = [
        "BTN_EAST",
        "BTN_C",
        "BTN_TR",
        "BTN_TR",
        "BTN_TL",
        "BTN_SOUTH",
        "BTN_NORTH",
        "BTN_Z",
        "BTN_WEST",
        "ABS_HAT0Y",
        ]
BUTTON_DICT = {
        "BTN_EAST": "C4",
        "BTN_C": "D4",
        "BTN_TR": "E4",
        "BTN_TL": "F4",
        "BTN_SOUTH": "G4",
        "BTN_NORTH": "A4",
        "BTN_Z": "B4",
        "BTN_WEST": "C5",
        }
TONE_DICT = {
        "C3": sa.WaveObject.from_wave_file("./TONES/C3.wav"),
        "D3": sa.WaveObject.from_wave_file("./TONES/D3.wav"),
        "E3": sa.WaveObject.from_wave_file("./TONES/E3.wav"),
        "F3": sa.WaveObject.from_wave_file("./TONES/F3.wav"),
        "G3": sa.WaveObject.from_wave_file("./TONES/G3.wav"),
        "A3": sa.WaveObject.from_wave_file("./TONES/A3.wav"),
        "B3": sa.WaveObject.from_wave_file("./TONES/B3.wav"),
        "C4": sa.WaveObject.from_wave_file("./TONES/C4.wav"),
        "D4": sa.WaveObject.from_wave_file("./TONES/D4.wav"),
        "E4": sa.WaveObject.from_wave_file("./TONES/E4.wav"),
        "F4": sa.WaveObject.from_wave_file("./TONES/F4.wav"),
        "G4": sa.WaveObject.from_wave_file("./TONES/G4.wav"),
        "A4": sa.WaveObject.from_wave_file("./TONES/A4.wav"),
        "B4": sa.WaveObject.from_wave_file("./TONES/B4.wav"),
        "C5": sa.WaveObject.from_wave_file("./TONES/C5.wav"),
        "D5": sa.WaveObject.from_wave_file("./TONES/D5.wav"),
        "E5": sa.WaveObject.from_wave_file("./TONES/E5.wav"),
        "F5": sa.WaveObject.from_wave_file("./TONES/F5.wav"),
        "G5": sa.WaveObject.from_wave_file("./TONES/G5.wav"),
        "A5": sa.WaveObject.from_wave_file("./TONES/A5.wav"),
        "B5": sa.WaveObject.from_wave_file("./TONES/B5.wav"),
        "C6": sa.WaveObject.from_wave_file("./TONES/C6.wav"),
        }

def list_prompt(inlist):
    while True:
        for item in inlist:
            print(f"{item} - {inlist[item]}")
        selection = input("Select your device: ")
        if selection in inlist:
            return inlist[selection]


def select_gamepad():
    gamepad_num = len(devices.gamepads)
    if gamepad_num > 1:
        gamepad_options = {}
        for index, gamepad in enumerate(devices.gamepads):
            gamepad_options[str(index + 1)] = gamepad
        return list_prompt(gamepad_options)
    elif gamepad_num == 1:
        return devices.gamepads[0]


def octave_up(note):
    note_name = note[0]
    note_octave = int(note[1]) + 1
    return f"{note_name}{note_octave}"

def octave_down(note):
    note_name = note[0]
    note_octave = int(note[1]) - 1
    return f"{note_name}{note_octave}"

def play_tones(gamepad):
    upper_state = False
    lower_state = False
    while True:
        events = gamepad.read()
        for event in events:
            if event.code in BUTTON_LIST:
                # print(event.ev_type, event.code, event.state)
                # print(event.code, event.state)
                if event.code == "ABS_HAT0Y":
                    if event.state == -1:
                        upper_state = True
                    if event.state == 0:
                        upper_state = False
                        lower_state = False
                    if event.state == 1:
                        lower_state = True
                elif event.state == 1: 
                    if upper_state:
                        TONE_DICT[octave_up(BUTTON_DICT[event.code])].play()
                    elif lower_state:
                        TONE_DICT[octave_down(BUTTON_DICT[event.code])].play()
                    else:
                        TONE_DICT[BUTTON_DICT[event.code]].play()

if __name__ == "__main__":
    gamepad = select_gamepad()
    play_tones(gamepad)
