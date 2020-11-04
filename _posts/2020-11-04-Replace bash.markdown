---
layout:     post
title:      "Replace bash"
subtitle:   ""
date:       2020-11-04 18:32:04
author:     "gcrth"
header-img: "img/post-bg-2015.jpg"
catalog: true
---

## Problem

In some situation, we would like to replace the bash with other shell. We would show how to replace the bash with zsh in the following blog.

## Solution

### The normal way

If you are in a normal system, you would be able to use following command to finish replacement.

```bash
chsh -s $(which zsh)
```

### If you have not permittion

It is likely that the command above can not success. You could do the similar thing by add the following content to `.bashrc` file.

```bash
export SHELL=$(which zsh)
[ -z "$ZSH_VERSION" ] && exec "$SHELL" -l
```
