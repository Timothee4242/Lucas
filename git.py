import subprocess, pyautogui as pa, time, keyboard as kb

path = r"D:\Enfants\Timothee\codes\Lucas" #Project-TAV"

subprocess.run(f'start cmd /K "cd /d {path}"', shell=True)
time.sleep(1)
pa.write("git fetch -a\ngit status\n")
while True:
    #action = pa.confirm('Enter option.', buttons=['See modifications', 'Commit', 'Merge', "Stop"])
    if kb.is_pressed("ctrl+alt+d"): #action == 'See modifications':
        while kb.is_pressed("ctrl") or kb.is_pressed("alt"): pass
        b = pa.prompt('Wich branch?')
        if b in (""," "): b = "Tests"
        pa.write(f"git diff {b} origin/{b}", 0.005)
        pa.press("enter")
    elif kb.is_pressed("ctrl+alt+c"): #action == "Commit":
        while kb.is_pressed("ctrl") or kb.is_pressed("alt"): pass
        pa.write("git add .\ngit commit -m")
        while not kb.is_pressed("enter"):pass
        pa.write("git push\n", 0.005)
    elif kb.is_pressed("alt+f4") or kb.is_pressed("ctrl+alt+suppr") or kb.is_pressed("ctrl+alt+shift+s+q"): break #action == "Stop": break
    elif kb.is_pressed("ctrl+alt+p"):
        while kb.is_pressed("ctrl") or kb.is_pressed("alt"): pass
        pa.write("git pull", 0.01)
        pa.press("enter")
    elif kb.is_pressed("ctrl+alt+m"):
        while kb.is_pressed("ctrl") or kb.is_pressed("alt"): pass
        b = pa.prompt('Wich branch?')
        if b in (""," "): b = "Tests"
        pa.write("git pull\ngit checkout -b temp\ngit add .\ngit commit -m", 0.001)
        while not kb.is_pressed("enter"):pass
        pa.write(f"git checkout {b}\ngit merge temp\ngit pull\ni", 0.001)
        while not kb.is_pressed("esc"):pass
        pa.write(":wq\ngit push\ngit branch -d temp\n")


   # print(kb._pressed_events.keys())
    #pa.prompt('What is your name?')

