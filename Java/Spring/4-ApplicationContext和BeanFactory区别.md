### 使用ApplicationContext和BeanFactory获取bean的区别

1. ApplicationContext 获取

``` java
ApplicationContext ac = new ClassPathXmlApplicationContext("beans.xml");
// 实例化beans.xml时，该文件中配置的bean被实例化（该bean的 scope 是singleton）
// 可在类的无参构造函数中打印语句验证
// 预先加载消耗内存
```

2. BeanFactory 获取
``` java
BeanFactory factory = new XmlBeanFactory(new ClassPathXmlApplicationContext("beans.xml"))
factory.getBean("userService")
// 实例化factory 时不会创建bean实例，只有当getBean 获取某个bean时才会创建bean实例
// 节约内存速度慢
```

> 使用应用上下文加载的常用方法：

- ClassPathXmlApplicationContext  类路径加载

- FileSystemXmlApplicationContext  文件系统加载

- XmlWebApplicationContext         web系统中加载

---
