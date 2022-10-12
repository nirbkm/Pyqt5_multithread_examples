import sys
import time


def flush_then_wait():
    sys.stdout.flush()
    sys.stderr.flush()
    time.sleep(0.5)



f = open('temp??_data.txt','w')
for x in range(100):
    time.sleep(0.25)
    f.write('{}'.format(x)+'\n')

f.close()

data = sys.argv[1].split(',')
for d in data:
    sys.stdout.write("{}\n".format(d+'\n'))

flush_then_wait()
#sys.stdout.write("Script stdout 1\n")
#sys.stdout.write("Script stdout 2\n")
#sys.stdout.write("Script stdout 3\n")
#sys.stderr.write("Total time: 00:05:00\n")
#sys.stderr.write("Total complete: 10%\n")
#flush_then_wait()
#
#sys.stdout.write("name=Martin\n")
#sys.stdout.write("Script stdout 4\n")
#sys.stdout.write("Script stdout 5\n")
#sys.stderr.write("Total complete: 30%\n")
#flush_then_wait()
#
#sys.stderr.write("Elapsed time: 00:00:10\n")
#sys.stderr.write("Elapsed time: 00:00:50\n")
#sys.stderr.write("Total complete: 50%\n")
#sys.stdout.write("country=Nederland\n")
#flush_then_wait()
#
#sys.stderr.write("Elapsed time: 00:01:10\n")
#sys.stderr.write("Total complete: 100%\n")
#sys.stdout.write("Script stdout 6\n")
#sys.stdout.write("Script stdout 7\n")
#sys.stdout.write("website=www.mfitzp.com\n")
#flush_then_wait()
