---
title: 开机校准过程故障排查
url: https://wiki.bambulab.com/zh/h2/troubleshooting/calibrate-failed
category: H2 系列 > H2 系列故障排除
updated: 2026-11-10T08:47:03.336Z
---

### 故障现象

新打印机或打印机恢复出厂设置后，在开机校准过程中出现了问题，无法继续校准。

### 解决方案

#### 1. 常见故障

请对照屏幕显示的 故障代码 ，点击下表中 对应机型的 Wiki 链接 获取故障排查指引。

| 故障代码 | 故障提示 | 解决方案 |
| --- | --- | --- |
| 0300-4030 | Z轴回零失败，请确认热床滑块固定螺丝已取出且热床升降无异物阻挡。 | X1 \| P2S/X2D \| H2 系列 \| A2L \| 拓竹H3C |
| 0300-4002 \ 0300-4038 | 热床调平失败。 | X1 \| P2S/X2D \| H2 系列 \| A2L \| 拓竹H3C |
| 0300-4032 | XY回零失败。 | 通用指南 \| 拓竹H3C |
| 0300-4036 | 喷嘴偏移校准失败。 | H2D\H2C \| X2D |
| 0300-4015 \ 0300-4037 | 喷嘴裹头位置检测失败。 | P2S \| X2D |
| 0300-4035 | 喷嘴清理失败。 | P2S \| H2 系列 \| X2D \| 拓竹H3C |
| 0500-4095 | 未检测到打印板。 | P2S/X2D \| H2 系列 \| A2L \| 拓竹H3C |
| 05FF-4031 \ 0300-4031 | 热端未安装，请安装后重新校准。（H2D\H2C 请检查左右热端是否未安装） | P2S \| X2D \| H2S \| H2D\H2C \| A2L |
| 0300-4039 | 喷嘴在位检测失败。 | H2 系列 \| P2S \| X2D |
| 0300-403A | 打印头控制板未连接。 | 拓竹H3C |
| 0300-8032 | 检测到 1 号工具从挂架上脱落。 | 拓竹H3C |
| 0502-4040 | 检测到有工具从挂架上脱落。 | 拓竹H3C |
| 2A00-8032 | 检测到 1 号打印头从挂架上脱落。 | 拓竹H3C |
| 2A00-8047 | 挂架回中失败。 | 拓竹H3C |
| 1A00-4007 | 挂架对位校准失败。 | 拓竹H3C |
| 2A00-8046 | 取用工具失败。 | 拓竹H3C |
| 2A00-8041 | 从挂架取出工具失败。 | 拓竹H3C |
| 2A00-8049 | 放置工具时工具头丢步。 | 拓竹H3C |
| 2A00-804A | 取用工具时工具头丢步。 | 拓竹H3C |

请参考以上列出的排查故障指引，在问题解决后请在屏幕上点击 重新校准。

