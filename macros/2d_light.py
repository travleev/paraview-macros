# By default, the colors in a paraview render view are modified to present 3d objects.
# This helps to understand the 3d shape of the objects, but makes the colors differ 
# from the color scale. For 2D maps, where three-dimensional form of the object is
# not important, another set of lights is more suitable.
#
# This script changes for all render views with the interaction mode set to "2D" the
# set of lights, so that the colors on the map exactly the same as colors on the scale.

for v in GetRenderViews():
    if v.InteractionMode == '2D':
        v.UseLight = False
        v.LightSwitch = 1
        v.OrientationAxesVisibility = 0
