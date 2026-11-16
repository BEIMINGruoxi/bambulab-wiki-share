---
title: 跳闸、设备漏电的排查建议
url: https://wiki.bambulab.com/zh/general/tripping-and-electric-issue
category: 拓竹打印机通用知识篇 > 跳闸、设备漏电的排查建议
updated: 2026-08-28T06:19:57.547Z
---

### 跳闸

家庭中常见的空气开关（漏电保护器）在漏电电流达到 0.03 A 时会立即断开。当整条回路上的所有电器累计的漏电电流超过此阈值，空气开关便会跳闸，实现漏电防护。

如果打印机工作过程中频繁引发跳闸，可以尝试以下方案：

- 临时方案：将打印机连接到其他电路插座，避免与其他大功率电器共用同一回路。
- 专业方案：为打印机单独安装空气开关并接入主电网（需由专业电工操作）。

重要说明：拓竹打印机符合 GB4341 和 IEC62368 安全标准，漏电流量仅为法规允许最大值的一半，安全性有保障。

### 漏电

正常情况下，打印机的微弱漏电会通过地线安全导出。如果您在使用过程中感觉到框架或热床金属板带有微弱电流，请按照后文检查设备地线完整性。

若打印机地线完整，则漏电原因可能会 家庭电路中地线缺失 ，漏电流无法通过电源线导出；
或 其他电器产生的漏电 ，通过打印机形成了“地线-3D 打印机-人体”通路，若打印机关机状态下依然感受到微弱电流，请及时联系专业电工检查。

### 安全提示

#### 重要提醒

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
> 在您对打印机进行故障排查或维护时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

### 所需工具

