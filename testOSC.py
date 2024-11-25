from pythonosc import udp_client
from time import sleep
# Dummy OSC server to handle responses (local communication)
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server


# Setup OSC client
# Replace with the correct address/port if different
sc_client = udp_client.SimpleUDPClient("127.0.0.1", 57110)

# Send /s_new to create a sine synth
# sc_client.send_message("/s_new", ["walk", -1, 1, 1, "position", 1])
# sleep(1)
# sc_client.send_message("/s_new", ["walk", -1, 1, 1, "position", 0])
# sleep(1)
# sc_client.send_message("/s_new", ["walk", -1, 1, 1, "position", -1])
# sleep(1)

sc_client.send_message("/s_new", ["jump", -1, 1, 1, "position", 0])
sleep(1)
sc_client.send_message("/s_new", ["jump", -1, 1, 1, "position", -1])
sleep(1)
sc_client.send_message("/s_new", ["jump", -1, 1, 1, "position", 1])
sleep(1)

location = [i/10 for i in range(-10, 10)]
for i in location:
    sc_client.send_message("/s_new", ["jump", -1, 1, 1, "position", i])
    sleep(0.2)

sc_client.send_message("/n_free", "all")


# Keep the script running to let the synth play
