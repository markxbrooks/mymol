#!/bin/env python
# run with @filename from pymol command line
from pathlib import Path
homedir = Path.home()
reinitialize
cd homedir + os.sep + "Desktop"
prot="1zy7"
chain = A
print(prot)
#fetch 1dw1
cmd.fetch(prot,name=prot)

select visible
#load 1dw1.map.ccp4
cmd.fetch(prot,type="2fofc")
objname = f"{prot}-A"
cmd.select(objname, "chain A")
cmd.hide("everything")
cmd.show("cartoon", objname)
#isomesh map, 1dw1.map, 3.0, sele, carve=1.6
cmd.isomesh("%s_map"%prot, "%s_2fofc"%prot, 3.0, objname, carve=1.6)

#color br2, map
cmd.color("br2", "%s_map"%prot)
#cmd.color("yellow", "%s_map"%prot)

#set mesh_width, 0.5
print cmd.get_setting_text('mesh_width')
cmd.set("mesh_width", 0.5)
print cmd.get_setting_text('mesh_width')

#bg_color black
cmd.bg_color("white")

#set ray_trace_fog, 0
print cmd.get_setting_text('ray_trace_fog')
cmd.set("ray_trace_fog", 0)
print cmd.get_setting_text('ray_trace_fog')

#set depth_cue, 0
print cmd.get_setting_text('depth_cue')
cmd.set("depth_cue", 0)
print cmd.get_setting_text('depth_cue')

#set ray_shadows, off
print cmd.get_setting_text('ray_shadows')
cmd.set("ray_shadows", "off")
print cmd.get_setting_text('ray_shadows')

#ray 1280,1024
#cmd.ray(1280,1024)
