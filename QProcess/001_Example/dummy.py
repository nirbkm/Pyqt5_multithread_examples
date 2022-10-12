import time
import sys


def flush_then_wait():
    sys.stdout.flush()
    sys.stderr.flush()
    time.sleep(0.5)


firstNumber = int(sys.argv[1])
secondNumber = int(sys.argv[2])
result = firstNumber + secondNumber
sys.stdout.write('Calculating..')
flush_then_wait()
time.sleep(0.5)
sys.stdout.write(f'{result}')

flush_then_wait()
