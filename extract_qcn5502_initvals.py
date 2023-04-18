import sys

fn = sys.argv[1]
ofn = sys.argv[2]
data = open(fn, 'rb').read()


def u32_to_bytes(bs):
    return b''.join(a.to_bytes(4, 'big') for a in bs)


of = open(ofn, 'w')

aw_arrs = set()


def w_arr(name, cols, vals):
    aw_arrs.add(name)
    ct = []
    ct.append(f'static const u32 {name}[][{cols}] = {{')
    if name == 'qcn550x_1p0_modes_fast_clock':
        ct.append('\t/* Addr      5G_HT20     5G_HT40   */')
    elif cols == 2:
        ct.append('\t/* Addr      allmodes  */')
    elif cols == 3:
        ct.append('\t/* Addr      5G          2G        */')
    elif cols == 5:
        ct.append('\t/* Addr      5G_HT20     5G_HT40     2G_HT40     2G_HT20   */')
    for i in range(0, len(vals), cols):
        vs = ', '.join('0x%08x' % x for x in vals[i:i+cols])
        ct.append(f'\t{{{vs}}},')
    ct.append('};')
    ct.append('')
    ct.append('')
    of.write('\n'.join(ct))


for tpl in [
    ([0x00029800, 0xafe68e30], 0x2e43c, 2, 'qcn550x_1p0_baseband_core'),
    ([0x00029810, 0xd00a8105], 0x2e284, 5, 'qcn550x_1p0_baseband_postamble'),
    ([0x00016000, 0x36db6db6], 0x16fd4, 2, 'qcn550x_1p0_radio_core'),
    ([0x00016098, 0xd2dd5554], 0x16d40, 5, 'qcn550x_1p0_radio_postamble'),
    ([0x0002a000, 0x00010000], 0x2b1fc, 2,
     'qcn550x_1p0_common_wo_xlna_rx_gain_table', lambda vals: vals[23] != 0x01910190),
    ([0x00029e44, 0xfe321e27], 0x29e48, 5,
     'qcn550x_1p0_common_wo_xlna_rx_gain_bounds', lambda vals: vals[-1] == 0x50302012),
    ([0x00016044, 0x024922e4], 0x2e2e8, 3, 'qcn550x_1p0_modes_xpa_tx_gain_table'),
    ([0x00029824, 0x5ac668d0], 0x29e14, 3,
     'qcn550x_1p0_baseband_postamble_dfs_channel'),
    ([0x00001030, 0x00000268], 0x2a254, 3, 'qcn550x_1p0_modes_fast_clock'),
    ([0x0002a000, 0x00010000], 0x2b1fc, 2,
     'qcn550x_1p0_common_rx_gain_table', lambda vals: vals[23] == 0x01910190),
    ([0x00029e44, 0xfe321e27], 0x29e48, 5,
     'qcn550x_1p0_common_rx_gain_bounds', lambda vals: vals[-1] != 0x50302012),
    ([0x00016290, 0x3871ad09], 0x2de20, 5, 'qcn550x_1p0_xlna_only'),
    ([0x00016044, 0x0491c2e4], 0x2e2e8, 3,
     'qcn550x_1p0_modes_no_xpa_tx_gain_table'),
    ([0x00016044, 0x049242e4], 0x2e2e8, 3,
     'qcn550x_1p0_modes_no_xpa_tx_gain_table'),
    ([0x00016044, 0x046e42e4], 0x2e2e8, 3,
     'qcn550x_1p0_modes_no_xpa_low_ob_db_tx_gain_table'),
    ([0x00016044, 0x0491c2c9], 0x2e2e8, 3,
     'qcn550x_1p0_modes_no_xpa_mcal_tx_gain_table', lambda vals: vals[-1] == 0xff000000),
    ([0x00016044, 0x049242c9], 0x2e2e8, 3,
     'qcn550x_1p0_modes_no_xpa_mcal_tx_gain_table', lambda vals: vals[-1] == 0xff000000),
    ([0x00016044, 0x0491c2c9], 0x2e2e8, 3,
     'qcn550x_1p0_modes_no_xpa_table_5_tx_gain_table', lambda vals: vals[-1] != 0xff000000),
    ([0x00016044, 0x049242c9], 0x2e2e8, 3,
     'qcn550x_1p0_modes_no_xpa_table_5_tx_gain_table', lambda vals: vals[-1] != 0xff000000),
    ([0x00016044, 0x8491c2e4], 0x2e2e8, 3,
     'qcn550x_1p0_modes_no_xpa_green_tx_gain_table'),
    ([0x00016044, 0x849242e4], 0x2e2e8, 3,
     'qcn550x_1p0_modes_no_xpa_green_tx_gain_table'),
]:
    if len(tpl) == 5:
        ff, ed, sz, name, fn = tpl
    else:
        ff, ed, sz, name = tpl
        def fn(vals): return True
    pos = 0
    while True:
        pos = data.find(u32_to_bytes(ff), pos)
        if pos == -1:
            break
        fail = False
        ipos = pos
        while True:
            pos += sz*4
            vv = int.from_bytes(data[pos:pos+4], 'big')
            if vv == 0:
                fail = True
                break
            if vv == ed:
                break
        vals = [int.from_bytes(data[i:i+4], 'big')
                for i in range(ipos, pos+sz*4, 4)]
        if fail or not fn(vals):
            continue
        w_arr(name, sz, vals)
        break

of.close()
