import subprocess

installs = [
        "pip install bs4",
        "pip install requests",
        "pip install urllib",
        "pip install validators"
    ]
print("Wait for the installations, Its in progress..!!!")
for install in installs:
    query = install.split()
    proc = subprocess.Popen(query, stdout=subprocess.PIPE)
    output, error = proc.communicate()
    if output!=None:
        print(output.decode('utf-8'))
    elif error!=None:
        print(error.decode('utf-8'))

print("Everything is set-up in the system, Now Scrape as much as you can..!")