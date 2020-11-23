def txt_zu_wav(eingabe, ausgabe, text_aus_datei = True, geschwindigkeit = 2, Stimmenname = "Zira"):
    from comtypes.client import CreateObject
    engine = CreateObject("SAPI.SpVoice")

    engine.rate = geschwindigkeit # von -10 bis 10

    for stimme in engine.GetVoices():
        if stimme.GetDescription().find(Stimmenname) >= 0:
            engine.Voice = stimme
            break
    else:
        print("Fehler Stimme nicht gefunden -> Standard wird benutzt")

    if text_aus_datei:
        datei = open(eingabe, 'r')
        text = datei.read()
        datei.close()
    else:
        text = eingabe

    stream = CreateObject("SAPI.SpFileStream")
    from comtypes.gen import SpeechLib

    stream.Open(ausgabe, SpeechLib.SSFMCreateForWrite)
    engine.AudioOutputStream = stream
    engine.speak(text)

    stream.Close()


# reads from a file named test.txt and converts to a .wav file
#txt_zu_wav("test.txt", "test_1.wav")