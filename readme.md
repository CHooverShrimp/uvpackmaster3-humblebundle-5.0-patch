# UVPackMaster Humble Bundle patch for Blender 5.0
This is a quick and dirty patch to make UVPM from Humble Bundle to work with Blender 5.0

This is not an engine patch, this is a Blender plugin patch. You would still need the engine to use UVPM.

## What's the issue?
The `bpy_types` module was reorganized into `bpy.type`
`__init__` in `UVPM3_OT_Engine` needs to accept more param to match modern Blender.

## Can I trust you with this?
You can trust me as much as you can trust the original author. As a gesture of transparency, I am pusing the whole zip package to github, then editing it, so you can verify the authenticity for yourself.

The changes to this repo reflect the changes to the original content.

## License
The original Blender addon was in GNU GPL. I supposes this too will be. I will include the license in a license file.

I don't clain ownership of the original plugin.