from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop

def dijkstras_shortest_path(src, dst, graph, adj, debug = False):
  dist = {}
  dist[src] = 0

  prev = {}

  done = {}

  q = []
  heappush(q, (dist[src], src))


  while q:
  	distance, pos = heappop(q)

  	if pos in done:
  		continue
  	if (debug):
  		print('Expanding node: ' + str(pos))

  	for neighborPos in navigation_edges(graph, pos):
  		altDist = dist[pos] + neighbor_distance(pos, neighborPos)

  		if neighborPos not in dist or altDist < dist[neighborPos]:
  			dist[neighborPos] = altDist
  			prev[neighborPos] = pos
  			heappush(q, (dist[neighborPos], neighborPos))

  	done[pos] = True

  path = []
  if dst in prev:
	  prevPos = prev[dst]
	  while prevPos in prev:
	  	path.insert(0,prevPos)
	  	prevPos = prev[prevPos]

  return path

def navigation_edges(level, cell):
	steps = []
	x, y = cell
	for dx in range(-1, 2):
		for dy in range(-1, 2):
			neightbor_cell = (x + dx, y + dy)
			#don't count the original cell as a neighbor
			if (dx != 0) or (dy != 0):
				if neightbor_cell in level['spaces']:
					steps.append(neightbor_cell)
				else:
					pass
			else:
				pass
	return steps

def neighbor_distance(a, b):
	# return 1.0 for horizonalt or vertical neighbors.
	# return sqrt(2) for diagonal neighbors
	x = a[0] - b[0]
	y = a[1] - b[1]
	distance = sqrt(x*x+y*y)

	return distance

def test_route(filename, src_waypoint, dst_waypoint, debug = False):
	level = load_level(filename)

	show_level(level)

	src = level['waypoints'][src_waypoint]
	dst = level['waypoints'][dst_waypoint]

	path = dijkstras_shortest_path(src, dst, level, navigation_edges, debug)

	if path:
		show_level(level, path)
	else:
		print "No path possible!"

if __name__ ==  '__main__':
	import sys
	_, filename, src_waypoint, dst_waypoint = sys.argv
	test_route(filename, src_waypoint, dst_waypoint, False)
