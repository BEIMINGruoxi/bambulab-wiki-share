---
title: 打印中挤出失败故障排查
url: https://wiki.bambulab.com/zh/general/troubleshooting/extrusion-failure
category: 拓竹打印机通用知识篇 > 故障排除
updated: 2026-09-24T11:37:34.123Z
---

### 故障现象

“挤出失败”是指打印过程中，挤出机没有按照预期将耗材送入热端并从喷嘴挤出。常见表现包括：

- 喷嘴完全不出料；
- 出料量明显变少或断断续续；
- 首层无法正常铺料；
- 打印中途出现空打；
- 挤出机发出“嗒嗒嗒”的声音；
- 打印结束后发现模型局部缺料。

### 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

### 状态自查

#### 1. 有无 HMS 报错

点击屏幕导航至助手，查看打印机屏幕中是否有 HMS 错误提示。与该现象相关的提示关键词为：

- 热端风扇转速异常
- 挤出电机过载

扫描屏幕二维码，根据上述错误提示对应的 Wiki 操作即可，若问题未解决，请继续浏览下文完成故障排查。

根据您的实际情况选择下列选项👇

A 系列 P1 系列 其他机型

点击屏幕右下角 助手 图标，进入助手页查看是否有 HMS 错误提示。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

P1 系列打印机若出现 HMS 错误提示，将会在屏幕提示。

您也可以通过 Bambu Studio 或 Bambu Handy，查看错误提示。

