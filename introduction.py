import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
from skrf import NetworkSet
from skrf.plotting import save_all_figs


class Introduction:

    def __init__(self):
        self.path = 'venv/Lib/site-packages/skrf/data/'
        self.ring_slot = rf.Network(self.path + 'ring slot.s2p')

    def run_networks_demo(self):
        print(self.ring_slot)

        short = rf.data.wr2p2_short
        delayshort = rf.data.wr2p2_delayshort

        diff = short - delayshort
        quot = short / delayshort
        print(diff)
        print(quot)

        line = rf.data.wr2p2_line
        delayshort_cascade = line ** short
        short_deembed = line.inv ** delayshort

        if delayshort_cascade == delayshort:
            print("Cascade verified.")
        if short_deembed == short:
            print("De-embed verified.")

        print(type(line.s))
        print(line.s.shape)
        print(line.frequency)
        first_ten_frequencies = line.f[0:10]
        print(first_ten_frequencies)

        rs_s21_mag = self.ring_slot.s_mag[:, 1, 0]
        print(rs_s21_mag)
        print(rs_s21_mag.min())
        print(rs_s21_mag.max())

        rs_s11_mag = self.ring_slot.s_mag[:, 0, 0]
        print(rs_s11_mag)

        freq_index = np.argmin(rs_s11_mag)
        freq_rs_s11_mag_min = self.ring_slot.f[freq_index]
        print(freq_rs_s11_mag_min)
        print(rs_s11_mag[freq_index])

        return

    def run_plotting_demo(self):
        rf.stylely()

        fig1, ax1 = plt.subplots()
        self.ring_slot.plot_s_db(ax=ax1)
        ax1.set_title('S-Parameters')

        fig2, ax2 = plt.subplots()
        self.ring_slot.plot_s_deg(m=0, n=1, ax=ax2)
        ax2.set_title('S12')

        fig3, ax3 = plt.subplots()
        self.ring_slot.plot_s_smith(m=0, n=0, lw=2, ax=ax3)
        self.ring_slot.plot_s_smith(m=1, n=1, lw=2, ax=ax3)
        ax3.set_title('SmithChart')

        save_all_figs()

        return

    def run_networkset_demo(self):
        networkset = rf.read_all(self.path, contains='ro')
        print(networkset)

        ro_ns = NetworkSet(networkset, name='ro set')
        print(ro_ns)

        return
