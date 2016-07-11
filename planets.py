# Exercise

planet_list = ["Mercury", "Mars"]

# Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Jupiter")
planet_list.append("Saturn")

# Use the extend() method to add another list of the last two planets
# in our solar system to the end of the list.
planet_list.extend(["Uranus", "Neptune"])

# Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")

# Use append() again to add Pluto to the end of the list.
planet_list.append("Pluto")

print(planet_list)

# Now that all the planets are in the list, slice the list in order to
# get the rocky planets into a new list called rocky_planets.
rocky_planets = planet_list[0:4]
rocky_planets += planet_list[-1:]
print(rocky_planets)

# Being good amateur astronomers, we know that Pluto is now a dwarf planet,
# so use the del operation to remove it from the end of planet_list.
del planet_list[8:]
print(planet_list)

# Iterating over planets
# Create another list containing tuples. Each tuple will hold the name of a spacecraft that
# we have launched, and the names of the planet(s) that it has visited, or landed on.
# (e.g. ('Cassini', 'Jupiter')). Iterate over your list of planets, and inside that loop,
# iterate over the list of tuples. Print, for each planet, which sattelites have visited.
spacecraft_visited = [("MR-1", "Mars"),
	("Spaceship1", "Saturn"),
	("Spaceship2", "Earth"),
	("Pegasus", "Venus"),
	("Star Destroyer", "Jupiter"),
	("Another Ship", "Saturn")]

# spacecraft_dict = dict()

for planet in planet_list:
	for craft, plan in spacecraft_visited:
		if planet == plan:
			output = ['{0} --visited by {1}.'.format(planet, craft)]
			print(output)

### Mercury, Venus, Earth, Mars,
### Jupiter, Saturn, Uranus, Neptune, Pluto
import code
code.interact(local=locals())
