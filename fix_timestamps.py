"""fix_timestamps.py -

Walk a tree and for each file or directory, set ctime and btime to equal mtime.

qtreewalk.py from
https://github.com/Qumulo/power-tools/
"""


import qtreewalk

from qumulo.lib.request import RequestError

args = None


def do_per_file(ent, d, out_file=None, rc=None):
    target_time = ent['modification_time']
    try:
        rc.fs.set_file_attr(path=ent['path'], creation_time=target_time, change_time=target_time)
    except RequestError, e:
        # This is likely to be a credentials timeout, make sure
        if "Need to log in first to establish credentials." in str(e):
            rc.login('equalizer', args.p)
            rc.fs.set_file_attr(path=ent['path'],
                                creation_time=target_time,
                                change_time=target_time)
        else:
            raise

qtreewalk.do_per_file = do_per_file

if __name__ == '__main__':
    args = qtreewalk.parse_args()
    qtreewalk.walk_tree(args.s, 'equalizer', args.p, args.d)
