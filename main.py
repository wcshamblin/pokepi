#!/usr/bin/python3
import requests
import sys
import urllib.request
pokemons=['bulbasaur', 'ivysaur', 'venusaur', 'charmander', 'charmeleon', 'charizard', 'squirtle', 'wartortle', 'blastoise', 'caterpie', 'metapod', 'butterfree', 'weedle', 'kakuna', 'beedrill', 'pidgey', 'pidgeotto', 'pidgeot', 'rattata', 'raticate', 'spearow', 'fearow', 'ekans', 'arbok', 'pikachu', 'raichu', 'sandshrew', 'sandslash', 'nidoran-f', 'nidorina', 'nidoqueen', 'nidoran-m', 'nidorino', 'nidoking', 'clefairy', 'clefable', 'vulpix', 'ninetales', 'jigglypuff', 'wigglytuff', 'zubat', 'golbat', 'oddish', 'gloom', 'vileplume', 'paras', 'parasect', 'venonat', 'venomoth', 'diglett', 'dugtrio', 'meowth', 'persian', 'psyduck', 'golduck', 'mankey', 'primeape', 'growlithe', 'arcanine', 'poliwag', 'poliwhirl', 'poliwrath', 'abra', 'kadabra', 'alakazam', 'machop', 'machoke', 'machamp', 'bellsprout', 'weepinbell', 'victreebel', 'tentacool', 'tentacruel', 'geodude', 'graveler', 'golem', 'ponyta', 'rapidash', 'slowpoke', 'slowbro', 'magnemite', 'magneton', 'farfetchd', 'doduo', 'dodrio', 'seel', 'dewgong', 'grimer', 'muk', 'shellder', 'cloyster', 'gastly', 'haunter', 'gengar', 'onix', 'drowzee', 'hypno', 'krabby', 'kingler', 'voltorb', 'electrode', 'exeggcute', 'exeggutor', 'cubone', 'marowak', 'hitmonlee', 'hitmonchan', 'lickitung', 'koffing', 'weezing', 'rhyhorn', 'rhydon', 'chansey', 'tangela', 'kangaskhan', 'horsea', 'seadra', 'goldeen', 'seaking', 'staryu', 'starmie', 'mr-mime', 'scyther', 'jynx', 'electabuzz', 'magmar', 'pinsir', 'tauros', 'magikarp', 'gyarados', 'lapras', 'ditto', 'eevee', 'vaporeon', 'jolteon', 'flareon', 'porygon', 'omanyte', 'omastar', 'kabuto', 'kabutops', 'aerodactyl', 'snorlax', 'articuno', 'zapdos', 'moltres', 'dratini', 'dragonair', 'dragonite', 'mewtwo', 'mew', 'chikorita', 'bayleef', 'meganium', 'cyndaquil', 'quilava', 'typhlosion', 'totodile', 'croconaw', 'feraligatr', 'sentret', 'furret', 'hoothoot', 'noctowl', 'ledyba', 'ledian', 'spinarak', 'ariados', 'crobat', 'chinchou', 'lanturn', 'pichu', 'cleffa', 'igglybuff', 'togepi', 'togetic', 'natu', 'xatu', 'mareep', 'flaaffy', 'ampharos', 'bellossom', 'marill', 'azumarill', 'sudowoodo', 'politoed', 'hoppip', 'skiploom', 'jumpluff', 'aipom', 'sunkern', 'sunflora', 'yanma', 'wooper', 'quagsire', 'espeon', 'umbreon', 'murkrow', 'slowking', 'misdreavus', 'unown', 'wobbuffet', 'girafarig', 'pineco', 'forretress', 'dunsparce', 'gligar', 'steelix', 'snubbull', 'granbull', 'qwilfish', 'scizor', 'shuckle', 'heracross', 'sneasel', 'teddiursa', 'ursaring', 'slugma', 'magcargo', 'swinub', 'piloswine', 'corsola', 'remoraid', 'octillery', 'delibird', 'mantine', 'skarmory', 'houndour', 'houndoom', 'kingdra', 'phanpy', 'donphan', 'porygon2', 'stantler', 'smeargle', 'tyrogue', 'hitmontop', 'smoochum', 'elekid', 'magby', 'miltank', 'blissey', 'raikou', 'entei', 'suicune', 'larvitar', 'pupitar', 'tyranitar', 'lugia', 'ho-oh', 'celebi', 'treecko', 'grovyle', 'sceptile', 'torchic', 'combusken', 'blaziken', 'mudkip', 'marshtomp', 'swampert', 'poochyena', 'mightyena', 'zigzagoon', 'linoone', 'wurmple', 'silcoon', 'beautifly', 'cascoon', 'dustox', 'lotad', 'lombre', 'ludicolo', 'seedot', 'nuzleaf', 'shiftry', 'taillow', 'swellow', 'wingull', 'pelipper', 'ralts', 'kirlia', 'gardevoir', 'surskit', 'masquerain', 'shroomish', 'breloom', 'slakoth', 'vigoroth', 'slaking', 'nincada', 'ninjask', 'shedinja', 'whismur', 'loudred', 'exploud', 'makuhita', 'hariyama', 'azurill', 'nosepass', 'skitty', 'delcatty', 'sableye', 'mawile', 'aron', 'lairon', 'aggron', 'meditite', 'medicham', 'electrike', 'manectric', 'plusle', 'minun', 'volbeat', 'illumise', 'roselia', 'gulpin', 'swalot', 'carvanha', 'sharpedo', 'wailmer', 'wailord', 'numel', 'camerupt', 'torkoal', 'spoink', 'grumpig', 'spinda', 'trapinch', 'vibrava', 'flygon', 'cacnea', 'cacturne', 'swablu', 'altaria', 'zangoose', 'seviper', 'lunatone', 'solrock', 'barboach', 'whiscash', 'corphish', 'crawdaunt', 'baltoy', 'claydol', 'lileep', 'cradily', 'anorith', 'armaldo', 'feebas', 'milotic', 'castform', 'kecleon', 'shuppet', 'banette', 'duskull', 'dusclops', 'tropius', 'chimecho', 'absol', 'wynaut', 'snorunt', 'glalie', 'spheal', 'sealeo', 'walrein', 'clamperl', 'huntail', 'gorebyss', 'relicanth', 'luvdisc', 'bagon', 'shelgon', 'salamence', 'beldum', 'metang', 'metagross', 'regirock', 'regice', 'registeel', 'latias', 'latios', 'kyogre', 'groudon', 'rayquaza', 'jirachi', 'deoxys-normal', 'turtwig', 'grotle', 'torterra', 'chimchar', 'monferno', 'infernape', 'piplup', 'prinplup', 'empoleon', 'starly', 'staravia', 'staraptor', 'bidoof', 'bibarel', 'kricketot', 'kricketune', 'shinx', 'luxio', 'luxray', 'budew', 'roserade', 'cranidos', 'rampardos', 'shieldon', 'bastiodon', 'burmy', 'wormadam-plant', 'mothim', 'combee', 'vespiquen', 'pachirisu', 'buizel', 'floatzel', 'cherubi', 'cherrim', 'shellos', 'gastrodon', 'ambipom', 'drifloon', 'drifblim', 'buneary', 'lopunny', 'mismagius', 'honchkrow', 'glameow', 'purugly', 'chingling', 'stunky', 'skuntank', 'bronzor', 'bronzong', 'bonsly', 'mime-jr', 'happiny', 'chatot', 'spiritomb', 'gible', 'gabite', 'garchomp', 'munchlax', 'riolu', 'lucario', 'hippopotas', 'hippowdon', 'skorupi', 'drapion', 'croagunk', 'toxicroak', 'carnivine', 'finneon', 'lumineon', 'mantyke', 'snover', 'abomasnow', 'weavile', 'magnezone', 'lickilicky', 'rhyperior', 'tangrowth', 'electivire', 'magmortar', 'togekiss', 'yanmega', 'leafeon', 'glaceon', 'gliscor', 'mamoswine', 'porygon-z', 'gallade', 'probopass', 'dusknoir', 'froslass', 'rotom', 'uxie', 'mesprit', 'azelf', 'dialga', 'palkia', 'heatran', 'regigigas', 'giratina-altered', 'cresselia', 'phione', 'manaphy', 'darkrai', 'shaymin-land', 'arceus', 'victini', 'snivy', 'servine', 'serperior', 'tepig', 'pignite', 'emboar', 'oshawott', 'dewott', 'samurott', 'patrat', 'watchog', 'lillipup', 'herdier', 'stoutland', 'purrloin', 'liepard', 'pansage', 'simisage', 'pansear', 'simisear', 'panpour', 'simipour', 'munna', 'musharna', 'pidove', 'tranquill', 'unfezant', 'blitzle', 'zebstrika', 'roggenrola', 'boldore', 'gigalith', 'woobat', 'swoobat', 'drilbur', 'excadrill', 'audino', 'timburr', 'gurdurr', 'conkeldurr', 'tympole', 'palpitoad', 'seismitoad', 'throh', 'sawk', 'sewaddle', 'swadloon', 'leavanny', 'venipede', 'whirlipede', 'scolipede', 'cottonee', 'whimsicott', 'petilil', 'lilligant', 'basculin-red-striped', 'sandile', 'krokorok', 'krookodile', 'darumaka', 'darmanitan-standard', 'maractus', 'dwebble', 'crustle', 'scraggy', 'scrafty', 'sigilyph', 'yamask', 'cofagrigus', 'tirtouga', 'carracosta', 'archen', 'archeops', 'trubbish', 'garbodor', 'zorua', 'zoroark', 'minccino', 'cinccino', 'gothita', 'gothorita', 'gothitelle', 'solosis', 'duosion', 'reuniclus', 'ducklett', 'swanna', 'vanillite', 'vanillish', 'vanilluxe', 'deerling', 'sawsbuck', 'emolga', 'karrablast', 'escavalier', 'foongus', 'amoonguss', 'frillish', 'jellicent', 'alomomola', 'joltik', 'galvantula', 'ferroseed', 'ferrothorn', 'klink', 'klang', 'klinklang', 'tynamo', 'eelektrik', 'eelektross', 'elgyem', 'beheeyem', 'litwick', 'lampent', 'chandelure', 'axew', 'fraxure', 'haxorus', 'cubchoo', 'beartic', 'cryogonal', 'shelmet', 'accelgor', 'stunfisk', 'mienfoo', 'mienshao', 'druddigon', 'golett', 'golurk', 'pawniard', 'bisharp', 'bouffalant', 'rufflet', 'braviary', 'vullaby', 'mandibuzz', 'heatmor', 'durant', 'deino', 'zweilous', 'hydreigon', 'larvesta', 'volcarona', 'cobalion', 'terrakion', 'virizion', 'tornadus-incarnate', 'thundurus-incarnate', 'reshiram', 'zekrom', 'landorus-incarnate', 'kyurem', 'keldeo-ordinary', 'meloetta-aria', 'genesect', 'chespin', 'quilladin', 'chesnaught', 'fennekin', 'braixen', 'delphox', 'froakie', 'frogadier', 'greninja', 'bunnelby', 'diggersby', 'fletchling', 'fletchinder', 'talonflame', 'scatterbug', 'spewpa', 'vivillon', 'litleo', 'pyroar', 'flabebe', 'floette', 'florges', 'skiddo', 'gogoat', 'pancham', 'pangoro', 'furfrou', 'espurr', 'meowstic-male', 'honedge', 'doublade', 'aegislash-shield', 'spritzee', 'aromatisse', 'swirlix', 'slurpuff', 'inkay', 'malamar', 'binacle', 'barbaracle', 'skrelp', 'dragalge', 'clauncher', 'clawitzer', 'helioptile', 'heliolisk', 'tyrunt', 'tyrantrum', 'amaura', 'aurorus', 'sylveon', 'hawlucha', 'dedenne', 'carbink', 'goomy', 'sliggoo', 'goodra', 'klefki', 'phantump', 'trevenant', 'pumpkaboo-average', 'gourgeist-average', 'bergmite', 'avalugg', 'noibat', 'noivern', 'xerneas', 'yveltal', 'zygarde', 'diancie', 'hoopa', 'volcanion', 'rowlet', 'dartrix', 'decidueye', 'litten', 'torracat', 'incineroar', 'popplio', 'brionne', 'primarina', 'pikipek', 'trumbeak', 'toucannon', 'yungoos', 'gumshoos', 'grubbin', 'charjabug', 'vikavolt', 'crabrawler', 'crabominable', 'oricorio-baile', 'cutiefly', 'ribombee', 'rockruff', 'lycanroc-midday', 'wishiwashi-solo', 'mareanie', 'toxapex', 'mudbray', 'mudsdale', 'dewpider', 'araquanid', 'fomantis', 'lurantis', 'morelull', 'shiinotic', 'salandit', 'salazzle', 'stufful', 'bewear', 'bounsweet', 'steenee', 'tsareena', 'comfey', 'oranguru', 'passimian', 'wimpod', 'golisopod', 'sandygast', 'palossand', 'pyukumuku', 'type-null', 'silvally', 'minior-red-meteor', 'komala', 'turtonator', 'togedemaru', 'mimikyu-disguised', 'bruxish', 'drampa', 'dhelmise', 'jangmo-o', 'hakamo-o', 'kommo-o', 'tapu-koko', 'tapu-lele', 'tapu-bulu', 'tapu-fini', 'cosmog', 'cosmoem', 'solgaleo', 'lunala', 'nihilego', 'buzzwole', 'pheromosa', 'xurkitree', 'celesteela', 'kartana', 'guzzlord', 'necrozma', 'magearna', 'marshadow', 'poipole', 'naganadel', 'stakataka', 'blacephalon', 'zeraora', 'deoxys-attack', 'deoxys-defense', 'deoxys-speed', 'wormadam-sandy', 'wormadam-trash', 'shaymin-sky', 'giratina-origin', 'rotom-heat', 'rotom-wash', 'rotom-frost', 'rotom-fan', 'rotom-mow', 'castform-sunny', 'castform-rainy', 'castform-snowy', 'basculin-blue-striped', 'darmanitan-zen', 'meloetta-pirouette', 'tornadus-therian', 'thundurus-therian', 'landorus-therian', 'kyurem-black', 'kyurem-white', 'keldeo-resolute', 'meowstic-female', 'aegislash-blade', 'pumpkaboo-small', 'pumpkaboo-large', 'pumpkaboo-super', 'gourgeist-small', 'gourgeist-large', 'gourgeist-super', 'venusaur-mega', 'charizard-mega-x', 'charizard-mega-y', 'blastoise-mega', 'alakazam-mega', 'gengar-mega', 'kangaskhan-mega', 'pinsir-mega', 'gyarados-mega', 'aerodactyl-mega', 'mewtwo-mega-x', 'mewtwo-mega-y', 'ampharos-mega', 'scizor-mega', 'heracross-mega', 'houndoom-mega', 'tyranitar-mega', 'blaziken-mega', 'gardevoir-mega', 'mawile-mega', 'aggron-mega', 'medicham-mega', 'manectric-mega', 'banette-mega', 'absol-mega', 'garchomp-mega', 'lucario-mega', 'abomasnow-mega', 'floette-eternal', 'latias-mega', 'latios-mega', 'swampert-mega', 'sceptile-mega', 'sableye-mega', 'altaria-mega', 'gallade-mega', 'audino-mega', 'sharpedo-mega', 'slowbro-mega', 'steelix-mega', 'pidgeot-mega', 'glalie-mega', 'diancie-mega', 'metagross-mega', 'kyogre-primal', 'groudon-primal', 'rayquaza-mega', 'pikachu-rock-star', 'pikachu-belle', 'pikachu-pop-star', 'pikachu-phd', 'pikachu-libre', 'pikachu-cosplay', 'hoopa-unbound', 'camerupt-mega', 'lopunny-mega', 'salamence-mega', 'beedrill-mega', 'rattata-alola', 'raticate-alola', 'raticate-totem-alola', 'pikachu-original-cap', 'pikachu-hoenn-cap', 'pikachu-sinnoh-cap', 'pikachu-unova-cap', 'pikachu-kalos-cap', 'pikachu-alola-cap', 'raichu-alola', 'sandshrew-alola', 'sandslash-alola', 'vulpix-alola', 'ninetales-alola', 'diglett-alola', 'dugtrio-alola', 'meowth-alola', 'persian-alola', 'geodude-alola', 'graveler-alola', 'golem-alola', 'grimer-alola', 'muk-alola', 'exeggutor-alola', 'marowak-alola', 'greninja-battle-bond', 'greninja-ash', 'zygarde-10', 'zygarde-50', 'zygarde-complete', 'gumshoos-totem', 'vikavolt-totem', 'oricorio-pom-pom', 'oricorio-pau', 'oricorio-sensu', 'lycanroc-midnight', 'wishiwashi-school', 'lurantis-totem', 'salazzle-totem', 'minior-orange-meteor', 'minior-yellow-meteor', 'minior-green-meteor', 'minior-blue-meteor', 'minior-indigo-meteor', 'minior-violet-meteor', 'minior-red', 'minior-orange', 'minior-yellow', 'minior-green', 'minior-blue', 'minior-indigo', 'minior-violet', 'mimikyu-busted', 'mimikyu-totem-disguised', 'mimikyu-totem-busted', 'kommo-o-totem', 'magearna-original', 'pikachu-partner-cap', 'marowak-totem', 'ribombee-totem', 'rockruff-own-tempo', 'lycanroc-dusk', 'araquanid-totem', 'togedemaru-totem'] #ALL THE POKEMONS
psbl={}
def leven_dist(str1, str2):
    m = len(str1)
    n = len(str2)
    lensum = float(m + n)
    d = []
    for i in range(m+1):
        d.append([i])
    del d[0][0]
    for j in range(n+1):
        d[0].append(j)
    for j in range(1,n+1):
        for i in range(1,m+1):
            if str1[i-1] == str2[j-1]:
                d[i].insert(j,d[i-1][j-1])
            else:
                minimum = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+2)
                d[i].insert(j, minimum)
    ldist = d[-1][-1]
    return ldist

