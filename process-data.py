import serial
import csv
import numpy as np
import matplotlib.pyplot as plt

time_out = 3
baud_rate = 9600
port = '/dev/tty.usbserial-A6026OJT'
data = []
samples = 1
output_filename = 'test.csv'


def trim_data(d, n=128, m=255):
    """
    Partitions an input array of data into a feature vector of size n:
    an n-sized array with normalized values with regard to m.
    If the input data is of a shorter length than n the returned array will be sparse.
    A larger input array will produce a denser result.
    :param d: Input array of data.
    :param n: Size of result array.
    :param m: Normalizing factor (maximum possible data value).
    :return: Array of size param n with input param data distributed over the array
             and normalized with regard to param m.
    """
    l = len(d)
    histogram = [0] * n
    s = int(l / n)
    if s == 0:
        s = int(1. / (float(l) / float(n)))
        for i, x in enumerate(d):
            histogram[i*s] = x/m
    else:
        for i in range(0, n):
            histogram[i] = sum(d[i*s:(i+1)*s])/(m*s)
    return histogram


def test_trim_data():
    assert [1., 1., 1.] == trim_data([1., 1., 1.], n=3, m=1)
    assert [1., 0., 0.] == trim_data([1.], n=3, m=1)
    assert [1., 0., 0., 1., 0., 0., 1., 0., 0., 0.] == trim_data([1., 1., 1.], n=10, m=1)
    assert [0.5, 0.5, 0.5] == trim_data([1., 1., 1.], n=3, m=2)
    assert [0.1, 0.1, 0.1] == trim_data([1., 1., 1.], n=3, m=10)
    assert [.2, 0., 0., .2, 0., 0., .2, 0., 0., 0.] == trim_data([1., 1., 1.], n=10, m=5)
    assert [1., 1., 1.] == trim_data([1., 1., 1., 1., 1., 1.], n=3, m=1)
    assert [.5, .5, .5] == trim_data([.25, .75, .25, .75, .25, .75], n=3, m=1)


def listen_for_gestures():
    ser = serial.Serial(port, baud_rate, timeout=time_out)
    for n in range(0, samples):
        total = []
        try:
            print("Listening for gesture for " + str(time_out) + " seconds..")
            for line in ser:
                line = line.decode()
                line = line.split(' ')
                del line[-1]
                values = list(map(int, line))
                total = total + values
        except serial.SerialException:
            print('caught SerialException!')
        print(total)
        sensor1 = []
        sensor2 = []
        sensor3 = []
        sensor4 = []
        for j in range(0, len(total), 4):
            sensor1.append(total[j+0])
            sensor2.append(total[j+1])
            sensor3.append(total[j+2])
            sensor4.append(total[j+3])
        sensor3.extend(sensor4)
        sensor2.extend(sensor3)
        sensor1.extend(sensor2)
        if len(sensor1) > 0:
            data.append(trim_data(sensor1))
            print("Stored result to memory: {0}".format(str(n + 1)))


def save_data():
    with open(output_filename, 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(data)
    print("Stored " + len(data) + " data samples to file: " + output_filename)


def plot(d):
    plt.bar(np.arange(128), tuple(d))
    plt.show()

if __name__ == '__main__':
    listen_for_gestures()
    print(data)