## Spring Initializr

- 对于Spring boot可以使用IDEA professional进行创建spring boot项目。也可以在http://start.spring.io/  创建项目然后本地IDE打开。

- 项目启动有多种方法：

    - 直接运行xxxxApplication文件
	
	- mvn  spring-boot：run
	
	- 运行mvn  install编译后，在target目录下 java -jar  xxx.jar
	
- helloworld

``` java
@RestController
public class HelloSpringBoot {


    @RequestMapping(value="/hello", method = RequestMethod.GET)
    public String hello() {
        return "Hello Spring Boot!";
    }
}

```
	