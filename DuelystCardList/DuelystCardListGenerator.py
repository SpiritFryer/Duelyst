card_names = {
  "Lyonar": ["Beam Shock", "Lionheart Blessing", "Sunstone Bracers", "Aegis Barrier", "Aerial Rift", "Auryn Nexus", "Magnetize", "Silverguard Squire", "Sundrop Elixir", "True Strike", "Azurite Lion", "Lasting Judgement", "Lightchaster", "Martyrdom", "Sun Bloom", "Sunstone Templar", "Tempest", "War Surge", "Windblade Adept", "Arclyte Sentinel", "Divine Bond", "Silverguard Knight", "Skywind Glaives", "Arclyte Regalia", "Decimate", "Holy Immolation", "Lysian Brawler", "Sunriser", "Suntide Maiden", "Circle of Life", "Ironcliffe Guardian", "Second Sun", "Elyx Stormblade", "Grandmaster Z'ir"],
  "Songhai": ["Inner Focus", "Juxtaposition", "Mana Vortex", "Ancestral Divination", "Bloodrage Mask", "Ghost Lightning", "Heartseeker", "Mist Walking", "Saberspine Seal", "Artifact Defiler", "Chakri Avatar", "Deathstrike Seal", "Eight Gates", "Kaido Assassin", "Mask of Shadows", "Mist Dragon Seal", "Phoenix Fire", "Tusk Boar", "Celestial Phantom", "Cyclone Mask", "Gore Horn", "Jade Monk", "Killing Edge", "Lantern Fox", "Onyx Bear Seal", "Twin Strike", "Four Winds Magi", "Heaven's Eclipse", "Keshrai Fanblade", "Widowmaker", "Hamon Bladeseeker", "Scarlet Viper", "Spiral Technique", "Storm Kage"],
  "Vetruvian": ["Siphon Energy", "Auroras Tears", "Blindscorch", "Scion's First Wish", "Bone Swarm", "Cosmic Flesh", "Dunecaster", "Ethereal Obelysk", "Fountain of Youth", "Pyromancer", "Rasha's Curse", "Sand Trap", "Scion's Second Wish", "Staff of Y'kir", "Astral Phasing", "Fireblaze Obelysk", "Imperial Mechanyst", "Inner Oasis", "Orb Weaver", "Portal Guardian", "Sand Howler", "Scion's Third Wish", "Wildfire Ankh", "Windstorm Obelysk", "Entropic Decay", "Hexblade", "Mirage Master", "Wind Shrike", "Starfire Scarab", "Star's Fury", "Aymara Healer", "Dominate Will", "Oserix", "Time Maelstrom"],
  "Abyssian": ["Darkfire Sacrifice", "Abyssal Crawler", "Grasp of Agony", "Horn of the Forsaken", "Void Pulse", "Blood Siren", "Consuming Rebirth", "Daemonic Lure", "Darkspine Elemental", "Gloomchaser", "Soulshatter Pact", "Spectral Blade", "Deathfire Crescendo", "Nightsorrow Assassin", "Rite of the Undervault", "Ritual Banishing", "Shadow Reflection", "Shadow Watcher", "Soul Grimwar", "Wraithling Fury", "Wraithling Swarm", "Abyssal Juggernaut", "Bloodmoon Priestess", "Breath of the Unborn", "Dark Seed", "Deepfire Devourer", "Black Solus", "Dark Transformation", "Nether Summoning", "Reaper of the Nine Moons", "Shadowdancer", "Vorpal Reaver", "Shadow Nova", "Spectral Revenant"],
  "Magmar": ["Amplification", "Dampening Wave", "Flash Reincarnation", "Greater Fortitude", "Diretide Frenzy", "Iridium Scale", "Kujata", "Mana Burn", "Natural Selection", "Tremor", "Young Silithar", "Earth Walker", "Kinetic Equilibrium", "Phalanxar", "Primordial Gazer", "Twin Fang", "Vindicator", "Adamantite Claws", "Chrysalis Burst", "Earth Sphere", "Egg Morph", "Elucidator", "Grimrock", "Mind Steal", "Veteran Silithar", "Kolossus", "Metamorphosis", "Plasma Storm", "Spirit Harvester", "Fractal Replication", "Makantor Warbeast", "Bounded Lifeforce", "Silithar Elder", "Unstable Leviathan"],
  "Vanar": ["Flash Freeze", "Polarity", "Aspect of the Fox", "Mesmerize", "Snow Chaser", "Bonechill Barrier", "Borean Bear", "Boundless Courage", "Chromatic Cold", "Coldbiter", "Crystal Cloaker", "Crystal Wisp", "Frostfire", "Hailstone Prison", "Hearth-sister", "Mark of Solitude", "Blazing Spines", "Cryogenesis", "Fenrir Warmaster", "Glacial Elemental", "Gravity Well", "Snowpiercer", "Wolfraven", "Aspect of the Drake", "Avalanche", "Razorback", "Spirit of the Wild", "Voice of the Winds", "Winterblade", "Arctic Displacer", "Frosthorn Rhyno", "Aspect of the Mountains", "Draugar Lord", "Ancient Grove"],
  "Neutral":["Dragonlark", "Helm of Mechaz0r", "Komodo Charger", "Maw", "Planar Scout", "Prophet of the White Palm", "Swamp Entangler", "Aethermaster", "Araki Headhunter", "Azure Horn Shaman", "Bloodtear Alchemist", "Bluetip Scorpion", "Ephemeral Shroud", "Flameblood Warlock", "Ghost Lynx", "Golem Metallurgist", "Healing Mystic", "Jaxi", "Manaforger", "Piercing Mantis", "Primus Fist", "Rock Pulverizer", "Rust Crawler", "Skyrock Golem", "Vale Hunter", "Wings of Mechaz0r", "Alcuin Loremaster", "Blaze Hound", "Bloodshard Golem", "Cannon of Mechaz0r", "Chaos Elemental", "Crimson Oculus", "Crossbones", "Golem Vanquisher", "Lady Locke", "Mirkblood Devourer", "Mogwai", "Prismatic Illusionist", "Putrid Dreadflayer", "Repulsor Beast", "Saberspine Tiger", "Sarlac the Eternal", "Shield Oracle", "Silvertongue Corsair", "Songweaver", "Spelljammer", "Sun Seer", "Sword of Mechaz0r", "Sworn Avenger", "Syvrel the Exile", "Venom Toth", "Void Hunter", "Wind Runner", "Wind Stopper", "Artifact Hunter", "Black Locust", "Chassis of Mechaz0r", "Dioltas", "Emerald Rejuvenator", "Fire Spitter", "Frostbone Naga", "Hailstone Golem", "Lightbender", "Mindwarper", "Moebius", "Owlbeast Sage", "Primus Shieldmaster", "Purgatos, the Realmkeeper", "Sand Burrower", "Silhouette Tracer", "Sun Elemental", "Thorn Needler", "Twilight Sorcerer", "Young Flamewing", "Ash Mephyt", "Brightmoss Golem", "Captain Hank Hart", "Dagger Kiri", "Dancing Blades", "Fireblazer", "Firestarter", "Keeper of the Vale", "Lux Ignis", "Rogue Warden", "Sworn Avenger", "The High Hand", "Zen'rui, the Blightspawned", "Archon Spellbinder", "Deathblighter", "Eclipse", "First Sword Akrane", "Jax Truesight", "Serpenti", "Storm Aratha", "Stormmetal Golem", "Dark Nemesis", "Dragonbone Golem", "Grailmaster", "Paddo", "Pandora", "Red Synja", "Rook", "Whistling Blade", "Zurael, the Lifegiver", "Khymera"]
}