try:
	requests.head("https://pokeapi.co/api/v2/pokemon/bulbasaur")
except:
	print("No route to pokeapi, check internet connection and try again.")
	exit()

if len(sys.argv)==2:
	if sys.argv[1] == "--help":
		print("""
Usage: pokepi [OPTION] [INPUT]

--pokemon <pokemon name>        Print pokedex entry for a pokemon
--move <move name>              Print pokedex entry for a move. Make sure to use a - instead of a space when using this option with a multi-word move.""")
		exit()
if len(sys.argv)==3:
	cmd_opt=True
else:
	if len(sys.argv)==2:
		print("Too little command line arguments! Use --help to display a help message. Exiting...")
		exit()
	elif len(sys.argv)>3:
		print("Too many command line arguments! If you're trying to call a multi-word move, use a - instead of a space")
		exit()
	cmd_opt=False
if cmd_opt==True:
	if str(sys.argv[1]).lower() == "--moves" or str(sys.argv[1]).lower() == "--move":
		ri="move"
	elif str(sys.argv[1]).lower() == "--pokemon":
		ri="pokemon"
	else:
		print("Incorrect command line arguments! Try the --help flag.")
		exit()
else:
	ri=str(input("Move or pokemon? --> ")).lower()
if ri=="m" or ri=="move" or ri=="moves":
	if cmd_opt==True:
		move=str(sys.argv[2]).lower()
	else:
		move=str(input("Move --> ")).lower().replace(" ", "-")
	try:
		m=requests.get("https://pokeapi.co/api/v2/move/"+move+"/")
		m=m.json()
	except:
		print("Not a valid move name! Maybe you mispelled?")
		exit()
	desc=str(m['effect_entries'][0]['effect']).replace("$effect_chance", str(m['effect_chance']))
	category=str(m['damage_class']['name']).capitalize()
	accuracy=str(m['accuracy']).capitalize()
	power=str(m['power'])
	mtype=str(m['type']['name']).capitalize()
	priority=str(m['priority'])
	pp=str(m['pp'])
	print(desc,"\n")
	print("Category:", category)
	print("Type:", mtype)
	print("Accuracy:", accuracy)
	print("Base power:", power)
	print("PP:", pp)
	print("Priority:", priority)
	exit()
