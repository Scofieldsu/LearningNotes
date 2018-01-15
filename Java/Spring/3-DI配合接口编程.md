### 接口编程示例

- 接口 ChangeLetter, 方法 change()
- 类UpperLetter 和 LowerLetter 实现接口ChangeLetter

使用接口访问bean：

``` java
ChangeLetter changeLetter = (ChangeLetter)ac.getBean("changeLetter");
System.out.println(changeLetter.change());
```

xml配置：
``` XML
<!--<bean id="changeLetter" class="com.inter.UpperLetter">-->
    <!--<property name="str" value="abcd"></property>-->
<!--</bean>-->

<bean id="changeLetter" class="com.inter.LowerLetter">
    <property name="str" value="EFCG"></property>
</bean>
```

- 使用不同类去实现，只需要修改xml配置。
