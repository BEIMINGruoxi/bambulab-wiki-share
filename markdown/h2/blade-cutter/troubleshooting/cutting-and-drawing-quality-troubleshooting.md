---
title: 1. 图案切不穿或未完全切穿
url: https://wiki.bambulab.com/zh/h2/blade-cutter/troubleshooting/cutting-and-drawing-quality-troubleshooting
category: H2 系列
updated: 2026-08-28T06:21:25.760Z
---

### 1. 图案切不穿或未完全切穿

#### 现象：

刀切加工后，图案切不穿或没有完全切穿，如下图所示：

| 〔图片〕 | 〔图片〕 |
| --- | --- |

#### 排查方案：

- 直接进行再次切割；

- 在被切割材料上进行刀压标定，并适当增加刀压，再次切割；标定流程可以参考 [Bambu Suite 材料参数标定和加工优化指导](https://wiki.bambulab.com/zh/h2/software/bambu-suite/manual/material-parameter-calibration-and-machining-optimization) 。
- 检查工具头上的刀切模组是否稳固，可以用手检查看是否会明显晃动，如不稳可适当拧紧扳手上的螺丝。扳手螺丝松动会导致刀切模组无法固定紧，在加工过程有可能上下左右晃动，从而影响加工质量。

![图片](https://wiki.bambulab.com/h2/blade-cutter/troubleshooting/cutting-and-drawing-quality-troubleshooting/frame_1123862560-2.png)

- 观察刀尖是否断裂或磨损，如损坏请更换新刀。（可借助放大镜与新刀对比）

良好刀尖：

![图片](https://wiki.bambulab.com/h2/blade-cutter/troubleshooting/cutting-and-drawing-quality-troubleshooting/image-8.png)

磨损刀尖：

![图片](https://wiki.bambulab.com/h2/blade-cutter/troubleshooting/cutting-and-drawing-quality-troubleshooting/img_v3_02ik_0db39d58-4273-4b7e-97a1-47906a4fbf4g.jpg)

断裂刀尖：

![图片](https://wiki.bambulab.com/h2/blade-cutter/troubleshooting/cutting-and-drawing-quality-troubleshooting/image-6.png)

- 确认在刀切垫板上实际放置的材料和软件材料组中选择的材料是一致的，若材料不一致有可能使用不匹配的刀压加工导致无法切穿。

![图片](https://wiki.bambulab.com/h2/blade-cutter/troubleshooting/cutting-and-drawing-quality-troubleshooting/image-7.png)

### 2. 刀头刮纸问题

#### 现象:

刀切加工的过程中，刀头刮纸，如下图所示。

![图片](https://wiki.bambulab.com/h2/blade-cutter/troubleshooting/cutting-and-drawing-quality-troubleshooting/image-5.png)

#### 排查方案：

- 检查切割模组是否稳固，如不稳可适当拧紧扳手螺丝。
  ![图片](https://wiki.bambulab.com/h2/blade-cutter/troubleshooting/cutting-and-drawing-quality-troubleshooting/frame_1123862560.png)
- 观察刀尖是否断裂，如断裂，请更换新刀。（可借助放大镜与新刀对比）
- 检查刀切粘板的粘性及表面是否有异物。确保纸张在垫板上铺平，可以采用滚轮适当压紧。 若材料没有完全贴合在垫板表面，则加工的时候很有可能会被刀头刮蹭。
- 如果发现刮纸路径是原始的图案中存在冗余线段导致的，请在Bambu Suite中删减冗余线段。
  ![图片](https://wiki.bambulab.com/h2/blade-cutter/troubleshooting/cutting-and-drawing-quality-troubleshooting/image.png)

### 3. 切割图案拐角粘连

#### 现象：

切割出来的图案有少部分拐角处有粘连，没有完全切穿，如下图所示。

![图片](https://wiki.bambulab.com/h2/blade-cutter/troubleshooting/cutting-and-drawing-quality-troubleshooting/image-1.png)

#### 排查方案：

渐进下刀以及路径转角为了更好的保护刀， 通常在一段切割路径转角的位置以及起始位置，会用更小的刀压下刀或者转刀，以此来减少刀尖的磨损，所以切割的图案在这些位置会有些粘连，这个属于正常现象。

![图片](https://wiki.bambulab.com/h2/blade-cutter/troubleshooting/cutting-and-drawing-quality-troubleshooting/image-2.png)

### 4. 加工图案变形

#### 现象：

刀切或画笔加工的图案明显变形，例如切（画）出来的圆明显不够圆，图案或文字明显扭曲、断线等，如下图所示：

![图片](https://wiki.bambulab.com/h2/blade-cutter/troubleshooting/cutting-and-drawing-quality-troubleshooting/image-3.png)

![图片](https://wiki.bambulab.com/h2/blade-cutter/troubleshooting/cutting-and-drawing-quality-troubleshooting/image-4.png)

#### 排查方案：

检查工具头上的刀切模组是否稳固，可以用手检查看是否会明显晃动，如不稳固可适当拧紧扳手上的螺丝。

![图片](https://wiki.bambulab.com/h2/blade-cutter/troubleshooting/cutting-and-drawing-quality-troubleshooting/frame_1123862560-1.png)

-
## 5. 打印后刀切发生偏位
### 现象：
打印后刀切，切割的路径出现明显偏移，如下图所示。

<table>
 <tr>
 <td width=50% ><img src="/h2/blade-cutter/troubleshooting/cutting-and-drawing-quality-troubleshooting/image_-_2025-11-28t120305.119.png" height="x"width="x"><br>图案整体往同一个方向偏移</td>
 <td><img src="/h2/blade-cutter/troubleshooting/cutting-and-drawing-quality-troubleshooting/screenshot-20251128-115854.png" height="x"width="x"><br>不同位置图案的偏移方向不一致</td>
 </tr>
 </table>

### 排查方案：

- **图案整体往同一个方向偏移：** 创建一个自定义材料参数，并增强切穿刀压；
![切穿刀压.png](/h2/blade-cutter/troubleshooting/cutting-and-drawing-quality-troubleshooting/切穿刀压.png =300x)

- **不同位置图案的偏移方向不一致：**
1. 手动测量打印出来的图案长宽，对比 Bambu Suite 中设置的尺寸是否有明显偏差；
2. 检查打印机设置，查看是否有任何自动缩放打印图案的设置，将其恢复默认；
3. 如果打印机并无任何缩放设置但打印后图案仍进行尺寸缩放，请联系在线技术支持。
-

### 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
> 如果本指南未解决您的问题， [请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5) ，我们随时准备为您解答疑问并提供帮助。
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
