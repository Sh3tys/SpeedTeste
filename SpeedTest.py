#Bibliotheque
import speedtest

#Function
def testResaux():
    teste = speedtest.Speedtest()
    download = teste.download()
    upload = teste.upload()
    return download, upload

#Progs Principal

if __name__ == "__main__":
    donwload, upload = testResaux()
    print(f"Download speed: {donwload}")
    print(f"Download speed: {upload}")

#END
