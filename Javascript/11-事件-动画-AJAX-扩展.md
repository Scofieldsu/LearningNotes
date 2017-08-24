
---

## 11-1 **事件**

jQuery能够绑定的事件主要包括：

- 鼠标事件

    - click: 鼠标单击时触发；
    - dblclick：鼠标双击时触发；
    - mouseenter：鼠标进入时触发；
    - mouseleave：鼠标移出时触发；
    - mousemove：鼠标在DOM内部移动时触发；
    - hover：鼠标进入和退出时触发两个函数，相当于mouseenter加上mouseleave。

- 键盘事件

键盘事件仅作用在当前焦点的DOM上，通常是\<input>和\<textarea>。

    - keydown：键盘按下时触发；
    - keyup：键盘松开时触发；
    - keypress：按一次键后触发。

- 其他事件

    - focus：当DOM获得焦点时触发；
    - blur：当DOM失去焦点时触发；
    - change：当\<input>、\<select>或\<textarea>的内容改变时触发；
    - submit：当\<form>提交时触发；
    - ready：当页面被载入并且DOM树完成初始化后触发。
    > 其中，ready仅作用于document对象。
    - 如果你遇到$(function () {...})的形式，牢记这是document对象的ready事件处理函数

---

## 11-2 **动画**

``` javascript 
var div = $('#test-show-hide');
div.hide(3000); // 在3秒钟内逐渐消失

div.show('slow'); // 在0.6秒钟内逐渐显示

toggle()方法则根据当前状态决定是show()还是hide()

div.slideUp(3000); // 在3秒钟内逐渐向上消失
slideDown()相反，而slideToggle()则根据元素是否可见来决定下一步动作

fadeIn()和fadeOut()的动画效果是淡入淡出，也就是通过不断设置DOM元素的opacity属性来实现，而fadeToggle()则根据元素是否可见来决定下一步动作

animate()，它可以实现任意动画效果，我们需要传入的参数就是DOM元素最终的CSS状态和时间，jQuery在时间段内不断调整CSS直到达到我们设定的值

var div = $('#test-animate');
div.animate({
    opacity: 0.25,
    width: '256px',
    height: '256px'
}, 3000, function () {
    console.log('动画已结束');
    // 恢复至初始状态:
    $(this).css('opacity', '1.0').css('width', '128px').css('height', '128px');
});

```

- jQuery的动画效果还可以串行执行，通过delay()方法还可以实现暂停

- jQuery也没有实现对background-color的动画效果，用animate()设置background-color也没有效果。这种情况下可以使用CSS3的transition实现动画效果

---

## 11-3 **AJAX**

ajax

jQuery在全局对象jQuery（也就是$）绑定了ajax()函数，可以处理AJAX请求。ajax(url, settings)函数需要接收一个URL和一个可选的settings对象，常用的选项如下：

- async：是否异步执行AJAX请求，默认为true，千万不要指定为false；

- method：发送的Method，缺省为'GET'，可指定为'POST'、'PUT'等；

- contentType：发送POST请求的格式，默认值为'application/x-www-form-urlencoded; charset=UTF-8'，也可以指定为text/plain、application/json；

- data：发送的数据，可以是字符串、数组或object。如果是GET请求，data将被转换成query附加到URL上，如果是POST请求，根据contentType把data序列化成合适的格式；

- headers：发送的额外的HTTP头，必须是一个object；

- dataType：接收的数据格式，可以指定为'html'、'xml'、'json'、'text'等，缺省情况下根据响应的Content-Type猜测。

``` javascript
// jQuery的jqXHR对象类似一个Promise对象，我们可以用链式写法来处理各种回调

var jqxhr = $.ajax('/api/categories', {
    dataType: 'json'
}).done(function (data) {
    ajaxLog('成功, 收到的数据: ' + JSON.stringify(data));
}).fail(function (xhr, status) {
    ajaxLog('失败: ' + xhr.status + ', 原因: ' + status);
}).always(function () {
    ajaxLog('请求完成: 无论成功或失败都会调用');
});

```

### get

``` javascript
var jqxhr = $.get('/path/to/resource', {
    name: 'Bob Lee',
    check: 1
});

//第二个参数如果是object，jQuery自动把它变成query string然后加到URL后面，实际的URL是：
/path/to/resource?name=Bob%20Lee&check=1
```

### post

``` javascript
// 传入的第二个参数默认被序列化为application/x-www-form-urlencoded

var jqxhr = $.post('/path/to/resource', {
    name: 'Bob Lee',
    check: 1
});
```

### getJSON

``` javascript
var jqxhr = $.getJSON('/path/to/resource', {
    name: 'Bob Lee',
    check: 1
}).done(function (data) {
    // data已经被解析为JSON对象了
});
```

---

## 11-4 **扩展**


编写一个jQuery插件的原则：

- 给$.fn绑定函数，实现插件的代码逻辑；
- 插件函数最后要return this;以支持链式调用；
- 插件函数要有默认值，绑定在$.fn.<pluginName>.defaults上；
- 用户在调用时可传入设定值以便覆盖默认值。

``` javascript
$.fn.highlight1 = function () {
    // this已绑定为当前jQuery对象:
    this.css('backgroundColor', '#fffceb').css('color', '#d85030');
    return this;
}

$.fn.highlight2 = function (options) {
    // 要考虑到各种情况:
    // options为undefined
    // options只有部分key
    var bgcolor = options && options.backgroundColor || '#fffceb';
    var color = options && options.color || '#d85030';
    this.css('backgroundColor', bgcolor).css('color', color);
    return this;
}

// 最终版

$.fn.highlight = function (options) {
    // 合并默认值和用户设定值:
    var opts = $.extend({}, $.fn.highlight.defaults, options);
    this.css('backgroundColor', opts.backgroundColor).css('color', opts.color);
    return this;
}

// 设定默认值:
$.fn.highlight.defaults = {
    color: '#d85030',
    backgroundColor: '#fff8de'
}
```

``` javascript
$.fn.external = function () {
    // return返回的each()返回结果，支持链式调用:
    return this.filter('a').each(function () {
        // 注意: each()内部的回调函数的this绑定为DOM本身!
        var a = $(this);
        var url = a.attr('href');
        if (url && (url.indexOf('http://')===0 || url.indexOf('https://')===0)) {
            a.attr('href', '#0')
             .removeAttr('target')
             .append(' <i class="uk-icon-external-link"></i>')
             .click(function () {
                if(confirm('你确定要前往' + url + '？')) {
                    window.open(url);
                }
            });
        }
    });
}

<!-- HTML结构 -->
<div id="test-external">
    <p>如何学习<a href="http://jquery.com">jQuery</a>？</p>
    <p>首先，你要学习<a href="/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000">JavaScript</a>，并了解基本的<a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML</a>。</p>
</div>

$('#test-external a').external();
```

---
## 11-5 **错误处理**

- try {
    ...
} catch (e) {
    ...
} finally {
    ...
}
