import bpy

# iniital objekt löschen
bpy.data.screens["Default"].name = "Default"
bpy.ops.object.delete(use_global=False)

# neues 8 Eck erstellen
bpy.ops.mesh.primitive_circle_add(vertices=8)

# Wechsle in Edit Mode
bpy.ops.object.editmode_toggle()

# Um 4 in Z Richtung extruden
bpy.ops.mesh.extrude_region_move(
TRANSFORM_OT_translate={"value":(0,0,4)})

# ganzes Objekt auswählen
bpy.ops.mesh.select_all(action='TOGGLE')
bpy.ops.mesh.select_all(action='TOGGLE')

# Auf Nullpounkt verschieben
bpy.ops.transform.translate(value=(-1, 4, -3), constraint_axis=(True,True,True))

# Baue Kopf 

# Teile Zylinder 

# Erstelle Skelett (Armature)

# Definiere Animationen (atmen und beissen)

# Wechsle zurück in Object Mode
bpy.ops.object.editmode_toggle()
