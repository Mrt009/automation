import webbrowser, time
url = input("Enter url : ")
duration = input("Enter the duration : ")
for i in range(500):
    webbrowser.open_new(url)
    time.sleep(int(duration))