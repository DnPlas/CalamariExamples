import calamari_7seg as sseg
import calamari_pot as pot

if __name__ == '__main__':
    pot = pot.Pot()
    dsp = sseg.SevenSeg()
    while True:
        number = int(pot.read()/102.4)
        dsp.write(str(number))
