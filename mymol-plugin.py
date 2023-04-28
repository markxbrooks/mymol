#!/bin/env python
# run with @filename from pymol command line
from pathlib import Path
from pymol import cmd

@cmd.extend
def fetch_map_mol(pdb_id, chain_id= "A", quiet=1):
    '''
DESCRIPTION

    Fetch PDB file from RCSB, select chain chain_id

USAGE

    fetch_map_mol pdb_id, [chain ]

EXAMPLE
    fetch_map_mol "2vug", "A
    '''

    homedir = Path.home()
    reinitialize
    cd homedir + os.sep + "Desktop"
    print(pdb_id)
    #fetch 1dw1
    cmd.fetch(pdb_id,name=pdb_id)

    select visible
    #load 1dw1.map.ccp4
    cmd.fetch(pdb_id,type="2fofc")
    objname = f{"{pdb_id}-{A}"}
    #select(f"{pdb_id} chain {A}, {objname}")
    #isomesh map, 1dw1.map, 3.0, sele, carve=1.6
    cmd.isomesh("%s_map"%pdb_id, "%s_2fofc"%pdb_id, 3.0, "sele", carve=1.6)

    #color br2, map
    cmd.color("br2", "%s_map"%pdb_id)
    #cmd.color("yellow", "%s_map"%pdb_id)

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