else:
	if ri=="p" or ri=="poke" or ri=="pokemon" and cmd_opt==False:
		pokemon=str(input("Pokemon --> ")).lower()
	elif cmd_opt==True:
		pokemon=str(sys.argv[2]).lower()
	else:
		print("Not a move or a pokemon, exiting...")
		exit()
if pokemon=="octet":
	print("""Often found in global chat, this pokemon is almost always helping out fellow players.
HP:  60  [====================>                                                                      ] 
Atk: 30  [==========>                                                                                ] 
Def: 50  [================>                                                                          ] 
SpA: 270 [==========================================================================================>] 
SpD: 70  [=======================>                                                                   ] 
Spd: 120 [========================================>                                                  ]
BST: 600 (Pseudo-ledgendary)
Abilities: Speed Boost (Hidden), Mute Mic, Magic Bounce (aka no u)
Catch rate: 0 (0%) Cute masterball.
Base Happiness: Wouldn't you like to know
Egg groups: N/A
""")
	exit()
try:
	r=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon+"/")
	r=r.json()
	pid=r['id']
	spurl=str(r['species']['url'])
	r2=requests.get(spurl)
	r2=r2.json()
except:
	for p in pokemons:
		ld=leven_dist(pokemon,p)
		if ld < 8:
			psbl[p]=ld
	if len(psbl)==0:
			print("Not a valid pokemon name! Maybe you misspelled?")
	else:
		print("Not a valid pokemon name! Maybe you meant", str(min(psbl, key=psbl.get)).capitalize() + "?")
	exit()
