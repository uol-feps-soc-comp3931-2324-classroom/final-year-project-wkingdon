from dolfinx import *
mesh = RectangleMesh((-1, -1), (1, 1), nx=10, ny=10)
V = FunctionSpace(mesh, 'P', 2) # quadratic polynomials
bc = DirichletBC(V, 0, 'on_boundary')
u = TrialFunction(V)
v = TestFunction(V)
a = dot(grad(u), grad(v))*dx
L = f*v*dx
u = Function(V) # unknown FEM function to be computed
solve(a == L, u, bc)
vtkfile = File('poisson.pvd'); vtkfile << u # store solution