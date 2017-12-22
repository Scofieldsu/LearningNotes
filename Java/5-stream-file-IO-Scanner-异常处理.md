## Stream

### 读取控制台输入

``` java
BufferedReader br = new BufferedReader(new 
                      InputStreamReader(System.in));
	
	
使用时函数   throws IOException
c = (char) br.read();
str = br.readLine();	

```


- FileInputStream 使用：InputStream f = new FileInputStream("C:/java/hello");

- FileOutputStream 使用：OutputStream f = new FileOutputStream("C:/java/hello")


``` java
import java.io.*;
 
public class fileStreamTest2{
  public static void main(String[] args) throws IOException {
    
    File f = new File("a.txt");
    FileOutputStream fop = new FileOutputStream(f);
    // 构建FileOutputStream对象,文件不存在会自动新建
    
    OutputStreamWriter writer = new OutputStreamWriter(fop, "UTF-8");
    // 构建OutputStreamWriter对象,参数可以指定编码,默认为操作系统默认编码,windows上是gbk
    
    writer.append("中文输入");
    // 写入到缓冲区
    
    writer.append("\r\n");
    //换行
    
    writer.append("English");
    // 刷新缓存冲,写入到文件,如果下面已经没有写入的内容了,直接close也会写入
    
    writer.close();
    //关闭写入流,同时会把缓冲区内容写入文件,所以上面的注释掉
    
    fop.close();
    // 关闭输出流,释放系统资源
 
    FileInputStream fip = new FileInputStream(f);
    // 构建FileInputStream对象
    
    InputStreamReader reader = new InputStreamReader(fip, "UTF-8");
    // 构建InputStreamReader对象,编码与写入相同
 
    StringBuffer sb = new StringBuffer();
    while (reader.ready()) {
      sb.append((char) reader.read());
      // 转成char加到StringBuffer对象中
    }
    System.out.println(sb.toString());
    reader.close();
    // 关闭读取流
    
    fip.close();
    // 关闭输入流,释放系统资源
 
  }
}

```

---

## 文件

- File

- FileReader

- FileWriter

----

- 创建目录：mkdir()创建一个文件夹；mkdirs()创建一个文件夹和它的所有父文件夹

``` java
String dirname = "/tmp/user/java/bin";
    File d = new File(dirname);
    // 现在创建目录
    d.mkdirs();
```

- 读取目录：list(); isDirectory();

``` java
String dirname = "/tmp";
    File f1 = new File(dirname);
    if (f1.isDirectory()) {
      System.out.println( "目录 " + dirname);
      String s[] = f1.list();
      for (int i=0; i < s.length; i++) {
        File f = new File(dirname + "/" + s[i]);
        if (f.isDirectory()) {
          System.out.println(s[i] + " 是一个目录");
        } else {
          System.out.println(s[i] + " 是一个文件");
        }
      }
    } else {
      System.out.println(dirname + " 不是一个目录");
    }
```


``` java
//删除文件及目录
  public static void deleteFolder(File folder) {
    File[] files = folder.listFiles();
        if(files!=null) { 
            for(File f: files) {
                if(f.isDirectory()) {
                    deleteFolder(f);
                } else {
                    f.delete();
                }
            }
        }
        folder.delete();
    }
```

---

## Scanner

``` shell
next() 与 nextLine() 区别
next():

1、一定要读取到有效字符后才可以结束输入。
2、对输入有效字符之前遇到的空白，next() 方法会自动将其去掉。
3、只有输入有效字符后才将其后面输入的空白作为分隔符或者结束符。
next() 不能得到带有空格的字符串。
nextLine()：

1、以Enter为结束符,也就是说 nextLine()方法返回的是输入回车之前的所有字符。
2、可以获得空白。

```

- 使用

``` java
Scanner scan = new Scanner(System.in); 
if(scan.hasNext()){
    String str1 = scan.next();
    String str2 = scan.nextLine();
}


```

---

## 异常


!(异常类)[images/java-exceptions.png]

- 所有的异常类是从 java.lang.Exception 类继承的子类。

- java 非检查性异常

!(非检查性异常)[images/java-exceptions1.png]

- java  检查性异常

!(检查性异常)[images/java-exceptions2.png]

- 异常方法

!(异常方法)[images/java-exceptions3.png]


### 捕获异常

``` java
try{
   // 程序代码
}catch(异常类型1 异常的变量名1){
  // 程序代码
}catch(异常类型2 异常的变量名2){
  // 程序代码
}catch(异常类型2 异常的变量名2){
  // 程序代码
} finally {
  //程序代码，无论是否发生异常，finally 代码块中的代码总会被执行。
}


```

- throws/throw

``` java
import java.io.*;
public class className
{
  public void deposit(double amount) throws RemoteException
  {
    // Method implementation
    throw new RemoteException();
  }
  //Remainder of class definition
}

```
