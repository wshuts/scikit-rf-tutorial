import skrf as rf


class Introduction:
    @staticmethod
    def run_demo():
        path = 'venv/Lib/site-packages/skrf/data/'
        ring_slot = rf.Network(path + 'ring slot.s2p')
        print(ring_slot)

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

        return
