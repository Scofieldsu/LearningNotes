
---

## **高阶函数**

- 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数.

---

## **map**


- 调用Array的map()方法，传入我们自己的函数，就得到了一个新的Array作为结果.

``` javascript
function pow(x) {
    return x * x;
}

var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
arr.map(pow); // [1, 4, 9, 16, 25, 36, 49, 64, 81]
```

---

## **reduce**

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

## **filter**


