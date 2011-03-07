Title: mount sshfs at boot
Date: 2009-05-25

Currently, Upstart in Ubuntu does not generate network events. Instead it
calls traditional sysvinit. By default NetworkManager is installed and
running; rather than emit network events to Upstart, it contains a run-parts
dispatcher (/etc/NetworkManager/dispatcher.d/) which itself simply relies on
ifupdown's run-parts dispatcher (/etc/network/*.d/). In particular you care
about /etc/network/if-up.d/ and /etc/network/if-down.d/

First set up a unencrypted ssh keypair, so you can ssh and mount the point
without a prompt. Write a script, place it in /etc/network/if-up.d/ and make
executable. The following was discovered on [UbuntuForums][1] and was
sufficient for me:



    #!/bin/sh
    ## http://ubuntuforums.org/showthread.php?t=430312
    ## The script will attempt to mount any fstab entry with an option
    ## "...,comment=$SELECTED_STRING,..."
    ## Use this to select specific sshfs mounts rather than all of them.
    SELECTED_STRING="sshfs"
    # Not for loopback
    [ "$IFACE" != "lo" ] || exit 0

    ## define a number of useful functions
    ## returns true if input contains nothing but the digits 0-9, false otherwise
    ## so realy, more like isa_positive_integer
    isa_number () {
        ! echo $1 | egrep -q '[^0-9]'
        return $?
    }

    ## returns true if the given uid or username is that of the current user
    am_i () {
            [ "$1" = "`id -u`" ] || [ "$1" = "`id -un`" ]
    }

    ## takes a username or uid and finds it in /etc/passwd
    ## echoes the name and returns true on success
    ## echoes nothing and returns false on failure
    user_from_uid () {
        if isa_number "$1"
        then
                    # look for the corresponding name in /etc/passwd
            local IFS=":"
            while read name x uid the_rest
            do
                    if [ "$1" = "$uid" ]
                            then
                                    echo "$name"
                                    return 0
                            fi
            done </etc/passwd
        else
            # look for the username in /etc/passwd
            if grep -q "^${1}:" /etc/passwd
            then
                   echo "$1"
                    return 0
            fi
        fi
        # if nothing was found, return false
            return 1
    }
    ## Parses a string of comma-separated fstab options and finds out the
    ## username/uid assigned within them.
    ## echoes the found username/uid and returns true if found
    ## echoes "root" and returns false if none found
    uid_from_fs_opts () {
            local uid=`echo $1 | egrep -o 'uid=[^,]+'`
            if [ -z "$uid" ]; then
                    # no uid was specified, so default is root
                    echo "root"
                    return 1
            else
                    # delete the "uid=" at the beginning
                    uid_length=`expr length $uid - 3`
                    uid=`expr substr $uid 5 $uid_length`
                    echo $uid
                    return 0
            fi
    }

    # unmount all shares first
    sh "/etc/network/if-down.d/umountsshfs"

    while read fs mp type opts dump pass extra
    do
        # check validity of line
        if [ -z "$pass" -o -n "$extra" -o "`expr substr ${fs}x 1 1`" = "#"];
        then
            # line is invalid or a comment, so skip it
            continue
            # check if the line is a selected line
            elif echo $opts | grep -q "comment=$SELECTED_STRING"; then

            # get the uid of the mount
            mp_uid=`uid_from_fs_opts $opts`
             if am_i "$mp_uid"; then
                            # current user owns the mount, so mount it normally
                            { sh -c "mount $mp" &&
                                        echo "$mp mounted as current user (`id-un`)" ||

                                        echo "$mp failed to mount as current user (`id -un`)";
                             } &
                    elif am_i root; then
                            # running as root, so sudo mount as user
                            if isa_number "$mp_uid"; then
                                    # sudo wants a "#" sign icon front of a numeric uid
                                    mp_uid="#$mp_uid"
                            fi
                            { sudo -u "$mp_uid" sh -c "mount $mp" &&
                                    echo "$mp mounted as $mp_uid" ||
                                    echo "$mp failed to mount as $mp_uid";
                            } &
                    else
                            # otherwise, don't try to mount another user's mount point
                            echo "Not attempting to mount $mp as other user $mp_uid"
    :
                            echo "Not attempting to mount $mp as other user $mp_uid"
                    fi
        fi
        # if not an sshfs line, do nothing
    done </etc/fstab
    wait

If you have a wifi or otherwise unreliable connection, place the following in
/etc/network/if-down.d/:



    #!/bin/bash
    # Not for loopback!
    [ "$IFACE" != "lo" ] || exit 0
    # comment this for testing
    exec 1>/dev/null # squelch output for non-interactive

    # umount all sshfs mounts
    mounted=`grep 'fuse.sshfs\|sshfs#' /etc/mtab | awk '{ print $2 }'`
    [ -n "$mounted" ] && { for mount in $mounted; do umount -l $mount; done; }

The final step is to make sure that [your connection starts at boot][2], if
you want to start networking (and sshfs) before anyone logs in.

   [1]: http://ubuntuforums.org/showthread.php?t=430312

   [2]: https://help.ubuntu.com/community/NetworkManager0.7#Adding%20Wired%20connections

