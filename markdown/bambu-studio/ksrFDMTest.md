---
title: 欧特克 FDM 测试模型介绍
url: https://wiki.bambulab.com/zh/bambu-studio/ksrFDMTest
category: Bambu Studio > 欧特克 FDM 测试模型介绍
updated: 2026-08-28T06:36:35.965Z
---

### 一、欧特克 FDM 测试

欧特克 FDM 测试 是由 Autodesk 与 Kickstarter 合作设计的标准校准和测试模型，用于评估 FDM 3D 打印机的性能。它将诸多高难度特征整合到一个几何模型中，让您可以精准了解打印机的优势与不足。

![banner.jpg](https://wiki.bambulab.com/software/bambu-studio/ksr-fdm-test/banner.jpg)

### 二、主要目标

- 提供客观的方式来 对比不同打印机、切片器设置和耗材 。
- 揭示机器的性能极限 ，例如：运动控制、挤出一致性、热端性能、散热能力等。
- 在初始设置或调试新材料时，作为 质量检查 的依据。
- 通过测试结果，您可以了解打印机距离 打印实际零件的理想输出 还有多大差距。
- 使用该测试文件有助于 避免实际打印失败和时间浪费 。

### 三、测试关注点

该模型可 评估 3D 打印机的多项关键打印质量指标 。在打印和开始调试前，建议您 先了解每个指标的含义 。

下表列出了该模型测试的主要指标：

在后续章节中， 将对每个指标进行详细说明 ，包括如何识别问题以及如何微调相关设置。

⏬ 选择标签页查看对应模块 ⏬

桥接测试 🌉 悬垂测试 🗻 尺寸精度 🎯 拉丝测试 🪡 公差测试 🧩

无支撑打印的水平结构，用于测试散热和挤出效果。

| 不同跨度桥接 | 桥接表面质量 |
| --- | --- |
| 〔图片〕 | 〔图片〕 |

无支撑打印的倾斜结构，用于测试打印机处理大角度悬垂的能力。

| 不同角度悬垂 | 45 度悬垂 |
| --- | --- |
| 〔图片〕 | 〔图片〕 |

通过小孔、槽位和薄壁结构测试打印机的尺寸精度。

| 多种精密几何结构 | 不同尺寸参考特征 |
| --- | --- |
| 〔图片〕 | 〔图片〕 |

通过细小的针状结构，暴露回抽设置不当或温度过高的问题。

![stringing_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/ksr-fdm-test/stringing_wiki.jpg)

通过嵌套圆柱结构，测试零件的配合松紧度。

![dimensions_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/ksr-fdm-test/pins_dimensions_wiki.jpg)

### 四、如何打印该模型

> ⚠️ 警告： 打印前请确保耗材干燥。 潮湿的耗材 会导致拉丝、表面质量差、尺寸精度下降等问题，这些问题可能会被误认为是测试要评估的打印机本身的问题。

#### 步骤 1：打开 Bambu Studio 并加载模型

在电脑上 启动 Bambu Studio 。

1. 在右侧操作窗口点击鼠标右键。
2. 选择 添加基础模型 。
3. 选择 欧特克 FDM 测试 。

![add_test_model_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/ksr-fdm-test/setting_1.jpg)

#### 步骤 2：选择打印机和耗材

1. 从配置文件列表中选择您的 Bambu Lab 打印机型号 （例如 A1、P1S、X1 Carbon）。
2. 选择要测试的 耗材 （例如 PLA 基础耗材）。
3. 从 标准 (Standard) 配置文件 开始测试。

> ℹ️ 注意： 测试结果与耗材和打印工艺直接相关，请使用您常用的耗材类型和打印配置文件。

![bambu_studio_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/ksr-fdm-test/setting_2.jpg)

#### 步骤 3：切片并打印

点击 切片 （1），然后发送到 打印平台 （2）。

![print_it_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/ksr-fdm-test/setting_3.jpg)

### 五、检查要点与优化方向

使用该模型提升打印质量是一个 迭代过程 ， 请每次只调整一个设置 。

避免同时修改多个设置 ，这会让您难以判断是哪个调整影响了结果。 请记录每次的调整内容，并注明对打印质量的影响 ，建议搭配照片和简短说明。

打印 模型 → 检查 结果 → 调整 单个设置 → 重复 上述步骤，直到打印结果符合您的要求。

![repeat_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/ksr-fdm-test/repeat_wiki_zh.jpg)

打印完成后，请检查以下方面：

#### 设备维护

首先，请确保设备得到妥善维护。良好的维护是稳定打印质量的基础。
维护不当会降低打印质量，同时增加故障排查难度，因为诊断过程中会引入更多变量。

[您可以通过此页面快速访问设备维护指南](https://wiki.bambulab.com/zh/home#maintenance-guides)

![maintenance_guides_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/ksr-fdm-test/setting_5.jpg)

#### 设备精度

检查模型上的所有针状结构是否能顺利取出。如果您有卡尺，也可以测量模型的外部尺寸。

| 验证实际尺寸 | 所有针状结构需可取出 |
| --- | --- |
| 〔图片〕 | 〔图片〕 |

您可以使用 Bambu Studio 内置的 测量工具 （1）来 测量任意两个表面之间的距离 （2），测量结果会实时显示（3）。

![dimensions_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/ksr-fdm-test/setting_6.jpg)

如果孔位过紧或壁厚尺寸不准确，请按以下顺序排查：

1. XYZ 轴清洁与润滑
2. 皮带张力检查
3. 设备精度校准（仅 H2 系列）
4. [耗材收缩率设置](https://wiki.bambulab.com/zh/knowledge-sharing/3d-prints-shrinkage)
5. [XY 孔位与轮廓补偿](https://wiki.bambulab.com/zh/software/bambu-studio/xy-hole-contour-compensation)

#### 拉丝问题

针状结构非常纤细，需要精准的挤出控制。
如果挤出控制不当，喷嘴在移动过程中可能会留下细小的熔丝，这种现象通常被称为拉丝。

过度拉丝通常表明回抽设置或打印温度存在问题。

如果您的针状结构表面有明显拉丝，请查看专门的 [拉丝故障排查页面](https://wiki.bambulab.com/zh/filament-acc/filament/print-quality/stringing-oozing) 。

![spires_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/ksr-fdm-test/spires_wiki_zh.jpg)

#### 桥接问题

检查桥接是否有下垂、熔滴或间隙不均的情况。

> ℹ️ 注意： 打印机与耗材的组合都有其极限。当桥接长度在 40–50 mm 左右有好的表现即属于非常好的结果，结果会因打印机、耗材和设置而异。

桥接质量良好意味着散热、温度、速度和桥接流量设置都较为合理。
如果您的桥接存在明显问题，建议查看我们的 [桥接参数设置 Wiki 页面](https://wiki.bambulab.com/zh/filament-acc/filament/print-quality/bridging) 。

![bridges_improove_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/ksr-fdm-test/bridges_improove_wiki_zh.jpg)

#### 悬垂问题

检查悬垂部分是否打印清晰，是否有下垂现象。
如果悬垂下垂、外观不一致或存在层缺失，您应该降低打印速度、减小层高或增加散热。
有关如何优化悬垂打印的详细信息，请查看我们的 [Wiki 页面](https://wiki.bambulab.com/zh/filament-acc/filament/print-quality/overhang) 。

> ℹ️ 注意： 并非所有打印机或耗材都能很好地打印大角度悬垂， 30 度以下的角度通常难度较大 。部分耗材需要较低的零件散热，这会影响桥接和悬垂打印效果，而增加散热又可能导致其他问题。

![overhang_tuned_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/ksr-fdm-test/overhang_tuned_wiki_zh.jpg)

#### 表面质量

检查顶面是否有横纹、间隙或不均匀的情况。顶面应光滑平整。
如需进一步提升表面质量，请查看专门的 [流量比校准 Wiki 页面](https://wiki.bambulab.com/zh/software/bambu-studio/calibration_flow_rate) 。

![flow_ratio_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/ksr-fdm-test/flow_ratio_wiki_zh.jpg)

### 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
> 如果本指南未解决您的问题， [请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5) ，我们随时准备为您解答疑问并提供帮助。
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
