from application import Application
from application import parse_command
from respond import respond #bura silinecek
from spotify import spotifycommand
from systemmanagement import increase_volume
from systemmanagement import decrease_volume


def main():

    while True:
        # Kullanıcıdan giriş al
        command = input("Bir komut girin (çıkmak için 'çık' yazın): ")
        command_lower = command.lower()

        if command.lower() == "çık":
            respond("Görüşmek üzere!")
            break

        elif command.startswith("open"):
            appname = parse_command(command)
            if appname:
                Application.openapp(appname)
            else:
                print("Uygulama adı belirtilmedi.")

        elif "spotify" in command.lower() or "track" in command.lower() or "song" in command.lower():
            spotifycommand(command)

        elif "volume up" in command.lower():
            increase_volume()

        elif "volume down" in command.lower():
            decrease_volume()





        else:
            respond("Bu konuda ne söyleyeceğimi bilmiyorum.")

if __name__ == "__main__":
    main()