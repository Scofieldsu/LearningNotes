
---

## 10-1 **jQuery**

- JavaScript世界中使用最广泛的一个库

- 消除浏览器差异：你不需要自己写冗长的代码来针对不同的浏览器来绑定事件，编写AJAX等代码；

- 简洁的操作DOM的方法：写$('#test')肯定比document.getElementById('test')来得简洁；

- 轻松实现动画、修改CSS等各种操作

- 目前jQuery有1.x和2.x两个主要版本，区别在于2.x移除了对古老的IE 6、7、8的支持，因此2.x的代码更精简。选择哪个版本主要取决于你是否想支持IE 6~8。

- jQuery只是一个jquery-xxx.js文件，但你会看到有compressed（已压缩）和uncompressed（未压缩）两种版本

- 使用jQuery

```javascript
<html>
<head>
    <script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
    ...
</head>
<body>
    ...
</body>
</html>

```
---

## 10-2 **$符号**

- $是著名的jQuery符号。实际上，jQuery把所有功能全部封装在一个全局变量jQuery中，而$也是一个合法的变量名，它是变量jQuery的别名

``` javascript
window.jQuery; // jQuery(selector, context)
window.$; // jQuery(selector, context)
$ === jQuery; // true
typeof($); // 'function'
```

- $本质上就是一个函数，但是函数也是对象，于是$除了可以直接调用外，也可以有很多其他属性。

- 注意，你看到的$函数名可能不是jQuery(selector, context)，因为很多JavaScript压缩工具可以对函数名和参数改名，所以压缩过的jQuery源码$函数可能变成a(b, c)。

- 绝大多数时候，我们都直接用$（因为写起来更简单嘛）。但是，如果$这个变量不幸地被占用了，而且还不能改，那我们就只能让jQuery把$变量交出来，然后就只能使用jQuery这个变量


``` javascript
$; // jQuery(selector, context)
jQuery.noConflict();
$; // undefined
jQuery; // jQuery(selector, context)
```

- 这种黑魔法的原理是jQuery在占用$之前，先在内部保存了原来的$,调用jQuery.noConflict()时会把原来保存的变量还原。


---

## 10-3 **选择器**

### 按ID查找：

``` javascript
// 查找<div id="abc">:
var div = $('#abc');
```
- jQuery对象类似数组，它的每个元素都是一个引用了DOM节点的对象。

- jQuery的选择器不会返回undefined或者null，而是返回jQuery对象 []，这样的好处是你不必在下一行判断if (div === undefined)。

### 按tag查找：

``` javascript
var ps = $('p'); // 返回所有<p>节点
ps.length; // 数一数页面有多少个<p>节点
```

### 按class查找：

``` javascript
var a = $('.red.green'); // 注意没有空格！
// 符合条件的节点：
// <div class="red green">...</div>
// <div class="blue green red">...</div>
```

### 按属性查找：

``` javascript
var icons = $('[name^=icon]'); // 找出所有name属性值以icon开头的DOM
// 例如: name="icon-1", name="icon-2"
var names = $('[name$=with]'); // 找出所有name属性值以with结尾的DOM
// 例如: name="startswith", name="endswith"

var icons = $('[class^="icon-"]'); // 找出所有class包含至少一个以`icon-`开头的DOM
// 例如: class="icon-clock", class="abc icon-home"

```

### 组合查找：

``` javascript
var emailInput = $('input[name=email]'); // 不会找出<div name="email">

var tr = $('tr.red'); // 找出<tr class="red ...">...</tr>
```

### 多项选择器：

```javascript
$('p,div'); // 把<p>和<div>都选出来
$('p.red,p.green'); // 把<p class="red">和<p class="green">都选出来
```

---

## 10-4 **层级选择器**

``` javascript
$('ul.lang li.lang-javascript'); // [<li class="lang-javascript">JavaScript</li>]
$('div.testing li.lang-javascript'); // [<li class="lang-javascript">JavaScript</li>]
```

- 子选择器：
    
    ```javascript
    $('ul.lang>li.lang-javascript'); // 可以选出[<li class="lang-javascript">JavaScript</li>]
    $('div.testing>li.lang-javascript'); // [], 无法选出，因为<div>和<li>不构成父子关系
    ```