types=[]
for i in range(0,len(r['types'])):
	types.append(str(r['types'][i]['type']['name']).capitalize())
stats=[]
for i in range(0,len(r['stats'])):
	stats.append(r['stats'][i]['base_stat'])
stats.reverse()
def stat_vis(s,m):
	return("["+"="*int((s/3))+">"+" "*int(m/3-int((s/3)))+"]")
mx=max(stats)
able=[]
for i in r["abilities"]:
	if i["is_hidden"]==True:
		able.append(i["ability"]["name"].capitalize()+" (Hidden)")
	else:
		able.append(i["ability"]["name"].capitalize())
for i in r2['flavor_text_entries']:
	if i['language']['name'] == "en":
		if r2['evolves_from_species'] != None:
			flavor=str(i['flavor_text'].replace('\n'," ")) + " It evolves from "+ str(r2['evolves_from_species']['name'].capitalize()+".")
		else:
			flavor=i['flavor_text'].replace('\n'," ")
		break
egg_groups=[]
for i in r2['egg_groups']:
	egg_groups.append(i['name'].capitalize())
catch_rate=int(r2["capture_rate"])
base_happiness=int(r2['base_happiness'])
print(flavor)
print(pokemon.capitalize()+" #"+str(pid)+" ["+str(', '.join(types))+"]")
print("HP: ", str(stats[0])+" "*(int(len(str(mx)))-int(len(str(stats[0])))),stat_vis(stats[0], mx),"\n"+"Atk:", str(stats[1])+" "*(int(len(str(mx)))-int(len(str(stats[1])))),stat_vis(stats[1], mx),"\n"+"Def:", str(stats[2])+" "*(int(len(str(mx)))-int(len(str(stats[2])))),stat_vis(stats[2], mx),"\n"+"SpA:", str(stats[3])+" "*(int(len(str(mx)))-int(len(str(stats[3])))),stat_vis(stats[3], mx),"\n"+"SpD:", str(stats[4])+" "*(int(len(str(mx)))-int(len(str(stats[4])))),stat_vis(stats[4], mx),"\n"+"Spd:", str(stats[5])+" "*(int(len(str(mx)))-int(len(str(stats[5])))),stat_vis(stats[5], mx))
if sum(stats)==600:
	print("BST: ", sum(stats), "(Pseudo-ledgendary by stats)")
elif sum(stats)>600 and pokemon!="slaking":
	print("BST:", sum(stats), "(Ledgendary by stats)")
else:
	print("BST:", sum(stats))
print("Abilities:", ", ".join(able))
print("Catch rate: ",catch_rate, "("+str(round((catch_rate/765.0)*100, 1))+"%)")
print("Base happiness: ", base_happiness, "("+str(int((base_happiness/255)*100))+"%)")
print("Egg groups: ", ", ".join(egg_groups))