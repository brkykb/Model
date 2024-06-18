import subprocess
from respond import respond
from spotify import sp
class Application:
    @staticmethod
    def openapp(appname):
        try:
            subprocess.run(["open", "-a", appname])
            respond(appname)

        except FileNotFoundError:
            print(f"Unable to find application named '{appname}'")

def parse_command(command):
    parts = command.split()
    if len(parts) > 1 and parts[0].lower() == "open":
        appname = " ".join(parts[1:])  # İlk kelime "open" olduğu için geri kalanı uygulama adı olarak al
        return appname

    else:
        return None