- 万用表：用于测量电路导通性和电阻值（使用方法参考： [如何使用万用表检测电路是否正常](https://wiki.bambulab.com/zh/knowledge-sharing/multimeter) ）
- 内六角螺丝刀：用于拆卸和安装部件

> 提示：使用万用表测量时，蜂鸣器响或电阻很低表示电路导通（正常）；无蜂鸣声或电阻很大表示电路阻断（异常）。

### 排查过程

#### 测量电源线（通用步骤）

除A1mini外，其他型号打印机的电源线都可以单独拆下。建议首先测量电源线的地线导通性，万用表使用电阻档，表笔分别搭在三角插两端的地线上。

![iamge1.jpg](https://wiki.bambulab.com/general/tripping-electric-issue/iamge1.jpg)

如果电阻值非常小，那么可以确定电源线地线正常，请进行后续步骤。如果电阻值非常大或无法测出，请更换新的电源线。

---

#### 测量打印机（选择型号）

A1mini 型号排查 A1 型号排查 X1/P1 型号排查 P2S/X2D 型号排查 H2 型号排查

- 测量步骤
  使用万用表的蜂鸣器档位或电阻档位，测量电源线与打印机框架之间的导通性。万用表使用“Ω”档，表笔分别搭在电源线地线以及Y轨道上。

![image2.jpg](https://wiki.bambulab.com/general/tripping-electric-issue/image2.jpg)

- 结果判断
  1. 正常：电阻很低 → 说明打印机无问题，建议咨询专业电工检查
  2. 异常：电阻很大 → 需要重新安装电源线，若故障依旧则需要更换电源线,可参考 [A1 mini 底座拆装指引](https://wiki.bambulab.com/zh/a1-mini/maintenance/bottom-base#%E6%AD%A5%E9%AA%A45%EF%BC%9A%E7%A7%BB%E9%99%A4%E7%94%B5%E6%BA%90%E7%BA%BF) 。

- 测量步骤
  将电源线安装在打印机上，测量电源线与热床之间的导通性，万用表使用“Ω”档，表笔分别搭在电源线以及热床金属板上。

![image3.jpg](https://wiki.bambulab.com/general/tripping-electric-issue/image3.jpg)

- 结果判断
  1. 正常：电阻很低 → 说明打印机无问题，建议咨询专业电工检查
  2. 异常（热床-电源线阻断）：进一步测量电源线与框架的导通性，表笔分别搭在电源线地线以及底部金属框架上。
  ![image4.jpg](https://wiki.bambulab.com/general/tripping-electric-issue/image4.jpg)
  a.如果正常 → 参考 [A1 电源开关更换指南](https://wiki.bambulab.com/zh/a1/maintenance/replacement_of_power_switch) 重新安装下图地线接头；重装后依然异常 → 需要 [更换热床](https://wiki.bambulab.com/zh/a1/maintenance/heatbed)
  ![image5.jpg](https://wiki.bambulab.com/general/tripping-electric-issue/image5.jpg)
  b. 如果异常 → 参考 [A1 电源开关更换指南](https://wiki.bambulab.com/zh/a1/maintenance/replacement_of_power_switch) 重新安装开关；重装后依然异常 → 需要更换开关

- 测量步骤
  测量电源线与热床之间的导通性，万用表使用“Ω”档，表笔分别搭载电源线地线以及热床的调平螺母上。

![image6.jpg](https://wiki.bambulab.com/general/tripping-electric-issue/image6.jpg)

- 结果判断

1. 正常：电阻很低 → 说明打印机无问题，建议咨询专业电工检查
2. 异常（热床-电源线阻断）：进一步测量电源线与框架的导通性，前门上铰链与金属框架连接，可以进行测量。
  ![image7.jpg](https://wiki.bambulab.com/general/tripping-electric-issue/image7.jpg)
  ![image8.jpg](https://wiki.bambulab.com/general/tripping-electric-issue/image8.jpg)
  a. 如果正常 → X1 参考 [更换右侧面板](https://wiki.bambulab.com/zh/x1/maintenance/replace-right-panel) ， [更换 X1 系列金属后面板](https://wiki.bambulab.com/zh/x1/maintenance/replace-rear-panel) ； P1 参考 [更换 P1 系列塑胶右侧板](https://wiki.bambulab.com/zh/p1/maintenance/p1s-right-panel) （P1S 需要移除右侧板，P1P 无须此步骤）， [更换 P1 系列金属背板](https://wiki.bambulab.com/zh/p1/maintenance/p1s-rear-panel)
  重新安装热床地线；重装后依然异常 → 需要更换热床
  X1/P1S
  ![图片](https://wiki.bambulab.com/x1/maintenance/replace-heat-bed-v3/ground_cable.jpg)
  P1P
  ![图片](https://wiki.bambulab.com/knowledge-sharing/leakage_current_detection/p1p%E5%9C%B0%E7%BA%BF.png)
  b. 如果异常 → 参考 [更换电源开关座](https://wiki.bambulab.com/zh/x1/maintenance/replace-power-switch-assembly) 重新安装开关地线；重装后依然异常 → 需要更换电源开关座

- 测量步骤
  测量"热床-电源线"之间的导通性，万用表使用“Ω”档，表笔分布搭在热床调平螺丝以及电源线地线上。
  ![image9.jpg](https://wiki.bambulab.com/general/tripping-electric-issue/image9.jpg)
- 结果判断

1. 正常：电阻很低 → 说明打印机无问题，建议咨询专业电工检查
2. 异常（热床-电源线阻断）：进一步测量电源线与框架的导通性
  ![image10.jpg](https://wiki.bambulab.com/general/tripping-electric-issue/image10.jpg)
  a. 如果正常 → 参考 [更换背板 | Bambu Lab Wiki](https://wiki.bambulab.com/zh/p2s/maintenance/replace-rear-panel) 、 [更换左侧板 | Bambu Lab Wiki](https://wiki.bambulab.com/zh/p2s/maintenance/replace-left-side-panel) 预先拆除侧板，重新安装热床地线；重装后依然异常 → 需要更换热床
  ![03_heated_bed_ground_wire_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/03_heated_bed_ground_wire_003.png)
  b. 如果异常 → 参考 [更换 P2S 电源开关插座](https://wiki.bambulab.com/zh/p2s/maintenance/replace-power-switch-assembly) 重新安装开关地线；重装后依然异常 → 需要更换电源开关插座
  ![05_grounding_screw_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/05_grounding_screw_005.png)

- 测量步骤
  测量"热床-电源线"之间的导通性，万用表使用“Ω”档，表笔分布搭在热床调平螺丝以及电源线地线上。
  ![image11.jpg](https://wiki.bambulab.com/general/tripping-electric-issue/image11.jpg)
- 结果判断

1. 正常：电阻接近0Ω → 说明打印机无问题，建议咨询专业电工检查
2. 异常（热床-电源线阻断）： 进一步测量电源线与框架的导通性
  ![image12.jpg](https://wiki.bambulab.com/general/tripping-electric-issue/image12.jpg)
  a. 如果正常 → 参考 [更换 H2D 热床组件](https://wiki.bambulab.com/zh/h2/maintenance/replace-heatbed-unit) 拆下背板，重新安装热床地线；重装后依然异常 → 需要更换热床
  ![图片](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-16.png)
  b. 如果异常 → 参考 [更换 H2D 电源开关插座](https://wiki.bambulab.com/zh/h2/maintenance/replace-power-socket) 重新安装开关地线；重装后依然异常 → 需要更换电源开关
  ![图片](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/image-22.png)

### 附录：X1系列打印机接线方式检查

#### 确保使用最优的 AC 控制板的接线方式

检查打印机的AC控制板的接线方式。打印机有两种接线方式（均满足IEC62368安全标准），使用右边的接线方式可能会使漏电流降低，但2种接线方式漏电流均在法规范围内。

- [更换 AC 电源板](https://wiki.bambulab.com/zh/x1/maintenance/replace-ac-board) （V2版本）
- [AC 电源板](https://wiki.bambulab.com/zh/p1/maintenance/ac-board) （V3版本）

![图片](https://wiki.bambulab.com/general/tripping-electric-issue/cn-ac-connect-wiring.png)

右边的接线方式漏电流更低：蓝色线缆连接到第一个座子，棕色线缆连接到第二个座子

### 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
> 如果本指南未解决您的问题， [请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5) ，我们随时准备为您解答疑问并提供帮助。
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
