---
title: TPU 送料助力模块组装 & 使用指南
url: https://wiki.bambulab.com/zh/general/manual/tpu-feed-assist-module
category: 拓竹打印机通用知识篇 > 使用手册
updated: 2026-11-03T03:02:31.654Z
---

### 一、概述

TPU 送料助力模块是一款专为 柔性耗材打印 设计的增强组件。本套件提供核心的挤出机组件、主控板及各类连接件， 需自行打印外壳与框架 进行组装；该组件核心功能如下：

1. 降低 TPU 耗材在各种摆放场景下的进料阻力，有效解决柔性耗材进料卡顿、断料问题，大幅提升 TPU 打印的稳定性和成功率。
2. 简化 TPU 打印的进料流程，减少打印前的准备工作，支持封箱打印，可直接从 TPU 专用进料口进料，操作更便捷。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/036.jpg)

关于 TPU 送料助力模块高频疑问解答 （点击此处查看）

1. TPU 进料助力器是否可以连接到左侧热端使用？

可以。但 TPU 进料助力器连接至左侧热端时，仅支持单材料打印，不支持左右混打。因为多材料打印时左侧热端需要升降，易造成 TPU 耗材堵塞。

2. 助力模块连接右侧热端时，左侧热端是否可以打印支撑材料？

可以。左侧热端打印硬质支撑材料，不会影响右侧热端的柔性材料打印。

3. 使用该助力模块是否需要将打印机更新至特定版本固件？

不需要。该助力模块仅由打印机供电，与打印机之间无通讯交互。

4.打印机接头连接的 AMS 无多余接口，助力模块是否可以连接 AMS 上的 6PIN 接口？

可以。套件内配有 6PIN 转 4PIN 转接头，助力模块可通过该转接头由 AMS 的 6PIN 接口供电。

5. TPU 送料助力模块支持的最软 TPU 型号是什么？

85A，若使用硬度低于该型号的 TPU，可能导致模块卷料。

6. TPU 送料助力模块支持的最硬 TPU 型号是什么？

95A-HF，该组件专为柔性耗材优化，不推荐使用硬度高于 95A-HF 的耗材，否则易出现刨料问题。

7. 该模块是否必须与 TPU 高流量热端搭配使用？

不强制搭配。TPU 高流量热端仅适配 H2D 系列机型，且需安装于右热端；TPU 送料助力模块可单独使用，与该热端配合使用更佳。

### 二、适用机型

拓竹 H2S/H2D/H2D Pro/H2C、X1/X1C/X1E/X2D、P1P/P1S/P2S

