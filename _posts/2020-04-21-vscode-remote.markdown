---
layout:     post
title:      "vscode 远程开发"
subtitle:   "vscode remote"
date:       2020-04-21 16:00:00
author:     "gcrth"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - 配置

---

## 问题  

我们常常会需要使用远程的环境进行开发，但是直接使用ssh连接后用vim的体验对于大部分人来说比较痛苦。vscode现在已经可以实现远程开发所需的大部分功能，但是对于复杂网络环境的配置始终缺少指导。本文将会带你解决最复杂网络环境下的vscode环境配置。

### 适用条件

请一定注意，下面的方案只适用于已经可以通过ssh连接的情况。如果无法连接，由于方案本身也是基于ssh连接的，将无法完成。常见的无法完成的情况为服务器为远程服务器（非局域网中的服务器），且无法获取公网IP。

---

## 解决方法

### 安装所需软件

假如本地为linux，使用openssh即可；如果为Windows，建议使用git bash中的ssh工具。

毫无疑问，我们需要安装vscode，稳定版即可。随后安装微软出的remote-ssh即可。

### 连接配置

微软的插件的思路很好，就是通过ssh建立起连接后，其他的数据都通过这个连接进行传输。而建立起ssh连接的方式是通过配置ssh的配置文件，那么我们下面就来讲解如何正确配置ssh文件。

#### ssh配置文件编写

这里的配置文件通常在`~/.ssh/config`处，Windows的`~`等价为user文件夹下的当前用户文件夹。

找到这个配置文件后我们通过文本编辑器打开。文件的主体结构为应为下面的形式。大写的单词为需要更改的部分。

```bash
Host CONNECT_NAME
  HostName IP_ADDR
  User LOGIN_USR_NAME
```

上面就是一个最简单的示例。但是大部分情况并不会像上面一样可以直接连接服务器，我们会需要通过ssh连接到跳板机后再连接到我们最终的服务器。而这种情况在新版本的ssh中已经充分考虑到了，通过添加`ProxyCommand`即可完成类似的功能。

```bash
Host jump
  HostName IP_ADDR
  User LOGIN_USR_NAME

Host CONNECT_NAME
  HostName IP_ADDR
  User LOGIN_USR_NAME
  ProxyCommand  ssh -q -W %h:%p jump
```

第二个配置项就是我们最终要登陆的服务器，而第一项就是跳板机。`ProxyCommand`的使用类似于递归函数，假如需要再跳一层的话可以配置为下面的形式。

```bash
Host jump_1
  HostName IP_ADDR
  User LOGIN_USR_NAME

Host jump_2
  HostName IP_ADDR
  User LOGIN_USR_NAME
  ProxyCommand  ssh -q -W %h:%p jump_1

Host CONNECT_NAME
  HostName IP_ADDR
  User LOGIN_USR_NAME
  ProxyCommand  ssh -q -W %h:%p jump_2
```

更多层以此类推即可。

这里需要特别注意的是Windows在新版本中带了一个openssh，但是功能并不全，这里推荐使用git bash中的ssh。假如一定要使用原生的，可以使用netcat等插件，具体可以参考<>。

#### vscode配置

linux用户到这里应该就可以用了，而Windows用户为了让vscode插件使用git bash中的ssh还需要多配置一项。具体的配置如下，假如安装时是默认项，那么改动应该与下面的一致。

```txt
"remote.SSH.path": "C:\\Program Files\\Git\\usr\\bin\\ssh.exe"
```

### 多说一句

连接上后vscode会需要在远端配置一些东西，大概需要下载几十兆的文件，可以耐心等待一下。如果中断了（比如你强行退出了），可能需要将vscode-sever的文件夹删除后让vscode重新配置。
