#!/usr/bin/python3
import requests
import sys
import urllib.request
import random
def get_all(v):
	r=requests.get("https://pokeapi.co/api/v2/"+v+"/")
	r=r.json()
	items=[]
	for item in r['results']:
		items.append(str(item['name']))
	return(items)
try:
	pokemons=get_all("pokemon")
	items=get_all("item")
	berries=get_all("berry")
	moves=get_all("move")
except:
	print("No route to pokeapi, check internet connection and try again.")
	exit()
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

if len(sys.argv)==2:
	if sys.argv[1] == "--help":
		print("""
Usage: pokepi [OPTION] [INPUT]

--pokemon <pokemon name>        Print pokedex entry for a pokemon. Make sure to use a - in places of spaces when using this with a name containing a space.
--move <move name>              Print pokedex entry for a move. Make sure to use a - in places of spaces when using this with a name containing a space.
--item <item name>              Print pokedex entry for an item. Make sure to use - in places of spaces when using this with a name containing a space.
--berry <berry name> Print pokedex entry for an berry.""")
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
	if str(sys.argv[1]).lower() == "--items" or str(sys.argv[1]).lower() == "--item":
		ri="item"
	if str(sys.argv[1]).lower() == "--moves" or str(sys.argv[1]).lower() == "--move":
		ri="move"
	if str(sys.argv[1]).lower() == "--berry":
		ri="berry"

	elif str(sys.argv[1]).lower() == "--pokemon":
		ri="pokemon"
	else:
		print("Incorrect command line arguments! Try the --help flag.")
		exit()
else:
	ri=str(input("Move, pokemon, item, or berry? --> ")).lower()
if ri=="i" or ri=="item" or ri=="items":
	if cmd_opt==True:
		item=str(sys.argv[2]).lower()
	else:
		item=str(input("Item --> ")).lower().replace(" ", "-")
	try:
		i=requests.get("https://pokeapi.co/api/v2/item/"+item+"/")
		i=i.json()
	except:
		for ii in items:
			ld=leven_dist(item, ii)
			if ld < 8:
				psbl[ii]=ld
		if len(psbl)==0:
				print("Not a valid item name! Maybe you misspelled?")
				exit()
		else:
			print("Not a valid item name! Assuming you meant", str(min(psbl, key=psbl.get)).replace("-", " ").capitalize() + "...")
			item=str(min(psbl, key=psbl.get))
			i=requests.get("https://pokeapi.co/api/v2/item/"+item+"/")
			i=i.json()
	for e in i['effect_entries']:
		if e['language']['name'] == "en":
			if i['category']['name']=="all-machines":
				effect=e['short_effect']
			else:
				effect=e['effect']
	fling_effect=i['fling_effect']
	fling_power=i['fling_power']
	held_by=[]
	if len(i['held_by_pokemon']) > 0:
		for h in i['held_by_pokemon']:
			held_by.append(h['pokemon']['name'].capitalize())
	print(effect)
	if fling_power != None:
		print("Fling power: ", fling_power)
		if fling_effect != None:
			print("Fling effect:", fling_effect)
		else:
			print("No fling effect")
	else:
		print("Not flingable.")
	if len(held_by) > 0:
		print("Held by: ", ', '.join(held_by))
	else:
		print("Not held by any wild pokemon")
	exit()
if ri=="b" or ri=="berry" or ri=="berrys" or ri=="berries":
	if cmd_opt==True:
		berry=str(sys.argv[2]).lower()
	else:
		berry=str(input("Berry --> ")).lower().replace(" ", "-")
	if berry=="":
		exit()
	try:
		b=requests.get("https://pokeapi.co/api/v2/berry/"+berry+"/")
		b=b.json()
	except:
		for bi in berries:
			ld=leven_dist(berry, bi)
			if ld < 5:
				psbl[bi]=ld
		if len(psbl)==0:
				print("Not a valid berry name! Maybe you misspelled?")
				exit()
		else:
			print("Not a valid berry name! Assuming you meant", str(min(psbl, key=psbl.get)).replace("-", " ").capitalize() + "...")
			berry=str(min(psbl, key=psbl.get))
			b=requests.get("https://pokeapi.co/api/v2/berry/"+berry+"/")
			b=b.json()
	firmness=b['firmness']['name']
	flavors={}
	for f in b['flavors']:
		flavors[str(f['flavor']['name'].capitalize())+":"]=f['potency']
	growth=b['growth_time']
	harvest=b['max_harvest']
	size=b['size']
	smooth=b['smoothness']
	soil=b['soil_dryness']
	print("Berry flavors:")
	print("\n".join("{}\t{}".format(k, v) for k, v in flavors.items()),"\n")
	print("Cycle time:", growth)
	print("Growth cycle: Planted -> Sprouted -> Taller -> Flowering -> Berries. Total time: "+str(int(growth)*4)+"h")
	print("Max harvest:", harvest, "berries")
	print("Soil dryness:", soil, "\n")
	print("Smoothness:", smooth)
	print("Firmness:", firmness.replace("-", " ").capitalize())
	print("Size:", str(size)+" millimeters ("+str(round(float(size)/25.4, 2)), "inches)")
	exit()
if ri=="m" or ri=="move" or ri=="moves":
	if cmd_opt==True:
		move=str(sys.argv[2]).lower()
	else:
		move=str(input("Move --> ")).lower().replace(" ", "-")
	if move=="":
		exit()
	try:
		m=requests.get("https://pokeapi.co/api/v2/move/"+move+"/")
		m=m.json()
	except:
		for mi in moves:
			ld=leven_dist(move, mi)
			if ld < 8:
				psbl[mi]=ld
		if len(psbl)==0:
				print("Not a valid move name! Maybe you misspelled?")
				exit()
		else:
			print("Not a valid move name! Assuming you meant", str(min(psbl, key=psbl.get)).replace("-", " ").capitalize() + "...")
			move=str(min(psbl, key=psbl.get))
			m=requests.get("https://pokeapi.co/api/v2/move/"+move+"/")
			m=m.json()
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
	if int(priority) < 0:
		print("Priority:", str(priority))
	elif int(priority) > 0:
		print("Priority:", "+"+str(priority))
	else:
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
	if pokemon=="":
		exit()
	if pokemon=="random":
		pokemon=random.choice(pokemons)
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
			exit()
	else:
		print("Not a valid pokemon name! Assuming you meant", str(min(psbl, key=psbl.get)).replace("-", " ").capitalize() + "...")
		pokemon=str(min(psbl, key=psbl.get))
		r=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon+"/")
		r=r.json()
		pid=r['id']
		spurl=str(r['species']['url'])
		r2=requests.get(spurl)
		r2=r2.json()
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
gnum=(float(r2['gender_rate'])/8.0)*100.0
for i in r2['egg_groups']:
	egg_groups.append(i['name'].capitalize())
catch_rate=int(r2["capture_rate"])
base_happiness=int(r2['base_happiness'])
print(pokemon.capitalize()+" #"+str(pid)+" ["+str(', '.join(types))+"]")
print(flavor)
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
print("Gender ratio: ", str(100.0-gnum)+"% Male, ", str(gnum)+"% female")