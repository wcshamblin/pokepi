#!/usr/bin/python3
import requests
import sys
import urllib.request
import random
import queue
import threading #fuck yea optimizing
def get_one(q, v):
	try:
		r=requests.get("https://pokeapi.co/api/v2/"+v+"/")
	except:
		q.put("rip")
		exit()
	r=r.json()
	q.put(r)
def get_all(q, v):
	try:
		r=requests.get("https://pokeapi.co/api/v2/"+v+"/")
	except:
		q.put("rip")
		exit()
	r=r.json()
	items=[]
	for item in r['results']:
		items.append(str(item['name']))
	q.put(items)
threads=[]
things_l=["pokemon", "item", "berry", "move"]
q=queue.Queue()
for u in things_l:
	t = threading.Thread(target=get_all, args=(q, u))
	threads.append(t)
	t.start()
for i in range(0,4):
	buf=q.get()
	if buf=="rip":
		print("No route to pokeapi, check internet connection and try again.")
		exit()
	if "leppa" in buf:
		berries=buf
	if "master-ball" in buf:
		items=buf
	if "bulbasaur" in buf:
		pokemons=buf
	if "tackle" in buf:
		moves=buf
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
inp=""
if len(sys.argv)==2:
	if sys.argv[1] == "--help":
		print("""
Usage: pokepi [INPUT]

<name>        Print pokedex entry for an item, move, pokemon, or berry. Make sure to use a - in places of spaces when using this with a name containing a space.""")
		exit()
if len(sys.argv)==2:
	cmd_opt=True
else:
	if len(sys.argv)>2:
		print("Too many command line arguments! If you're trying to call a multi-word name, use a - instead of a space")
		exit()
	cmd_opt=False
if cmd_opt==True:
	inp=str(sys.argv[1]).lower()
else:
	while inp=="":
		inp=str(input("Pokedex --> ")).lower().replace(" ", "-")
psbl={}
if inp not in berries+items+pokemons+moves:
	for ii in berries+items+pokemons+moves:
		ld=leven_dist(inp, ii)
		if len(inp)<=5:
			if ld < 5:
				psbl[ii]=ld
		else:
			if ld < 8:
				psbl[ii]=ld

	if len(psbl)==0:
			print("Not a valid name! Maybe you misspelled?")
			exit()
	else:
		inp=str(min(psbl, key=psbl.get))
		print("Not a valid name, assuming you meant", inp.capitalize().replace("-", " "))
if inp in berries:
	ri="berry"
if inp in items:
	ri="item"
if inp in pokemons:
	ri="pokemon"
if inp in moves:
	ri="move"
if "-berry" in inp:
	ri="berry"
	inp=inp.replace("-berry", "")
if ri=="item":
	item=inp
	i=requests.get("https://pokeapi.co/api/v2/item/"+item+"/").json()
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
	print(effect.replace("\n:", ":"))
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
		print("Not held by any wild pokemon.")
	exit()
if ri=="berry":
	berry=inp
	b=requests.get("https://pokeapi.co/api/v2/berry/"+berry+"/").json()
	effect=str(requests.get(b["item"]["url"]).json()["effect_entries"][0]["effect"].replace("\n:", ":"))
	firmness=b['firmness']['name']
	flavors={}
	for f in b['flavors']:
		flavors[str(f['flavor']['name'].capitalize())+":"]=f['potency']
	growth=b['growth_time']
	harvest=b['max_harvest']
	size=b['size']
	smooth=b['smoothness']
	soil=b['soil_dryness']
	print("Effect:\n"+effect)
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
if ri=="move":
	move=inp
	m=requests.get("https://pokeapi.co/api/v2/move/"+move+"/").json()
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
pokemon=inp
r=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon+"/").json()
pid=r['id']
spurl=str(r['species']['url'])
r2=requests.get(spurl).json()
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