- 过滤器：

    ``` javascript
    $('ul.lang li'); // 选出JavaScript、Python和Lua 3个节点

    $('ul.lang li:first-child'); // 仅选出JavaScript
    $('ul.lang li:last-child'); // 仅选出Lua
    $('ul.lang li:nth-child(2)'); // 选出第N个元素，N从1开始
    $('ul.lang li:nth-child(even)'); // 选出序号为偶数的元素
    $('ul.lang li:nth-child(odd)'); // 选出序号为奇数的元素
    ```
---

## 10-5 **查找和过滤**

### 过滤

- 最常见的查找是在某个节点的所有子节点中查找，使用find()方法，它本身又接收一个任意的选择器

``` javascript
var ul = $('ul.lang'); // 获得<ul>
var dy = ul.find('.dy'); // 获得JavaScript, Python, Scheme
var swf = ul.find('#swift'); // 获得Swift
var hsk = ul.find('[name=haskell]'); // 获得Haskell
```

### 查找

- filter()方法可以过滤掉不符合选择器条件的节点：
    
    ``` javascript
    var langs = $('ul.lang li'); // 拿到JavaScript, Python, Swift, Scheme和Haskell
    var a = langs.filter('.dy'); // 拿到JavaScript, Python, Scheme
    ```
- map()方法把一个jQuery对象包含的若干DOM节点转化为其他对象
    ``` javascript
    var langs = $('ul.lang li'); // 拿到JavaScript, Python, Swift, Scheme和Haskell
    var arr = langs.map(function () {
    return this.innerHTML;
    }).get(); // 用get()拿到包含string的Array：['JavaScript', 'Python', 'Swift', 'Scheme', 'Haskell']
    ```
- 一个jQuery对象如果包含了不止一个DOM节点，first()、last()和slice()方法可以返回一个新的jQuery对象，把不需要的DOM节点去掉

   ``` javascript
   var langs = $('ul.lang li'); // 拿到JavaScript, Python, Swift, Scheme和Haskell
   var js = langs.first(); // JavaScript，相当于$('ul.lang li:first-child')
   var haskell = langs.last(); // Haskell, 相当于$('ul.lang li:last-child')
   var sub = langs.slice(2, 4); // Swift, Scheme, 参数和数组的slice()方法一致
   ```

---

## 10-6 **操作DOM**

### 修改Text和Html

- jQuery的API设计非常巧妙：无参数调用text()是获取文本，传入参数就变成设置文本，HTML也是类似操作，

### 修改CSS

``` javascript
 $('#test-css li.dy>span').css('background-color', '#ffd351').css('color', 'red');
```
- jQuery对象的所有方法都返回一个jQuery对象（可能是新的也可能是自身），这样我们可以进行链式调用，非常方便。

``` javascript
var div = $('#test-div');
div.hasClass('highlight'); // false， class是否包含highlight
div.addClass('highlight'); // 添加highlight这个class
div.removeClass('highlight'); // 删除highlight这个class

var a = $('a[target=_blank]');
a.hide(); // 隐藏
a.show(); // 显示
```

``` javascript
// 浏览器可视窗口大小:
$(window).width(); // 800
$(window).height(); // 600

// HTML文档大小:
$(document).width(); // 800
$(document).height(); // 3500

// 某个div的大小:
var div = $('#test-div');
div.width(); // 600
div.height(); // 300
div.width(400); // 设置CSS属性 width: 400px，是否生效要看CSS是否有效
div.height('200px'); // 设置CSS属性 height: 200px，是否生效要看CSS是否有效
```
- attr()和removeAttr()方法用于操作DOM节点的属性

- attr()和prop()对于属性checked处理有所不同：

```javascript
var radio = $('#test-radio');
radio.attr('checked'); // 'checked'
radio.prop('checked'); // true
```

- 对于表单元素，jQuery对象统一提供val()方法获取和设置对应的value属性：


---

## 10-7 **修改DOM**

- 添加新的DOM节点，除了通过jQuery的html()这种暴力方法外，还可以用append()方法

- append()把DOM添加到最后，prepend()则把DOM添加到最前。

- 同级节点可以用after()或者before()方法

- 删除DOM节点，拿到jQuery对象后直接调用remove()方法就可以了。如果jQuery对象包含若干DOM节点，实际上可以一次删除多个DOM节点