![1.png](https://wiki.bambulab.com/h2c/1.png)

#### 2. 非常见故障

若上表无对应 HMS 链接，请点击打印机屏幕右上角 “跳过” 开机校准，进入主页点击 “ [助手](https://wiki.bambulab.com/zh/x1/troubleshooting/how-to-enter-the-specific-code-page) ” 查看 HMS 信息，然后在 [HMS 主页面](https://wiki.bambulab.com/zh/hms/home) 查询具体的 HMS 代码并进行故障排除。

![20251223-151435.jpg](https://wiki.bambulab.com/h2c/troubleshoting/unclogging/20251223-151435.jpg)

### 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。
> 如果问题仍未解决，请提交 [服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5) 并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn) ，它能够即时解答常见问题，并为您提供操作指导。

## 故障现象
新打印机或打印机恢复出厂设置后，在开机校准过程中出现了问题，无法继续校准。
![20251017-153923.jpg](/h2/troubleshooting/calibrate-failed/20251017-153923.jpg =600x)

出现上图故障提示后，请点击屏幕右上角 **“跳过”** 开机校准，进入主页点击“助手”查看HMS信息，然后在[HMS 主页面](https://wiki.bambulab.com/zh/hms/home)查询具体的HMS代码并进行故障排除。

### 常见故障原因：

**1. 打印机回中、调平过程存在异常。**
HMS代码：[HMS_0300-2500-0001-0005：Z轴电机转动动受阻,请检查Z滑块、Z同步带轮是否有异物卡住。](https://wiki.bambulab.com/zh/h2/troubleshooting/hmscode/0300_2500_0001_0005)
**2. 喷嘴偏移校准失败。**
HMS代码：[HMS_0300-2500-0001-000A：喷嘴偏移校准失败。检测到喷嘴粘料,可能影响打印质量。请清理喷嘴后重试。](https://wiki.bambulab.com/zh/h2/troubleshooting/hmscode/0300_2500_0001_000A)
**3. 喷嘴在位检测失败。**
HMS代码：[HMS_0300-2600-0001-000B：喷嘴在位检测失败；左挤出机喷嘴未安装或安装不到位。](https://wiki.bambulab.com/zh/h2/troubleshooting/hmscode/0300_2600_0001_000B)
**4. 固件未更新。**

## 故障排查
### 步骤1. 检查 Z滑块、Z同步带轮状态
请分别检查Z轴滑块与热床下方（图中所指位置）是否有异物。若有异物或阻塞，请小心清理异物。清理后进行回中测试，若测试正常无报错，则成功清理。
<div>

<img src="/h2/troubleshooting/hmscode/0300_2500_0001_0005/image-2_cn.png" width="385" height=" "/>
<img src="/h2/troubleshooting/hmscode/0300_2500_0001_0005/image-3_cn.png" width="415" height=" "/>

</div>

请小心倾斜打印机，检查底部Z同步带轮是否被异物卡住。可以手动拖拽同步带，观察是否阻塞Z轴运动。若有异物或阻塞，请小心清理异物。

![Z轴同步带卡滞、打印机底部异物检查](/h2/troubleshooting/hmscode/0300_2500_0001_0005/image-1_cn.png =600x)

### 步骤2. 检查喷嘴安装状态
请检查喷嘴是否正确安装，与热端加热组件紧密贴合,中间无任何异物；喷嘴卡扣是否正确扣紧，手动摇晃喷嘴是否松动，热端硅胶套是否安装到位。最后检查并清理干净喷嘴尖端的残余耗材。
<div>

<img src="/h2/19.卡扣正确.jpg" width="385" height=" "/>
<img src="/h2/manual/验证热端功能.gif" width="415" height=" "/>

</div>

若确认喷嘴安装正常，但问题依旧，那么请参考[更换 H2D 左右热端加热组件](https://wiki.bambulab.com/zh/h2/maintenance/hotend-heating-assembly)的步骤,重新安装一次加热组件。

### 步骤3. 调换喷嘴组件
如果确认加热组件安装正常，但打印机仍然报错，我们建议您调换左右喷嘴，并再次执行校准，并观察是否仍出现报错。详细更换步骤请参考：[更换 H2D 热端](https://wiki.bambulab.com/zh/h2/maintenance/replace-hotend)。

如果校准通过，则需要着重检查原喷嘴是否存在损坏，并手考虑更换新的喷嘴。如果校准仍然失败，则可能是传感器故障，请根据以下步骤继续进行故障排查。

### 步骤4. 检查喷嘴偏移校准传感器
断开喷嘴偏移校准传感器连接线,并重新连接。详细拔插步骤可参考：[更换 H2D 喷嘴偏移校准传感器](https://wiki.bambulab.com/zh/h2/maintenance/replace-nozzle-offset-calibration-sensor)。

<div>

<img src="/h2/maintenance/replace-nozzle-offset-calibration-sensor/image-15.png" width="400" height=" "/>
<img src="/h2/maintenance/replace-nozzle-offset-calibration-sensor/image-16.png" width="400" height=" "/>

</div>

重新插拔后，您可以再次进行校准测试。如果问题依旧存在，则可能是喷嘴偏移传感器损坏，建议您联系[拓竹技术支持](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并[提交打印机近期日志](https://wiki.bambulab.com/zh/h2/troubleshooting/how-to-upload-log)。

> 以下步骤请根据你实际使用的喷嘴（用于回中和校准的喷嘴）选择对应排查步骤：若使用右侧喷嘴，重点检查右涡流线圈；若使用左侧喷嘴，重点检查左涡流线圈。
{.is-info}

### 步骤5. 右喷嘴涡流线圈故障排查
**1. 检查涡流线圈外观**
移除喷嘴组件后，会看到涡流线圈被一层黑色醋酸胶带覆盖，下图为揭开胶带后的涡流线圈。无需揭开胶带，直接检查覆盖的胶带是否有受损或裸露线圈的情况。如果线圈受损，则需要更换该涡流线圈。
![右涡流线圈.png](/h2/troubleshooting/calibrate-failed/右涡流线圈.png =800x)

**2. 重新插拔右涡流线圈**
如果涡流线圈外观正常，则可能是涡流线圈接头松动或接触不良。此时，您需要重新插拔涡流线圈的连接线。插拔接头需要移除部件散热风扇和挤出接口板，然后撕掉贴在右涡流线圈接口上的胶布，将右涡流线圈连接线沿着插头所在的平面向外推出，并重新安装。
![image-35.png](/h2/maintenance/replace-nozzle-eddy-sensor/image-35.png =800x)
详细插拔步骤请参考: [H2D左右涡流线圈更换指南](https://wiki.bambulab.com/zh/h2/maintenance/replace-nozzle-eddy-sensor)

### 步骤6. 左涡流线圈故障排查
左侧涡流线圈位于工具头内部，通常不易出现破损或断裂。然而，可能会出现位置偏移或接头接触不良的问题。
您可以在移除部件冷却风道后，对左涡流线圈进行重新插拔。详细插拔步骤请参考: [H2D左右涡流线圈更换指南](https://wiki.bambulab.com/zh/h2/maintenance/replace-nozzle-eddy-sensor)

![image-15.png](/h2/maintenance/replace-nozzle-eddy-sensor/image-15.png =800x)

完成后可以再次进行校准，如果依旧存在故障，建议您联系[拓竹技术支持](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并[提交打印机近期日志](https://wiki.bambulab.com/zh/h2/troubleshooting/how-to-upload-log)。
