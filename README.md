QCN5502 Initvals
================

QCN5502 is a 4x4:4 802.11n WiFi SoC that is very similar to QCA956x. This repo contains QCN5502 initvals for various devices.

After obtaining ath_hal.ko from the manufacturer GPL dump or firmware, the initvals can be extracted using `python3 extract_qcn5502_initvals.py ath_hal.ko vals.h`

Overall, these initvals are very similar to QCA956x initvals found in ath9k except for adding 0x20000 to many addresses and adding 4th-chain related addresses. I don't know why the initvals are slightly different for different devices but it doesn't seem to make a big difference.

vals_ath9k_proposed.h contains initvals that I'm proposing for inclusion in ath9k. I edited certain values to enable the clock doubler, which matches stock firmware behavior and seems necessary for decent performance.

```
--- vals_dlink_dap-2682.h
+++ vals_ath9k_proposed.h
@@ -248,8 +248,8 @@ static const u32 qcn550x_1p0_radio_core[
 	{0x0001608c, 0x119f080a},
 	{0x00016090, 0x24926490},
 	{0x00016094, 0x00000000},
-	{0x000160a0, 0xc2108ffe},
-	{0x000160a4, 0x812fc370},
+	{0x000160a0, 0x02108ffe},
+	{0x000160a4, 0x812fc373},
 	{0x000160a8, 0x423c8300},
 	{0x000160b4, 0x92480000},
 	{0x000160c0, 0x006db6d8},
@@ -263,8 +263,8 @@ static const u32 qcn550x_1p0_radio_core[
 	{0x00016148, 0x00008058},
 	{0x00016288, 0xa0307860},
 	{0x0001628c, 0x50000000},
-	{0x00016290, 0x4b960503},
-	{0x00016294, 0x80000000},
+	{0x00016290, 0x4b96250b},
+	{0x00016294, 0x00000000},
 	{0x00016380, 0x00000000},
 	{0x00016384, 0x00000000},
 	{0x00016388, 0x00800700},
@@ -394,10 +394,10 @@ static const u32 qcn550x_1p0_radio_core[
 
 static const u32 qcn550x_1p0_radio_postamble[][5] = {
 	/* Addr      5G_HT20     5G_HT40     2G_HT40     2G_HT20   */
-	{0x00016098, 0xd2dd5554, 0xd2dd5554, 0xc4128f5c, 0xc4128f5c},
-	{0x0001609c, 0x0a566f3a, 0x0a566f3a, 0x0fd08f25, 0x0fd08f25},
-	{0x000160ac, 0xa4647c00, 0xa4647c00, 0x24646800, 0x24646800},
-	{0x000160b0, 0x01885f52, 0x01885f52, 0x00fe7f46, 0x00fe7f46},
+	{0x00016098, 0xd2055554, 0xd2055554, 0xc2028f5c, 0xc2028f5c},
+	{0x0001609c, 0x02566f3a, 0x02566f3a, 0x07d08f25, 0x07d08f25},
+	{0x000160ac, 0x24647c01, 0x24647c01, 0x24646801, 0x24646801},
+	{0x000160b0, 0x09885f52, 0x09885f52, 0x08fe7f46, 0x08fe7f46},
 	{0x00016104, 0xb7a00000, 0xb7a00000, 0xfff80001, 0xfff80001},
 	{0x0001610c, 0xc0000000, 0xc0000000, 0x00000000, 0x00000000},
 	{0x00016140, 0x10804008, 0x10804008, 0x50804008, 0x50804008},
@@ -1047,7 +1047,6 @@ static const u32 qcn550x_1p0_common_rx_g
 
 static const u32 qcn550x_1p0_xlna_only[][5] = {
 	/* Addr      5G_HT20     5G_HT40     2G_HT40     2G_HT20   */
-	{0x00016290, 0x3871ad09, 0x3871ad09, 0x3871ad09, 0x3871ad09},
 	{0x00029820, 0x206a022e, 0x206a022e, 0x206a01ae, 0x206a022e},
 	{0x00029824, 0x5ac640d0, 0x5ac640d0, 0x5ac621f1, 0x5ac621f1},
 	{0x00029828, 0x06903081, 0x06903081, 0x0712b281, 0x052e6381},
```

```
--- vals_dlink_dap-2682.h
+++ vals_asus_rt-acrh12.h
@@ -48,7 +48,7 @@ static const u32 qcn550x_1p0_baseband_co
 	{0x00029fc4, 0x0001efb5},
 	{0x00029fcc, 0x40000014},
 	{0x00029fd0, 0x02993b93},
-	{0x00029fd4, 0x81e5a8ab},
+	{0x00029fd4, 0x81e5a8aa},
 	{0x0002a20c, 0x00000000},
 	{0x0002a218, 0x00000000},
 	{0x0002a21c, 0x00000000},
@@ -102,9 +102,9 @@ static const u32 qcn550x_1p0_baseband_co
 	{0x0002a40c, 0x00820820},
 	{0x0002a414, 0x1ce739ce},
 	{0x0002a418, 0x2d001dce},
-	{0x0002a41c, 0x1ce739ce},
+	{0x0002a41c, 0x1ce739cf},
 	{0x0002a420, 0x000001ce},
-	{0x0002a424, 0x1ce739ce},
+	{0x0002a424, 0x1ee739ce},
 	{0x0002a428, 0x000001ce},
 	{0x0002a42c, 0x1ce739ce},
 	{0x0002a430, 0x1ce739ce},
```

