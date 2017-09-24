# making waves

This repo contains the python files responsible for baking and rendering a 2D wave simulation. 

The first step is simulation, done by the mesh_creator file. This python file outputs the location of the vertices of the mesh for each frame in the animation. Each frame gets a .ply file, which describes a mesh.

In fact, every vertex of the mesh has a constant x and y coordinate - the only thing that changes is the z coordinates. According to the wave equation,

<img src="https://latex.codecogs.com/gif.latex?\frac{d^2u}{dt^2}=c^2\nabla^2u" /> 

where u is a function of x and y (in our 2D case). We numerically integrate this equation using the recurrence relation in this paper: https://people.ece.cornell.edu/land/courses/ece5760/LABS/f2009/FPGAfd.pdf

The rendering is done in Blender using their Python API: bpy. The blend.py file defines handlers for the renderer - these are methods which are called when a new frame is loaded. The handlers defined in the blend.py file simply load the .ply meshes, and then delete them after rendered. 
