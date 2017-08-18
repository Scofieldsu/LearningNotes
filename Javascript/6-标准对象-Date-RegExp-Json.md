
---

## 6-1 **标准对象**

- typeof 获取对象的类型，返回字符串：number ，string，boolean，function，undefined，object。注意：null和数组的类型也是object。

- 不要使用new Number()、new Boolean()、new String()创建包装对象；

- 用parseInt()或parseFloat()来转换任意类型到number；

- 用String()来转换任意类型到string，或者直接调用某个对象的toString()方法；

- 通常不必把任意类型转换为boolean再判断，因为可以直接写if (myVar) {...}；

- typeof操作符可以判断出number、boolean、string、function和undefined；

- 判断Array要使用Array.isArray(arr)；

- 判断null请使用myVar === null；

- 判断某个全局变量是否存在用typeof window.myVar === 'undefined'；

- 函数内部判断某个变量是否存在用typeof myVar === 'undefined'

- 注意：null和undefined没有toString()方法。Number类型的调用toString ：
    - 123..toString()
    - (123).toString()


---

## 6-2 **Date**

``` javascript

// 当前时间是浏览器从本机操作系统获取的时间，所以不一定准确，因为用户可以把当前时间设定为任何值。

var now = new Date();
now; // Wed Jun 24 2015 19:49:22 GMT+0800 (CST)
now.getFullYear(); // 2015, 年份
now.getMonth(); // 5, 月份，注意月份范围是0~11，5表示六月
now.getDate(); // 24, 表示24号
now.getDay(); // 3, 表示星期三
now.getHours(); // 19, 24小时制
now.getMinutes(); // 49, 分钟
now.getSeconds(); // 22, 秒
now.getMilliseconds(); // 875, 毫秒数
now.getTime(); // 1435146562875, 以number形式表示的时间戳

```

- 创建Date对象
    
    1. JavaScript的月份范围用整数表示是0~11
       ``` javascript
       var d = new Date(2015, 5, 19, 20, 15, 30, 123);
        d; // Fri Jun 19 2015 20:15:30 GMT+0800 (CST)

       ```

    
    2. 创建一个指定日期和时间的方法是解析一个符合ISO 8601格式的字符串
        ``` javascript
        var d = Date.parse('2015-06-24T19:49:22.875+08:00');
        d; // 1435146562875
        
        var d = new Date(1435146562875);
        d; // Wed Jun 24 2015 19:49:22 GMT+0800 (CST)

        ```

- 时区   

    - ```javascript
      var d = new Date(1435146562875);
      d.toLocaleString(); // '2015/6/24 下午7:49:22'，本地时间（北京时区+8:00），显示的字符串与操作系统设定的格式有关
      d.toUTCString(); // 'Wed, 24 Jun 2015 11:49:22 GMT'，UTC时间，与本地时间相差8小时
      ```

    - 时间戳是一个自增的整数，它表示从1970年1月1日零时整的GMT时区开始的那一刻，到现在的毫秒数。假设浏览器所在电脑的时间是准确的，那么世界上无论哪个时区的电脑，它们此刻产生的时间戳数字都是一样的，所以，时间戳可以精确地表示一个时刻，并且与时区无关

    - 获取时间戳
       - Date.now()  or  new Date().getTime() 


---

## 6-3 **RegExp**

- \d  匹配一个数字;\w  匹配一个字母或数字; .   匹配任意字符

- *表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符

- 用'\\'转义

- [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；

- [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'js2015'等等；

- [a-zA-Z\_\$][0-9a-zA-Z\_\$]*可以匹配由字母或下划线、$开头，后接任意个由一个数字、字母或者下划线、$组成的字符串，也就是JavaScript允许的变量名；

- [a-zA-Z\_\$][0-9a-zA-Z\_\$]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。

- A|B可以匹配A或B，所以(J|j)ava(S|s)cript可以匹配'JavaScript'、'Javascript'、'javaScript'或者'javascript'。

- ^表示行的开头，^\d表示必须以数字开头。

- $表示行的结束，\d$表示必须以数字结束

### **创建正则表达式**

 ``` javascript

var re1 = /ABC\-001/;
var re2 = new RegExp('ABC\\-001');

//测试匹配
var re = /^\d{3}\-\d{3,8}$/
re.test('010-12345')
 ```

- 切割字符串
    - ``` javascript
      'a b   c'.split(/\s+/); // ['a', 'b', 'c']
      'a,b, c  d'.split(/[\s\,]+/); // ['a', 'b', 'c', 'd']
      'a,b;; c  d'.split(/[\s\,\;]+/); // ['a', 'b', 'c', 'd']

      ```

- 分组()表示的就是要提取的分组（Group）
    - ```javascript
      var re = /^(\d{3})-(\d{3,8})$/;
      re.exec('010-12345'); // ['010-12345', '010', '12345']
      re.exec('010 12345'); // null
      ```

- 贪婪匹配

    - 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符

    - 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
       ``` javascript
       var re = /^(\d+?)(0*)$/;
       re.exec('102300'); // ['102300', '1023', '00']
       ```

- 全局搜索
    - JavaScript的正则表达式还有几个特殊的标志，最常用的是g，表示全局匹配

    - ``` javascript
      var r1 = /test/g;
      // 等价于:
      var r2 = new RegExp('test', 'g');
      ```
    - 全局匹配可以多次执行exec()方法来搜索一个匹配的字符串。当我们指定g标志后，每次运行exec()，正则表达式本身会更新lastIndex属性，表示上次匹配到的最后索引.

    - 全局匹配类似搜索，因此不能使用/^...$/，那样只会最多匹配一次

    - 正则表达式还可以指定i标志，表示忽略大小写，m标志，表示执行多行匹配

---

## 6-4 **Json - JavaScript Object Notation**

- 在JSON中，一共就这么几种数据类型：

    - number：和JavaScript的number完全一致；
    - boolean：就是JavaScript的true或false；
    - string：就是JavaScript的string；
    - null：就是JavaScript的null；
    - array：就是JavaScript的Array表示方式——[]；
    - object：就是JavaScript的{ ... }表示方式

- JSON还定死了字符集必须是UTF-8

- JSON的字符串规定必须用双引号""，Object的键也必须用双引号""

- 序列化
    - ``` javascript 
        var xiaoming = {
        name: '小明',
        age: 14,
        gender: true,
        height: 1.65,
        grade: null,
        'middle-school': '\"W3C\" Middle School',
        skills: ['JavaScript', 'Java', 'Python', 'Lisp']
        };

        JSON.stringify(xiaoming, null, '  '); 
        /* 
        {"name": "小明",
        "age": 14,
        "gender": true,
        "height": 1.65,
        "grade": null,
        "middle-school": "\"W3C\" Middle School",
        "skills": [
        "JavaScript",
        "Java",
        "Python",
        "Lisp"]
        } 
        */
      ``` 
    - 第二个参数用于控制如何筛选对象的键值，如果我们只想输出指定的属性，可以传入Array
    - 还可以传入一个函数，这样对象的每个键值对都会被函数先处理，convert， 把所有属性值都变成大写

- 反序列化
    - 用JSON.parse()把它变成一个JavaScript对象