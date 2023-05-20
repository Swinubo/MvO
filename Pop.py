def popper(FREQUENCY, LENGTH): #Hz, waves per second, seconds to play sound
    import math        #import needed modules
    import pyaudio     #sudo apt-get install python-pyaudio

    PyAudio = pyaudio.PyAudio     #initialize pyaudio

    #See https://en.wikipedia.org/wiki/Bit_rate#Audio
    BITRATE = 80000    #number of frames per second/frameset.

    BITRATE = max(BITRATE, FREQUENCY+100)

    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    RESTFRAMES = NUMBEROFFRAMES % BITRATE
    WAVEDATA = ''    

    #generating wawes
    for x in range(NUMBEROFFRAMES):
        WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

    for x in range(RESTFRAMES): 
        WAVEDATA = WAVEDATA+chr(128)

    p = PyAudio()
    stream = p.open(format = p.get_format_from_width(1), 
                    channels = 1, 
                    rate = BITRATE, 
                    output = True)

    stream.write(WAVEDATA)
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    #NOTE THAT ALL THIS CODE IS NOT MINE IT WAS WRITTEN BY "Liam" ON STACK OVERFLOW AND IT WAS POSTED IN 2015 