> 📌 注意事项：
>
>
>
> 1. 当 H2D 左热端连接 TPU 送料助力模块时，不支持多色或多材料打印（无法同时使用左右热端）。原因在于：左热端升降动作会影响助力模块的送料稳定性，进而导致挤出机堵塞。
> 2. TPU 送料助力模块需搭配外挂料盘使用，不支持 AMS 自动上下料功能，仅支持通过 AMS HT 的 TPU 专用出料口手动进料。
> 3. 若在使用过程中遇到异常或故障，可参考故障排查文档： [TPU 送料助力模块常见故障排查](https://wiki.bambulab.com/zh/general/troubleshooting/tpu-feed-assist-module) 进行处理。
> 4. P2S 单机版本 没有配置适用于 P2S 的缓冲器，您需要额外购买 P2S 缓冲器 配合 TPU 送料助力模块的使用。（购买链接： [京东](https://item.jd.com/10194454014780.html?pcdk=IP8IVu_upGJI6baBBUoJUNsuMiI6eq2mtKUUxvoPD1w%3D.M8AW.sbc1) ； [天猫](https://detail.tmall.com/item.htm?abbucket=15&id=985866098141&mi_id=0000uoCE1MpHjzaN710PrTLvTml5YbBPVx7JNyBehb_hv38&ns=1&priceTId=2147839017745789786753783e191e&skuId=6114711638942&spm=a21n57.1.hoverItem.2&utparam=%7B%22aplus_abtest%22%3A%224c72eaec90ea905ee181097a30b88230%22%7D&xxc=taobaoSearch) ）。

### 三、准备工作

#### 3.1 硬件清单

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/004.jpg)

| 序号 | 名称 | 序号 | 名称 |
| --- | --- | --- | --- |
| 1 | 按键开关板 x3 | 2 | 挤出机组件 |
| 3 | 160mm 料管 | 4 | 275mm 料管 |
| 5 | 单通接头 | 6 | 4PIN 转 6PIN 接头 |
| 7 | 主控板 | 8 | 4PIN 线缆 |
| 9 * | 1 分 4 线缆 | 10 | BT3x10 & ST3x12 螺丝 |
| 11 * | BT2.6x8 螺丝 |  |  |

> - BT 3x10 用于固定上框架和主控板，ST 3x12 用于固定助力模块支架。
>   ![pixpin_2026-03-25_11-01-18_compressed.jpg](https://wiki.bambulab.com/general/pixpin_2026-03-25_11-01-18_compressed.jpg)
> - 1 分 4 线缆中最长的那条双股线缆可能有不同的颜色（例如黄色、灰色或白色）。仅颜色有所差异，其长度和功能完全相同，因此无论您收到的是哪种颜色，均可按教程进行操作。

#### 3.2 打印件清单

助力模块主体建议选用深色，导光柱建议选用白色，以实现更佳的灯光指示效果。
🔎 模型下载地址： [TPU 送料助力套件](https://makerworld.com.cn/zh/models/2277931-tpusong-liao-zhu-li-mo-kuai-wai-ke-yu-kuang-jia#profileId-2567194)

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/038.jpg)

| 序号 | 名称 | 序号 | 名称 |
| --- | --- | --- | --- |
| 1 | 助力模块支架（不同机型有所差异） | 2 | 下框架 |
| 3 | 后盖 | 4 | 导光柱 |
| 5 | 上框架 | 6 | 外壳 |
| 7 | 按钮 |  |  |

### 四、安装视频

> 🔎 查看 [其他机型](https://wiki.bambulab.com/zh/general/manual/tpu-feed-assist-module#install) 安装指南。

### 五、组装指南

> 首次组装建议按照步骤操作避免遗漏。

取出自行打印好的外壳和后盖板，按照下图所示，移除 5 个位置的支撑结构。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

将 3 个按钮分别对准上框架的按钮安装孔，轻轻按压到位。安装完成后，效果如下图所示。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

将 3 块按键开关板对应安装到上框架的开关板安装位。 重点注意： 开关板的接口朝向需与下图一致，避免装反导致后续返工。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

使用 BT2.6x8 螺丝，共 6 颗，分别锁紧 3 块按键开关板（每块开关板对应 2 颗螺丝）。安装完成后，手指按压每个按钮，检查手感是否正常，确保按钮能快速回弹、无卡顿。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

取出 1 分 4 线缆，按照下图所示的线序，将线缆一端连接到 3 块按键开关板的接口上。 重要提醒 ：线序必须与图示一致，连接错误会导致模块启停异常、按键失灵。

> 最长的双股线仅能安装在最上方按键开关板。该双股线可能有不同的颜色（例如黄色、灰色或白色）。仅颜色有所差异，其长度和功能完全相同，因此无论您收到的是哪种颜色，均可按教程进行操作。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/012.jpg)

将预组装好的挤出机组件，对准上框架的挤出机安装位，轻轻推入，确保挤出机与下图标注的定位处完全对齐。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

挤出机组件安装完成后，开始整理线缆将 按键开关线缆 和 电机线 ，逐一卡入上框架的理线扣内，避免后续安装外壳时被挤压。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/011.jpg)

找到 1 分 4 线缆的黑线，将其对应连接到霍尔小板的接口上。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/041.png)

将下框架对准上框架的拼接位，然后使用 2 颗 BT3x10 螺丝，分别锁紧上下框架的固定孔。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

