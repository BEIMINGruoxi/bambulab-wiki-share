---
title: XY同步皮带
url: https://wiki.bambulab.com/zh/p1/maintenance/xy-timing-belt
category: P1 系列 > P1 系列机器维护
updated: 2026-08-28T08:23:58.388Z
---

### XY 同步皮带

有两种方法可以实现更换 XY 皮带：

- 方法一 ：将原有皮带保留在打印机上，然后将新皮带与旧皮带首尾粘接，通过牵引的方式完成皮带更换。该方法更换皮带相对简单，更适用于 XY 皮带磨损等场景。详细的方法您可以参阅该 Wiki： [更换 XY 同步皮带](https://wiki.bambulab.com/zh/x1/maintenance/how-to-replace-the-XY-belt)
- 方法二 ：将原有皮带从打印机上取下，再将新皮带依次穿入打印机。该方法更换皮带相对困难，花费时间较长，更适用于 XY 皮带断裂等场景。详细方法您可继续参阅本 Wiki。

![图片](https://wiki.bambulab.com/p1/maintenance/xy-belt/belt.jpg)

### 工具

- H2.0/1.5 内六角扳手
- 平头镊子或一字螺丝刀
- 瞬干胶

### 准备工作

- 关闭打印机，断开电源。
- 拆卸外壳，请参考以下wiki：
  [P1S 塑料左侧面板](https://wiki.bambulab.com/zh/p1/maintenance/p1s-left-panel)
  [P1S 塑料右侧面板](https://wiki.bambulab.com/zh/p1/maintenance/p1s-right-panel)
  [P1S 金属背板](https://wiki.bambulab.com/zh/p1/maintenance/p1s-rear-panel)

### 视频指南

### 拆除指南

#### 第 1 步 - 松出XY张紧器

根据要更换的皮带，参考 [XY张紧器惰轮](https://wiki.bambulab.com/zh/p1/maintenance/xy-idler-pulley) 的相关内容，松出对应位置的XY张紧器。

|  |  |
| --- | --- |
| 〔图片〕 | 〔图片〕 |

#### 第2步 - 拆除工具头外壳

参考 [工具头外壳](https://wiki.bambulab.com/zh/p1/maintenance/toolhead-housing) 的相关内容，拆除工具头外壳。

![图片](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/shell_removed.jpg)

#### 第3步 - 解锁皮带

移除锁定皮带的螺丝，用一字螺丝刀或平头镊子将限位块撬出，然后向皮带松脱的方向用力，将皮带从工具头上松脱出来。

同样的操作，解锁另一端皮带。

![图片](https://wiki.bambulab.com/p1/maintenance/xy-belt/remove_belt_locking_screw.jpg)

![图片](https://wiki.bambulab.com/p1/maintenance/xy-belt/pull_out_the_stopper.jpg)

![图片](https://wiki.bambulab.com/p1/maintenance/xy-belt/loosen_the_belt.jpg)

#### 第4步 - 移除 皮带

逐步拉动皮带，将皮带完全从各个隋轮、电机齿轮上移除。

|  |  |
| --- | --- |
| 〔图片〕 | 〔图片〕 |

|  |  |
| --- | --- |
| 〔图片〕 | 〔图片〕 |

#### 第5步 - 移除张紧轮

将张紧轮从皮带上取下。

![图片](https://wiki.bambulab.com/p1/maintenance/xy-belt/remove_the_xy_tensioner.jpg)

（类似的步骤，可以移除另一根皮带）

### 安装指南

#### 第1步 - 穿皮带

将张紧轮穿到皮带上，然后根据下列图片的顺序，穿好皮带。可以利用一些工具（如镊子）帮助完成穿皮带。

|  |  |
| --- | --- |
| 〔图片〕 | 〔图片〕 |

|  |  |
| --- | --- |
| 〔图片〕 | 〔图片〕 |

|  |  |
| --- | --- |
| 先将皮带末端弯曲少许 〔图片〕 | 可以利用镊子引导皮带的走向 〔图片〕 |

|  |  |
| --- | --- |
| 〔图片〕 | 〔图片〕 |

#### 第2步 - 贴附限位块

在皮带的两端分别用瞬干胶固定一个限位块。

![图片](https://wiki.bambulab.com/p1/maintenance/xy-belt/attach_stoppers.jpg)

#### 第3步 - 锁皮带

弯曲皮带，将其沿侧面固定槽向上（或向下）推到位。拉动皮带并利用内六角扳手将同步带固定块完全压入安装到位，拧入1颗螺丝固定。

同样的操作，锁定皮带的另外一端。

|  |  |
| --- | --- |
| 〔图片〕 | 〔图片〕 |

#### 第4步 - 安装工具头外壳

参考 [工具头外壳](https://wiki.bambulab.com/zh/p1/maintenance/toolhead-housing) 的相关内容，安装好工具头外壳。

![图片](https://wiki.bambulab.com/p1/maintenance/toolhead-enclosure/front_cover_installed.jpg)

#### 第5步 - 安装XY张紧轮

参考 [XY张紧器惰轮](https://wiki.bambulab.com/zh/p1/maintenance/xy-idler-pulley) 的相关内容，安装好已松出的张紧器，并重新张紧皮带。

![图片](https://wiki.bambulab.com/p1/maintenance/xy-motor/lock_the_tensioners.jpg)

### 校准

更换碳棒后，需要重新张紧皮带。

1. 关闭打印机。
2. 松开皮带张紧器的四颗螺钉（但不要卸下）。轻轻前后移动工具头几次，然后将其移至打印机的后端。
3. 再次拧紧四颗螺钉。皮带张紧器中的弹簧系统会自动将皮带调整到正确的张力。 注意： 只需像拧其他螺钉一样适度拧紧，请勿过度拧紧皮带张紧螺钉。过度拧紧可能导致损坏，且不会提升效果。

### 如何验证完成

接上打印机电源，开启打印机，在屏幕上操作，运行设备自检流程，如自检通过，说明操作成功。

![图片](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/self-test.jpg)

### 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
> 如果本指南未解决您的问题， [请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5) ，我们随时准备为您解答疑问并提供帮助。
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
