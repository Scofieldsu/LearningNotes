
---
Json web token (JWT)是一种用于双方之间传递安全信息的简洁的、URL安全的表述性声明规范。JWT作为一个开放的标准（RFC 7519），定义了一种简洁的，自包含的方法用于通信双方之间以Json对象的形式安全的传递信息。因为数字签名的存在，这些信息是可信的，JWT可以使用HMAC算法或者是RSA的公私秘钥对进行签名。

---

jwt包含了使用.分隔的三部分：

- Header     头部

- Playload   负载

- Signature  签名

``` python

Header

在header中通常包含了两部分：token类型和采用的加密算法。

{
  "alg": "HS256",
  "typ": "JWT"
}  
接下来对这部分内容使用 Base64Url 编码组成了JWT结构的第一部分。


Payload

Token的第二部分是负载，它包含了claim， Claim是一些实体（通常指的用户）的状态和额外的元数据，有三种类型的claim： reserved, public 和 private.

Reserved claims: 这些claim是JWT预先定义的，在JWT中并不会强制使用它们，而是推荐使用，常用的有 iss（签发者）, exp（过期时间戳）, sub（面向的用户）, aud（接收方）, iat（签发时间）。
Public claims：根据需要定义自己的字段，注意应该避免冲突
Private claims：这些是自定义的字段，可以用来在双方之间交换信息
负载使用的例子：

{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}
上述的负载需要经过Base64Url编码后作为JWT结构的第二部分。


Signature

创建签名需要使用编码后的header和payload以及一个秘钥，使用header中指定签名算法进行签名。例如如果希望使用HMAC SHA256算法，那么签名应该使用下列方式创建：

HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)  
签名用于验证消息的发送者以及消息是没有经过篡改的。


完整的JWT

JWT格式的输出是以.分隔的三段Base64编码，与SAML等基于XML的标准相比，JWT在HTTP和HTML环境中更容易传递。

```
