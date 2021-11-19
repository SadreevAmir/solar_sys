import matplotlib.pyplot as plt
import numpy as np
t = []
v = []
r = []
def graphic(satellite_v, satellite_r,  time):
    t.append(time)
    v.append(satellite_v)
    r.append(satellite_r)

def stats(satellite_v, satellite_r,  time, output_filename):

    distance = str(satellite_r)
    time1 = str(time)
    velocity = str(satellite_v)

    with open(output_filename, 'a') as out_file:
        out_file.write(time1)
        out_file.write("\n")
        out_file.write(velocity)
        out_file.write("\n")
        out_file.write(distance)
        out_file.write("\n")



def draw_garphic():

    plt.subplots(2,2, figsize=(10,10))

    #subplot 1
    sp = plt.subplot(221)
    plt.plot(r, v)
    plt.title('v(r)')
    plt.xlabel('r, m')
    plt.ylabel('v, m/s')

    #subplot 2
    sp = plt.subplot(222)
    plt.plot(t, v)
    plt.title('v(t)')
    plt.xlabel('t, s')
    plt.ylabel('v, m/s')

    #subplot 3
    sp = plt.subplot(223)
    plt.plot(t, r)
    plt.title('r(t)')
    plt.xlabel('t, s')
    plt.ylabel('r, m')

    plt.show()





