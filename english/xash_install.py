#	Include Library
import os
import time
import sys

#	Variable
run_server = "screen -S server ./xash3d -game cstrike -dev 3 +public 1 +maxplayers 32 +port 27016 +map de_dust2 +sv_nat 0"
dl_server = "wget https://github.com/qberkdc/Xash3D-CH/releases/download/xashlinux_v2/xashch-server.zip; apt install unzip -y; dpkg --add-architecture i386; apt-get install libstdc++6:i386 -y; apt-get install lib32stdc++6; apt-get install libstdc++6; unzip xashch-server.zip; rm xashch-server.zip; chmod -R 777 xashch-server"
opt_server = "nano xashch-server/cstrike/server.cfg"

#	Function
def download_game():
	global run_server, dl_server, opt_server;
	print("The installation is starting.");
	time.sleep(2.0); os.system(dl_server);
	print("The installation is finished, do you want to start the server?")
	response = input("(Y or N): ");
	
	if("y" in response or "Y" in response):
		print("All right, then let's set up our server settings.");
		time.sleep(4.0); os.system(opt_server);
	else:
		print("All right, then let's just set up our server settings.");
		time.sleep(4.0); os.system(opt_server);

	time.sleep(1.5); print("Structuring has ended");
	time.sleep(1.5); print("You can start other necessary configurations and installations for your server.");
	time.sleep(1.5); print("We wish you a good day :)\n");
	
	if("y" in response or "Y" in response):
		print("Server starting.");
		time.sleep(4.0); os.system(run_server);
		
	time.sleep(1.5); sys.exit();
	
#	Call function
download_game();
