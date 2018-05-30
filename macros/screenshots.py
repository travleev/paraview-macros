import os
import datetime

# Screenshots are stored to the folder `pvss`(ParaView ScreenShot), 
# under the user profile folder
base = os.path.join(os.environ['USERPROFILE'], 'pvss')
if not os.path.exists(base):
    os.mkdir(base)
# Screenshots are stored in a new timestamp folder
tstamp = datetime.datetime.now().isoformat().replace(':', '-')
basefolder = os.path.join(base, tstamp)
os.mkdir(basefolder)

# Save the state, used for screenshots:
SaveState(os.path.join(basefolder, 'state.pvsm'))
# Each layout is stored in separate folder, figure names -- from the view titles
vd = servermanager.ProxyManager().GetProxiesInGroup('views')
print 'Screenshots:'
for (name, i), l in GetLayouts().items():
    folder = os.path.join(basefolder, name)
    os.mkdir(folder)
    for iv, v in enumerate(GetViewsInLayout(l)):
        # Each view screenshot is named by its index. The view window names
        # are not used for 2 reasons: (1) I don't know how to get this name and
        # (2) these names are not unique (there can be two views with the same
        # window name. 
        for (n, i), vv in vd.items():
            if vv is v:
                name = n
                vd.pop((n, i))
        fname = os.path.join(folder, '{}.png'.format(name))
        print fname, 
        if SaveScreenshot(fname, v):
            print 'ok'
        else:
            print 'failed'
 