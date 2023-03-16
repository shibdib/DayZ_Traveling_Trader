# Trader movement script for DayZ Expansion
# By Shibdib https://github.com/shibdib
import random
import json

# Location options
locationOptions = [[[3708.786865, 402.01, 5974.589844, -131.125488],[3710.265137, 402.01, 5973.340820, -158.777390]],
    [[14353.624023, 3.326771, 13229.217773, 82.998276],[14378.793945, 3.325975, 13271.585938, -156.011154]],
    [[4973.928711, 9.510984, 2436.782959, -36.000050],[4943.928711, 9.510984, 2436.782959, -66.000050]],
    [[1756.656372, 1.415564, 2027.359741, -31.993799],[1766.656372, 1.415564, 2027.359741, -71.993799]],
    [[1156.719727, 6.513331, 2406.355225, -91.993446],[1153.964844, 6.463035, 2409.763184, 159.004440]]]

# Item list options
itemListOptions = ["Essentials1", "Essentials1", "Essentials1", "Essentials1"]

# Gear
traderGear = "CargoPants_Green,M65Jacket_Khaki,UKAssVest_Black,WorkingGloves_Black,AviatorGlasses,PilotkaCap," \
             "TTSKOBoots,AssaultBag_Black"


# Move the trader and quest giver npc to a random location, then set up a trade zone around them
def travelling_trader():
    chosen_location = random.choice(locationOptions)
    chosen_item_list = random.choice(itemListOptions)
    trader_file = open('F:/SteamLibrary/steamapps/common/DayZServer/mpmissions/dayzOffline.chernarusplus/expansion'
                      '/traders/moving.map', 'w')
    string = "ExpansionTraderBoris." + chosen_item_list + "|" + str(chosen_location[0][0]) + " " + str(chosen_location[0][1]) + " " + str(chosen_location[0][2]) + "|" + str(chosen_location[0][3]) + " 0.000000 -0.000000|" + traderGear
    trader_file.write(string)
    trader_file.close()
    # Now move the quest giver npc to a random location
    with open('F:/SteamLibrary/steamapps/common/DayZServer/profile/ExpansionMod/Quests/NPCs/traveling.json', 'r') as json_file:
        data = json.load(json_file)
        data["Position"] = [chosen_location[1][0], chosen_location[1][1], chosen_location[1][2]]
        data["Orientation"] = [chosen_location[1][3], 0, 0]
        with open('F:/SteamLibrary/steamapps/common/DayZServer/profile/ExpansionMod/Quests/NPCs/traveling.json',
                  'w') as new_file:
            json.dump(data, new_file, indent=4, sort_keys=True)
    # Set the location in the trader find quest
    with open('F:/SteamLibrary/steamapps/common/DayZServer/profile/ExpansionMod/Quests/Objectives/Travel/SHIB-OBJ-2303-Trader.json', 'r') as json_file:
        data = json.load(json_file)
        data["Position"] = [chosen_location[1][0], chosen_location[1][1], chosen_location[1][2]]
        with open('F:/SteamLibrary/steamapps/common/DayZServer/profile/ExpansionMod/Quests/Objectives/Travel/SHIB-OBJ-2303-Trader.json',
                  'w') as new_file:
            json.dump(data, new_file, indent=4, sort_keys=True)
    # Now set up the trade zone around the trader
    with open('F:/SteamLibrary/steamapps/common/DayZServer/mpmissions/dayzOffline.chernarusplus/expansion'
                      '/traderzones/moving.json', 'r') as json_file:
        data = json.load(json_file)
        data["Position"] = [chosen_location[1][0], chosen_location[1][1], chosen_location[1][2]]
        with open('F:/SteamLibrary/steamapps/common/DayZServer/mpmissions/dayzOffline.chernarusplus/expansion'
                      '/traderzones/moving.json',
                  'w') as new_file:
            json.dump(data, new_file, indent=4, sort_keys=True)
    # Finally update the trader's marker
    with open('F:/SteamLibrary/steamapps/common/DayZServer/mpmissions/dayzOffline.chernarusplus/expansion'
                      '/settings/MapSettings.json', 'r') as json_file:
        data = json.load(json_file)
        # Find and set the trader marker
        for m in data["ServerMarkers"]:
            if m["m_UID"] == "Traveling Trader":
                m["m_Position"] = [chosen_location[1][0], chosen_location[1][1], chosen_location[1][2]]
        with open('F:/SteamLibrary/steamapps/common/DayZServer/mpmissions/dayzOffline.chernarusplus/expansion'
                      '/settings/MapSettings.json',
                  'w') as new_file:
            json.dump(data, new_file, indent=4, sort_keys=True)


travelling_trader()
