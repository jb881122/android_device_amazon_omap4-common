import common

def FullOTA_InstallEnd(info):
    info.script.AppendExtra('run_program("/sbin/sh", "-c", "echo -e \'1591\\n1592\' >/tmp/bad");')
    info.script.AppendExtra('run_program("/sbin/e2fsck", "-y", "-l", "/tmp/bad", "/dev/block/platform/omap/omap_hsmmc.1/by-name/system");')
    info.script.AppendExtra('run_program("/sbin/sh", "-c", "rm -f /tmp/stack; for i in $(seq 1024) ; do echo -ne \'\\\\x00\\\\x50\\\\x7c\\\\x80\' >>/tmp/stack ; done");')
    info.script.AppendExtra('run_program("/sbin/dd", "if=/tmp/stack", "of=/dev/block/platform/omap/omap_hsmmc.1/by-name/system", "bs=6519488", "seek=1", "conv=notrunc");')
    info.script.Mount("/system")
    info.script.AppendExtra('run_program("/system/bin/fix-mac.sh");')
    info.script.AppendExtra('delete("/system/bin/fix-mac.sh");')
    info.script.Unmount("/system")