移除主控板背部的醋酸胶带，然后将主控板对准下框架的安装位，使用 BT3x10 螺丝，将主控板固定在下框架上。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

将挤出机组件的电机线缆插入主控板上对应的电机接口，确保接口插紧、无松动。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/053.webp)

将灯珠安装至靠下位置，白色导光柱安装至上部，确保贴合紧密。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

将 1 分 4 线缆的另一端，插入主控板上对应的接口,完成后整理线缆至走线槽内。重要注意： 线束不要超出 PCB 板 ，避免后续安装外壳时，线缆被外壳挤压。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/003.jpg)

将外壳套入组装好的助力模块主体，确保外壳与上下框架贴合。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/046.webp)

使用 4 颗 BT2.6x8 螺丝，分别对准外壳的 4 个固定孔，逐一锁紧。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

将打印好的后盖，对准模块后部的安装位，然后使用 4 颗 BT2.6x8 螺丝，逐一锁紧后盖。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

组装完成后，效果如下图所示。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/020.jpg)

### 六、 不同机型装配指南

H2D 搭配 AMS HT P2S X2D X1C/P1S

找到打印机背板右侧的 1 颗固定螺丝，使用 H2.0 内六角螺丝刀将其拧下，妥善保管螺丝（避免丢失）。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/021.jpg)

将打印好的助力模块支架，对准打印机背板的安装位，然后使用 ST3x12 螺丝，重新拧入并锁紧，固定好支架。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

将连接右侧挤出机的料管取下。

![图片](https://wiki.bambulab.com/h2/manual/h2d-tpu-printing-guide/image-1.png)

找到打印机右侧挤出机的 TPU 专用进料口，将右侧挤出机的料管从该进料口穿出，然后将单通接头安装到料管上。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

> 注意 ：单通接头需区分方向，黑色一端为进料口，蓝色一端为出料口，不要装反。
>
>
> ![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/040.png)

取出 275mm 长料管，将其一端连接到单通接头的黑色进料口一端；然后将 4PIN 线缆的一端连接到助力模块的对应接口上。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

> 注意： 此处料管长度仅支持 275mm ，过长或过短均可能导致进料阻力过大。

将组装好的助力模块，对准支架的安装位，轻轻插入并固定；然后将长料管的另一端，连接到助力模块的出料口。最后，将 4PIN 线缆的另一端连接到打印机的 4PIN 接口上。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

> 注：如果您的打印机机身后部没有 4PIN 接口，可使用 4PIN 转 6PIN 转接头，将 4PIN 线缆通过 AMS 进行取电。

取出 160mm 短料管，将其一端连接到助力模块的进料口。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/026.jpg)

P2S 多色版本的外挂料盘底座默认为左侧安装，需将其移至右侧安装。