![screencn.png](https://wiki.bambulab.com/wiki/how_to_use_wiki/studio-assistant-hms.png)

点击屏幕左下角 助手 图标，进入助手页查看是否有 HMS 错误提示。

![screencn.png](https://wiki.bambulab.com/x1/troubleshooting/intro-hms/screencn.png)

#### 2. 是否发生在首层

首层是指模型与热床接触的第一层。请参考下面图片，确认故障是否发生在第一层。若故障发生在非首层，可点击下方按钮跳转至非首层挤出失败故障排查。

| 〔图片〕 | 〔图片〕 |
| --- | --- |
| 首层 | 非首层 |

### 首层挤出失败

通过屏幕手动控制打印机进料，观察耗材是否正确挤出。

根据您的实际情况选择下列选项👇

A1 系列 & A2L X1 系列 & P1 系列 P2S & H2S X2D H2D & H2C

将喷嘴温度提高到 略高于 耗材要求的温度（以PLA为例，设置热端温度为250℃），点击屏幕上的“挤出”按钮挤出耗材,尝试手动挤出，观察耗材是否正确挤出。耗材应呈直线状连续流出，如下图所示：

> 注意：若使用 TPU 材料，“进料”按钮最多只能点击三次。同时避免快速连续点击“退料”按钮，以防出现卡料或缠料。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

若耗材能正确挤出，则说明故障原因可能是首层偏低（即首层热端太靠近热床）。点击跳转对应机型 Wiki 查看解决方案。

[A1 & A1 mini](https://wiki.bambulab.com/zh/a1-mini/troubleshooting/print-issues-troubleshooting) [A2L](https://wiki.bambulab.com/zh/a2l/maintenance/first-layer-quality-calibration#first_layer_is_too_low)

若耗材无法正确挤出，请根据非首层挤出失败方案继续排查。

将喷嘴温度提高到 略高于 耗材要求的温度（以PLA为例，设置热端温度为250℃），点击屏幕上的“挤出”按钮挤出耗材,尝试手动挤出。

> 注意：若使用 TPU 材料，“进料”按钮最多只能点击三次。同时避免快速连续点击“退料”按钮，以防出现卡料或缠料。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

> P1 系列请参考下图。手动挤出（下键）或退出（上键）耗材。
>
>
> ![p1s_extrude.jpg](https://wiki.bambulab.com/general/troubleshooting/extrusion-failure/p1s_extrude.jpg)

观察耗材是否正确挤出。耗材应呈直线状连续流出，如下图所示：

![filament_flow_1.jpg](https://wiki.bambulab.com/knowledge-sharing/filament_flow_1.jpg)

若耗材能正确挤出，则说明故障原因可能是首层偏低（即首层热端太靠近热床）。点击跳转 Wiki 查看解决方案。

[X1 系列 & P1 系列](https://wiki.bambulab.com/zh/x1/troubleshooting/first-layer-printing-optimization-guide)

若耗材无法正确挤出，请根据非首层挤出失败方案继续排查。

将喷嘴温度提高到 略高于 耗材要求的温度（以PLA为例，设置热端温度为250℃），点击屏幕上的“挤出”按钮挤出耗材,尝试手动挤出。

> 注意：若使用 TPU 材料，“进料”按钮最多只能点击三次。同时避免快速连续点击“退料”按钮，以防出现卡料或缠料。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

观察耗材是否正确挤出。耗材应呈直线状连续流出，如下图所示：

![图片](https://wiki.bambulab.com/p2s/maintenance/cold-pull-maintenance-hotend/20251113-142241.jpg)

若耗材能正确挤出，则说明故障原因可能是首层偏低（即首层热端太靠近热床）。点击跳转 Wiki 查看解决方案。

[P2S](https://wiki.bambulab.com/zh/p2s/troubleshooting/first-layer-printing-optimization-guide#first_layer_is_too_low) [H2S](https://wiki.bambulab.com/zh/h2s/troubleshooting/first-layer-printing-optimization-guide)

若耗材无法正确挤出，请根据非首层挤出失败方案继续排查。

将喷嘴温度提高到 略高于 耗材要求的温度（以PLA为例，设置热端温度为250℃），点击屏幕上的“挤出”按钮挤出耗材,尝试手动挤出，观察耗材是否正确挤出。耗材应呈直线状连续流出，如下图所示：

> 注意：若使用 TPU 材料，“进料”按钮最多只能点击三次。同时避免快速连续点击“退料”按钮，以防出现卡料或缠料。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

观察耗材是否正确挤出。耗材应呈直线状连续流出，如下图所示：

![图片](https://public-cdn.bblmw.com/wiki/new/x2d/clogging/005.png)

若耗材能正确挤出，则说明故障原因可能是首层偏低（即首层热端太靠近热床）。点击跳转 Wiki 查看解决方案。

[X2D](https://wiki.bambulab.com/zh/x2d/troubleshooting/first-layer-printing-optimization-guide)

若耗材无法正确挤出，请根据非首层挤出失败方案继续排查。

将喷嘴温度提高到 略高于 耗材要求的温度（以PLA为例，设置热端温度为250℃），点击屏幕上的“挤出”按钮挤出耗材,尝试手动挤出，观察耗材是否正确挤出。耗材应呈直线状连续流出，如下图所示：

> 注意：若使用 TPU 材料，“进料”按钮最多只能点击三次。同时避免快速连续点击“退料”按钮，以防出现卡料或缠料。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

观察耗材是否正确挤出。耗材应呈直线状连续流出，如下图所示：

![图片](https://wiki.bambulab.com/h2c/troubleshoting/unclogging/compressed_file/4.webp)

若耗材能正确挤出，则说明故障原因可能是首层偏低（即首层热端太靠近热床）。点击跳转 Wiki 查看解决方案。

[H2D](https://wiki.bambulab.com/zh/h2/troubleshooting/first-layer-printing-optimization-guide) [H2C](https://wiki.bambulab.com/zh/h2c/troubleshooting/first-layer-printing-optimization-guide)

若耗材无法正确挤出，请根据非首层挤出失败方案继续排查。

### 非首层挤出失败

#### 步骤一 更换耗材，观察故障是否消失

更换其他耗材（建议使用官方 PLA Basic 或 PETG 测试），通过打印机屏幕 [手动进料](https://wiki.bambulab.com/zh/general/troubleshooting/extrusion-failure#first_layer) ，观察耗材是否正常挤出。

- 若更换耗材后，故障消失，说明可能是耗材粗细不均导致。
- 若所有耗材均出现挤出失败现象，请继续排查。

#### 步骤二 使用默认参数切片打印

若您在修改了打印参数，或修改打印速度（使用了运动模式/狂暴模式）。请使用默认参数重新对模型进行切片打印，打印时请使用标准模式或静音模式进行测试。

P 系列：

![图片](https://wiki.bambulab.com/p1/screen-operation/%E5%B1%8F%E5%B9%95%E6%93%8D%E4%BD%9C/6.%E6%89%93%E5%8D%B0%E9%80%9F%E5%BA%A6.jpeg)

A 系列及其他型号打印机：

| A 系列 〔图片〕 | 其他 〔图片〕 |
| --- | --- |

- 若故障消失，说明可能是参数/打印速度设置不当，导致耗材来不及熔化造成的挤出不足。
- 若故障依旧，请继续排查。

#### 步骤三 观察耗材能否送出挤出机

> 注意：部分机型在控制挤出机挤出时会提醒需要升温，选择 仍然进料/本次不再提示 即可。
>
>
> ![code_zh.jpg](https://wiki.bambulab.com/general/troubleshooting/extrusion-failure/code_zh.jpg)

根据您的实际情况选择下列选项👇

A 系列 X1 系列 & P1 系列 P2S H2S X2D H2D & H2C

确认喷嘴处于室温，按下切刀刀柄切断耗材。移除工具头前盖和硅胶套，然后打开卡扣，移除热端。更多操作细节请参考 Wiki： [更换热端/喷嘴](https://wiki.bambulab.com/zh/a1/maintenance/replace-hotend) 。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

点击屏幕主页 控制→挤出机 ，通过按向下及向上箭头图标，控制挤出机进料及退料。观察耗材是否能送出挤出机，下图所示为耗材成功送出挤出机。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

- 若耗材可以送出挤出机，说明是热端堵塞导致，请选择您的打印机机型，点击跳转 Wiki 清理热端。

[A2L](https://wiki.bambulab.com/zh/a2l/maintenance/cold-pull-maintenance-hotend) [A1 系列](https://wiki.bambulab.com/zh/a1-mini/troubleshooting/nozzle-clog)

- 若耗材无法送出挤出机，请继续排查。

确认喷嘴处于室温，按下切刀刀柄切断耗材。打开工具头前盖，然后拧下 2 颗热端固定螺丝，移除热端。更多操作细节请参考 Wiki： [更换热端/喷嘴](https://wiki.bambulab.com/zh/x1/maintenance/replace-hotend) 。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

打开打印机，点击屏幕主页 控制→喷嘴和挤出机 ，通过按向下及向上箭头图标，控制挤出机进料及退料。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

> P1 系列请参考下图。手动挤出（下键）或退出（上键）耗材。
>
>
> ![p1s_extrude.jpg](https://wiki.bambulab.com/general/troubleshooting/extrusion-failure/p1s_extrude.jpg)

观察耗材是否能送出挤出机，下图所示为耗材成功送出挤出机。

![extrude_success.png](https://wiki.bambulab.com/general/troubleshooting/extrusion-failure/extrude_success.png)

- 若耗材可以送出挤出机，说明是热端堵塞导致，请选择您的打印机机型，点击跳转 Wiki 清理热端： [喷嘴/热端堵塞](https://wiki.bambulab.com/zh/x1/troubleshooting/nozzle-clog) 。
- 若耗材无法送出挤出机，请继续排查。

确认喷嘴处于室温，按下切刀刀柄切断耗材。移除工具头前盖和硅胶套，然后打开卡扣，移除热端。更多操作细节请参考 Wiki： [更换热端/喷嘴](https://wiki.bambulab.com/zh/p2s/troubleshooting/clogging) 。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

点击屏幕主页 控制→喷嘴和挤出机 ，通过按向下及向上箭头图标，控制挤出机进料及退料。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

观察耗材是否能送出挤出机，下图所示为耗材成功送出挤出机。

![图片](https://wiki.bambulab.com/p2s/manual/jichu2.webp%22)

- 若耗材可以送出挤出机，说明是热端堵塞导致，请选择您的打印机机型，点击跳转 Wiki 清理热端： [喷嘴/热端堵塞](https://wiki.bambulab.com/zh/p2s/maintenance/cold-pull-maintenance-hotend) 。
- 若耗材无法送出挤出机，请继续排查。

确认喷嘴处于室温，按下切刀刀柄切断耗材。移除工具头前盖和硅胶套，然后打开卡扣，移除热端。更多操作细节请参考 Wiki： [更换热端/喷嘴](https://wiki.bambulab.com/zh/h2s/troubleshooting/nozzle-clog) 。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

点击屏幕主页 控制→喷嘴和挤出机 ，通过按向下箭头图标，控制挤出机进料。观察耗材是否能送出挤出机，下图所示为耗材成功送出挤出机。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

观察耗材是否能送出挤出机，下图所示为耗材成功送出挤出机。

![extrude_success_h2s.png](https://wiki.bambulab.com/general/troubleshooting/extrusion-failure/extrude_success_h2s.png)

- 若耗材可以送出挤出机，说明是热端堵塞导致，请选择您的打印机机型，点击跳转 Wiki 清理热端： [喷嘴/热端堵塞](https://wiki.bambulab.com/zh/h2s/troubleshooting/nozzle-clog) 。
- 若耗材无法送出挤出机，请继续排查。

确认喷嘴处于室温，手动推动工具头至尾部的切刀顶杆，向后按压工具头，确保 热端与挤出机之间的耗材被完全切断 。

![图片](https://public-cdn.bblmw.com/wiki/new/x2d/toolheadhousing/extruder-cleaning-guide/043.webp)

移除工具头前盖和硅胶套，然后打开卡扣，移除热端。更多操作细节请参考 Wiki： [更换热端/喷嘴](https://wiki.bambulab.com/zh/x2d/maintenance/replace-hotend-and-silicone-sock) 。

![unlock_right_click.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_and_sock/unlock_right_click.jpg)

点击屏幕主页 控制→喷嘴和挤出机 ，根据实际情况选择左边/右边，通过按向下及向上箭头图标，控制挤出机进料及退料。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

观察耗材是否能送出挤出机，下图所示为耗材成功送出挤出机。

![图片](https://public-cdn.bblmw.com/wiki/new/x2d/clogging/002.webp)

- 若耗材可以送出挤出机，说明是热端堵塞导致，请选择您的打印机机型，点击跳转 Wiki 清理热端： [喷嘴/热端堵塞](https://wiki.bambulab.com/zh/x2d/maintenance/cold-pull-maintenance-hotend) 。
- 若耗材无法送出挤出机，请继续排查。

确认喷嘴处于室温，按下切刀刀柄切断耗材。移除工具头前盖和硅胶套，然后打开卡扣，移除热端。更多操作细节请参考 Wiki：

[H2C 感应热端](https://wiki.bambulab.com/zh/h2c/maintenance/replace-induction-hotend) [H2D & H2C 左热端](https://wiki.bambulab.com/zh/h2/maintenance/replace-hotend)

| 〔图片〕 | 〔图片〕 |
| --- | --- |

点击屏幕主页 控制→喷嘴和挤出机 ，根据实际情况选择左边/右边，通过按向下及向上箭头图标，控制挤出机进料及退料。

| 〔图片〕 | 〔图片〕 |
| --- | --- |

观察耗材是否能送出挤出机，下图所示为耗材成功送出挤出机。

![图片](https://wiki.bambulab.com/general/troubleshooting/extrusion-failure/extruder_success_h2d.jpg)

- 若耗材可以送出挤出机，说明是热端堵塞导致，请选择您的打印机机型，点击跳转 Wiki 清理热端。

[H2C](https://wiki.bambulab.com/zh/h2c/troubleshooting/unclogging) [H2D](https://wiki.bambulab.com/zh/h2/troubleshooting/unclogging)

- 若耗材无法送出挤出机，请继续排查。

#### 步骤四 观察齿轮是否转动

继续通过屏幕手动控制挤出机进退料，观察挤出机齿轮是否转动。

请点击切换不同机型的操作步骤👇

A 系列 & H2S X1 系列 & P1 系列 & P2S X2D H2D & H2C

手动控制打印机进退料，观察工具头内的旋转轮是否旋转，旋转轮可以显示挤出机齿轮的旋转状态。

![a_extruder_gear.jpg](https://wiki.bambulab.com/general/troubleshooting/extrusion-failure/a_extruder_gear.jpg)

- 若齿轮无法转动，可能是耗材变形或残留，导致挤出机堵塞。请根据您的机型选择下列选项，参考对应 Wiki 清理挤出机。

[A1 系列](https://wiki.bambulab.com/zh/a1-mini/troubleshooting/extruder-clog) [A2L](https://wiki.bambulab.com/zh/a2l/maintenance/extruder-cleaning-guide) [H2S](https://wiki.bambulab.com/zh/h2s/troubleshooting/extruder-cleaning-guide)

- 若齿轮可以转动，请继续排查。

手动控制打印机进退料，从工具头侧面的小窗，观察挤出机齿轮的旋转状态。

![extruder_gear.jpg](https://wiki.bambulab.com/general/troubleshooting/extrusion-failure/extruder_gear.jpg)

- 若齿轮无法转动，可能是耗材变形或残留，导致挤出机堵塞。请根据您的机型选择下列选项，参考对应 Wiki 清理挤出机。

[X1 系列](https://wiki.bambulab.com/zh/x1/troubleshooting/extruder-clog) [P1 系列](https://wiki.bambulab.com/zh/p1/maintenance/extruder-cleaning-guide) [P2S](https://wiki.bambulab.com/zh/p2s/maintenance/extruder-cleaning-guide)

- 若齿轮可以转动，请继续排查。

1. 手动控制打印机进退料，从工具头侧面的小窗，观察挤出机齿轮的旋转状态。若齿轮可以转动，请前往下一步继续排查。

![extruder_gear.jpg](https://wiki.bambulab.com/general/troubleshooting/extrusion-failure/extruder_gear.jpg)

1. 若齿轮无法转动，请判断故障发生在左喷嘴一侧还是右喷嘴一侧。

- 若故障发生在左喷嘴一侧，可能是主挤出机堵塞，请参考 Wiki 清理主挤出机： [X2D 主挤出机堵塞清洁维护](https://wiki.bambulab.com/zh/x2d/maintenance/extruder-cleaning-guide)
- 若故障发生在右喷嘴一侧，请检查辅助挤出机的料管是否安装到位，若没有安装到位重新进行安装后再进行尝试。

| 按压辅助挤出机进料口气动接头，拔除料管 〔图片〕 | 使用扳手拧松辅助挤出机出料口的夹紧螺母，拔除料管 〔图片〕 |
| --- | --- |

> 安装出料口料管时，请确认铁氟龙料管插入到底。使用开口六角扳手拧紧螺母，直到听见"哒哒"声即说明锁紧。

- 若故障发生在右喷嘴一侧且料管已经安装到位，但耗材仍无法正常进入辅助挤出机，检查辅助挤出机即可。详细操作请参考 Wiki 清理主挤出机： [X2D 辅助挤出机堵塞清洁维护](https://wiki.bambulab.com/zh/x2d/maintenance/auxiliary-extruder-cleaning-guide)

1. 手动控制打印机进退料，透过挤出机前盖观察挤出机齿轮的旋转状态。若齿轮可以转动，请前往下一步继续排查。

![h2d_extruder_gear.jpg](https://wiki.bambulab.com/general/troubleshooting/extrusion-failure/h2d_extruder_gear.jpg)

1. 若齿轮无法转动，可能是挤出机前盖或从动杆发生堵塞。请根据您的机型选择下列选项，参考对应 Wiki 清理。

[H2C](https://wiki.bambulab.com/zh/h2c/troubleshooting/extruder-cleaning-guide) [H2D](https://wiki.bambulab.com/zh/h2/troubleshooting/dual-extruder-Idlers-clogging)

![前盖导向螺丝.png](https://wiki.bambulab.com/h2/maintenance/replace-dual-extruder-filament-guide/%E5%89%8D%E7%9B%96%E5%AF%BC%E5%90%91%E8%9E%BA%E4%B8%9D.png)

#### 步骤五 拔出耗材，观察耗材是否被正确咬合

按压工具头上方料管接口的黑色外圈，垂直用力拔出料管，露出料管内耗材。其他机型移除料管操作可参考： [拓竹铁氟龙料管介绍](https://wiki.bambulab.com/zh/filament-acc/acc/ptfe-tube) ，然后尝试手动向外拔出料管内的耗材。

![a2l-pack-001-s02-press-toolhead-inlet-collar.png.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/packing/a2l-pack-001-s02-press-toolhead-inlet-collar.png.png)

- 若耗材拉不动或有明显阻力，说明是正确咬合，请前往下一步进行排查。
- 若耗材可以比较轻松地前后抽动，说明挤出机齿轮咬合不足，可能是挤出机齿轮安装异常或齿轮解耦。选择您的打印机机型，根据下列指引，检查挤出机内部部件是否安装正确。

请点击切换不同机型的操作步骤👇

A 系列 X 列 & P 系列 H2D & H2C H2S

关闭打印机电源，移除挤出机前盖 4 颗固定螺丝，然后拆除挤出机前盖，检查挤出机内部安装：

- 检查从动轮弹簧压片安装是否到位
- 检查轴承是否卡滞或脱落
- 检查侧边固定螺丝是否锁紧

详细操作细节请参考以下 Wiki，固定螺丝及弹簧压片位置如下图所示：

[A1 系列](https://wiki.bambulab.com/zh/a1-mini/troubleshooting/extruder-clog) [A2L](https://wiki.bambulab.com/zh/a2l/maintenance/replace-extruder-gear-assembly)

![a1_check.jpg](https://wiki.bambulab.com/general/troubleshooting/extrusion-failure/a1_check1.jpg)

若上述部件安装均正常，但仍可用手轻松拉动被咬合的耗材。开启打印机，点击屏幕 控制 → 挤出机（图示 6 号） ，通过屏幕点击向上/向下箭头，控制挤出电机转动，尝试手动进料。

![jcj015.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/017.png)

然后尝试向上拔出耗材，观察主动齿轮（#1）和传动齿轮（#2）是否同轴旋转，若主动齿轮和传动齿轮其中只有一个旋转，则说明齿轮解耦，需要更换挤出机齿轮组件。

[A1 系列](https://wiki.bambulab.com/zh/a1-mini/troubleshooting/extruder-clog) [A2L](https://wiki.bambulab.com/zh/a2l/maintenance/replace-extruder-gear-assembly)

![图片](https://wiki.bambulab.com/general/troubleshooting/extrusion-failure/extruder_gear.png)

您也可以固定住主动齿轮，然后用手轻轻转动传动齿轮，测试是否齿轮解耦。

| 正常 〔图片〕 | 齿轮解耦 〔图片〕 |
| --- | --- |

关闭打印机电源，拆下挤出机，检查挤出机内部安装：

- 检查从动轮弹簧压片安装是否到位
- 检查轴承是否卡滞或脱落
- 检查侧边固定螺丝是否锁紧

详细操作细节请参考以下 Wiki。

[P1 系列](https://wiki.bambulab.com/zh/p1/maintenance/extruder-cleaning-guide) [X1 系列](https://wiki.bambulab.com/zh/x1/troubleshooting/extruder-clog) [P2S](https://wiki.bambulab.com/zh/p2s/maintenance/replace-extruder-components) [X2D](https://wiki.bambulab.com/zh/x2d/maintenance/replace-extruder-components)

若上述部件安装均正常，但仍可用手轻松拉动被咬合的耗材。您可以固定住主动齿轮，然后用手轻轻转动传动齿轮。

| 正常 〔图片〕 | 齿轮解耦 〔图片〕 |
| --- | --- |

若主动齿轮和传动齿轮其中只有一个旋转，则说明齿轮解耦，请参考上述 Wiki 操作更换挤出机齿轮。

关闭打印机电源，检查从动轮组件和挤出机齿轮安装是否正确。

详细操作细节请参考以下 Wiki。

[从动轮组件](https://wiki.bambulab.com/zh/h2/maintenance/replace-dual-extruder-idlers-and-filament-sensor) [挤出机齿轮](https://wiki.bambulab.com/zh/h2/maintenance/replace-dual-extruder-gears-switch-cam)

若上述部件安装均正常，但仍可用手轻松拉动被咬合的耗材。您可以固定住主动齿轮，然后用手轻轻转动传动齿轮。

| 正常 〔图片〕 | 齿轮解耦 〔图片〕 |
| --- | --- |

若主动齿轮和传动齿轮其中只有一个旋转，则说明齿轮解耦，请参考上述 Wiki 操作更换挤出机齿轮。

关闭打印机电源，移除挤出机前盖 4 颗固定螺丝，然后拆除挤出机前盖，检查挤出机内部安装：

- 检查从动轮弹簧压片安装是否到位
- 检查轴承是否卡滞或脱落
- 检查侧边固定螺丝是否锁紧

详细操作细节请参考 Wiki： [更换挤出机齿轮](https://wiki.bambulab.com/zh/h2s/maintenance/replace-extruder-gear-assembly) ，固定螺丝及弹簧压片位置如下图所示：

![h2s_check.jpg](https://wiki.bambulab.com/general/troubleshooting/extrusion-failure/h2s_check.jpg)

开启打印机，若上述部件安装均正常，但仍可用手轻松拉动被咬合的耗材，点击屏幕 控制 → 喷嘴和挤出机 → 挤出机（图示 1 号） ，通过屏幕点击向上/向下箭头，控制挤出电机转动。

![喷嘴和挤出机-h2s.png](https://wiki.bambulab.com/h2s/manual/screen-operation/%E5%96%B7%E5%98%B4%E5%92%8C%E6%8C%A4%E5%87%BA%E6%9C%BA-h2s.png)

然后尝试向上拔出耗材，观察主动齿轮（#1）和传动齿轮（#2）是否同轴旋转。若主动齿轮和传动齿轮其中只有一个旋转，则说明齿轮解耦，需要 [更换挤出机齿轮](https://wiki.bambulab.com/zh/h2s/maintenance/replace-extruder-gear-assembly) 。

![图片](https://wiki.bambulab.com/general/troubleshooting/extrusion-failure/extruder_gear_h2s.jpg)

您也可以固定住主动齿轮，然后用手轻轻转动传动齿轮，测试是否齿轮解耦。

| 正常 〔图片〕 | 齿轮解耦 〔图片〕 |
| --- | --- |

#### 步骤六 观察挤出电机是否正常转动

观察挤出电机能否转动，若挤出电机可以持续转动，且用手略微增加阻力不影响其转动，说明挤出电机工作正常。

| 挤出电机正常转动 〔图片〕 | 挤出电机位置 〔图片〕 |
| --- | --- |

请点击切换不同机型的操作步骤👇

A 系列 X1 系列 & P1 系列 P2S H2S H2C & H2D

关闭打印机电源，拆除挤出机前盖及挤出机齿轮，以便观察挤出电机。详细操作细节请参考以下 Wiki:

[A1 系列](https://wiki.bambulab.com/zh/a1-mini/troubleshooting/extruder-clog) [A2L](https://wiki.bambulab.com/zh/a2l/maintenance/replace-extruder-gear-assembly)

![jcj015.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-extruder-gear-assembly/jcj015.jpg)

开启打印机，点击屏幕 控制 → 挤出机（图示 6 号） ，通过屏幕点击向上/向下箭头，控制挤出电机转动。

![jcj015.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/017.png)

观察挤出电机是否正常转动。

- 若挤出电机正常转动，且人为略微增加阻力不会使其停止旋转。请点击联系 [人工客服](https://support.bambulab.cn/liveChat/?from=5) ，建议您将上述操作结果通过文字描述、图片或动图形式告知人工客服，帮助我们快速定位问题。
- 若挤出电机可以转动，但在工作时人为略微增加阻力可以轻易被停止，说明电机扭矩不足，需更换挤出机。请点击跳转对应机型更换挤出电机指南：
  [A1 系列](https://wiki.bambulab.com/zh/a1/maintenance/A1_Extruder_motor_replacement) [A2L](https://wiki.bambulab.com/zh/a2l/maintenance/replace-a3508-extruder-motor)

- 挤出电机无法转动，关闭打印机，让电机冷却一段时间再重新测试，若挤出电机恢复转动，说明可能是挤出电机过热保护导致停转。若该现象在 10℃-30℃ 频繁出现，建议更换挤出电机后，观察故障是否解决。请点击跳转对应机型更换挤出电机指南：
  [A1 系列](https://wiki.bambulab.com/zh/a1/maintenance/A1_Extruder_motor_replacement) [A2L](https://wiki.bambulab.com/zh/a2l/maintenance/replace-a3508-extruder-motor)

- 若更换挤出电机后，故障依旧存在，说明可能是由打印机电路故障。请按以下顺序更换部件进行排查，测试故障是否消失：TH 板 → USB 数据线 → MC 板。

| 机型 | 更换 TH 板 | USB 数据线 | MC 板 |
| --- | --- | --- | --- |
| A1 | 更换 TH 板 | USB 数据线 | MC 板 |
| A1 mini | 更换 TH 板 | USB 数据线 | MC 板 |
| A2L | 更换 TH 板 | USB 数据线 | MC 板 |

关闭打印机电源，移除挤出机，以便观察挤出电机。详细操作细节请参考 Wiki:

[X1 系列](https://wiki.bambulab.com/zh/x1/maintenance/replace-extruder) [P1 系列](https://wiki.bambulab.com/zh/p1/maintenance/extruder-unit)

| 〔图片〕 | 〔图片〕 |
| --- | --- |

开启打印机，点击屏幕 控制 → 喷嘴和挤出机 → 挤出机（图示 1 号） ，通过屏幕点击向上/向下箭头，控制挤出电机转动。

![20250513-165810.jpg](https://wiki.bambulab.com/screen-operation/20250513-165810.jpg)

P1 系列可通过按键选择 控制 → 挤出机 ，手动挤出（下键）或退出（上键）耗材。

![8.挤出机.jpg](https://wiki.bambulab.com/p1/screen-operation/%E5%B1%8F%E5%B9%95%E6%93%8D%E4%BD%9C/8.%E6%8C%A4%E5%87%BA%E6%9C%BA.jpg)

观察挤出电机是否正常转动。

- 若挤出电机正常转动，且人为略微增加阻力不会使其停止旋转。请点击联系 [人工客服](https://support.bambulab.cn/liveChat/?from=5) ，建议您将上述操作结果通过文字描述、图片或动图形式告知人工客服，帮助我们快速定位问题。
- 若挤出电机可以转动，但在工作时人为略微增加阻力可以轻易被停止，说明电机扭矩不足，需更换挤出机。请点击跳转对应机型更换挤出电机指南：
  [X1 系列](https://wiki.bambulab.com/zh/x1/maintenance/replace-the-extrude-motor) [P1 系列](https://wiki.bambulab.com/zh/p1/maintenance/replace-extruder-motor)

- 挤出电机无法转动，关闭打印机，让电机冷却一段时间再重新测试，若挤出电机恢复转动，说明可能是挤出电机过热保护导致停转。若该现象在 10℃-30℃ 频繁出现，建议更换挤出电机后，观察故障是否解决。请点击跳转对应机型更换挤出电机指南：
  [X1 系列](https://wiki.bambulab.com/zh/x1/maintenance/replace-the-extrude-motor) [P1 系列](https://wiki.bambulab.com/zh/p1/maintenance/replace-extruder-motor)

- 若更换挤出电机后，故障依旧存在，说明可能是由打印机电路故障。请按以下顺序更换部件进行排查，测试故障是否消失：TH 板 → USB 数据线 → MC 板。

| 机型 | 更换 TH 板 | USB 数据线 | MC 板 |
| --- | --- | --- | --- |
| X1 系列 | 更换 TH 板 | USB 数据线 | MC 板 |
| P1 系列 | 更换 TH 板 | USB 数据线 | MC 板 |

关闭打印机电源，移除挤出机，以便观察挤出电机。详细操作细节请参考 Wiki: [更换挤出机配件](https://wiki.bambulab.com/zh/p2s/maintenance/replace-extruder-components)

| 〔图片〕 | 〔图片〕 |
| --- | --- |

开启打印机，点击屏幕 控制 → 喷嘴和挤出机 → 挤出机（图示 1 号） ，通过屏幕点击向上/向下箭头，控制挤出电机转动。

![nozzle-cn-1.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/nozzle-cn-1.png)

观察挤出电机是否正常转动。

- 若挤出电机正常转动，且人为略微增加阻力不会使其停止旋转。请点击联系 [人工客服](https://support.bambulab.cn/liveChat/?from=5) ，建议您将上述操作结果通过文字描述、图片或动图形式告知人工客服，帮助我们快速定位问题。
- 若挤出电机可以转动，但在工作时人为略微增加阻力可以轻易被停止，说明电机扭矩不足，需更换挤出机。请点击跳转 [更换挤出电机指南](https://wiki.bambulab.com/zh/p2s/maintenance/replace-3508-extruder-servo-motor)
- 挤出电机无法转动，关闭打印机，让电机冷却一段时间再重新测试，若挤出电机恢复转动，说明可能是挤出电机过热保护导致停转。若该现象在 10℃-30℃ 频繁出现，建议更换挤出电机后，观察故障是否解决。请点击跳转 [更换挤出电机指南](https://wiki.bambulab.com/zh/p2s/maintenance/replace-3508-extruder-servo-motor)
- 若更换挤出电机后，故障依旧存在，说明可能是由打印机电路故障。请按以下顺序更换部件进行排查，测试故障是否消失：TH 板 → USB 数据线 → MC 板。

| 机型 | 更换 TH 板 | USB 数据线 | MC 板 |
| --- | --- | --- | --- |
| P2S | 更换 TH 板 | USB 数据线 | MC 板 |

关闭打印机电源，拆除挤出机前盖及挤出机齿轮，以便观察挤出电机。详细操作细节请参考 Wiki: [更换挤出机齿轮](https://wiki.bambulab.com/zh/h2s/maintenance/replace-extruder-gear-assembly)

![图片](https://public-cdn.bblmw.com/wiki/new/aether/h2s/troubleshooting/hmscode/0300_0900_0001_0001/image-4.png)

开启打印机，点击屏幕 控制 → 喷嘴和挤出机 → 挤出机（图示 1 号） ，通过屏幕点击向上/向下箭头，控制挤出电机转动。

![喷嘴和挤出机-h2s.png](https://wiki.bambulab.com/h2s/manual/screen-operation/%E5%96%B7%E5%98%B4%E5%92%8C%E6%8C%A4%E5%87%BA%E6%9C%BA-h2s.png)

观察挤出电机是否正常转动。

- 若挤出电机正常转动，且人为略微增加阻力不会使其停止旋转。请点击联系 [人工客服](https://support.bambulab.cn/liveChat/?from=5) ，建议您将上述操作结果通过文字描述、图片或动图形式告知人工客服，帮助我们快速定位问题。
- 若挤出电机可以转动，但在工作时人为略微增加阻力可以轻易被停止，说明电机扭矩不足，需更换挤出机。请点击跳转 [更换挤出电机指南](https://wiki.bambulab.com/zh/h2s/maintenance/replace-extruder-motor)
- 挤出电机无法转动，关闭打印机，让电机冷却一段时间再重新测试，若挤出电机恢复转动，说明可能是挤出电机过热保护导致停转。若该现象在 10℃-30℃ 频繁出现，建议更换挤出电机后，观察故障是否解决。请点击跳转 [更换挤出电机指南](https://wiki.bambulab.com/zh/h2s/maintenance/replace-extruder-motor)
- 若更换挤出电机后，故障依旧存在，说明可能是由打印机电路故障。请按以下顺序更换部件进行排查，测试故障是否消失：TH 板 → USB 数据线 → MC 板。

| 机型 | 更换 TH 板 | USB 数据线 | MC 板 |
| --- | --- | --- | --- |
| H2S | 更换 TH 板 | USB 数据线 | MC 板 |

关闭打印机电源，拆除挤出机前盖及挤出机齿轮，以便观察挤出电机。详细操作细节请参考 Wiki: [更换挤出机齿轮](https://wiki.bambulab.com/zh/h2/maintenance/replace-dual-extruder-gears-switch-cam)

![h2d_motor.png](https://wiki.bambulab.com/general/troubleshooting/extrusion-failure/h2d_motor.png)

开启打印机，点击屏幕 控制 → 喷嘴和挤出机 → 挤出机（图示 4 号） ，通过屏幕点击向上/向下箭头，控制挤出电机转动。

![20250513-165810.jpg](https://wiki.bambulab.com/general/troubleshooting/extrusion-failure/h2d_2.png)

- 若挤出电机正常转动，且人为略微增加阻力不会使其停止旋转。请点击联系 [人工客服](https://support.bambulab.cn/liveChat/?from=5) ，建议您将上述操作结果通过文字描述、图片或动图形式告知人工客服，帮助我们快速定位问题。
- 若挤出电机可以转动，但在工作时人为略微增加阻力可以轻易被停止，说明电机扭矩不足，需更换挤出机。请点击跳转 [更换挤出电机指南](https://wiki.bambulab.com/zh/h2/maintenance/replace-extruder-servo-motor)
- 挤出电机无法转动，关闭打印机，让电机冷却一段时间再重新测试，若挤出电机恢复转动，说明可能是挤出电机过热保护导致停转。若该现象在 10℃-30℃ 频繁出现，建议更换挤出电机后，观察故障是否解决。请点击跳转 [更换挤出电机指南](https://wiki.bambulab.com/zh/h2/maintenance/replace-extruder-servo-motor)
- 若更换挤出电机后，故障依旧存在，说明可能是由打印机电路故障。请按以下顺序更换部件进行排查，测试故障是否消失：TH 板 → USB 数据线 → MC 板。

| 机型 | 更换 TH 板 | USB 数据线 | MC 板 |
| --- | --- | --- | --- |
| H2D | 更换 TH 板 | USB 数据线 | MC 板 |
| H2C | 更换 TH 板 | USB 数据线 | MC 板 |

### 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
> 如果本指南未解决您的问题， [请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5) ，我们随时准备为您解答疑问并提供帮助。
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
