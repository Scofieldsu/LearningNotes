
---
## 12-1 **underscore**

- 正如jQuery统一了不同浏览器之间的DOM操作的差异，让我们可以简单地对DOM进行操作，underscore则提供了一套完善的函数式编程的接口，让我们更方便地在JavaScript中实现函数式编程。

- jQuery在加载时，会把自身绑定到唯一的全局变量$上，underscore与其类似，会把自身绑定到唯一的全局变量_上


- 用underscore实现map()操作如下

    > _.map([1, 2, 3], (x) => x * x); // [1, 4, 9]

- underscore的map()还可以作用于Object

    > _.map({ a: 1, b: 2, c: 3 }, (v, k) => k + '=' + v); // ['a=1', 'b=2', 'c=3']

---

## 12-2 **Collections**

- underscore为集合类对象提供了一致的接口。集合类是指Array和Object，暂不支持Map和Set

### every/some

- 当集合的所有元素都满足条件时，\_.every()函数返回true，当集合的至少一个元素满足条件时，_.some()函数返回true

``` javascript 
// 所有元素都大于0？
_.every([1, 4, 7, -3, -9], (x) => x > 0); // false
// 至少一个元素大于0？
_.some([1, 4, 7, -3, -9], (x) => x > 0); // true
```

### max/min

``` javascript
var arr = [3, 5, 7, 9];
_.max(arr); // 9
_.min(arr); // 3

// 空集合会返回-Infinity和Infinity，所以要先判断集合不为空：
_.max([])
-Infinity
_.min([])
Infinity

// 如果集合是Object，max()和min()只作用于value，忽略掉key
_.max({ a: 1, b: 2, c: 3 }); // 3
```

### groupBy

- 把集合的元素按照key归类，key由传入的函数返回

``` javascript
var scores = [20, 81, 75, 40, 91, 59, 77, 66, 72, 88, 99];
var groups = _.groupBy(scores, function (x) {
    if (x < 60) {
        return 'C';
    } else if (x < 80) {
        return 'B';
    } else {
        return 'A';
    }
});
// 结果:
// {
//   A: [81, 91, 88, 99],
//   B: [75, 77, 66, 72],
//   C: [20, 40, 59]
// }
```

### shuffle / sample

``` javascript
shuffle()用洗牌算法随机打乱一个集合
_.shuffle([1, 2, 3, 4, 5, 6]); // [3, 5, 4, 6, 2, 1]

sample()则是随机选择一个或多个元素：
// 注意每次结果都不一样：
// 随机选1个：
_.sample([1, 2, 3, 4, 5, 6]); // 2
// 随机选3个：
_.sample([1, 2, 3, 4, 5, 6], 3); // [6, 1, 4]
```

---

## 12-3 **Arrays**

- underscore为Array提供了许多工具类方法，可以更方便快捷地操作Array

### first / last

``` javascript
var arr = [2, 4, 6, 8];
_.first(arr); // 2
_.last(arr); // 8
```

### flatten

- flatten()接收一个Array，无论这个Array里面嵌套了多少个Array，flatten()最后都把它们变成一个一维数组

``` javascript
_.flatten([1, [2], [3, [[4], [5]]]]); // [1, 2, 3, 4, 5]

```

### zip / unzip

- zip()把两个或多个数组的所有元素按索引对齐，然后按索引合并成新数组

``` javascript
var names = ['Adam', 'Lisa', 'Bart'];
var scores = [85, 92, 59];
_.zip(names, scores);
// [['Adam', 85], ['Lisa', 92], ['Bart', 59]]

var namesAndScores = [['Adam', 85], ['Lisa', 92], ['Bart', 59]];
_.unzip(namesAndScores);
// [['Adam', 'Lisa', 'Bart'], [85, 92, 59]]
```

### object

``` javascript
var names = ['Adam', 'Lisa', 'Bart'];
var scores = [85, 92, 59];
_.object(names, scores);
// {Adam: 85, Lisa: 92, Bart: 59}
```

### range

``` javascript
// 从0开始小于10:
_.range(10); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

// 从1开始小于11：
_.range(1, 11); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// 从0开始小于30，步长5:
_.range(0, 30, 5); // [0, 5, 10, 15, 20, 25]

// 从0开始大于-10，步长-1:
_.range(0, -10, -1); // [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
```

---

## 12-4 **Functions**

### bind 

``` javascript
var log = _.bind(console.log, console);
log('Hello, world!');
// 输出Hello, world!
```

### partial

``` javascript
var pow2N = _.partial(Math.pow, 2);
pow2N(3); // 8
pow2N(5); // 32
pow2N(10); // 1024

var cube = _.partial(Math.pow, _, 3);
cube(3); // 27
cube(5); // 125
cube(10); // 1000
```

### memoize

- 如果一个函数调用开销很大，我们就可能希望能把结果缓存下来，以便后续调用时直接获得结果

``` javascript
var factorial = _.memoize(function(n) {
    console.log('start calculate ' + n + '!...');
    if (n < 2) {
        return 1;
    }
    return n * factorial(n - 1);
});

factorial(10); // 3628800
// 输出结果说明factorial(1)~factorial(10)都已经缓存了:
// start calculate 10!...
// start calculate 9!...
// start calculate 8!...
// start calculate 7!...
// start calculate 6!...
// start calculate 5!...
// start calculate 4!...
// start calculate 3!...
// start calculate 2!...
// start calculate 1!...

factorial(9); // 362880
// console无输出
```

### once

- once()保证某个函数执行且仅执行一次。如果你有一个方法叫register()，用户在页面上点两个按钮的任何一个都可以执行的话，就可以用once()保证函数仅调用一次，无论用户点击多少次

### delay

``` javascript
var log = _.bind(console.log, console);
_.delay(log, 2000, 'Hello,', 'world!');
// 2秒后打印'Hello, world!':
```

---

## 12-5 **objects**

### keys/allKeys

- keys()可以非常方便地返回一个object自身所有的key,allKeys()除了object自身的key，还包含从原型链继承下来的

### values

- 返回object自身但不包含原型链继承的所有值

- 没有allValues()

### mapObject

``` javascript
var obj = { a: 1, b: 2, c: 3 };
// 注意传入的函数签名，value在前，key在后:
_.mapObject(obj, (v, k) => 100 + v); // { a: 101, b: 102, c: 103 }
```

### invert

- 把object的每个key-value来个交换，key变成value，value变成key

### extend / extendOwn

- extend()把多个object的key-value合并到第一个object并返回

- 注意：如果有相同的key，后面的object的value将覆盖前面的object的value。

- extendOwn()和extend()类似，但获取属性时忽略从原型链继承下来的属性。


### clone

- clone()是“浅复制”。所谓“浅复制”就是说，两个对象相同的key所引用的value其实是同一对象

### isEqual

- isEqual()对两个object进行深度比较，如果内容完全相同，则返回true

``` javascript

var o1 = { name: 'Bob', skills: { Java: 90, JavaScript: 99 }};
var o2 = { name: 'Bob', skills: { JavaScript: 99, Java: 90 }};

o1 === o2; // false
_.isEqual(o1, o2); // true
```

---

## 12-6 **Chaining**

- underscore提供了把对象包装成能进行链式调用的方法，就是chain()函数：

``` javascript
_.chain([1, 4, 9, 16, 25])
 .map(Math.sqrt)
 .filter(x => x % 2 === 1)
 .value();
// [1, 3, 5]
```