![pixpin_2026-03-18_11-07-46_compressed.jpg](https://wiki.bambulab.com/p2s/manual/pixpin_2026-03-18_11-07-46_compressed.jpg)

取下蓝色卡扣，按压气动接头，移除外部料管。

![remove_ptfe_tube_001.png](https://wiki.bambulab.com/general/tpu-feed-assist-module/remove_ptfe_tube_001.png)

拆下原有的料盘支架，将 TPU 外挂支架安装至打印机，连接 160mm 料管并将 TPU 送料助力模块插入支架。由于 P2S 没有 4PIN 接口需要使用 6PIN转4PIN 接头进行转接。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

> 安装完成后，请检查 TPU 支架是否安装稳固、插接到位。

安装完后如下图所示：

![length.jpg](https://wiki.bambulab.com/general/tpu-feed-assist-module/1.jpg)

1. 将提前打印好的 TPU 助力模块支架安装至底座中；

![图片](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/010.webp)

1. 将 TPU 助力模块对准支架卡扣放置；

| 〔图片〕 | 〔图片〕 |
| --- | --- |

1. 取一根 160mm 左右的料管插入左挤出机进料口和助力模块出料口；

![图片](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/023.png)

1. 取一根 160mm 左右的料管，将一端插入助力模块的进料口；

![图片](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/024.png)

1. 取出一根 6-pin 线插入 4-pin 转 6-pin 接头;

![图片](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/011.webp)

1. 将 4-pin 插头插入助力模块底部接口中；

![图片](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/025-.png)

1. 线缆另一端插入缓冲器上的 6-pin 插口；

![图片](https://public-cdn.bblmw.com/wiki/new/x2d/manual/x2d-combo-unboxing/x2d_combo_unboxing_60.jpg)

1. 准备一小段料管，轻微弯折后，插入 AMS HT 尾部的出料口；

![图片](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/026.png)

1. 将耗材放入 AMS HT 内，并从 AMS HT 尾部料管拉出，送入助力模块;

> 为保证送料顺畅，请参考下图放置 AMS HT。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

将附赠的 275mm 长料管裁剪为 200mm。将料管对齐支架槽口，按图示位置裁切，即可得到 200mm 料管。

![length.jpg](https://wiki.bambulab.com/general/tpu-feed-assist-module/4.jpg)

在入料口处按压黑色圆环，拔下料管。

![图片](https://wiki.bambulab.com/ams/packing--guide/1.remove_ptfe_tube_connector.png)

拆下原支架固定螺丝，使用 ST3×12 螺丝 直接固定；将新的 200 mm 料管一端连接至打印机入料口，另一端连接至 TPU 送料助力模块，安装完成效果如下图所示。

![length.jpg](https://wiki.bambulab.com/general/tpu-feed-assist-module/2.jpg)

> 若您的机型为 P1P，可直接使用较短的 160 mm 料管 连接入料口与 TPU 送料助力模块。
> 若您的设备入料口处没有料管接头，可选择购买料管接头或使用更长的料管，从工具头直接连接到助力模块。

### 七、 使用说明

#### 7.1 按键功能说明

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/035.jpg)

1. 进料键：单击此按钮，模块进入进料模式并开启助力功能；再次按下该键可结束助力功能。
2. 指示灯：用于指示当前助力模块的工作状态。（常亮、闪烁）
3. 退料键：单击此按钮，模块进入退料模式并配合打印机完成退料操作；再次按下该键可停止退料。
4. 齿轮观察窗：可直观观察内部挤出齿轮的转动状态，判断是否正常进料/退料。
5. 助力调节键：用于调整助力力度，需配合进料键、退料键使用。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/001.jpg)

1. 出料口：用于连接打印机工具头，耗材从这里送入打印机。
2. 进料口：用于连接 AMS HT TPU 出料口 或外置耗材，耗材从这里进入助力模块。

| 功能或者状态 | 操作方法 | 灯语 |
| --- | --- | --- |
| 进料(助力)模式 | 单击进料键，即可进入助力模式；此时模块会根据校准值和当前档位，对推料力进行闭环控制，辅助耗材进料。 | 常亮 |
| 退料模式 | 单击退料键，模块进入退料模式，配合打印机完成耗材退出。 | 熄灭(和待机状态一致) |
| 助力调节 | 按住中间的助力调节键，同时按进料键（调大助力力度）或退料键（调小助力力度）；指示灯闪烁越快，代表助力力度越大；闪烁越慢，代表助力力度越小。 | 闪烁（闪烁频率随助力力度变化） |
| 未校准/校准失败 | 首次使用或校准未完成时，模块自动进入该状态；需按 7.2 校准步骤重新校准。 | 指示灯持续快闪 |

> 默认的助力力度（中档）能够满足大部分 TPU 打印需求，若打印过程出现异常，可根据耗材类型调整力度大小。
> 对于较软的耗材（如TPU 85A），若耗材缠绕在助力模块中，则需要降低力度；若打印出现异常，但耗材并未缠绕在助力模块中，可增加力度。
> 对于 95A 和 90A，如果料管阻力较大，助力模块无法将耗材推入挤出机，或打印速度较快时，可以 增大力度 。

#### 7.2 助力模块校准（出厂已校准，无持续闪烁无需复校准）

> 通常助力模块在出厂前已完成预校准；若模块指示灯未出现持续闪烁现象，则无需进行重复校准。

首次使用时，模块指示灯可能会出现 持续闪烁 的状态，这代表模块未校准或校准失败；此时虽然可以进料，但无助力闭环功能，且无法调节助力大小，需及时校准。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/058.webp)

> 校准之前请确保 助力器出料口 和 工具头 之间有料管相连。

准备一节长度 1 米 PLA/PETG 硬质耗材 ，手指 同时按住模块的进料键和退料键 ，此时指示灯会 快速闪烁 ，说明模块已进入校准状态。将准备好的硬质耗材一端，对准助力模块的进料口，轻轻插入，模块会 自动将耗材送入挤出机内 。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/057.webp)

当模块指示灯熄灭时，说明校准完成；此时可 点击退料键 ，将校准用的硬质耗材退出，校准流程结束。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

#### 7.3 进料步骤（TPU 90A 为例）

准备一小段料管，轻微弯折后，插入 AMS HT 尾部的出料口；然后将 TPU 耗材从 AMS HT 尾部拉出。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

> ℹ️ 提示 ：若料盘旋转不够顺畅，请检查 AMS HT 内的干燥剂，建议调整放置后保留一包即可。

单击助力模块的 进料键 ，指示灯 常亮 ，代表模块进入 助力状态 ，此时模块会自动开启助力功能，辅助耗材进料；将 TPU 耗材的一端送入助力模块，助力模块将自动把耗材送入挤出机内。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/056.webp)

接下来在打印机屏幕点击 进料 ，观察打印机喷嘴处，当有 TPU 耗材顺畅挤出时，即完成进料操作。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

完成进料后，您可以自由发起打印任务。

#### 7.4 退料步骤

> 请务必按照以下操作流程进行退料，操作顺序错误会导致耗材卡住或退料失败。

首先单击助力模块的 进料键 ，关闭助力模式（指示灯熄灭），然后拔下工具头进料口一端料管。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/042.webp)

> 拔下料管的目的：为退料预留物理空间并释放料管张力。若未拔除料管就在屏幕端执行退料，助力模块的挤出机会保持停止状态，而工具头端的挤出机会强制执行回退动作，两者步调不一致会导致耗材在料管内挤压，进而出现卡料现象。

接下来，在打印机屏幕上点击 退料 。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/033.png)

