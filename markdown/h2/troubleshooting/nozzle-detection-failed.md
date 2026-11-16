---
title: 03004039：喷嘴在位检测失败，请查看帮助解决问题。
url: https://wiki.bambulab.com/zh/h2/troubleshooting/nozzle-detection-failed
category: H2 系列 > H2 系列故障排除
updated: 2026-08-28T06:37:42.205Z
---

### 故障描述

开机校准阶段，设备将检查喷嘴是否正确安装在工具头上，当喷嘴未安装或因其他因素导致检测失败，就会提示该报错。

### 故障排除

#### 步骤1. 检查喷嘴安装

如图所示，请将左侧拨片向下拨动，使其完全贴合喷嘴后，再将右侧卡扣向下扣牢。（另一喷嘴的安装操作相同，但是左右对称，注意区分）

![图片](https://wiki.bambulab.com/h2/17.%E6%89%A3%E7%B4%A7%E5%8D%A1%E6%89%A3.webp)

注意，卡扣错误锁紧是因为同时向下拨动拨片与卡扣，导致左侧拨片错误卡进了右侧卡扣中。

![d卡扣.jpg](https://wiki.bambulab.com/h2/maintenance/replace-hotend/d%E5%8D%A1%E6%89%A3.jpg)

向左推动 H2C 的感应热端锁紧拉柄，然后用手晃动感应热端，确保感应热端被锁紧。

![图片](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-induction-hotend/019.webp)

#### 步骤2. 使用 H2 适配的喷嘴

检查是否安装第三方喷嘴，或其他机型的喷嘴（如 A1/A1 mini），请使用 H2 系列适配的喷嘴。更多 H2 适配的喷嘴信息，请点击 [拓竹热端喷嘴介绍](https://wiki.bambulab.com/zh/filament-acc/acc/nozzles) 查看。

| H2 系列普通喷嘴 | A1 系列普通喷嘴 |
| --- | --- |
| 〔图片〕 | 〔图片〕 |

#### 步骤3. 检查涡流传感器安装

H2D H2S H2C

H2D 的右喷嘴可参考 [更换 H2D 挤出机前盖导向](https://wiki.bambulab.com/zh/h2/maintenance/replace-dual-extruder-filament-guide) ，拆除热端、前盖导向。然后检查右挤出力传感器安装(下图两个螺丝)是否松动。若松动，请重新安装。

![图片](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-eddy-sensor/image-27.png)

左喷嘴可先拆卸部件冷却风道的 4 个固定螺丝，移除部件冷却风扇风道。

![图片](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-eddy-sensor/image-3.png)

![图片](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-eddy-sensor/image-8.png)

![图片](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-eddy-sensor/image-1.png)

然后拧松下图螺丝，解锁涡流线圈。

![图片](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-eddy-sensor/image-17.png)

使用对折一次的 A4 纸，插入涡流线圈前的缝隙中，确保 A4 纸能够以较低阻力拉出，再锁紧螺丝。

| 〔图片〕 | 〔图片〕 | 〔图片〕 |
| --- | --- | --- |

可参考 [更换 H2S 涡流线圈](https://wiki.bambulab.com/zh/h2s/maintenance/replace-eddy-sensor) ,重新安装位于喷嘴上方的涡流线圈，并完成间距调整。

![图片](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-16.png)

右喷嘴可参考 [更换 H2C 右涡流线圈](https://wiki.bambulab.com/zh/h2c/maintenance/replace-right-eddy-sensor) ,重新安装位于感应加热组件上方的涡流线圈。

左喷嘴可先拆卸部件冷却风道的 4 个固定螺丝，移除部件冷却风扇风道。

![图片](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-eddy-sensor/image-3.png)

![图片](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-eddy-sensor/image-8.png)

![图片](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-eddy-sensor/image-1.png)

然后拧松下图螺丝，解锁涡流线圈。

![图片](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-eddy-sensor/image-17.png)

使用对折一次的 A4 纸，插入涡流线圈前的缝隙中，确保 A4 纸能够以较低阻力拉出，再锁紧螺丝。

| 〔图片〕 | 〔图片〕 | 〔图片〕 |
| --- | --- | --- |

#### 步骤4. 检查喷嘴偏移校准传感器

- 检查传感器表面，若磨损严重，请更换传感器。
- 拆卸螺钉，检查连接线是否松动，若松动请重新拔插接头。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

- 检查安装方向，如果反向安装请重新调整。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

### 功能验证

在打印机屏幕上点击 设置——打印校准——喷嘴偏移校准 ，重新开始校准程序。若校准程序能够顺利完成，则喷嘴检测功能恢复正常。

![图片](https://wiki.bambulab.com/h2/manual/nozzle-offset-calibration/20251120-171523.jpg)

### 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
> 如果本指南未解决您的问题， [请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5) ，我们随时准备为您解答疑问并提供帮助。
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
