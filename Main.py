import os
import pathlib

def GetPathOfBOTN_Boolean():
    botn_path = str("E:\\SteamLibrary\\steamapps\\common\\Breeders of the Nephelym Alpha") # Make Sure what this path is right, if not please change path :D
    return pathlib.Path(botn_path).is_dir()
def GetPathofBOTN():
    botn_path = str("E:\\SteamLibrary\\steamapps\\common\\Breeders of the Nephelym Alpha")
    return os.path.abspath(botn_path)

def Main():
    print(f"You're BOTN(Breeders of the Nephelym) Path is {GetPathofBOTN()}")
    if(GetPathOfBOTN_Boolean() is True):
        with open("{}".format(GetPathofBOTN() + "\\imma.degenerate"), "w") as write_file:
            write_file.write(str(""))
            print("You Can Now Have Incest!!! This Script created by RikkoMatsumatoOfficial!!!")
            os._exit(443)
    else:
        print("Please Download BOTN(Breeders of the Nephelym)!!!")
        os._exit(43321)

if __name__ == "__main__":
    Main()
