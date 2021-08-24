#!/usr/bin/env python

from vtk import (vtkStructuredPointsReader, vtkDataSetMapper, vtkActor,
                 vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor, vtkGenericDataObjectReader)

def read_density(file_name):
    
	# Read the source file.
	reader = vtkStructuredPointsReader()
	reader.SetFileName(file_name)
	reader.Update()  # Needed because of GetScalarRange
	output = reader.GetOutput()
	output_port = reader.GetOutputPort()
	scalar_range = output.GetScalarRange()

	# Create the mapper that corresponds the objects of the vtk file
	# into graphics elements
	mapper = vtkDataSetMapper()
	mapper.SetInputConnection(output_port)
	mapper.SetScalarRange(scalar_range)

	# Create the Actor
	actor = vtkActor()
	actor.SetMapper(mapper)

	# Create the Renderer
	renderer = vtkRenderer()
	renderer.AddActor(actor)
	renderer.SetBackground(1, 1, 1) # Set background to white

	return renderer

def read_atoms(file_name):

	reader = vtkGenericDataObjectReader()
	reader.SetFileName(file_name)
	reader.Update()

	output = reader.GetOutput()
	print(output)
	mapper = vtkDataSetMapper()
	mapper.SetInputData(output)

	# Create the Actor
	actor = vtkActor()
	actor.SetMapper(mapper)

	# Create the Renderer
	renderer = vtkRenderer()
	renderer.AddActor(actor)
	renderer.SetBackground(1, 1, 1) # Set background to white

	return renderer

def main():

	density = read_density("DensityProfile_CO2.vtk")
	atoms = read_atoms('FrameworkAtoms.vtk')

	# Create the RendererWindow
	renderer_window = vtkRenderWindow()
	renderer_window.SetSize(800, 500)
	renderer_window.AddRenderer(density)

	# Create the RendererWindowInteractor and display the vtk_file
	interactor = vtkRenderWindowInteractor()
	interactor.SetRenderWindow(renderer_window)
	interactor.Initialize()
	interactor.Start()


if __name__ == '__main__':
    main()