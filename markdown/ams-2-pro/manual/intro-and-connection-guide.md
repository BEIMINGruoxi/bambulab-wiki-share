---
title: AMS 2 Pro 各模块介绍和连接配置
url: https://wiki.bambulab.com/zh/ams-2-pro/manual/intro-and-connection-guide
category: AMS 2 Pro > 使用手册
updated: 2026-08-28T08:34:09.511Z
---

### 模块介绍

#### 外观和三维尺寸

| AMS 2 Pro外观 | 三维尺寸图 |
| --- | --- |
| 〔图片〕 | 〔图片〕 |

#### 耗材插槽

AMS 2 Pro有 4 个耗材插槽，每个槽内各有一个上下料器。它有独立的电机和齿轮推动耗材丝向前或将其绕回料盘，有一个传感器来检测耗材。当插入耗材丝时，它会往里拉动耗材丝；当需要将耗材卷回料盘时，主动轴会转动料盘将耗材缠绕回收。每个上下料器入口 内嵌陶瓷加强防磨衬套 ，可以更好地保护入料口防止其在长时间使用后被耗材丝磨损。

| 耗材插槽 | 上下料器入口 |
| --- | --- |
| 〔图片〕 | 〔图片〕 |

#### 五通

五通 位于AMS 2 Pro的尾部，由四个霍尔传感器、一个磁性旋转编码器和一个无刷电机组成。 它将四个耗材插槽合并为一个。 霍尔传感器检测耗材丝何时到达特定位置，激活无刷电机为耗材提供第二级驱动力。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

#### 供料缓冲器

AMS 2 Pro和打印机之间需要连接一个缓冲器，它由滑块、弹簧和霍尔传感器组成。AMS将耗材推入工具头挤出机时，由于耗材的压力，滑块向前移动，通过霍尔传感器检测滑块移动的位置，供料缓冲器将信号反馈回 AMS 和打印机。通过控制AMS的进给速度，可以确保耗材的张力在控制范围内，这样工具头挤出机就可以轻松而精确地工作。

H2D打印机内部自带供料缓冲器，缓冲器内部还具有耗材传感器， 可以检测是否有耗材丝通过缓冲器或者耗材丝是否断在缓冲器内部 。另外，在用外挂料盘打印时，缓冲器还具备缠料检测功能，可以检测到外挂料盘是否缠料。

![图片](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-7.png)

