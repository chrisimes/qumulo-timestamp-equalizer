"""fix_timestamps.py -

Walk a tree and for each file or directory, set ctime and btime to equal mtime.

qtreewalk.py from
https://github.com/Qumulo/power-tools/
"""


import qtreewalk


def do_per_file(ent, d, out_file=None, rc=None):
    msg = "%s mtime is %s, setting ctime/btime to match" % (d['path'] + ent['name'], ent['modification_time'])
    qtreewalk.log(msg)
    target_time = ent['modification_time']
    rc.fs.set_file_attr(path=ent['path'], creation_time=target_time, change_time=target_time)

qtreewalk.do_per_file = do_per_file

if __name__ == '__main__':
    args = qtreewalk.parse_args()
    qtreewalk.walk_tree(args.s, 'admin', args.p, args.d)
