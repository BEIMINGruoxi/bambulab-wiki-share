---
title: E1 空气净化器开箱和安装指南
url: https://wiki.bambulab.com/zh/e1/manual/unboxing-installation-guide
category: E1 > 使用手册
updated: 2026-11-11T03:21:19.485Z
---

拓竹 E1 净化器是用于拓竹 3D 打印机的空气过滤设备，可在打印过程中对打印机内部空气进行循环净化，减少打印过程中产生的气味、颗粒物和挥发性有机化合物外逸，为您提供更清洁、更安全的打印环境。

本文将介绍 E1 净化器的安装与使用方法，并提供打印机适配信息、固件要求及使用相关的注意事项。

![bambu_lab_e1_purifier.jpg](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/bambu_lab_e1_purifier.jpg)

### 适配机型及要求

拓竹H3C, H2S, H2D, P2S¹ 打印机升级固件后，即可使用 E1 净化器的全部功能（自动模式和手动模式），并可在打印机端查看、设置净化器功能；

其他 封箱机型² 仍可通过手动模式使用净化器，但无法与净化器自动联动，也无法在打印机端控制净化器，待适配固件版本发布后，即可升级固件，使用净化器的全部功能。

A1 mini 加装泡泡罩后，也可通过手动模式使用净化器，但无法与净化器自动联动，也无法在打印机端控制净化器。

