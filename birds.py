def sightings(arr):

	sights = {}

	for i in arr:

		if i in sights.keys():
			sights[i] += 1
		else:
			sights[i] = 1

	types = list(sights.keys())
	no_of_sights = list(sights.values())

	print(types)
	print(no_of_sights)

	print(f"Type {types[no_of_sights.index(max(no_of_sights))]}")

sightings([1,1,2,2,2,3,3,3])