import speech
import sys


def main(args):
    cancel = False
    text = []
    args = args[1:]
    for x in args:
        if x == "-c":
            cancel = True
        elif x[0] != "-":
            text.append(x)
    ret = speech.initialize()
    if ret is not False:
        sr = speech.getInstance()
        if cancel:
            sr.cancelSpeech()
        sr.speak(" ".join(text))

if __name__ == '__main__':
    main(sys.argv)
    
