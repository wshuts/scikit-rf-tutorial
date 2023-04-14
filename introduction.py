import skrf as rf


class Introduction:
    @staticmethod
    def run_demo():
        path = 'venv/Lib/site-packages/skrf/data/'
        ring_slot = rf.Network(path + 'ring slot.s2p')

        short = rf.data.wr2p2_short
        delayshort = rf.data.wr2p2_delayshort
        diff = short - delayshort
        quot = short / delayshort

        line = rf.data.wr2p2_line
        delayshort_cascade = line ** short
        short_deembed = line.inv ** delayshort

        if delayshort_cascade == delayshort:
            print("Cascade verified.")
        if short_deembed == short:
            print("De-embed verified.")

        return
