
---

## **Express**

``` javascript
var express = require('express');
var app = express();

app.get('/', function (req, res) {
    res.send('Hello World!');
});

app.listen(3000, function () {
    console.log('Example app listening on port 3000!');
});
```

---

## **koa 1.0**

``` javascript
var koa = require('koa');
var app = koa();

app.use('/test', function *() {
    yield doReadFile1();
    var data = yield doReadFile2();
    this.body = data;
});

app.listen(3000);
```
- 用generator实现异步比回调简单了不少，但是generator的本意并不是异步,为了简化异步代码，ES7（目前是草案，还没有发布）引入了新的关键字async和await

``` javascript
async function () {
    var data = await fs.read('/file1');
}
```

---
## **koa 2.0**

``` javascript 
app.use(async (ctx, next) => {
    await next();
    var data = await doReadFile();
    ctx.response.type = 'text/plain';
    ctx.response.body = data;
});
```