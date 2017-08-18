
---

## **高阶函数**

- 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数.

---

## 5-1 **map**


- 调用Array的map()方法，传入我们自己的函数，就得到了一个新的Array作为结果.

``` javascript
function pow(x) {
    return x * x;
}

var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
arr.map(pow); // [1, 4, 9, 16, 25, 36, 49, 64, 81]
```

---

## 5-2 **reduce**

- Array的reduce()把一个函数作用在这个Array的[x1, x2, x3...]上，这个函数必须接收两个参数，reduce()把结果继续和序列的下一个元素做累积计算.

``` javascript
var sum = function(x, y) {
    return x + y
}
var arr = [1, 3, 5, 7, 9];
arr.reduce(sum); // 25
```

> *练习*：不要使用JavaScript内置的parseInt()函数，利用map和reduce操作实现一个string2int()函数

- 把一个字符串13579先变成Array——[1, 3, 5, 7, 9]，再利用reduce()就可以写出一个把字符串转换为Number的函数.

``` javascript 
function string2int(s) {
  return s.split('').map(function(x){return x-'0'}).reduce(function(x,y){return x*10+y});
}

string2int('13579') // 13579
```

---

## 5-3 **filter**

- filter()把传入的函数依次作用于每个元素，然后根据返回值是true还是false决定保留还是丢弃该元素

``` javascript 
var arr = ['A', '', 'B', null, undefined, 'C', '  '];
var r = arr.filter(function (s) {
    return s && s.trim(); // 注意：IE9以下的版本没有trim()方法
});
r; // ['A', 'B', 'C']
```

- 回调函数

``` javascript 
var arr = ['apple', 'strawberry', 'banana', 'pear', 'apple', 'orange', 'orange', 'strawberry'];

arr.filter(function (element, index, self) {
    return self.indexOf(element) === index;
}); 

// ['apple','strawberry','banana','pear','orange']

```

---

## 5-4 **sort**

- Array的sort()方法默认把所有元素先转换为String再排序.

- sort()方法会直接对Array进行修改，它返回的结果仍是当前Array

---

## 5-5 **闭包（closure）**

- 概念：定义在一个函数内部的函数；能够读取函数内部变量的函数。

- 用途：读取函数内部的变量；让这些变量的值始终保持在内存中。

- 使用注意：

    - 闭包会使得函数中的变量都被保存在内存中，造成网页性能问题，解决办法是退出函数之前，将不使用的局部变量全部删除；

    -  闭包会在父函数外部改变父函数内部变量的值，所以，如果把父函数当做对象使用，闭包当做它的公用方法，内部变量当做私有属性，一定小心不要随便改变父函数内部变量的值。


``` javascript

　　var name = "The Window";
　　var object = {
　　　　name : "My Object",
　　　　getNameFunc : function(){
　　　　　　return function(){
　　　　　　　　return this.name;
　　　　　　};
　　　　}
　　};
　　alert(object.getNameFunc()()); //The Window

var name = "The Window";
　　var object = {
　　　　name : "My Object",
　　　　getNameFunc : function(){
　　　　　　var that = this;
　　　　　　return function(){
　　　　　　　　return that.name;
　　　　　　};
　　　　}
　　};
　　alert(object.getNameFunc()()); // My Object

```

## 5-6 **箭头函数（Arrow Function，ES6新增）**

- 例如 ：x => x*x

``` javascript
// 两个参数:
(x, y) => x * x + y * y

// 无参数:
() => 3.14

// 可变参数:
(x, y, ...rest) => {
    var i, sum = x + y;
    for (i=0; i<rest.length; i++) {
        sum += rest[i];
    }
    return sum;
}

```
- 箭头函数内部的this是词法作用域，由上下文确定。

## 5-7 **生成器（generator，ES6新增）**

