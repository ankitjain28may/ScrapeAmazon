import subprocess

installs = [
        "pip3 install bs4",
        "pip3 install requests",
        "pip3 install urllib",
        "pip3 install validators"
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