patch_links = ["[1]: https://forums.duelyst.com/t/patch-0-0-1-notes/442", "[2]: https://forums.duelyst.com/t/patch-0-0-2-notes/534", "[3]: https://forums.duelyst.com/t/patch-0-0-3-notes/552", "[4]: https://forums.duelyst.com/t/patch-0-0-4-notes/622", "[5]: https://forums.duelyst.com/t/patch-0-0-5-notes/741", "[6]: https://forums.duelyst.com/t/patch-0-0-6-notes-updated-jan-6/829", "[7]: https://forums.duelyst.com/t/patch-0-0-7-notes-updated-jan-13/902", "[8]: https://forums.duelyst.com/t/patch-0-0-8-notes-pending-release-on-1-20-12-00pm-pst/957", "[9]: https://forums.duelyst.com/t/patch-0-0-9-notes-pending-release-on-1-27-12-00pm-pst/1033", "[10]: https://forums.duelyst.com/t/patch-0-0-10-notes-pending-release-on-tue-feb-3rd-12-00pm-pst/1149", "[11]: https://forums.duelyst.com/t/patch-0-0-11-notes/1263", "[12]: https://forums.duelyst.com/t/patch-0-0-12-notes-pending-release-tue-feb-17th-12pm-pst/1361", "[13]: https://forums.duelyst.com/t/patch-0-0-13-notes-released-mon-2-23-15/1516", "[14]: https://forums.duelyst.com/t/patch-0-0-14-notes-pending-release-on-3-3-12pm-pst/1824", "[15]: https://forums.duelyst.com/t/patch-0-0-15-notes-pending-release-on-3-10-12pm-pst/2505", "[16]: https://forums.duelyst.com/t/patch-0-0-16-notes-pending-release-on-3-17-12pm-pst/3134", "[17]: https://forums.duelyst.com/t/patch-0-0-17-notes-pending-release-on-3-24-12pm-pst/3641", "[18]: https://forums.duelyst.com/t/patch-0-0-18-notes-pending-release-on-3-31-12pm-pst/4117", "[19]: https://forums.duelyst.com/t/patch-0-0-19-notes-pending-release-on-4-7-12pm-pst/4477", "[20]: https://forums.duelyst.com/t/patch-0-0-20-notes-pending-release-on-4-14-12pm-pst/4751", "[21]: https://forums.duelyst.com/t/patch-0-0-21-notes-pending-release-on-4-21-12pm-pst/5087", "[22]: https://forums.duelyst.com/t/patch-0-0-22-notes-pending-release-on-4-28-12pm-pst/5338", "[23]: https://forums.duelyst.com/t/patch-0-0-23-notes-pending-release-on-5-5-12pm-pst/5612", "[24]: https://forums.duelyst.com/t/patch-0-0-24-notes-pending-release-on-5-12-12pm-pst/5829", "[25]: https://forums.duelyst.com/t/patch-0-0-25-notes-pending-release-on-5-19-12pm-pst/6047", "[26]: https://forums.duelyst.com/t/patch-0-0-26-notes-pending-release-on-5-26-12pm-pst/6407", "[27]: https://forums.duelyst.com/t/patch-0-0-27-notes-pending-release-on-6-2-1pm-pst/7322", "[28]: https://forums.duelyst.com/t/patch-0-0-28-notes-pending-release-on-6-9-2pm-pst/8058", "[29]: https://forums.duelyst.com/t/patch-0-0-29-notes-pending-release-on-6-16-1pm-pst/8610", "[30]: https://forums.duelyst.com/t/patch-0-0-30-notes-pending-release-on-6-23-1pm-pst/8994", "[31]: https://forums.duelyst.com/t/patch-0-0-31-notes-pending-release-on-6-30-1pm-pst/9440", "[32]: https://forums.duelyst.com/t/patch-0-0-32-notes-pending-release-on-7-7-2pm-pst/10128", "[33]: https://forums.duelyst.com/t/patch-0-33-0-notes-start-of-private-beta-pending-release-on-7-14-3pm-pst/10493", "[34]: https://forums.duelyst.com/t/patch-0-34-0-notes-pending-release-on-7-21-1pm-pst/11077", "[35]: https://forums.duelyst.com/t/patch-0-35-0-notes-pending-release-on-7-28-2pm-pst/11763", "[36]: https://forums.duelyst.com/t/patch-0-36-0-notes-pending-release-on-8-4-2pm-pst/12109", "[37]: https://forums.duelyst.com/t/patch-0-37-0-notes-pending-release-on-8-11-2pm-pst/12477", "[38]: https://forums.duelyst.com/t/patch-0-38-0-notes-pending-release-on-8-18-2pm-pst/12902", "[39]: https://forums.duelyst.com/t/patch-0-39-0-notes-pending-release-on-8-25-3pm-pst/14554", "[40]: https://forums.duelyst.com/t/patch-0-40-0-notes-pending-release-9-1-3pm-pst/15408", "[41]: https://forums.duelyst.com/t/patch-0-41-0-notes-pending-release-9-8-3pm-pst/15946", "[42]: https://forums.duelyst.com/t/patch-0-42-0-notes-pending-release-9-15-1pm-pst/16480", "[43]: https://forums.duelyst.com/t/patch-0-43-0-notes-pending-release-9-22-2pm-pst/17003", "[44]: https://forums.duelyst.com/t/patch-0-44-0-notes-pending-release-9-29-3pm-pst/17317", "[45]: https://forums.duelyst.com/t/duelyst-beta-v0-45-0-end-of-september-patch/17397", "[46]: https://forums.duelyst.com/t/duelyst-beta-0-46-0-pending-release-10-6-2pm-pst/17580", "[47]: https://forums.duelyst.com/t/duelyst-beta-0-47-0-pending-release-10-13-2pm-pst/17829", "[48]: https://forums.duelyst.com/t/duelyst-beta-0-48-0-pending-release-10-20-4pm-pst/19548", "[49]: https://forums.duelyst.com/t/duelyst-beta-0-49-0-pending-release-10-27-4pm-pst/20188", "[50]: https://forums.duelyst.com/t/duelyst-beta-0-50-0-pending-release-11-3-10pm-pst/20553", "[51]: https://forums.duelyst.com/t/duelyst-beta-0-51-0-pending-release-11-10-5pm-pst/21296", "[52]: https://forums.duelyst.com/t/duelyst-beta-0-52-0-pending-release-11-19-2pm-pst/21703", "[53]: https://forums.duelyst.com/t/duelyst-beta-0-53-0-end-of-november-patch/22367", "[54]: https://forums.duelyst.com/t/duelyst-beta-0-54-0-pending-release-12-15-2-30pm-pst/23148", "[55]: https://forums.duelyst.com/t/duelyst-beta-0-55-0-end-of-december-patch/24353", "[56]: https://forums.duelyst.com/t/duelyst-beta-0-56-0-pending-release-1-14-afternoon-pst/25510", "[57]: https://forums.duelyst.com/t/duelyst-beta-0-57-0-pending-release-1-29-morning-pst/27005"]

