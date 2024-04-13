#	Include Library
import os
import time
import sys

#	Variable
run_server = "screen -AmdS server ./xash3d -game cstrike -dev 3 +public 1 +maxplayers 32 +port 27016 +map de_dust2 +sv_nat 0; screen -r server"
dl_server = "wget https://github.com/qberkdc/Xash3D-CH/releases/download/xashlinux_v2/xashch-server.zip; apt install unzip -y; dpkg --add-architecture i386; apt-get install libstdc++6:i386 -y; apt-get install lib32stdc++6; apt-get install libstdc++6; unzip xashch-server.zip; rm xashch-server.zip; chmod -R 777 xashch-server"
opt_server = "nano xashch-server/cstrike/server.cfg"

#	Function
def download_game():
	global run_server, dl_server, opt_server;
	print("Kurulum basliyor.");
	time.sleep(2.0); os.system(dl_server);
	print("Kurulum bitti, sunucuyu baslatmak istermisiniz?")
	response = input("(E veya H): ");
	
	if("e" in response or "E" in response):
		print("Pekala o halde sunucu ayarlarimizi yapilandiralim.");
		time.sleep(4.0); os.system(opt_server);
	else:
		print("Pekala o halde sadece sunucu ayarlarimizi yapilandiralim.");
		time.sleep(4.0); os.system(opt_server);

	time.sleep(1.5); print("Yapilandirma sona erdi");
	time.sleep(1.5); print("Sunucunuz icin gerekli diger yapilandirma ve kurulumlara baslayabilirsiniz.");
	time.sleep(1.5); print("Iyi gunler dileriz :)\n");
	
	if("e" in response or "E" in response):
		print("Sunucun baslatiliyor.");
		time.sleep(4.0); os.system(run_server);
		
	time.sleep(1.5); sys.exit();
	
#	Call function
download_game();