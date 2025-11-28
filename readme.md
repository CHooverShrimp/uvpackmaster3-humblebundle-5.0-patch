# UVPackMaster Humble Bundle patch for Blender 5.0
This is a quick and dirty patch to make UVPM from Humble Bundle to work with Blender 5.0

This is not an engine patch, this is a **Blender plugin** patch. You would still need the engine, which must be purchased from UVPackMaster to use UVPM in Blender.

## What's the issues?
The `bpy_types` module was reorganized into `bpy.type`

`__init__` in `UVPM3_OT_Engine` needs to accept more param to match modern Blender.

## Can I trust you with this?
This is a patch to `uvpackmaster3-addon-3.4.4-u5.zip`, the recommended version for Humble Bundle users.

You can trust me as much as you can trust the original author. As a gesture of transparency, I am pusing the original zip package to github first, then editing it, so you can verify the authenticity for yourself.

The changes to this repo reflect the changes to the original content. You can download the original package from [UvPackMaster's website](https://uvpackmaster.com/for-blender/downloads/) (https://uvpackmaster.com/for-blender/downloads/).

## License
The original Blender addon was in GNU GPL. I supposes this too will be. I will include the license in a license file.

I don't clain ownership of the original plugin.