patches = ["[0.0.1][1]:", "[0.0.2][2]:", "[0.0.3][3]:", "[0.0.4][4]:", "[0.0.5][5]:", "[0.0.6][6]:", "[0.0.7][7]:", "[0.0.8][8]:", "[0.0.9][9]:", "[0.0.10][10]:", "[0.0.11][11]:", "[0.0.12][12]:", "[0.0.13][13]:", "[0.0.14][14]:", "[0.0.15][15]:", "[0.0.16][16]:", "[0.0.17][17]:", "[0.0.18][18]:", "[0.0.19][19]:", "[0.0.20][20]:", "[0.0.21][21]:", "[0.0.22][22]:", "[0.0.23][23]:", "[0.0.24][24]:", "[0.0.25][25]:", "[0.0.26][26]:", "[0.0.27][27]:", "[0.0.28][28]:", "[0.0.29][29]:", "[0.0.30][30]:", "[0.0.31][31]:", "[0.0.32][32]:", "[0.33.0][33]:", "[0.34.0][34]:", "[0.35.0][35]:", "[0.36.0][36]:", "[0.37.0][37]:", "[0.38.0][38]:", "[0.39.0][39]:", "[0.40.0][40]:", "[0.41.0][41]:", "[0.42.0][42]:", "[0.43.0][43]:", "[0.44.0][44]:", "[0.45.0][45]:", "[0.46.0][46]:", "[0.47.0][47]:", "[0.48.0][48]:", "[0.49.0][49]:", "[0.50.0][50]:", "[0.51.0][51]:", "[0.52.0][52]:", "[0.53.0][53]:", "[0.54.0][54]:", "[0.55.0][55]:", "[0.56.0][56]:", "[0.57.0][57]:"]

patches_string = ""
for patch in patches:
  patches_string += "**{}**\n".format(patch)

for faction in card_names:
  with open("{}.txt".format(faction), "w") as fout:
    fout.write("<details><summary>**{}**</summary>\n\n".format(faction))
    for card in card_names[faction]:
      fout.write("<details><summary>**{}**</summary>\n{}</details>\n\n".format(card, patches_string))
    fout.write("</details>\n")
  
    fout.write("\n\n\n")
    for patch_link in patch_links:
      fout.write(patch_link + "\n")
      
      
