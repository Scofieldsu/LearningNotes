
---

## 8-1 **浏览器**

- *IE 6~11*：国内用得最多的IE浏览器，历来对W3C标准支持差。从IE10开始支持ES6标准；

- *Chrome*：Google出品的基于Webkit内核浏览器，内置了非常强悍的JavaScript引擎——V8。由于Chrome一经安装就时刻保持自升级，所以不用管它的版本，最新版早就支持ES6了；

- *Safari*：Apple的Mac系统自带的基于Webkit内核的浏览器，从OS X 10.7 Lion自带的6.1版本开始支持ES6，目前最新的OS X 10.11 El Capitan自带的Safari版本是9.x，早已支持ES6；

- *Firefox*：Mozilla自己研制的Gecko内核和JavaScript引擎OdinMonkey。早期的Firefox按版本发布，后来终于聪明地学习Chrome的做法进行自升级，时刻保持最新；

- 移动设备上目前iOS和Android两大阵营分别主要使用Apple的Safari和Google的Chrome，由于两者都是Webkit核心，结果HTML5首先在手机上全面普及（桌面绝对是Microsoft拖了后腿），对JavaScript的标准支持也很好，最新版本均支持ES6。

---

## 8-2 **浏览器对象**

- **window**：window对象不但充当全局作用域，而且表示浏览器窗口。
    
    - innerWidth和innerHeight属性，可以获取浏览器窗口的内部宽度和高度。内部宽高是指除去菜单栏、工具栏、边框等占位元素后，用于显示网页的净宽高。(IE<=8不支持)

    - outerWidth和outerHeight属性，可以获取浏览器窗口的整个宽高

- **navigator**:
   
    - *navigator.appName*：浏览器名称
    - *navigator.appVersion*：浏览器版本
    - *navigator.language*：浏览器设置的语言
    - *navigator.platform*：操作系统类型
    - *navigator.userAgent*：浏览器设定的User-Agent字符串
    - 常见做法：var width = window.innerWidth || document.body.clientWidth;

- **screen**：

    - *screen.width*：屏幕宽度，以像素为单位
    - *screen.height*：屏幕高度，以像素为单位
    - *screen.colorDepth*：返回颜色位数，如8、16、24

- **location**：location对象表示当前页面的URL信息，用location.href获取
 
 > http://www.example.com:8080/path/index.html?a=1&b=2#TOP
 
    - location.protocol; // 'http'
    - location.host; // 'www.example.com'
    - location.port; // '8080'
    - location.pathname; // '/path/index.html'
    - location.search; // '?a=1&b=2'
    - location.hash; // 'TOP' 

    - 要加载一个新页面，可以调用location.assign()。如果要重新加载当前页面，调用location.reload()方法

- **document**:document对象表示当前页面。由于HTML在浏览器中以DOM形式表示为树形结构，document对象就是整个DOM树的根节点

    - 用document对象提供的getElementById()和getElementsByTagName()可以按ID获得一个DOM节点和按Tag名称获得一组DOM节点

    - document对象还有一个cookie属性，可以获取当前页面的Cookie。

---

## 8-3 **操作DOM**

- HTML文档被浏览器解析后就是一棵DOM树，要改变HTML的结构，就需要通过JavaScript来操作DOM

- 最常用的方法是document.getElementById()和document.getElementsByTagName()，以及CSS选择器document.getElementsByClassName()

``` javascript 
// 返回ID为'test'的节点：
var test = document.getElementById('test');

// 先定位ID为'test-table'的节点，再返回其内部所有tr节点：
var trs = document.getElementById('test-table').getElementsByTagName('tr');

// 先定位ID为'test-div'的节点，再返回其内部所有class包含red的节点：
var reds = document.getElementById('test-div').getElementsByClassName('red');

// 获取节点test下的所有直属子节点:
var cs = test.children;

// 获取节点test下第一个、最后一个子节点：
var first = test.firstElementChild;
var last = test.lastElementChild;

```

- 第二种方法是使用querySelector()和querySelectorAll()，需要了解selector语法，然后使用条件来获取节点.(低版本的IE<8不支持querySelector和querySelectorAll。IE8仅有限支持)

```javascript
// 通过querySelector获取ID为q1的节点：
var q1 = document.querySelector('#q1');

// 通过querySelectorAll获取q1节点内的符合条件的所有节点：
var ps = q1.querySelectorAll('div.highlighted > p');
```

- 这里的DOM节点是指Element，但是DOM节点实际上是Node，在HTML中，Node包括Element、Comment、CDATA_SECTION等很多种，以及根节点Document类型，但是，绝大多数时候我们只关心Element，也就是实际控制页面结构的Node，其他类型的Node忽略即可。根节点Document已经自动绑定为全局变量document

---

## 8-4 **更新DOM**

- 一种是修改innerHTML属性，这个方式非常强大，不但可以修改一个DOM节点的文本内容，还可以直接通过HTML片段修改DOM节点内部的子树

- 第二种是修改innerText或textContent属性，这样可以自动对字符串进行HTML编码，保证无法设置任何HTML标签。（两者的区别在于读取属性时，innerText不返回隐藏元素的文本，而textContent返回所有文本。另外注意IE<9不支持textContent）

- **修改css**：DOM节点的style属性对应所有的CSS，可以直接获取或设置。因为CSS允许font-size这样的名称，但它并非JavaScript有效的属性名，所以需要在JavaScript中改写为驼峰式命名fontSize


---

## 8-5 **插入DOM**

