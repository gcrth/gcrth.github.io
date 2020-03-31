---
layout:     post
title:      "gitignore不生效"
subtitle:   ""
date:       2020-03-31 16:00:00
author:     "gcrth"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - git
    # - Meta
---

## 问题  

在git已经将部分文件纳入到版本管理中后，有时会更新.gitignore文件希望把这部分文件排除出去，但是提交后这部分文件依然在git记录中。

---

## 解决方法

上面gitignore似乎没有生效的原因是我们没有清理git的缓存，我们可以通过下面的命令清理缓存，然后正常提价即可。

```bash
git rm -r --cached .
```

假如还不行，请检查gitignore的语法，可以借助vscode等工具。
