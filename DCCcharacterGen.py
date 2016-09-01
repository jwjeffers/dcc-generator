import random;

def farmer():
    result = d8()
    if result == 1:
        return "Potato Farmer"
    if result == 2:
        return "Wheat Farmer" 
    if result == 3:
        return "Turnip Farmer"
    if result == 4:
        return "Corn Farmer"
    if result == 5:
        return "Rice Farmer"
    if result == 6:
        return "Parsnip Farmer"
    if result == 7:
        return "Radish Farmer"
    if result == 8:
        return "Rutabaga Farmer"
    
def cartitems():
    result = d6()
    if result == 1:
        print("Tommatoes are in your cart")
    if result == 2:
        print("nothing are in your cart")
    if result == 3:
        print("straw are in your cart")
    if result == 4:
        print("your dead are in your cart")
    if result == 5:
        print("dirt are in your cart")
    if result == 6:
        print("rocks are in your cart")
        
def gender():
    result = d10()
    if result == 1 or result == 2 or result == 3 or result == 4 or result == 5 or result == 6 or result == 7 or result == 8 or result == 9:
        print("Male")
    if result == 10:
        print("Female")

def startingmoney():
    coppers = 0
    for x in range(0,5):
        coppers = coppers + d12()
    return coppers
    
def d12():
    return random.randint(1,12)

def d10():
    return random.randint(1,10)
    
def d6():
    return random.randint(1,6)

def d8():
    return random.randint(1,8)


