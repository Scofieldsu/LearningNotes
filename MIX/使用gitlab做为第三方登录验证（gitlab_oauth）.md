GitLab as an OAuth2 provider(第三方应用集成gitlab登录)
---------------------------------------------

- **在gitlab个人资料设置-应用，增加新的应用，即可生成application ID 和secret**

 ![新增应用](images/gitlab_oauth/0_1.png)

 ![ID和密钥](images/gitlab_oauth/0_2.png)

## 授权码模式获取access_token

- **GET请求: gitlab地址/oauth/authorize ,参数如下图：**

![get请求参数](images/gitlab_oauth/1.png)

- **登录gitlab后，需要确认认证**

![确认认证](images/gitlab_oauth/2.png)

- **确认认证后，gitlab会生成code作为参数，回调到redirect_uri**

![回调](images/gitlab_oauth/3.png)

- **根据code再去请求获取acces_token**

![获取access_token](images/gitlab_oauth/4.png)

---

##  密码模式获取access_token

![密码模式获取access_token](images/gitlab_oauth/6.png)

---

## 得到access_token后请求gitlab api获取相关信息

- **例：获取当前用户信息**

![获取当前用户信息](images/gitlab_oauth/5.png)


