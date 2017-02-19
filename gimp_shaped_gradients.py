#! /usr/bin/env python
from gimpfu import *
import gimp

def paths_to_paint_gradients(image, drawable):
	pdb.gimp_context_push()
	pdb.gimp_image_undo_group_start(image)

	#image = gimp.image_list()[0]
	#drawable = pdb.gimp_image_get_active_drawable(image)

	pdb.gimp_image_undo_group_start(image)

	cnt, vectors = pdb.gimp_image_get_vectors(image)
	if cnt > 0:

		for id in vectors:
			vector = gimp.Vectors.from_id(id)
			pdb.gimp_image_select_item(image,2,vector)
			pdb.gimp_selection_grow(image, 1)
			pdb.gimp_edit_blend(drawable, # drawable_ID
				2, #blend_mode, fg to transparent
				7, #paint_mode, ADD
				7, #gradient_type, shapedlinear
				100.0, #opacity
				0.0, # offset
				0, # repeat
				False, # reverse, from the inside to the outside
				False, # supersample
				1, # max_depth,
				0.2, # threshold
				True, # dither
				0.0, # x1
				0.0, # x2
				1.0, # y1
				1.0  # y2
			)

		pdb.gimp_selection_none(image)

	pdb.gimp_image_undo_group_end(image)
	pdb.gimp_context_pop()
	print "Finished"

register(
	'shaped-gradient-for-yaoi-shader',
	'Paints shaped gradients by closed paths',
	'Paints shaped gradients by closed paths for yaoi shader',
	'iszotic',
	'iszotic aka isothetic',
	'19/02/2017',
	'<Image>/Filters/Paths/Paint shaped gradients...',
	'',
	[],
	[],
	paths_to_paint_gradients
)
#https://github.com/devolonter/gimp-cut-to-pieces/blob/master/cut-to-pieces.py
#Thanks to Arthur Bikmullin aka devolonter
main()