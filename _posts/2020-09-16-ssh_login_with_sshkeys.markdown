---
layout:     post
title:      "ssh免密登录"
subtitle:   ""
date:       2020-09-16 02:39:43
author:     "gcrth"
header-img: "img/post-bg-2015.jpg"
catalog: true
tag:
    - ssh
---

## 问题

使用公私钥对登录远程的机器，相对于使用密码登录来说，是一种比较安全的方式。为了较高的安全性可以在配置完下面免密登录后关闭密码登录。

## 解决办法

可以使用下面的命令生成公私钥对。使用默认设置即可。生成的密钥位于`~/.ssh`中。Windows的电脑可以使用git bash完成这一步。

```bash
ssh-keygen
```

可以使用下面的命令将公钥传到服务器端。

```bash
ssh-copy-id USR_NAME@SERVER_IP
```

也可以将公钥的内容传到服务器中。公钥文件为`~/.ssh/id_rsa.pub`，粘贴的目标文件为`~/.ssh/authorized_keys`。假如服务器已经存有其他公钥，将新的公钥存到后面即可。

更加复杂的情况可以参考<https://blog.tjll.net/ssh-kung-fu/#public-key-cryptography>。
