import numpy as np
import pyglet
import random
import colorsys
from color import *

random.seed()

red = Color(rgb=(1,0,0))
green = Color(rgb=(0,1,0))

#def TemperatureToColor(temperature):
#	return InterpolateColors([green, red], temperature)

def UpdateTemperatures(dt, cells, grid_width, grid_height):
	k = 0.1

	if len(cells) != grid_width * grid_height:
		print("Invalid cells info given. Exiting.")
		return


#	print(cells)

	rows = [cells[y,:] for y in range(cells.shape[0])]
#	print(rows)
#	print("---")
	#[zip(row[:], row[1:]) for row in ]

	#cell_pairs = [zip(row[:], row[1:]) for row in [cells[i:i+grid_width] for i in ]

# NOTE: 1D cells
#	cell_pairs = zip(cells[:], cells[1:])
#	temperature_changes = [0.0] * len(cells)
#	for i, cell_pair in enumerate(cell_pairs):
#		i_left = i
#		i_right = i+1
#		left_cell = cell_pair[0]
#		right_cell = cell_pair[1]
#
#		dT = left_cell - right_cell
#		dq = -k * (left_cell - right_cell) * dt
#
#		# TODO: Need a way to deal with too large step sizes causing temperatures to just swap rapidly
#		#if abs(dq) > abs(dT / 2):
#			#temperature_changes[i_left]
#			
#		temperature_changes[i_left] += dq
#		temperature_changes[i_right] -= dq
#
#	cells += temperature_changes

def GetCellColors(cells):
	n = len(cells)
	colors = np.array([[green, red]]*n)
	return InterpolateColors(colors, cells.flatten())
		


window = pyglet.window.Window(width = 500, height = 500)

grid_width, grid_height = 4, 1
cell_count = grid_width * grid_height
cell_size = min(window.width // grid_width, window.height // grid_height)

cells = np.random.rand(grid_width, grid_height)
#cells = np.array([random.random() for i in range(cell_count)])

grid_vertices = np.array([[x,y, x,y+cell_size, x+cell_size,y+cell_size, x+cell_size,y] for x in np.linspace(0, window.width-cell_size, grid_width) for y in np.linspace(0, window.height-cell_size, grid_height)]).flatten()
#cell_colors = GetCellColors(cells)

@window.event
def on_draw():
	window.clear()

	v_count = len(grid_vertices) // 2
	vertex_colors = np.concatenate(np.repeat(GetCellColors(cells), 4))
	print(vertex_colors)
	pyglet.graphics.draw(v_count, pyglet.gl.GL_QUADS, ('v2f', grid_vertices), ('c3f', vertex_colors))

@window.event
def update(dt):
	UpdateTemperatures(dt, cells, grid_width, grid_height)

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()