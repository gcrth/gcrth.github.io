import time
import os

path_to_blog='_posts/'
time_short=time.strftime("%Y-%m-%d", time.localtime())
time_long=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

blog_name_short='ssh_login_with_sshkeys'
blog_name=time_short+'-'+blog_name_short+'.markdown'

if not os.path.exists(path_to_blog) :
    raise ValueError
if os.path.exists(path_to_blog+blog_name) :
    raise ValueError


file=open(path_to_blog+blog_name,'w')
file.write('''---
layout:     post
title:      "'''+blog_name_short+'''"
subtitle:   ""
date:       '''+time_long+'''
author:     "gcrth"
header-img: "img/post-bg-2015.jpg"
catalog: true
---
''')
