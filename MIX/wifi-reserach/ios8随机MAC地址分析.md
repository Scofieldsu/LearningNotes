### ios8 MAC随机化分析

在iPhone 5s中发现了MAC随机化（细节如下），但在iPhone 5和iPad Mini中却没有。我怀疑这与新一代iPhone的操作系统架构差异有关。


#### *在iPhone 5s中，MAC随机化仅在以下情况下发生：*

- 手机处于睡眠模式（显示关闭，未被使用）
- Wi-Fi应该打开但不关联
- 位置服务应在隐私设置中关闭

#### *在上述条件下，iPhone5s将在探测请求中使用随机MAC，具有以下特征：*

- 随机化的MAC是本地管理的MAC。

- **在电话显示屏关闭后大约120-150秒钟，手机将传送第一批具有随机MAC的探测请求**。

- 在2.4 GHz和5 GHz频段内，批次内和所有通道内的所有探测请求都使用相同的随机MAC地址。

- **下一批次的探测请求会随着批次之间的升级间隔而增加，最大间隔约为385秒，然后下一批次再次以大约120-150秒作为初始时间。跟踪时间为1小时**。

- 所有这些探测请求都使用相同的随机MAC地址。

- **探测请求中使用的随机MAC地址在每次手机被激活并随后进入睡眠模式时都会更改。意味着每个新的睡眠周期都使用一个新的随机MAC**。

- 处于睡眠模式的探测请求不要求特定的SSID（称为空探测）。这似乎是一个额外的隐私功能，以防止在手机的无线配置文件中的SSID显示在睡眠模式。

- 无论手机是否在充电，MAC随机化都会发生。

## 结论

**测请求中使用的随机MAC地址在每次手机被激活并随后进入睡眠模式时都会更改。意味着每个新的睡眠周期都使用一个新的随机MAC**。

原文地址：https://blog.mojonetworks.com/ios8-mac-randomization-analyzed/

---

相关：https://blog.mojonetworks.com/ios8-mac-randomgate/

专利《一种获取WiFi终端真实MAC地址的装置及方法》：   https://www.google.com/patents/CN107094293A?cl=zh

---
