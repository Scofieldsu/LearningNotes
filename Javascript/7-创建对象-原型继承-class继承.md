
---

## 7-1 **面向对象**

- JavaScript通过原型（prototype）来实现面向对象编程

    ``` javascript
    var Student = {
    name: 'Robot',
    height: 1.2,
    run: function () {
        console.log(this.name + ' is running...');
       }
    };

    var xiaoming = {
        name: '小明'
    };

    xiaoming.__proto__ = Student;

    xiaoming.name; // '小明'
    xiaoming.run(); // 小明 is running...
    ```

    - 使用Object.crteate() 可以传入一个原型对象，并创建基于该原型的新对象

    ``` javascript
    // 原型对象:
    var Student = {
    name: 'Robot',
    height: 1.2,
    run: function () {
        console.log(this.name + ' is running...');
       }
    };

    function createStudent(name) {
    // 基于Student原型创建一个新对象:
    var s = Object.create(Student);
    // 初始化新对象:
    s.name = name;
    return s;
    }

    var xiaoming = createStudent('小明');
    xiaoming.run(); // 小明 is running...
    xiaoming.__proto__ === Student; // true
    ```

---

## 7-2 **创建对象**

- JavaScript对每个创建的对象都会设置一个原型，指向它的原型对象

- 数组的原型链：arr ----> Array.prototype ----> Object.prototype ----> null

- 函数的原型链： foo ----> Function.prototype ----> Object.prototype ----> null

- 构造函数

    ``` javascript 
    function Student(name) {
        this.name = name;
        this.hello = function () {
            alert('Hello, ' + this.name + '!');
        }
    }

    var xiaoming = new Student('小明');
    xiaoming.name; // '小明'
    xiaoming.hello(); // Hello, 小明!

    ```
    - 用new Student()创建的对象还从原型上获得了一个constructor属性，它指向函数Student本身


--- 

## 7-3 **原型继承**