while 1:
    Gear=random.randint(1,24)
    Item=random.randint(1,100)
    Luck=random.randint(1,30)

    print("This is a DCC Character Generator:")
    print("-------------------------------------")
    print("STR " + str(d6() + d6() + d6()))
    print("AGI " + str(d6() + d6() + d6()))
    print("STA " + str(d6() + d6() + d6()))
    print("PER " + str(d6() + d6() + d6()))
    print("INT " + str(d6() + d6() + d6()))
    print("LUCK " + str(d6() + d6() + d6()))
    gender()
    print("Starting Money:" + str(startingmoney())+ "cp")
    if Item==1:
           print("Occupation/Trade Goods: Alchemist, Staff, Oil(1 flask)")
    if Item==2:
           print("Occupation/Trade Goods: Animal Trainer, Club, Pony")
    if Item==3:
           print("Occupation/Trade Goods: Armorer, Hammer (as club), Iron Helmet")
    if Item==4:
           print("Occupation/Trade Goods: Astrologer, Dagger, Spyglass")
    if Item==5:
           print("Occupation/Trade Goods: Barber, Razor(as dagger), Scissors")
    if Item==6:
           print("Occupation/Trade Goods: Beadle, staff, holy symbol")
    if Item==7:
           print("Occupation/Trade Goods: Beekeeper, staff, jar of honey")
    if Item==8:
           print("Occupation/Trade Goods: Blacksmith, Hammer(as club), steel tongs")
    if Item==9:
           print("Occupation/Trade Goods: Butcher, cleaver(axe), side of beef")
    if Item==10:
           print("Occupation/Trade Goods: Caravan guard, short sword, linen(1 yard)")
    if Item==11:
           print("Occupation/Trade Goods: Cheesemaker, cudgel(as staff), stinky cheese")
    if Item==12:
           print("Occupation/Trade Goods: Cobbler, awl(as dagger), shoehorn")
    if Item==13:
           print("Occupation/Trade Goods: Confidence artist,Dagger,Quality cloak")
    if Item==14:
           print("Occupation/Trade Goods: Cooper,Crowbar (as club),Barrel")
    if Item==15:
           print("Occupation/Trade Goods: Costermonger,Knife (as dagger),fruit")
    if Item==16:
           print("Occupation/Trade Goods: Cutpurse,Dagger,Small chest")
    if Item==17:
           print("Occupation/Trade Goods: Ditch digger,Shovel (as staff),Fine dirt (1 lb.)")
    if Item==18:
           print("Occupation/Trade Goods: Dwarven apothacarist,Cudgel (as staff),Steel vial")
    if Item==19:
           print("Occupation/Trade Goods: Dwarven blacksmith,Hammer (as club),Mithril (1 oz.)")
    if Item==20:
           print("Occupation/Trade Goods: Dwarven blacksmith,Hammer (as club),Mithril (1 oz.)")
    if Item==21:
           print("Occupation/Trade Goods: Dwarven chest-maker,Chisel (as dagger),Wood (10 lbs)")
    if Item==22:
           print("Occupation/Trade Goods: Dwarven herder,Staff,Sow")
    if Item==23:
           print("Occupation/Trade Goods: Dwarven miner,Pick (as club),Lantern")
    if Item==24:
           print("Occupation/Trade Goods: Dwarven miner,Pick (as club),Lantern")
    if Item==25:
           print("Occupation/Trade Goods: Dwarven mushroom-farmer,Shovel,Sack")
    if Item==26:
           print("Occupation/Trade Goods: Dwarven rat-catcher,Club,Net")
    if Item==27:
           print("Occupation/Trade Goods: Dwarven stonemason,Hammer (as club),Fine stone (10 lbs)")
    if Item==28:
           print("Occupation/Trade Goods: Dwarven stonemason,Hammer (as club),Fine stone (10 lbs)")
    if Item==29:
           print("Occupation/Trade Goods: Elven artisan,Staff,Clay (1 lb.)")
    if Item==30:
           print("Occupation/Trade Goods: Elven barrister,Quill (as dart),Book")
    if Item==31:
           print("Occupation/Trade Goods: Elven chandler,Scissors (as dagger),Candles (20)")
    if Item==32:
           print("Occupation/Trade Goods: Elven falconer,Dagger,Falcon")
    if Item==33:
           print("Occupation/Trade Goods: Elven forester,Staff,Herbs (1 lb.)")
    if Item==34:
           print("Occupation/Trade Goods: Elven forester,Staff,Herbs (1 lb.)")
    if Item==35:
           print("Occupation/Trade Goods: Elven glassblower,Hammer (as club),Glass beads")
    if Item==36:
           print("Occupation/Trade Goods: Elven navigator,Shortbow,Spyglass")
    if Item==37:
           print("Occupation/Trade Goods: Elven sage,Dagger,Parchment and quill pen")
    if Item==38:
           print("Occupation/Trade Goods: Elven sage,Dagger,Parchment and quill pen")
    if Item==39:
           print("Occupation/Trade Goods:" + farmer() + ",Pitchfork (as spear),Hen")
    if Item==40:
           print("Occupation/Trade Goods:" + farmer() + ",Pitchfork (as spear),Hen")
    if Item==41:
           print("Occupation/Trade Goods:" + farmer() + ",Pitchfork (as spear),Hen")
    if Item==42:
           print("Occupation/Trade Goods:" + farmer() + ",Pitchfork (as spear),Hen")
    if Item==43:
           print("Occupation/Trade Goods:" + farmer() + ",Pitchfork (as spear),Hen")
    if Item==44:
           print("Occupation/Trade Goods:" + farmer() + ",Pitchfork (as spear),Hen")
    if Item==45:
           print("Occupation/Trade Goods:" + farmer() + ",Pitchfork (as spear),Hen")
    if Item==46:
           print("Occupation/Trade Goods:" + farmer() + ",Pitchfork (as spear),Hen")
    if Item==47:
           print("Occupation/Trade Goods:" + farmer() + ",Pitchfork (as spear),Hen")
    if Item==48:
           print("Occupation/Trade Goods: Fortune-teller,Dagger,Tarot deck")
    if Item==49:
           print("Occupation/Trade Goods: Gambler,Club,Dice")
    if Item==50:
           print("Occupation/Trade Goods: Gongfarmer,Trowel (as dagger),Sack of night soil")
    if Item==51:
           print("Occupation/Trade Goods: Grave digger,Shovel (as staff),Trowel")
    if Item==52:
           print("Occupation/Trade Goods: Grave digger,Shovel (as staff),Trowel")
    if Item==53:
           print("Occupation/Trade Goods: Guild beggar,Sling,Crutches")
    if Item==54:
           print("Occupation/Trade Goods: Guild beggar,Sling,Crutches")
    if Item==55:
           print("Occupation/Trade Goods: Halfling chicken butcher,Handaxe,Chicken meat (5 lbs.)")
    if Item==56:
           print("Occupation/Trade Goods: Halfling dyer,Staff,Fabric (3 yards)")
    if Item==57:
           print("Occupation/Trade Goods: Halfling dyer,Staff,Fabric (3 yards)")
    if Item==58:
           print("Occupation/Trade Goods: Halfling glovemaker,Awl (as dagger),Gloves (4 pairs)")
    if Item==59:
           print("Occupation/Trade Goods: Halfling gypsy,Sling,Hex doll")
    if Item==60:
           print("Occupation/Trade Goods: Halfling haberdasher,Scissors (as dagger),Fine suits (3 sets)")
    if Item==61:
           print("Occupation/Trade Goods: Halfling mariner,Knife (as dagger),Sailcloth (2 yards)")
    if Item==62:
           print("Occupation/Trade Goods: Halfling moneylender,Short sword,5 gp 10 sp 200 cp")
    if Item==63:
           print("Occupation/Trade Goods: Halfling trader,Short sword,20 sp")
    if Item==64:
           print("Occupation/Trade Goods: Halfling vagrant,Club,Begging bowl")
    if Item==65:
           print("Occupation/Trade Goods: Healer,Club,Holy water (1 vial)")
    if Item==66:
           print("Occupation/Trade Goods: Herbalist,Club,Herbs (1 lb.)")
    if Item==67:
           print("Occupation/Trade Goods: Herder,Staff,Herding dog")
    if Item==68:
           print("Occupation/Trade Goods: Hunter,Shortbow,Deer pelt")
    if Item==69:
           print("Occupation/Trade Goods: Hunter,Shortbow,Deer pelt")
    if Item==70:
           print("Occupation/Trade Goods: Indentured servant,Staff,Locket")
    if Item==71:
           print("Occupation/Trade Goods: Jester,Dart,Silk clothes")
    if Item==72:
           print("Occupation/Trade Goods: Jeweler,Dagger,Gem worth 20 gp")
    if Item==73:
           print("Occupation/Trade Goods: Locksmith,Dagger,Fine tools")
    if Item==74:
           print("Occupation/Trade Goods: Mendicant,Club,Cheese dip")
    if Item==75:
           print("Occupation/Trade Goods: Mercenary,Longsword,Hide armor")
    if Item==76:
           print("Occupation/Trade Goods: Merchant,Dagger,4 gp 14 sp 27 cp")
    if Item==77:
           print("Occupation/Trade Goods: Miller/baker,Club,Flour (1 lb.)")
    if Item==78:
           print("Occupation/Trade Goods: Minstrel,Dagger,Ukulele")
    if Item==79:
           print("Occupation/Trade Goods: Noble,Longsword,Gold ring worth 10 gp")
    if Item==80:
           print("Occupation/Trade Goods: Orphan,Club,Rag doll")
    if Item==81:
           print("Occupation/Trade Goods: Ostler,Staff,Bridle")
    if Item==82:
           print("Occupation/Trade Goods: Outlaw,Short sword,Leather armor")
    if Item==83:
           print("Occupation/Trade Goods: Ropemaker,Knife (as dagger),Rope (100’)")
    if Item==84:
           print("Occupation/Trade Goods: Scribe,Dart,Parchment (10 sheets)")
    if Item==85:
           print("Occupation/Trade Goods: Shaman,Mace,Herbs (1 lb.)")
    if Item==86:
           print("Occupation/Trade Goods: Slave,Club,Strange-looking rock")
    if Item==87:
           print("Occupation/Trade Goods: Smuggler,Sling,Waterproof sack")
    if Item==88:
           print("Occupation/Trade Goods: Soldier,Spear,Shield")
    if Item==89:
           print("Occupation/Trade Goods: Squire,Longsword,Steel helmet")
    if Item==90:
           print("Occupation/Trade Goods: Squire,Longsword,Steel helmet")
    if Item==91:
           print("Occupation/Trade Goods: Tax collector,Longsword,100 cp")
    if Item==92:
           print("Occupation/Trade Goods: Trapper,Sling,Badger pelt")
    if Item==93:
           print("Occupation/Trade Goods: Trapper,Sling,Badger pelt")
    if Item==94:
           print("Occupation/Trade Goods: Urchin,Stick (as club),Begging bowl")
    if Item==95:
           print("Occupation/Trade Goods: Wainwright,Club,Pushcart")
           cartitems()
    if Item==96:
           print("Occupation/Trade Goods: Weaver,Dagger,Fine suit of clothes")
    if Item==97:
           print("Occupation/Trade Goods: Wizard’s apprentice,Dagger,Black grimoire")
    if Item==98:
           print("Occupation/Trade Goods: Woodcutter,Handaxe,Bundle of wood")
    if Item==99:
           print("Occupation/Trade Goods: Woodcutter,Handaxe,Bundle of wood")
    if Item==100:
           print("Occupation/Trade Goods: Woodcutter,Handaxe,Bundle of wood")
    if Gear==1:
        print("Adventuring Gear: Backpack, worth 2gp")
    if Gear==2:
        print("Adventuring Gear: Candle, worth 1cp")
    if Gear==3:
        print("Adventuring Gear: Chain 10', worth 30gp")
    if Gear==4:
        print("Adventuring Gear: Chalk (1 piece), worth 1cp")
    if Gear==5:
        print("Adventuring Gear: Chest (empty), 2gp")
    if Gear==6:
        print("Adventuring Gear: Crowbar, 2gp")
    if Gear==7:
        print("Adventuring Gear: Flask (empty), 3cp")
    if Gear==8:
        print("Adventuring Gear: Flint&Steel, worth 15cp")
    if Gear==9:
        print("Adventuring Gear: Grappling hook, 1gp")
    if Gear==10:
        print("Adventuring Gear: Hammer (small), worth 5sp")
    if Gear==11:
        print("Adventuring Gear: Holy symbol, worth 25gp")
    if Gear==12:
        print("Adventuring Gear: Holy water (1 vial, 1d4 any undead), worth 25gp")
    if Gear==13:
        print("Adventuring Gear: Iron Spikes, each 1sp")
    if Gear==14:
        print("Adventuring Gear: Latern, worth 10gp")
    if Gear==15:
        print("Adventuring Gear: Mirror (hand-sized), worth 10gp")
    if Gear==16:
        print("Adventuring Gear: Oil (1 flask), worth 2sp")
    if Gear==17:
        print("Adventuring Gear: Pole (10'), 15cp")
    if Gear==18:
        print("Adventuring Gear: Rations, per day 5cp")
    if Gear==19:
        print("Adventuring Gear: Rope (50'), worth 25cp")
    if Gear==20:
        print("Adventuring Gear: Sack (large), worth 12cp")
    if Gear==21:
        print("Adventuring Gear: Sack (small), worth 8cp")
    if Gear==22:
        print("Adventuring Gear: Theives' tools, worth 25gp")
    if Gear==23:
        print("Adventuring Gear: Torch, each 1cp")
    if Gear==24:
        print("Adventuring Gear: Waterskin, 5sp")
    if Luck==1:
           print("Birth Augur and Lucky Roll: Harsh Winter: All attack rolls")
    if Luck==2:
           print("Birth Augur and Lucky Roll: The Bull: All melee attack rolls")
    if Luck==3:
           print("Birth Augur and Lucky Roll: Fortunate Date: Missile Fire attack rolls")
    if Luck==4:
           print("Birth Augur and Lucky Roll: Raised by Wolves: Unarmed attack rolls")
    if Luck==5:
           print("Birth Augur and Lucky Roll: Conceived on horseback: Mounted attack rolls")
    if Luck==6:
           print("Birth Augur and Lucky Roll: Born on the Battlefield: Damage rolls")
    if Luck==7:
           print("Birth Augur and Lucky Roll: Path of the bear: Meleee damage rolls")
    if Luck==8:
           print("Birth Augur and Lucky Roll: Hawkeye: Missile damage rolls")
    if Luck==9:
           print("Birth Augur and Lucky Roll: Pack hunter: Attack and damage rolls for 0-level starting weapon")
    if Luck==10:
           print("Birth Augur and Lucky Roll: Born under the loom: Skill checks (including theif skills)")
    if Luck==11:
           print("Birth Augur and Lucky Roll: Fox's Cunning: Find/ disable traps")
    if Luck==12:
           print("Birth Augur and Lucky Roll: Four-leafed clover: Find secret doors")
    if Luck==13:
           print("Birth Augur and Lucky Roll: Seventh son: Spell Cheecks")
    if Luck==14:
           print("Birth Augur and Lucky Roll: The raging storm: Spell damage")
    if Luck==15:
           print("Birth Augur and Lucky Roll: Righteous heart: Turn unholy checks")
    if Luck==16:
           print("Birth Augur and Lucky Roll: Survived the Plague: Magical healing*")
    if Luck==17:
           print("Birth Augur and Lucky Roll: Lucky sign: Saving throws")
    if Luck==18:
           print("Birth Augur and Lucky Roll: Guardian angel: Saving throws to escape traps")
    if Luck==19:
           print("Birth Augur and Lucky Roll: Survived a spider bite: Saving throws agaisnt poison")
    if Luck==20:
           print("Birth Augur and Lucky Roll: Struck by lightning: Reflex saving throws")
    if Luck==21:
           print("Birth Augur and Lucky Roll: Lived through famine: fortitude saving throws")
    if Luck==22:
           print("Birth Augur and Lucky Roll: Resisted Temptation: Willpower saving throws")
    if Luck==23:
           print("Birth Augur and Lucky Roll: Charmed house: Armour Class")
    if Luck==24:
           print("Birth Augur and Lucky Roll: Speed of the cobra: Initiative")
    if Luck==25:
           print("Birth Augur and Lucky Roll: Bountiful harvest: Hit Points (applies at each level)")
    if Luck==26:
           print("Birth Augur and Lucky Roll: Warrior's arm: Ciritical hits table(doubles affects)")
    if Luck==27:
           print("Birth Augur and Lucky Roll: Unholy house: Corruption rolls")
    if Luck==28:
           print("Birth Augur and Lucky Roll: The Broken Star: Fumbles (doubles result)")
    if Luck==29:
           print("Birth Augur and Lucky Roll: Harsh Winter: Birdsong: Number of languages")
    if Luck==30:
           print("Birth Augur and Lucky Roll: Wild child: Speed (each +1/-1 = +5/-5 speed)")   
    print("------------------------------------")
    input("Another character? Press Enter then.")
