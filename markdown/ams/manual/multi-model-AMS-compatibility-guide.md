---
title: 多机型 AMS 连接指南
url: https://wiki.bambulab.com/zh/ams/manual/multi-model-AMS-compatibility-guide
category: AMS > 用户手册
updated: 2026-11-10T08:46:58.078Z
---

### 使用 AMS 连接打印机

使用 AMS 与打印机连接时，需根据打印机机型，选用适配的 AMS 型号、缓冲器，并为多台 AMS 连接的场景匹配对应的料管拓展口。

#### AMS

Bambu Lab AMS 分为一代 AMS、AMS 2 Pro、AMS HT 以及 A 系列专用的 AMS lite。

> 注意 ：AMS 自带 6-pin 线缆台阶高度为 1.1 mm，AMS 2 Pro 自带 6-pin 线缆台阶高度为 2.5 mm。
>
>
> ![image6.png](https://wiki.bambulab.com/ams-2-pro/troubleshooting/ams2pro-communication-anomalies/image6.png)

AMS、AMS 2 Pro 和 AMS-HT（后文统称 AMS）均为两级进料，由内部的上下料组件（#1）将耗材送入助力电机（#2）后，助力电机继续将耗材送入打印机的工具头。

由于工具头挤出机消耗的速度和助力电机送料的速度很难完全一致，因此 AMS 连接打印机时必须通过缓冲器 。

![二级进料.png](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/%E4%BA%8C%E7%BA%A7%E8%BF%9B%E6%96%99.png)

而 AMS lite 为一级进料，耗材由上下料组件直接送入工具头，因此无需通过缓冲器。

![ams_lite1.jpg](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/ams_lite1.jpg)

> 注意：AMS lite 仅兼容 A 系列打印机，且单台 A 系列设备仅允许连接一台 AMS lite。

#### 缓冲器

介绍： 缓冲器上滑块的滑行距离为耗材提供了一段缓冲长度，AMS 会根据滑块所处位置，及时助力送出耗材，并且不影响工具头挤出。

![图片](https://wiki.bambulab.com/ams/ams-function-introduction/ams%E5%8A%A9%E5%8A%9B.gif)

类型：

| 机型 | 缓冲器 | 购买链接 |
| --- | --- | --- |
| A 系列 | 〔图片〕 | A 系列料线选通器 |
| X1/P1 系列 | 单台 AMS： 多台 AMS： 〔图片、图片〕 | 供料选通器 料线选通器 |
| P2S | 〔图片〕 | P2S 供料缓冲器 |
| H2 系列 | H2D/H2C： H2S： 〔h2dbuffer.avif、h2sbuffer.avif〕 | H2D/H2C 供料缓冲器 H2S 供料缓冲器 |
| X2D | 〔filament_buffer-x2d.png〕 | X2D 供料缓冲器 |

#### 料管拓展口

介绍： 料管拓展口为“四进一出”结构，目的是并联多个 AMS 的料管，满足更多耗材的使用需求。
类型： 料管拓展口分为普通料管拓展口和 H2 系列专用料管拓展口。其中 H2C 打印机需使用 H2 系列专用料管拓展口；P2S 和 X2D 需使用普通料管拓展口； 其他型号打印机可根据需求选购。

| 类型 | 图片 | 购买链接 |
| --- | --- | --- |
| 料管拓展口 | 〔图片〕 | 料管拓展口 |
| H2 系列专用料管拓展口 | 〔图片〕 | H2 系列专用料管拓展口 |

### AMS 连接指南

> 请点击下列按钮，选择您的打印机型号，以查看对应打印机的连接指南。

H2 系列 X2D X1 /P1 系列 P2S A1 系列 A2L

- 最大连接数量 ：最多支持 同时连接 4 台 AMS 2 Pro 和 8 台 AMS HT。
- 多色打印支持 ：由于 H2C/H2D 为双喷嘴打印机，且最极限的场景可以把所有连接的 AMS 2 Pro/HT 全部连接到同一个喷嘴上，另一个喷嘴使用外挂料盘进料，所以最多可以打印的颜色为 4*4+8*1+1（外挂料盘）= 25 色 。 H2S 为单喷嘴打印机，所以最多支持 24 色 打印。
- 配件需求 ：内置缓冲器， 无需额外购买 ；部分场景需要购买 [料管拓展口](https://wiki.bambulab.com/zh/ams/manual/multi-model-AMS-compatibility-guide#%E6%96%99%E7%AE%A1%E6%8B%93%E5%B1%95%E5%8F%A3) 。

> AMS 与 H2D/H2C 的连接方式相同，可根据需求进行调整，具体请参考： [H2C + 多台 AMS 连接指南](https://wiki.bambulab.com/zh/h2c/how-to-connect-ams) 。

##### 线缆连接

每台 AMS 背部都有两个 6-pin 口，能够串联起多台 AMS 设备，满足供电与通信需求。

![图片](https://wiki.bambulab.com/ams-2-pro/manual/6pin%E7%BA%BF%E7%BC%86.png)

> 注意：连接 AMS 2 Pro 或 AMS HT 时，请务必使用标配的新版本 6-pin 连接线，若使用上一代 AMS 的 6-pin 连接线可能导致 AMS 与打印机的通信不稳定，而上一代 AMS 可以兼容新版本的 6-pin 连接线。

##### 料管连接

H2D/H2C ：

- H2D/H2C 的缓冲器具备两个进料口，如果使用一台 AMS + 外挂料盘，或同时使用两台 AMS，可以直接连接在缓冲器上。

![图片](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/amspro&ht_22.jpg)

- 如需同时使用 2 台 AMS + 外挂料盘，或使用 3 台及以上数量的 AMS ，需要 使用料管拓展口 拓展。 打印机和每台 AMS 之间必须有缓冲器 ；因此连接多台 AMS 时，料管拓展口需要连接在 AMS 与 缓冲器之间，请勿接反。

![料管拓展口](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/img_v3_00km_beb23ea0-305b-4dc9-8505-5c35d40b16dg.jpg)

> 注意： ：H2C 设备需要使用 H2C 专用料管拓展口 。
>
>
> ![图片](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/h2c_%E4%B8%93%E7%94%A8%E6%96%99%E7%AE%A1%E6%8B%93%E5%B1%95%E5%8F%A3.png)

- 最大连接数量：同时连接 4 台 AMS 2 Pro 和 8 台 AMS HT；

![图片](https://wiki.bambulab.com/ams-2-pro/manual/%E6%96%99%E7%AE%A1.png)

H2S：

- 由于 H2S 为单头打印机，因此 H2S 连接两台 AMS 时，也需使用料管拓展口。

![图片](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/3.jpg)

- 最大连接数量 ：最多支持 同时连接 4 台 AMS 2 Pro 和 8 台 AMS HT。
- 多色打印支持 ：由于 X2D 为双喷嘴打印机，且最极限的场景可以把所有连接的 AMS 2 Pro/HT 全部连接到同一个喷嘴上，另一个喷嘴使用外挂料盘进料，所以最多可以打印的颜色为 4*4+8*1+1（外挂料盘）= 25 色 。
- 配件需求 ：超过两台 AMS 的连接场景需要购买 [料管拓展口](https://wiki.bambulab.com/zh/ams/manual/multi-model-AMS-compatibility-guide#%E6%96%99%E7%AE%A1%E6%8B%93%E5%B1%95%E5%8F%A3) 。

##### 线缆连接

每台 AMS 背部都有两个 6-pin 口，能够串联起多台 AMS 设备，满足供电与通信需求。

![x2d-cable.jpg](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/x2d-cable1.jpg)

> 注意：
>
>
>
> - 连接 AMS 2 Pro 或 AMS HT 时，请务必使用标配的新版本 6-pin 连接线，若使用上一代 AMS 的 6-pin 连接线可能导致 AMS 与打印机的通信不稳定，而上一代 AMS 可以兼容新版本的 6-pin 连接线。
> - X2D 未连接外排风扇时，缓冲器的两个 6-pin 接口均可连接 AMS 设备。

##### 料管连接

- 最大连接数量：4 台 AMS 2 Pro + 8 台 AMS HT + 外挂料盘；

![tube_connection.jpg](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/tube_connection.jpg)

- 仅使用一台 AMS + 外挂料盘，或同时使用两台 AMS 时，可直接连接在缓冲器上；

![ams-external-spool.jpg](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/ams-external-spool1.jpg)

- 使用 2 台 AMS + 外挂料盘，或使用 3 台及以上数量的 AMS 时，需使用 料管拓展口 。

![x2d-ams.jpg](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/x2d-ams.jpg)

> 注意： 打印机和每台 AMS 之间必须有缓冲器 。因此使用多台 AMS 时，料管拓展口需要连接在 AMS 与 缓冲器之间，请勿接反。
>
>
> ![4-in-1-x2d.jpg](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/4-in-1-x2d.jpg)

- 最大连接数量 ：X1/P1 最多支持同时连接4台 AMS 2 Pro 或 4 台 AMS HT，一共4台。
- 配件需求 ：
  - X1/P1 连接 1 台 AMS 时，需自行购买 [供料缓冲器，进料管接头，4-pin线](https://detail.tmall.com/item.htm?id=906162436922&pisk=ga-ocFAhwU77MNPqjWSSkanhEi0v2gsCtBEd9MCEus5XvUCKPDDhid7-FBdpo6A2i_JR9YtHoQ9NyBvIF95eTBfpyqn9FLsCYfInXcpWrL6MMQfUztkFLT4EHazRYdDNYfhtXreVPbIeexJlJEJVG9qPL9RUusWRg9WUYB5VuOWTaMSeTxjVKOazazrF0ZW1g85FLazVuO6Q887F8xvVG9XPYMRF0xXCg6SFYbsbY1xecnlNATRo96ZJ0Tbl_L5yeLK43aUWEsxBvnWkEwJzdkremTbkmLeAcgQJ8d_62do3cgpMuiWHAAzhtNYe2i-rgc7f8nRV3QHLRtYHLhs5jJoyngfl7n7Sxvdwnp8OonHZfgjPaeIWpRcJn3AJFnvLLrSl2EbMqGo_a6LvIHXHAXiDspJ68Zx3ZgWUuP7L_k6qpnzQRaWfn13Oq2A5ibg3bxD054_PhThtnx4QRaWfn1HmnPN5zt6-6&skuId=5766287773398&spm=pc_detail.30350276.guessitem.d1) 。
  - X1/P1 连接多台 AMS 时，需要购买 [料线选通器](https://detail.tmall.com/item.htm?id=693987695729&pisk=gzhiYqi0XAy1dnSeZiP6pRd0SWvK-5NbmmCYDSE2LkrIMAEvCIY0x4y95mnxKomExluTDFGmKcgzBm0X5rrq0mqxBpd-5VNbg3FDwQ3sIVaovcXauy84oPXwJRWTg4Yzg3KJw9QUChFqWeu0jXuUArfauroVLkzTYrWagmrULzzRbSPq0eVUoz6NbO54TJz7Yt7abO7FYz4GQGyVQe0UArP40myw-2rQuSrqgg54qjlIT3Pb7cxYSMl8SRqr7lutWX7UpOgUxHxEtAca43Ehgsl3SqrJfiCkHuk7X8EmYBCgi2zmx8HMq1mmu4M4KjjwW0oEnmzIdnX0qxutFxyH7Cu3sl2q9D7fB5Dqfj2sIZTS85oIFuwwdHan6be0VJjeb233b8DmXH14XY0Ex8hdv_FrFDc0U7Sy49WzHg5b8EhFhtwaRyqJe5vmfkx6n_8H-T9_Qya92eYhhtwaRyqJ-eX5fRzQW3C..&spm=pc_detail.30350276.guessitem.d3&skuId=4927627985197) ， [进料管接头](https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-25177047232.29.22ee3c0eBzRKFx&id=707575712100&rn=badc7578a26628b4999a1abad3488a03&abbucket=10&pisk=gRYx0x_cHYDDo0uSprmkSmjWLGhoq0A4yKRQSOX0fLpJBdIm_svGWGBJOic2IdxRBL9Rhrcq0G693TvgSIY94Pde_EcVSj72gN7sKv0HBIRV73rXT5YYP81DNr1150b7re2lNv0n-QdV7NMnKnmW0a1ltP_1ctO5NT5gh191cQO5U15_hN6jwQ6PFr11hO_5N11dGNaf58a5O6efGGsXNQ6P1N66CNGRPT515O915jnZBTNfIPKWY9AlnDfz5PTRMgikGTg6aU1vD9dXyPa__sIAdI6-HxouegONXFPaWMOXYd5Bh-MOQUdWlH9IEoXXv1dHXIgbPZY2GHs6RAr6pZpOAEs81yO2GtbRNeGgYTYRndTAVX4djaThAZto4xjGk6p6uKFT5pOktESyWve5QnfFP1LZOlBOfg5H-eeRNJXdsoG-wlrNc_SnMV7VMlbXo_BnMVEabglPw9c-wlrNc_5RKjhTblSra) ， [4-pin线](https://detail.tmall.com/item.htm?id=694052067560&pisk=g7IZYIfHklEZVTPlUTx48xl27sK9GnP7QiOXntXDCCAgMRpD011Hom6_W-y2Tsd65hb6nm5BOsifCi7K0TBAfRKbBhB9DnV7Nu1VBOKxTjgGAGlnxd6HnjvgRHqchSc3NuZ5BPv9c9V55ybOxp9DmdAMo22eUKHMmEvGKJJDhf0mjsX3LBp2nfvijkDHhKiDmK0MK9vWhI0mjd0hKBpDmIfDmJ-H9KxDisxmgPBGnDJWSR5X3q7Iz7YJZOAEm0kJQF0Vpqir49JM7gAwTeTCYd8wZERpk2jGOtj1XeUZSnBCzs7cZWg6saJPTU_aac5P6KX2n1r-UBjN3M8ORf0MUhRwrGYZF8BBowSefGVxy96esU-CRyF6lh5NyQLgJWCVLC1cbecaOI_5dGYFZWiFME7cfHjgtuSr2jpHevSA7j02SppeNJyUxtA7eh2Xux3xkexJLQw6Cq3vSppeNJyEkqLHepR7Cd1..&spm=pc_detail.30350276.guessitem.d2&skuId=4926397845849) 。
  - 部分场景需要购买 [料管拓展口](https://wiki.bambulab.com/zh/ams/manual/multi-model-AMS-compatibility-guide#%E6%96%99%E7%AE%A1%E6%8B%93%E5%B1%95%E5%8F%A3) 。

##### 连接 1 台 AMS

##### 连接多台 AMS

- 最大连接数量 ：P2S 最多支持同时连接 4 台 AMS 2 Pro 和 4 台 AMS HT，一共 8 台，合计 20 个槽位。
- 配件需求 ：
  - P2S-Combo 自带缓冲器， 无需额外购买 ；
  - P2S 单机 + AMS 单机时，还需要购买 [P2S 供料缓冲器](https://wiki.bambulab.com/zh/ams/manual/multi-model-AMS-compatibility-guide#%E7%BC%93%E5%86%B2%E5%99%A8) 。
  - 部分场景需要购买 [料管拓展口](https://wiki.bambulab.com/zh/ams/manual/multi-model-AMS-compatibility-guide#%E6%96%99%E7%AE%A1%E6%8B%93%E5%B1%95%E5%8F%A3) 。

##### 线缆连接

缓冲器上有两个 6-pin 插口，可同时连接多台 AMS；AMS 背部也有两个 6-pin 插口，能够相互串联，满足多台 AMS 供电和通信。

![图片](https://public-cdn.bblmw.com/wiki/new/p2s/manual/diagram1compressed.png)

> 注意：
>
>
>
> - 连接 AMS 2 Pro 或 AMS HT 时，请务必使用标配的新版本 6-pin 连接线，若使用上一代 AMS 的 6-pin 连接线可能导致 AMS 与打印机的通信不稳定，而上一代 AMS 可以兼容新版本的 6-pin 连接线。
> - 不支持同时将两台 AMS 设备连接 P2S 缓冲器的两个 6-pin 接口，其中一个接口为备用口，用于为外设（如延时摄影套件）供电及通信扩展。

##### 料管连接

- 连接 3 台以下数量的 AMS 时，可直接连接在缓冲器上。

![p2s_ht_ams_2.png](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/p2s_ht_ams_2.png)

- 连接 3 台及以上数量的 AMS 时，需要使用料管拓展口，实现“多进一出”的功能。

> 打印机和每台 AMS 之间必须有缓冲器 。因此使用多台 AMS 时，料管拓展口需要连接在 AMS 与 缓冲器之间，请勿接反。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

- 最大连接数量 ：最多支持同时连接 4 台 AMS，可任意搭配（具体请参考： [A 系列 AMS 连接教程](https://wiki.bambulab.com/zh/a1/manual/ams-connection-guide) ），或仅连接一台 AMS lite。

![a1-ams.png](https://wiki.bambulab.com/a1/ams-connection-guide/a1_ams.png)

- 配件需求 ：需购买 [A 系列料线选通器](https://wiki.bambulab.com/zh/ams/manual/multi-model-AMS-compatibility-guide#%E7%BC%93%E5%86%B2%E5%99%A8) 。

![img_v3_02q7_a49d9f49-25a8-49bb-b540-10798bbd15cg.jpg](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/img_v3_02q7_a49d9f49-25a8-49bb-b540-10798bbd15cg.jpg)

- 固件适配计划 ： 请将打印机升级至 01.07.00.00 及以上版本。

> 注意： 请勿使用 AMS 自带的缓冲器或 AMS Hub 连接 A 系列打印机至 AMS，否则会导致缓冲器或 AMS Hub 使用功能异常或损坏，在此种情况下，该缓冲器或 AMS Hub 将不予保修。因此，请您使用 A 专用的料线选通器 连接 AMS。

- 最大连接数量 ：最多支持同时连接 4 台 AMS 和 1 台 AMS lite，（具体请参考： [A2L AMS 连接指南](https://wiki.bambulab.com/zh/a2l/manual/a2l-ams-connection-guide) ），最多可实现 19 色打印；

![image_(85).png](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/image_(85).png)

- 配件需求 ：A2L 连接一台 AMS 时，无需额外购买任何配件，直接将打印机与 AMS 通过料管中继接头（工具盒内）连接即可；如需连接两台及以上 AMS，则需购买 [料管拓展口](https://wiki.bambulab.com/zh/ams/manual/multi-model-AMS-compatibility-guide#%E6%96%99%E7%AE%A1%E6%8B%93%E5%B1%95%E5%8F%A3) 。

##### 线缆连接

打印机背部有 1 个 6-pin 插口，可直接连接 AMS 设备；AMS 背部有两个 6-pin 插口，可相互串联多台 AMS，满足多台 AMS 供电和通信。

![image_(86).png](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/image_(86).png)

##### 料管连接

- 连接一台 AMS：可直接将 AMS 料管连接至料管中继接头；
- 连接多台 AMS：需用一段 70mm 左右的料管连接料管中继接头和料管拓展口，然后将多台 AMS 的料管连接至料管拓展口，可参考下图。

![料管连接.jpg](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/%E6%96%99%E7%AE%A1%E8%BF%9E%E6%8E%A5.jpg)

###拓竹H3C

- 最大连接数量 ：最多支持 同时连接 4 台 AMS/AMS 2 Pro/AMS HT。
- 多色打印支持 ：可将 4 台 AMS 2 Pro 全部连接到 1 号打印头，并使用 AMS 3H 中的 8 个槽位，所以最多可以打印的颜色为 4*4+8 = 24 色 。
- 配件需求 ：需自行购买拓竹H3C 缓冲器；部分场景需要购买 [料管拓展口](https://wiki.bambulab.com/zh/ams/manual/multi-model-AMS-compatibility-guide#%E6%96%99%E7%AE%A1%E6%8B%93%E5%B1%95%E5%8F%A3) 。

> 具体请参考： [拓竹H3C 连接多台 AMS 指南](https://wiki.bambulab.com/zh/h3c/manual/ams-connection-guide) 。

### AMS 烘干功能要求

有关 AMS 烘干功能的详细信息，请参考： [AMS 2 Pro 与 AMS HT 耗材烘干指南](https://wiki.bambulab.com/zh/ams-2-pro/manual/drying-function) 。

#### AMS 2 Pro 烘干供电要求

- H2 系列/P2S 连接一台 AMS 2 Pro 时，可直接通过打印机取电进行烘干，无需额外配件；
- H2 系列/P2S 连接多台 AMS 2 Pro 时，仅其中 1 台可使用打印机供电，其余需通过 专用电源适配器（需单独购买） 独立供电。

-
- H2 系列/P2S/X2D 连接多台 AMS 2 Pro 时，仅其中 1 台可使用打印机供电，其余需通过**专用电源适配器（需单独购买）** 独立供电。
-

- X1/P1/A 系列使用 AMS 2 Pro 烘干, 每台 AMS 2 Pro 都 必须通过电源适配器 供电才能使用烘干功能。

> 注意：如果 打印机正在进料或者打印，且同时使用打印机供电给 AMS 2 Pro 进行烘干，为了优先确保打印功率，烘干功率自动会降低 ，建议外接电源适配器以获得更好的烘干效果。

> 注意 ：AMS 2 Pro 官方电源适配器规格为 24V 4A。为确保设备安全与正常使用， 请务必使用官方配件。使用第三方适配器可能会导致设备损坏，并影响保修权益 。

|  |  |
| --- | --- |
| 〔图片〕 | 〔图片〕 |

#### AMS HT 烘干供电要求

无论连接什么型号的打印机， 每台 AMS HT 都需要外接电源才能启用烘干，不支持从打印机取电烘干（电源线标配，无需额外购买）。

![图片](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/image-1.png)

#### 烘干功能通信要求

使用烘干功能的时候， AMS 2 Pro/HT 必须通过 6-pin 连接线与打印机连接通信，不支持离线烘干模式。

> 注意：请务必使用 AMS 2 Pro 和 AMS HT 标配的新版本 6-pin 连接线，若使用上一代 AMS 的 6-pin 连接线可能导致 AMS 与打印机的通信不稳定，而上一代 AMS 可以兼容新版本的 6-pin 连接线。

### 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
> 如果本指南未解决您的问题， [请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5) ，我们随时准备为您解答疑问并提供帮助。
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
