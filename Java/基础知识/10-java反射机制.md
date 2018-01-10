## java 反射机制

---

### 常用

- 获得类的包名和类名:
   ``` java   
   person.getClass().getPackage().getName();
   person.getClass().getName()
   ```

- 创建类对象：
  ``` java
  Class<?>  class1 = null; 
  Class<?>  class2 = null; 
  class1 = Class.forName("com.xxx.xxx.Person");
  class2= Person.class
  Person person = (Person) class1.newInstance();//要实例化的这个类Person，一定要有无参构造函数
  ```

- 获得构造函数集合：
   
   ``` java
        Constructor<?>[] constructors = class1.getConstructors();

        person1 = (Person) constructors[0].newInstance();
   ```
   
- 操作成员变量：

   ``` java
        Object obj = class1.newInstance();
        Field personNameField = class1.getDeclaredField("name");
        personNameField.setAccessible(true);
        personNameField.set(obj, "xxxx");
   ```
   
- 得到类的一些属性： 继承的接口，父类，函数信息，成员信息，类型等:

   ``` java
   
   class1.getSuperclass();  //父类
   Field[] fields = class1.getDeclaredFields(); //成员信息
   Method[] methods = class1.getDeclaredMethods();  //函数集合
       methods[i].getName();                    //函数名
	   methods[i].getReturnType();              // 函数返回类型
	   Modifier.toString(methods[i].getModifiers());   //访问修饰符
	   methods[i]                                  //函数
	Class<?> interfaces[] = class1.getInterfaces();   //  接口集合
   ```
   
- 调用类方法：

   ``` java
   // 调用无参方法
    Method method = class1.getMethod("fly");
    method.invoke(class1.newInstance());

	//调用有参方法
    method = class1.getMethod("walk",int.class);
    method.invoke(class1.newInstance(),100);
   ```
   
- 获得类加载器信息

    ``` java
	 String nameString = class1.getClassLoader().getClass().getName();
	
	
     1）Bootstrap ClassLoader 此加载器采用c++编写，一般开发中很少见。

     2）Extension ClassLoader 用来进行扩展类的加载，一般对应的是jre\lib\ext目录中的类

     3）AppClassLoader 加载classpath指定的类，是最常用的加载器。同时也是java中默认的加载器。
	```