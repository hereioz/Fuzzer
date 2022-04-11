import socket, argparse, time

class __main__:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Packet Sniffer')
        self.parser.add_argument('-i',  dest='IP', type=str ,help='Destnation IP Address', required=True)
        self.parser.add_argument('-p',  dest='Port', type=int ,help='Destnation Port', required=True)
        self.parser.add_argument('-s',  dest="Sleep", default=0.3, type=float ,help='Sleep Time Between Packets', required=False)
        self.args = self.parser.parse_args()
        
class Fuzzer:
    def __init__(self, ip, port, sleep):
        self.port = int(port)
        self.ip = ip
        self.sleep = sleep
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.connection.connect((self.ip, int(self.port)))

    def send(self):
        try:
            for i in range(100, 100**1000, 100):
                try:
                    self.connection.send(('A'*i).encode("utf-8"))
                    print("Trying.. {}".format(i), end='\r')
                except socket.error as e:
                    print("{0}:{1}.  crashed on {2} chars".format(self.ip, self.port, i))
                    return 1
                    
                time.sleep(self.sleep)

            print("Done.. no crashes ):")

        except KeyboardInterrupt:
            exit(0)

    def close(self):
        self.connection.close()


main = __main__()
Fuzzing = Fuzzer(main.args.IP, main.args.Port, main.args.Sleep)
Fuzzing.connect()
Fuzzing.send()
Fuzzing.close()