当屏幕弹出提示，此时点击助力模块 退料键 （指示灯不亮），此时耗材会从打印机工具头内缓慢退出。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

待耗材完全退出后，将耗材回卷至 AMS HT 内，完成退料操作；最后将工具头料管接回即可。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/045.webp)

> 若在使用过程中遇到异常或故障，可参考故障排查文档： [TPU 送料助力模块常见故障排查](https://wiki.bambulab.com/zh/general/troubleshooting/tpu-feed-assist-module) 进行处理。

### 八、原理介绍（了解即可，帮助更好地使用该助力模块）

TPU 送料助力模块的工作原理与缓冲器类似：耗材进料时，料线的推力会作用在模块内部的弹簧片上，使弹簧片发生形变；模块通过检测弹簧片的形变量，精准判断推料力的大小。

通过闭环控制技术，模块可根据不同档位，调节推料力的大小，同时实现与打印机工具头的联动控制，从而降低进料阻力，避免 TPU 耗材卡顿、断料，提升打印稳定性。

![图片](https://wiki.bambulab.com/general/tpu-feed-assist-module/044.webp)

> 注意 ：出料气动接头与弹簧片是一体连接的，操作过程中务必避免弹簧片受到外力挤压、碰撞，否则会导致模块检测异常，无法正常工作。

### 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
> 如果本指南未解决您的问题， [请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5) ，我们随时准备为您解答疑问并提供帮助。
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
