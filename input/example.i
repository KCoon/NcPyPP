12 G17 G90
T1 M6
//G1 X-9 Y-29.184
//G1 Z-11.5
//G1 X-7.811 Y-27.994
//G2 X-5.689 Y-27.994 I1.061 J-1.061
//G1 X-4.5 Y-29.184
[[bore:
X=23.33
Y=-26.16
Z=-16.5
H=0.5
r_1=3
r_2=2
phi_1=0
clearance=2
retraction=5
F=2000
]]
[[contour:
Z=-5
H=1
r=0.5
ap=0.4
clearance=2
retraction=5
gap=1
F=2000
[[Line(0, 0,)]]
[[Line(5, 0, )]]
[[circle(7, 2, , 5, 2, ccw)]]
[[Line(7, 5, )]]
]]
[[contour:
Z=-14
H=2.5
r=0.5
ap=0.4
clearance=2
retraction=5
gap=1
F=2000
[[Line(0, -38.184,)]]
[[Line(38.184, 0,)]]
[[Line(0, 38.184,)]]
[[Line(-38.184, 0,)]]
[[Line(0, -38.184,)]]
]]
[[contour:
Z=-11.5
H=1
r=0.5
ap=0.4
clearance=2
retraction=5
gap=1
F=2000
[[Line(-9, -29.184,)]]
[[Line(-7.811, -27.994, )]]
[[circle(-5.689, -27.994, , -6.75, -29.055, cw)]]
[[Line(-4.5, -29.184, )]]
[[Line(-2.957, -27.641, )]]
[[circle(-1.543, -27.641, , -2.25, -28.348, cw)]]
[[Line(0, -29.184,)]]
[[Line(1.72, -27.464,)]]
[[circle(2.78, -27.464, , 2.25, -27.994, cw)]]
[[Line(4.5, -29.184,)]]
[[Line(6.361, -27.323,)]]
[[circle(7.139, -27.323, , 6.75, -27.712, cw)]]
[[Line(9, -29.184,)]]
]]
[[polybore:X=36
Y=36
Z=-20.5
H=3
r_1=3
r_2=2
phi_1=0
clearance=2
retraction=5
F=2000
failure=0.001
]]
[[polybore:
X=36
Y=-36
Z=-20.5
H=3
r_1=3
r_2=2
phi_1=0
clearance=2
retraction=5
F=2000
failure=0.001
]]
[[polybore:
X=-36
Y=-36
Z=-20.5
H=3
r_1=3
r_2=2
phi_1=0
clearance=2
retraction=5
F=2000
failure=0.001
]]
[[polybore:
X=-36
Y=36
Z=-20.5
H=3
r_1=3
r_2=2
phi_1=0
clearance=2
retraction=5
F=2000
failure=0.001
]]
[[Sphere:
X=-18.38
Y=0
Z=-10.5
r_1=10
r_2=3
phi_1=112.5
phi_2=292.5
theta_1=90
theta_2=0
clearance=2
retraction=5
gap=2
F=2000
step=0.078]]
[[cylinder:
X=0
Y=18.38
Z=-5
H=4.5
r_1=4
r_2=3
phi_1=90
clearance=2
retraction=5
gap=8
F=2000]]
[[bore:
X=26.16
Y=-23.33
Z=-16.5
H=0.5
r_1=3
r_2=2
phi_1=0
clearance=2
retraction=5
F=2000
]]
