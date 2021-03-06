
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

- JavaScript的原型继承实现方式就是：

    - 定义新的构造函数，并在内部用call()调用希望“继承”的构造函数，并绑定this；

    - 借助中间函数F实现原型链继承，最好通过封装的inherits函数完成；

    - 继续在新的构造函数的原型上定义新方法

    ``` javascript 
    function inherits(Child, Parent) {
    var F = function () {};
    F.prototype = Parent.prototype;
    Child.prototype = new F();
    Child.prototype.constructor = Child;
    }

    function Student(props) {
    this.name = props.name || 'Unnamed';
    }

    Student.prototype.hello = function () {
    alert('Hello, ' + this.name + '!');
    }

    function PrimaryStudent(props) {
    Student.call(this, props);
    this.grade = props.grade || 1;
    }

    // 实现原型继承链:
    inherits(PrimaryStudent, Student);

    // 绑定其他方法到PrimaryStudent原型:
    PrimaryStudent.prototype.getGrade = function () {
    return this.grade;
    };
    ```

---

## 7-4 **class继承（ES6新增）**

``` javascript 
class Student {
    constructor(name) {
        this.name = name;
    }

    hello() {
        alert('Hello, ' + this.name + '!');
    }
}


class PrimaryStudent extends Student {
    constructor(name, grade) {
        super(name); // 记得用super调用父类的构造方法!
        this.grade = grade;
    }

    myGrade() {
        alert('I am at grade ' + this.grade);
    }
}
```

- 不是所有的主流浏览器都支持ES6的class。如果一定要现在就用上，就需要一个工具把class代码转换为传统的prototype代码，可以试试Babel这个工具。

