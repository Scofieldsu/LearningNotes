## 3-1 **条件判断**
---

- JavaScript使用if () { ... } else { ... }来进行条件判断

- JavaScript把null、undefined、0、NaN和空字符串''视为false


---
## 3-2 **循环**

- JavaScript的循环有两种，一种是for循环，通过初始条件、结束条件和递增条件来循环执行语句块： for (i=1;i<=100,i++) {}

- for循环的3个条件都是可以省略的，如果没有退出循环的判断条件，就必须使用break语句退出循环，否则就是死循环. for(;;) { ... break}

- for循环的一个变体是for ... in循环，它可以把一个对象的所有属性依次循环出来. 注意：for ... in循环可以直接循环出Array的索引;得到的是String而不是Number. 

- var a =['a','b']; for (var i in a) { alert (i)}  // '0','1'

- while循环只有一个判断条件，条件满足，就不断循环，条件不满足时则退出循环.

- do { ... } while()循环

---
## 3-3 **Map**

- JavaScript的对象有个小问题，就是键必须是字符串

- 初始化Map需要一个二维数组，或者直接初始化一个空Map

- var m = new Map([['Michael', 95], ['Bob', 75], ['Tracy', 85]]);

- m.get() ; m.set() ; m.delete()

---
## 3-4 **Set**

- Set是一组key的集合，但不存储value。由于key不能重复，所以，在Set中，没有重复的key。

- 要创建一个Set，需要提供一个Array作为输入，或者直接创建一个空Set

- var s = new Set ( [ 1, 2, 3, 3, '3' ] );
   
   - s ; // Set {1, 2, 3, "3"}

- s.add(); s.delete()

---

## 3-5 **iterable**

- 遍历Array可以采用下标循环，遍历Map和Set就无法使用下标。

- ES6标准引入了新的iterable类型，Array、Map和Set都属于iterable类型

- 具有iterable类型的集合可以通过新的for ... of循环来遍历

- for ... in循环将把name包括在内，但Array的length属性却不包括在内。

- for ... of循环则完全修复了这些问题，它只循环集合本身的元素：

- 例如：

    -  var a = ['a','b','c']; a.name = 'hello'

            - for (var i in a) {
                alert(i) // '0','1','2','name'}

            - for (var i of a) {
                alert(i) // 'a','b','c'}

