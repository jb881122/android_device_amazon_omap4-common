import common

def FullOTA_InstallEnd(info):
    info.script.Mount("/system")
    info.script.AppendExtra('run_program("/system/bin/fix-mac.sh");')
    info.script.AppendExtra('delete("/system/bin/fix-mac.sh");')
    info.script.Unmount("/system")
