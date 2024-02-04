import os
import marshal
import base64
import time
import calendar
import sys

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
PURPLE = '\033[95m'
RESET = '\033[0m'

logo = f"""
{YELLOW}███╗░░░███╗░█████╗░██████╗░░██████╗██╗░░██╗░█████╗░██╗░░░░░
{RED}████╗░████║██╔══██╗██╔══██╗██╔════╝██║░░██║██╔══██╗██║░░░░░
{MAGENTA}██╔████╔██║███████║██████╔╝╚█████╗░███████║███████║██║░░░░░
{YELLOW}██║╚██╔╝██║██╔══██║██╔══██╗░╚═══██╗██╔══██║██╔══██║██║░░░░░
{RED}██║░╚═╝░██║██║░░██║██║░░██║██████╔╝██║░░██║██║░░██║███████╗
{MAGENTA}╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝
{YELLOW}AUTHOR: DCM.X-505
{RED}TEAM: DSAC
{YELLOW}JANGAN LUPA KASIH START DI: https://github.com/otoraritas
"""
current_time = time.localtime()

year = current_time.tm_year
day = current_time.tm_mday
month_number = current_time.tm_mon

month_name = calendar.month_name[month_number]

os.system("clear")

print(logo)

if len(sys.argv) != 4:
    print(f"{RED}Usage: pyenc <file> <output> <layers>")
    sys.exit(1)

file = sys.argv[1]
out = sys.argv[2]
jumlah = int(sys.argv[3])

baca = open(file, "r").read()

for i in range(jumlah):
    com = compile(baca, "", "exec")
    encrypt_marshal = marshal.dumps(com)

encrypted_base64 = base64.b64encode(encrypt_marshal)

baru = open(out, "w")

baru.write("import marshal, base64\n")
baru.write("#apa lu mau recode/decode hahh? wkwk\n#enc by tools dcm\n#siapa yg bisa decode script ini ?\n#jawabannya tidak ada yg bisa!!\n")
baru.write("exec(marshal.loads(base64.b64decode("+repr(encrypted_base64)+")))\n")

print("")
print(f"{BLUE}==========================================================================")
print(f"{YELLOW}Encryption Successful. File Saved in {out}")
print(f"{BLUE}Number of Encryption Layers: {jumlah}")
print(f"{MAGENTA}Encryption Successful on {year}-{day}-{month_name}")
print(f"{BLUE}==========================================================================")
