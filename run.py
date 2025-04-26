import multiprocessing


# This file is part of Bujji.
def startBujji():
    print("Bujji is starting...")
    from main import start
    start()

# This function will listen for the hotword and trigger the assistant
def listenHotWord():
    print("Listening for hotword...")
    from engine.features import hotword
    hotword()


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=startBujji)
    p2 = multiprocessing.Process(target=listenHotWord)
    p1.start()
    p2.start()
    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()
    print("Bujji has stopped.")



