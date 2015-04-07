__author__ = 'Peter_Howe<haobibo@gmail.com>'

from textmind.maps import SetMultimap

from quiz import dbutil


ips = SetMultimap(ordered=True)
filltimes = SetMultimap(ordered=True)

def get_exp_fills(ExpId=7):
    cur = dbutil.get_cur()
    cur.execute('CALL P_GetExpFills(%s,null,null)' % ExpId)
    for r in cur:
        sina_uid = r['SiteUid']
        filltime = r['LastFill']
        ip = r['IPAddr']

        filltimes[sina_uid].add(filltime)
        ips[sina_uid].add(ip)

    uids = ips._dict.keys()
    for uid in uids:
        line = 'IP\t%s\t' % uid
        for ip in ips[uid]:
            line += ip + '\t'
        line += '\n'

        line += 'TIME\t%s\t' % uid
        times = sorted(filltimes[uid])
        for t in times:
            str_time = '%02d%02d_%02d%02d%02d' % (t.month, t.day, t.hour, t.minute, t.second)
            line += str_time + '\t'

        print line



if __name__ == '__main__':
    get_exp_fills(ExpId=7)