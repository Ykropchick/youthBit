from template import Daemon
from time import sleep
from datetime import datetime
import sys
from sqlite3 import connect

class NotionDaemon(Daemon):
    def create_notions(self):
        pass

    def run(self):
        while True:
            sleep(10)
            now = datetime.now()
            if now.hour == 0 and now.minute == 0:
                self.create_notions()


if __name__ == "__main__":
    d = NotionDaemon("./pidfile.pid")
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            d.start()
        elif 'stop' == sys.argv[1]:
            d.stop()
        elif 'restart' == sys.argv[1]:
            d.restart()
        elif 'check' == sys.argv[1]:
            d.is_running()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print(f"usage: {sys.argv[0]} start|stop|restart|check")
        sys.exit(2)
