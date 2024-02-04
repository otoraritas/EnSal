import os, time

print("proses setup..")
os.system("cp -r .module/enc.py $HOME/../usr/bin; cp -r .module/pyenc $HOME/../usr/bin; chmod +x $HOME/../usr/bin/pyenc")
time.sleep(2)
print("proses setup selesai..\nUsage: pyenc <file> <output> <lapisan_enc>")
