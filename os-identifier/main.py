import sys
import platform

info = platform.freedesktop_os_release()
class Id:
    def __init__(self):
        import sys
        self.platform = sys.platform

class Os(Id):
    def send_back(self):
        if "linux" in self.platform:
            print("Os: ", info["NAME"], " Version: ", info["VERSION_ID"])

        elif "win32" in self.platform:
            print("Os: Windows")

        elif "darwin" in self.platform:
            print("Os: MacOS")
    
        else:
            raise Exception(f"Unknown OS: {self.platform}")
