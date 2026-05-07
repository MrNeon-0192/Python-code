import os
import platform
def shutdown():
    os.system.name=platform.system()
    if platform.system()=="Windows":
        os.system("shutdown /s /t 1")
    elif platform.system()=="Linux" or platform.system() =="Darwin":     
        os.system("shutdown -h now")
    else:
        print("Unsupported operating system")
if __name__=="__main__":
    confirm=input("Are you sure you want to shutdown your computer? (yes/no): ")
    if confirm.lower() in ["yes", "y"]:
        shutdown()