```
--- vals_dlink_dap-2682.h
+++ vals_asus_zenwifi_ac_mini_cd6.h
@@ -48,7 +48,7 @@ static const u32 qcn550x_1p0_baseband_co
 	{0x00029fc4, 0x0001efb5},
 	{0x00029fcc, 0x40000014},
 	{0x00029fd0, 0x02993b93},
-	{0x00029fd4, 0x81e5a8ab},
+	{0x00029fd4, 0x81e5a8aa},
 	{0x0002a20c, 0x00000000},
 	{0x0002a218, 0x00000000},
 	{0x0002a21c, 0x00000000},
@@ -102,7 +102,7 @@ static const u32 qcn550x_1p0_baseband_co
 	{0x0002a40c, 0x00820820},
 	{0x0002a414, 0x1ce739ce},
 	{0x0002a418, 0x2d001dce},
-	{0x0002a41c, 0x1ce739ce},
+	{0x0002a41c, 0x1ce739cf},
 	{0x0002a420, 0x000001ce},
 	{0x0002a424, 0x1ce739ce},
 	{0x0002a428, 0x000001ce},
@@ -1064,7 +1064,7 @@ static const u32 qcn550x_1p0_xlna_only[]
 	{0x00029fc0, 0x813e4788, 0x813e4788, 0x813e4789, 0x813e4789},
 	{0x00029fd4, 0x81e5a89a, 0x81e5a89a, 0x81e5a89a, 0x81e5a89a},
 	{0x0002a3a4, 0x3a3e3e00, 0x3a3e3e00, 0x3a3e3e00, 0x3a3e3e00},
-	{0x0002a424, 0x1ce739cb, 0x1ce739cb, 0x1ce739cb, 0x1ce739cb},
+	{0x0002a424, 0x1ce739cb, 0x1ce739cb, 0x1ce739cf, 0x1ce739cf},
 	{0x0002ae18, 0x00000000, 0x00000000, 0x04008020, 0x04008020},
 	{0x0002ae20, 0x000001b5, 0x000001b5, 0x000001b2, 0x000001b2},
 	{0x0002be18, 0x00000000, 0x00000000, 0x04008020, 0x04008020},
```

```
--- vals_dlink_dap-2682.h
+++ vals_netgear_ex7300v2_ex6400v2.h
@@ -1076,7 +1076,7 @@ static const u32 qcn550x_1p0_xlna_only[]
 
 static const u32 qcn550x_1p0_modes_no_xpa_tx_gain_table[][3] = {
 	/* Addr      5G          2G        */
-	{0x00016044, 0x049242e4, 0x049242e4},
+	{0x00016044, 0x0491c2e4, 0x0491c2e4},
 	{0x00016048, 0x64925a70, 0x64925a70},
 	{0x00016148, 0x00008050, 0x00008050},
 	{0x00016280, 0x42222000, 0x42222000},
@@ -1262,7 +1262,7 @@ static const u32 qcn550x_1p0_modes_no_xp
 
 static const u32 qcn550x_1p0_modes_no_xpa_mcal_tx_gain_table[][3] = {
 	/* Addr      5G          2G        */
-	{0x00016044, 0x049242c9, 0x049242c9},
+	{0x00016044, 0x0491c2c9, 0x0491c2c9},
 	{0x00016048, 0x64925a70, 0x64925a70},
 	{0x00016148, 0x00008050, 0x00008050},
 	{0x00016280, 0x42222000, 0x42222000},
@@ -1351,7 +1351,7 @@ static const u32 qcn550x_1p0_modes_no_xp
 
 static const u32 qcn550x_1p0_modes_no_xpa_table_5_tx_gain_table[][3] = {
 	/* Addr      5G          2G        */
-	{0x00016044, 0x049242c9, 0x049242c9},
+	{0x00016044, 0x0491c2c9, 0x0491c2c9},
 	{0x00016048, 0x64925a70, 0x64925a70},
 	{0x00016148, 0x00008050, 0x00008050},
 	{0x00016280, 0x42222000, 0x42222000},
@@ -1440,7 +1440,7 @@ static const u32 qcn550x_1p0_modes_no_xp
 
 static const u32 qcn550x_1p0_modes_no_xpa_green_tx_gain_table[][3] = {
 	/* Addr      5G          2G        */
-	{0x00016044, 0x849242e4, 0x849242e4},
+	{0x00016044, 0x8491c2e4, 0x8491c2e4},
 	{0x00016048, 0x64925a70, 0x64925a70},
 	{0x00016280, 0x42222000, 0x42222000},
 	{0x00016284, 0x0060800b, 0x0060800b},
```

```
--- vals_dlink_dap-2682.h
+++ vals_tplink_archer-a9-v6.h
@@ -36,7 +36,7 @@ static const u32 qcn550x_1p0_baseband_co
 	{0x00029d14, 0x00c0040b},
 	{0x00029d18, 0x00000000},
 	{0x00029e08, 0x0038230c},
-	{0x00029e24, 0x990bb515},
+	{0x00029e24, 0x990bb514},
 	{0x00029e28, 0x0c6f0000},
 	{0x00029e30, 0x06336f77},
 	{0x00029e34, 0x6af6532f},
```

