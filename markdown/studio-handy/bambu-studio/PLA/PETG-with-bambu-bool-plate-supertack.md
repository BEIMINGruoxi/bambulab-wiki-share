---
title: 拓竹增稳低温打印板首层不兼容 Support for PLA/PETG，直接在打印板表面打印 Support f
url: https://wiki.bambulab.com/zh/studio-handy/bambu-studio/PLA/PETG-with-bambu-bool-plate-supertack
category: Bambu Suite, Bambu Studio & Bambu Handy
updated: 2026-09-09T10:02:20.941Z
---

拓竹增稳低温打印板首层不兼容 Support for PLA/PETG，直接在打印板表面打印 Support for PLA/PETG 会损坏打印板，故 Bambu Studio 在切片完成检测到有首层存在 Support for PLA/PETG 时会出现错误提示并禁止打印。

### 打印建议

1.建议在使用 Support for PLA/PETG 时按如下方式选择仅在支撑界面使用支撑材料。

![20241108-182318.jpg](https://wiki.bambulab.com/bambu-studio/pla-petg/20241108-182318.jpg)

2.当打印的模型无法避免在首层使用支撑材料时，可以通过增加阀层（阀层数不小于 2）来避免 Support for PLA/PETG直接打印在打印板上。

![20241108-182336.jpg](https://wiki.bambulab.com/bambu-studio/pla-petg/20241108-182336.jpg)