> 提示
>
>
>
> 1. P2S 单机版无 6-pin 接口，需另购并安装缓冲器，否则无法支持自动模式；安装步骤请参考： [更换 P2S 缓冲器](https://wiki.bambulab.com/zh/p2s/maintenance/replace-filament-buffer) 。
> 2. P1P 用户需另购并安装 P1P-P1S 升级包；安装步骤请参考： [P1P-P1S 升级包安装指引](https://wiki.bambulab.com/zh/p1/manual/p1p-to-p1s) 。

### 外观介绍

![1_appearance_overview.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/1_appearance_overview.png)

|  |  |  |  |
| --- | --- | --- | --- |
| 1 | 风速按钮 | 2 | 开/关按钮 |
| 3 | 显示屏 | 4 | 后盖 |
| 5 | 进风口 | 6 | 电源插座 |
| 7 | 6-pin 接口 | 8 | 出风口 |

### 安全提示

使用前，请确保：

- 净化器外观完好、无损坏。
- 已关闭电源开关。
- 滤芯已平稳安装至净化器内部。

放置要求：

- 在净化器 前方预留 5 厘米、后方预留 20 厘米 的工作空间，并避免风管过度弯折。
- 请勿在净化器上放置任何物品。

电源要求：

- 请务必使用净化器自带的电源线。
- 请勿过度拧捏、弯折或扭转电源线，避免线芯折断或外漏，造成安全风险。
- 在维护或者移动净化器前，请务必先断开电源。

使用过程中，请注意：

- E1 净化器仅限于配合拓竹 3D 打印机使用，用于过滤 3D 打印过程中产生的废气，不可用于激光排烟。
- 移动净化器前，务必先断开电源；严禁通过拉扯电源线来移动净化器。
- 如果出现异响、异味、高温、风扇不规则旋转等异常情况，请立即断开电源、开窗通风、并停止使用。
- 请勿倾斜净化器，或者倚靠、坐在净化器上。
- 由于净化器无法过滤一氧化碳 （CO） 或氡 （Rn），因此在发生燃烧和危险化学品事故时，不能将净化器用作安全设备。
- 同时使用净化器和燃气灶、燃气热水器等家用燃气用具时，请注意通风换气，避免一氧化碳 （CO） 中毒。
- 请勿从进/出风口内放入液体、粉末、可燃物或任何异物。
- 滤芯严重堵塞时，请立即断开电源并停止使用，否则会缩短净化器的寿命，甚至造成损坏。
- 更换滤芯时，请使用官方滤芯，以确保最佳的过滤效果。更换滤芯的步骤请参考这篇 Wiki： [E1 滤芯更换指南](https://wiki.bambulab.com/zh/e1/maintenance/replace-purifier-air-filter) 。

### 包装内配件

![2_included_accessories.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/2_included_accessories.png)

1. 主机
2. 风管转接口
3. 外排转接件
4. 密封圈
5. 风管
6. 6-pin 连接线
7. 电源线

### 视频指南

### 安装前准备

#### 升级固件

安装前，务必完成打印机的固件版本升级，确保设备兼容性。

- 拓竹H3C：01.01.00.00 版本及以上
- H2D：01.04.00.00 版本及以上
- H2S：01.03.00.00 版本及以上
- P2S：01.03.00.00 版本及以上

#### 准备工具与材料

- H2.0 内六角扳手
- 排气风管（选配） ：如需将过滤后的空气排放至室外，可提前准备或购买排气风管，并参考安装步骤 6 进行安装。
- 螺丝包 ：H2 系列打印机需另购 BT3x8 螺丝；P2S（旧背板）、X1 系列、P1 系列需另购 ST3x8 螺丝，用于安装转接件。
- 部分机型需另外安装升级套件后使用，请参考《适配机型及要求》章节。

#### 打印并安装风管转接件

> 提示：
>
>
>
> - 您可在 MakerWorld 搜索（或点击链接） [E1 净化器-风管转接件](https://makerworld.com.cn/models/3200756) ，下载并打印转接件模型；
> - 移除或锁紧螺丝时，请使用 H2.0 内六角扳手操作。部分机型的机身螺丝孔较紧，可尝试用螺丝提前拧几圈，以便后续安装。

👇点击选择机型，查看对应步骤：

拓竹H3C H2 系列 P2S X2D X1C/P1S/P1P X1E A1 mini （加装泡泡罩）

1. 点击链接，下载并打印转接件模型。

下载链接 ： [E1 净化器-风管转接件](https://makerworld.com.cn/models/3200756)

推荐耗材 ：推荐使用 PETG 耗材打印该模型，以获得更好的打印效果和使用性能。您也可以根据实际需求选择其他适用耗材进行打印。

![3_h3c_air_exhaust_adapter_for_e1.jpg](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/3_h3c_air_exhaust_adapter_for_e1.jpg)

1. 在打印机背面，卸下图示 3 颗螺丝。

![4_screws_on_h3c_printer_back_to_remove.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/4_screws_on_h3c_printer_back_to_remove.png)

1. 对齐转接件孔位，拧入 3 颗螺丝。

![5_screws_on_h3c_printer_back_to_install.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/5_screws_on_h3c_printer_back_to_install.png)

1. 点击链接，下载并打印风管转接件模型。

下载链接 ：

[H2 系列风管转接件.3mf](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/e1_hose_adapter_for_h2_series.3mf)

推荐耗材 ：推荐使用 PETG 耗材打印该模型，以获得更好的打印效果和使用性能。您也可以根据实际需求选择其他适用耗材进行打印。

1. 找到自动排气格栅两侧的螺丝孔，将转接件对齐放置在其上。

| 〔图片〕 | 〔图片〕 |
| --- | --- |
| 未对齐 ❌ | 已对齐 |

1. 使用 H2.0 内六角扳手将 4 颗螺丝锁入并拧紧。

![h2_series_adapter_four_screws.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/h2_series_adapter_four_screws.png)

P2S 分新、旧两种背板，请根据实际背板类型进行安装。

###### 旧背板（无外排风扇安装口）

1. 点击链接，下载并打印风管转接件模型（一共需要打印两件）。

下载链接 ：

[P2S 风管转接件.3mf](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/e1_hose_adapter_for_p2s_old_back_panel.3mf)

推荐耗材 ：推荐使用 PETG 耗材打印该模型，以获得更好的打印效果和使用性能。您也可以根据实际需求选择其他适用耗材进行打印。

1. 对准机身侧边的散热格栅，卡入拓展支架，并使用 2 颗螺丝锁紧。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

1. 将转接件的凸起卡入支架底部，并将转接件顶部盖在支架上。

![p2s_snap_the_adapter_protrusion.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/p2s_snap_the_adapter_protrusion.png)

1. 轻轻上下移动，即可固定到位。

![p2s_lock.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/p2s_lock.png)

###### 新背板（有外排风扇安装口）

1. 点击链接，下载并打印风管转接件模型。

下载链接 ：

[P2S 风管转接件.3mf](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/e1_hose_adapter_for_p2s_new_back_panel.3mf)

推荐耗材 ：推荐使用 PETG 耗材打印该模型，以获得更好的打印效果和使用性能。您也可以根据实际需求选择其他适用耗材进行打印。

1. 移除外排风扇连接线，然后将外排风扇取下。

![nbp_p2s_remove_exhaust_fan.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/nbp_p2s_remove_exhaust_fan.png)

1. 确保外排风扇已拆下，将转接件卡入风扇安装口，并左右移动以固定。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

1. 点击链接，下载并打印风管转接件模型。

下载链接 ：

[X2D 风管转接件.3mf](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/e1_hose_adapter_for_x2d.3mf)

推荐耗材 ：推荐使用 PETG 耗材打印该模型，以获得更好的打印效果和使用性能。您也可以根据实际需求选择其他适用耗材进行打印。

1. 移除外排风扇连接线，然后将外排风扇取下。

![x2d_remove_cable.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/x2d_remove_cable.png)

1. 将转接件凸起的卡扣 朝向背板左侧 ，卡入风扇安装口，左右移动即可固定。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

> 提示
>
>
>
> 如需在 P1P 机型使用净化器，请务必使用官方升级套件完成封箱后再继续。

1. 点击链接，下载并打印风管转接件模型。

下载链接 ：

[X1C/P1S/P1P 风管转接件.3mf](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/e1_hose_adapter_for_x1c-p1s-p1p.3mf)

推荐耗材 ：推荐使用 PETG 耗材打印该模型，以获得更好的打印效果和使用性能。您也可以根据实际需求选择其他适用耗材进行打印。

1. 移除图示螺丝。

![x1p1_one_screw.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/x1p1_one_screw.png)

1. 对准螺丝孔，将转接件放置在其上，并拧入 4 颗螺丝（请勿使用上一步已移除的螺丝）。

![x1p1_install.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/x1p1_install.png)

1. 点击链接，下载并打印风管转接件模型。

下载链接 ：

[X1E 风管转接件.3mf](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/e1_hose_adapter_for_x1e.3mf)

推荐耗材 ：推荐使用 PETG 耗材打印该模型，以获得更好的打印效果和使用性能。您也可以根据实际需求选择其他适用耗材进行打印。

1. 移除图示螺丝。

![x1e_one_screw.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/x1e_one_screw.png)

1. 对准螺丝孔，将转接件放置在其上，并拧入 3 颗螺丝。

![x1e_three_screws.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/x1e_three_screws.png)

1. 点击链接，下载并打印风管转接件模型。

下载链接 ： [A1 mini 泡泡罩风管转接件.3mf](https://wiki.bambulab.com/e1/manual/unboxing-installation-guide/purifier_adapter_for_a1_mini_bubble.3mf)

推荐耗材 ：推荐使用 PETG 耗材打印该模型，以获得更好的打印效果和使用性能。您也可以根据实际需求选择其他适用耗材进行打印。

![a1_mini_hose_adapter.jpg](https://wiki.bambulab.com/e1/manual/unboxing-installation-guide/a1_mini_hose_adapter.jpg)

1. 在泡泡罩背面，找到四个螺丝孔位。

![a1_mini_1.png](https://wiki.bambulab.com/e1/manual/unboxing-installation-guide/a1_mini_1.png)

1. 模型凸起的边缘置于下侧，对齐螺丝孔位，使用 H2.0 内六角扳手锁入四颗 BT3×8 螺丝。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

### 安装步骤

#### 1. 移除外包装

- 打开外箱，取出配件、缓冲材料及快速入门指南。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

- 取出净化器，移除外部的防潮袋。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

- 在风管中，取出电源线与 6-pin 连接线。

![10_take_out_cables.webp](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/10_take_out_cables.webp)

- 取下配件的包装袋，将 3 个密封圈分别安装至 风管两端 及 风管转接口 的凹槽处，确保安装到位。

> 注意 ：取下配件包装袋时，袋内密封圈可能会散落。请在平整台面上小心拆封，避免遗失。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

#### 2. 安装外排转接件

- 将风管转接口插入外排转接件，按压到底，确保连接处无缝隙；

![13_insert_air_duct_adapter_into_exhaust_adapter.webp](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/13_insert_air_duct_adapter_into_exhaust_adapter.webp)

- 将外排转接件卡入净化器背面的出风口。

![14_install_the_exhaust_adapter.webp](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/14_install_the_exhaust_adapter.webp)

#### 3. 安装风管

- 将风管拉伸至所需长度；

![15_extend_the_air_duct.webp](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/15_extend_the_air_duct.webp)

- 将风管一端插入打印机风管转接件，听到“咔哒”声即安装到位。

> 注意： 安装后请轻拉风管，确认连接牢固。如有松动，请重新安装。

![16_insert_one_end_of_air_duct_into_adapter.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/16_insert_one_end_of_air_duct_into_adapter.png)

- 将风管另一端插入净化器背面进风口。

![17_the_other_end_into_the_air_inlet.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/17_the_other_end_into_the_air_inlet.png)

#### 4. 插入 6-pin 连接线

- 将 6-pin 连接线磁环靠近的一端连接至净化器背面对应的接口。

| 磁环 〔图片〕 | 接口位置 〔图片〕 |
| --- | --- |

- 将另一端连接至打印机背部的 任一 6-pin 接口 。

![20_h3c_6-pin_port.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/20_h3c_6-pin_port.png)

- 如机身无多余 6-pin 接口，可将净化器连接至与打印机关联的 AMS 设备（暂不包含 AMS lite）上的 6-pin 接口。

![21_ams_6-pin_port.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/21_ams_6-pin_port.png)

#### 5. 连接电源

将电源线插入电源接口中；

![22_connect_power.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/22_connect_power.png)

等待净化器启动，查看净化器屏幕，确认出现下图所示的图标，即为连接成功。

![23_connection_success_icon_on_purifier_screen.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/23_connection_success_icon_on_purifier_screen.png)

同时，查看打印机屏幕，确认是否出现净化器图标。

![24_connection_success_icon_on_h3c_screen.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/24_connection_success_icon_on_h3c_screen_cn.png)

#### 6. 加装排气风管（选配件）

如需将过滤后的空气排放至室外，可另购排气风管。

将排气风管末端完全拉伸展开，逆时针旋入净化器出风口处的转接口；

| 〔图片〕 | 〔图片〕 |
| --- | --- |

> 安装时，需留意不要过度弯折风管。

风管另一端排放至室外。

![27_other_end_of_air_duct_to_outdoors.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/27_other_end_of_air_duct_to_outdoors.png)

### 使用教程

#### 模式介绍

净化器支持自动模式和手动模式两种使用方式。 在固件版本支持的情况下，推荐您在自动模式下使用净化器 。

若当前打印机固件版本暂不支持，您可通过手动启停净化器、调节风速档位等方式，在手动模式下使用。

##### 自动模式（推荐）

- 启用条件 ：确保打印机、净化器已接入电源和 6-pin 连接线（且显示连接成功的图标），且打印机固件版本已支持 E1 净化器。
- 启用方式 ：首次使用默认为自动模式。您也可以按下风速按钮，切换风速档位， 确认屏幕的风扇状态为 auto 即可 。

##### 手动模式

- 启用方式 ：您可在打印任务开始时，开启净化器，并设置对应的风速。请在 [按钮功能](#按钮功能) 章节查看具体说明。

> 注意 ：打印结束至少 5 分钟后再关闭净化器

- 风速设置 ：针对不同类型的耗材，推荐您设定不同的风速档位：
  | 耗材类型 | 推荐风速档位 |
  | --- | --- |
  | PLA, PETG,TPU,PVA, PLA/PETG 专用支撑耗材 | 2 档 |
  | PC, ABS, ASA, PAHT, PET, PA, PPA, PPS, Support for ABS, Support for PA/PET | 1 档 |

#### 按钮功能

![28_button_functions.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/28_button_functions.png)

1. 开关按钮
  - 短按：唤醒或熄灭屏幕。
  - 长按（约 1.5s）：休眠或唤醒净化器；休眠后，净化器会停止运行并待机。
2. 风速按钮
  - 短按：调整风速，共有一档、二档、三档、自动档四种档位。
  - 长按（约 1.5s）：切换屏幕页面，查看滤芯状态、错误信息（如有）或返回 空气质量主页。

#### 显示屏图标

![29_display_icons.png](https://public-cdn.bblmw.com/wiki/new/e1/manual/unboxing-installation-guide/29_display_icons.png)

1. 连接状态 。使用 6-pin 连接线插入净化器和打印机的对应接口，净化器主页会自动显示该图标。若未显示该图标，可能为设备固件不支持，请在打印机屏幕更新固件后再查看。
2. 滤芯类型 。
3. 实时 PM 2.5 。展示经过滤芯后的外排空气质量。
4. 风扇状态 。默认为自动模式 （auto）。短按风速按键，可以在自动、一档、二档、三档和停止之间循环切换。

#### 打印机屏幕功能

> 提示：
>
>
>
> - 以下屏幕截图以拓竹H3C 机型为例，不同机型显示可能有差异，请以实际为准。
> - 固件未适配的机型，暂不支持在打印机屏幕操作。

- 打印机屏幕上，进入 空调系统 页面，点击「 净化器 」进入控制页面，可调节净化器风速强度模式。

| 〔图片〕 | 〔图片〕 | 〔图片〕 |
| --- | --- | --- |

- 点击「 设置 」→「 更多设置 」→「 打印选项 」→「 外接净化器自动模式参数设置 」，查看不同耗材的净化强度和延时关闭时长；
- 打开「 请设置耗材对应的净化器参数 」后方按钮，可修改默认的参数。发起打印后，净化器会根据配置的参数运行及延时关闭。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

| 〔图片〕 | 〔图片〕 |
| --- | --- |

### 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
> 如果本指南未解决您的问题， [请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5) ，我们随时准备为您解答疑问并提供帮助。
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