如果您需要将AMS 2 Pro连接至X1或P1系列打印机，则需要额外购买缓冲器（连接1台）或 [AMS Hub](https://item.jd.com/10147107132256.html) （连接多台）来连接使用。

![图片](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-8.png)

如果您需要将 AMS 2 Pro 连接至 A1 系列打印机，则需要额外购买 A1 系列料线选通器来连接使用。请勿使用 AMS 自带的缓冲器或 AMS Hub 连接，否则会导致缓冲器使用功能异常或损坏，在此种情况下，该缓冲器或 AMS Hub 将不予保修。

![ams_hub.png](https://wiki.bambulab.com/a1/ams-connection-guide/ams_hub.png)

#### 防潮系统

##### 湿度传感器

AMS 2 Pro的正前方配备了一个湿度传感器，可以检测AMS舱内的湿度和温度。您可以在打印机的显示屏/Bambu Studio/Bambu Handy中查看AMS当前的湿度状态。

![图片](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image.png)

![图片](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-1.png)

##### 烘干模块

AMS 2 Pro配备了两个烘干模块，它由加热片，风扇，以及NTC温度传感器构成，最大可以烘干的温度是65℃。

![图片](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-2.png)

![图片](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-3.png)

##### 内循环系统

烘干模块位于AMS主框架下面，烘干时热风从内循环出风口吹出（靠近五通），加热耗材后，再从前面两个内循环进风口把空气吸到加热模块，重新加热，形成一套内循环系统。

![图片](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-4.png)

##### 进出气口

AMS 2 Pro配备了两个主动开关的进出气风门，底部风门为进气口，后侧风门为出气口。

在烘干耗材时，AMS 2 Pro会通过外循环的方式，将湿气从内部排出。在进行外循环时，进气口和出气口会打开，请确保进气口和出气口不被其他物品遮挡，以获得最佳烘干效果。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

##### 干燥剂和密封胶圈

AMS 2 Pro出厂配备变色硅胶干燥剂，位于后方的从动支撑轴下方。干燥剂吸收水分，保持舱内空气干燥。吸湿后，黄色颗粒变为深绿色，此时需更换或烘干干燥剂后重复使用。
注意 ：干燥剂需从密封透明袋中取出后再放入 AMS。

上盖与外壳之间的橡胶密封圈可保持 AMS 密封性，防止外部湿气进入。当湿度超出预设标准时，湿度传感器会提醒用户。

| 干燥剂状态 | 干燥剂 | 橡胶密封圈 |
| --- | --- | --- |
| 〔左：失效干燥剂；右：正常干燥剂〕 | 〔图片〕 | 〔图片〕 |

注意：干燥剂需从密封透明塑料袋中取出后，再放入AMS中。

#### 电源适配器

使用6-pin连接线连接H2系列打印机和单台AMS 2 Pro，即可使用AMS 2 Pro的烘干功能 。如果需要同时烘干多台AMS 2 Pro内的耗材，则需要使用拓竹官方电源适配器来给其余的AMS 2 Pro供电。

> 注意 ：AMS 2 Pro 官方电源适配器规格为 24V 4A。为确保设备安全与正常使用， 请务必使用官方配件。使用第三方适配器可能会导致设备损坏，并影响保修权益 。

如果X1或P1系列打印机配合AMS 2 Pro一起使用并启用AMS 2 Pro的烘干功能，则每台AMS 2 Pro都需要使用拓竹官方电源适配器来为其供电。电源适配器的使用方式如下图所示：

![图片](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-15.png)

#### RFID模块

AMS 2 Pro中配备了两个RFID线圈，通过它们可以识别 Bambu Lab官方耗材上的 RFID 标签，还可以通过它实现耗材余量估算、自动续料等功能。

![图片](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-16.png)

#### 料管拓展口

料管拓展口能同时将4个进料模块连接到打印机，在连接多台AMS 2 Pro至H2系列打印机时，需要用到料管拓展口，最多可以连接4台AMS 2 Pro以实现16色打印。

![图片](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-17.png)

### 连接和配置AMS 2 Pro

连接AMS 2 Pro至H2系列打印机 连接 AMS 2 Pro 至 X2D 打印机 连接 AMS 2 Pro 至 X1 和 P1 系列打印机 连接 AMS 2 Pro 至 P2S 打印机 连接 AMS 2 Pro 至 A1 系列打印机

1. 将上盖玻璃放至打印机顶部。将AMS 2 Pro放置于打印机的顶部。
  从配件盒中取出铁氟龙料管，一端插入AMS 2 Pro的出料口，另一端插入打印机的任一进料口，向前推送铁氟龙料管直至无法前进，大约10cm （从打印机正面观察缓冲器旁边的窗口，如果能观察到铁氟龙料管，即插入到位）。 上下进料口分别对应不同热端，AMS 2 Pro的料管连接上进料口，使用右热端进行多色打印，AMS 2 Pro 连接下进料口，则使用左热端进行多色打印。
  | 连接铁氟龙料管 | 确保在这个窗口能看到料管 |
  | --- | --- |
  | 〔图片〕 | 〔图片〕 |
2. 从配件盒中取出6-pin连接线，两端分别插入打印机和AMS的任一6-pin接口，如下图所示。
  ![图片](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-20.png)
  > 注意：请务必使用 AMS 2 Pro 和 AMS HT 标配的新版本 6-pin 连接线，若使用上一代 AMS 的 6-pin 连接线可能导致 AMS 与打印机的通信不稳定，而上一代 AMS 可以兼容新版本的 6-pin连接线。
  到此单台AMS 2 Pro的连接就已经完成了，如果您只使用一台AMS 2 Pro，那么该连接方式就可以正常使用AMS的各项功能（包括烘干），无需再额外连接电源适配器。

1. 将 AMS 2 Pro 放置于打印机上盖。将料管一端插入 AMS 2 Pro 出料口，推荐将另一端插入缓冲器上进料口（对应左热端）；

![pixpin_2026-03-06_09-52-38.png](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/pixpin_2026-03-06_09-52-38.png)

1. 将 6-pin 线分别插入缓冲器和 AMS 的任一接口。

![pixpin_2026-03-06_09-53-36.png](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/pixpin_2026-03-06_09-53-36.png)

> 注意：请务必使用 AMS 2 Pro 标配的新版本 6-pin 连接线，若使用上一代 AMS 的 6-pin 连接线可能导致 AMS 与打印机的通信不稳定，而上一代 AMS 可以兼容新版本的 6-pin 连接线。

1. 将上盖玻璃放至打印机顶部。使用2颗M3*21.5螺丝将缓冲器固定至打印机。将550mm铁氟龙料管一端插入AMS 2 Pro的出料口，另一端插入缓冲器的左侧。将370mm铁氟龙料管一端插入打印机的进料口，另一端插入缓冲器的右侧。
  ![图片](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-21.png)
2. 4-pin连接线L型接口端连接至打印机，另一端连接至缓冲器下方。6-pin连接线一端连接至AMS 2 Pro任-6-pin接口，另一端连接至缓冲器左侧。将24V 4A电源连接至AMS 2 Pro的电源适配器接口（如需使用烘干功能的话）。
  ![图片](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-22.png)
  > 注意：请务必使用 AMS 2 Pro 和 AMS HT 标配的新版本 6-pin 连接线，若使用上一代 AMS 的 6-pin 连接线可能导致 AMS 与打印机的通信不稳定，而上一代 AMS 可以兼容新版本的 6-pin连接线。

1. 将 AMS 2 Pro 放至打印机顶部。
2. 将 350 mm 铁氟龙料管的一端插入机箱进料口,另一端插入缓冲器右侧。
3. 将 600 mm 铁氟龙料管一端插入 AMS 2 Pro 的出料口，推入到底，另一端插入缓冲器左侧任一进料口。
  ![p2s-ams1.jpg](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/p2s-ams1.jpg)
4. 将 6-pin 连接线的两端分别插入打印机缓冲器和 AMS 2 Pro 的任一 6-pin 接口。
  ![p2s-ams2.jpg](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/p2s-ams2.jpg)

- A1 系列：具体步骤请参考： [A1 系列 AMS 连接教程](https://wiki.bambulab.com/zh/a1/manual/ams-connection-guide)
- A2L：具体步骤请参考： [A2L AMS 连接指南](https://wiki.bambulab.com/zh/a2l/manual/a2l-ams-connection-guide)

### 将多台 AMS 连接至打印机的方法 （X1/P1 系列，P2S 打印机）

> 💡 X1/P1 系列打印机连接多台 AMS 有两种方法。
>
>
>
> - 方法一 ：使用供料缓冲器与料管拓展口连接多台 AMS，具体方法参考本章节内容。
> - 方法二 ：使用 AMS Hub 连接多台 AMS，连接方法请参考： [连接 AMS Hub 和多台 AMS](https://wiki.bambulab.com/zh/x1/manual/Connect-AMS-Hub-and-multi-AMS) 。
>   ![p2s-ams2.jpg](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/ams-hub.jpg)

#### 所需工具与材料

- 打印机一台
- AMS 2 Pro 或 AMS 若干台
- PTFE 料管 若干
- [料管拓展口](https://wiki.bambulab.com/zh/parts-acc/ptfe_adapter)
- P2S 缓冲器（P2S 适用）
  ![p2s-filament-buffer](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/p2s-filament-buffer.png)

#### 连接步骤

##### 步骤 1. 准备工作

- 关闭 AMS 电源并停止打印机工作。
- 确保供料缓冲器已安装到位。 P2S供料缓冲器的具体安装步骤请参考： [更换 P2S 缓冲器](https://wiki.bambulab.com/zh/p2s/maintenance/replace-filament-buffer) 。
- 准备好 PTFE 料管，并剪切备用。

##### 步骤 2. PTFE 料管插入 AMS

- 将 PTFE 料管插入所有AMS背面按钮处

![步骤1.jpg](https://wiki.bambulab.com/ams-2-pro/manual/%E6%AD%A5%E9%AA%A41.jpg)

##### 步骤 3. 安装料管拓展口

- 将 PTFE 料管插入料管拓展口。
  确保接口连接牢固、无松动。

![步骤2.jpg](https://wiki.bambulab.com/ams-2-pro/manual/%E6%AD%A5%E9%AA%A42.jpg)

- 然后，将剪切好的 10cm PTFE 料管 插入料管拓展口和供料缓冲器

![步骤3.jpg](https://wiki.bambulab.com/ams-2-pro/manual/%E6%AD%A5%E9%AA%A43.jpg)

⚠️ 安装料管拓展口需要注意以下两点：

1. 料管拓展口应安装在供料缓冲器 左侧。

正确方法是将料管拓展口接在左边，这样多台AMS的进料不仅做到了多进一出，还能同时用到供料缓冲器的功能。若接到右边，则会因不通过缓冲器，可能导致进料失败。

- P2S 连接示例：

| 正确做法 | 错误做法 |
| --- | --- |
| 〔正确做法.jpg〕 | 〔错误做法2.jpg〕 |

- X1/P1 系列连接示例：

| 正确做法 | 错误做法 |
| --- | --- |
| 〔正确做法.jpg〕 | 〔错误做法2.jpg〕 |

2. 料管拓展口和供料缓冲器之间 料管不要太长。

当多AMS连接的时候，PTFE 料管太长或太弯曲，容易导致阻力过大影响进料。因此料管拓展口和供料缓冲器之间的料管剪至 10cm 左右最佳。

- P2S 连接示例：

| 正确短线 | 接线过长 |
| --- | --- |
| 〔正确做法.jpg〕 | 〔错误做法2.jpg〕 |

- X1/P1 系列连接示例：

| 正确短线 | 接线过长 |
| --- | --- |
| 〔正确短线.jpg〕 | 〔接线过长.jpg〕 |

###### 步骤 4. 将打印机上的料管插入供料缓冲器

![步骤33.jpg](https://wiki.bambulab.com/ams-2-pro/manual/%E6%AD%A5%E9%AA%A433.jpg)

##### 步骤 5. 检查与固定

- 确认所有接口已插紧并锁定。
- 开启打印任务，检验料管路径顺畅无阻碍。

### 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
> 如果本指南未解决您的问题， [请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5) ，我们随时准备为您解答疑问并提供帮助。
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
