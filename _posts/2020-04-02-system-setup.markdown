---
layout:     post
title:      "新装系统配置"
subtitle:   ""
date:       2020-04-02 16:00:00
author:     "gcrth"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - 配置

---

## 问题  

新安装的系统在可以运行实验前都需要配置环境，本文将以ubuntu和manjaro在中国境内的配置方法为例进行配置。本人使用的是pytorch框架，所以这里除了共同部分还提供了pytorch的配置，tensorflow日后有时间会补上。

---

## 解决方法

### ubuntu

本文中采用的版本为18.04.4，其他的版本大同小异。

#### 显示问题

首先ubuntu对于nVidia显卡的支持需要依靠闭源的驱动，而开源的驱动稳定性差，很有可能没有正确显示。我们可以通过以下方式进行暂时的修复。

首先我们要通过U盘启动，在选择界面不要直接选择install选项，而是按e进入启动项的编辑界面。找到`quite splash`字样，假如有`---`，将其删除然后加上`nomodeset`。改完后按F10开机。

在正确安装系统后，我们重启进入正式的系统，但是不要直接进系统，可能无法正常显示。我们需要在开机界面按shift进入选择界面，然后按照上面的流程编辑启动项。

在开机后安装闭源驱动应该可解决显示问题。假如无法解决可以编辑`/etc/default/grub`，加上`nomodeset`解决显示问题，但是想要正确使用cuda必须安装闭源驱动。

#### 换源

由于在中国境内的网络问题，在安装软件前需要配置镜像。这里推荐一个好用的[脚本](https://github.com/tuna/oh-my-tuna)，是清华源推出用来一键配置清华源的。使用的时候可以使用以下命令。

```bash
wget https://tuna.moe/oh-my-tuna/oh-my-tuna.py
python oh-my-tuna.py
```

如此以来就可以一键配置多个镜像。

如果希望手工配置可以参考<https://mirrors.tuna.tsinghua.edu.cn/help/AOSP/>，页面中给出了镜像官方的配置建议。

#### 安装驱动

在换好源后，我们可以开始配置驱动，主要是nVidia显卡驱动。ubuntu桌面版本给出了图像化的选择界面，位于软件更新器的设置中，选项卡名为附加驱动。这里推荐使用带有tested字样的版本。

如果需要通过命令行安装可以参考<https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-18-04-bionic-beaver-linux>，但是最推荐通过上面的方式安装不容易出错。

### manjaro

这里使用的是kde版本，版本号为19.0.2。其他版本应该差不多。

#### 安装

安装没有太多的问题，只需要在安装时的驱动选项改为nofree即可。不出意外的话，nVidia的驱动也会自动安装上。

#### 配置源

这里的使用脚本配置源大部分和ubuntu类似，这里讲一下手动配置的方法。

```bash
sudo pacman-mirrors -i -c China -m rank
sudo pacman -Syyu
```

通过编辑`/etc/pacman.conf`配置ArchlinuxCN，在文件尾添加以下内容

```txt
[archlinuxcn]
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
```

然后执行更新。

```bash
sudo pacman -Syy && sudo pacman -S archlinuxcn-keyring
```

### 输入法

```bash
sudo pacman -S fcitx-sogoupinyin
sudo pacman -S fcitx-im # 全部安装
sudo pacman -S fcitx-configtool # 图形化配置工具
```

编辑`~/.xprofile`，添加

```txt
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
```

### 通用

#### python环境配置

下面使用conda进行环境的配置，这里推荐每个项目都根据需要分开配置环境。

conda下载可以使用下面的命令。这里需要注意版本。

```bash
weget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

然后，执行脚本即可。

```bash
sh Miniconda3-latest-Linux-x86_64.sh
```

这里根据提示执行即可，大部分使用默认即可。但是最后一项推荐使用yes，让脚本帮助配置bashrc，相对更加方便。

安装后需要配置镜像，参考换源章节即可。

使用下面的命令建立并进入环境。

```bash
conda update -n base conda                   //update最新版本的conda
conda create -n ENV_NAME python=VERSION_NO   //创建python3.5的xxxx虚拟环境
conda activate ENV_NAME                      //开启xxxx环境
conda deactivate                             //关闭环境
conda env list                               //显示所有的虚拟环境
```

#### 安装pytorch

在建立的环境中使用以下命令安装pytorch，这也是官方推荐的方式。

```bash
conda install pytorch torchvision cudatoolkit=10.1 -c pytorch
```

其他的版本和选项（比如cpu版），可以参考<https://pytorch.org/>中的quick start。

假如是安装推荐方法配置的镜像，`-c`参数不需要去掉，但是假如直接将路径配到`default_channels`中，就需要去掉。

确认安装前可以确认一下版本，假如是上面的命令，版本中应该有cu_101字样。

##### cuda

通过上面的方法可以直接安装cuda，这里的cuda是基于驱动的，安装新版的cuda需要新的驱动。

假如需要编写cuda的程序，可以通过下面的命令安装额外的包。具体可以参考<https://anaconda.org/conda-forge/cudatoolkit-dev>。

```bash
conda install -c conda-forge cudatoolkit-dev
```

#### 其他

然后根据不同的项目安装其他的软件，很多提供写好的requirement，可以使用下面的命令安装。

```bash
pip install -r requirement.txt
```

#### zsh

安装zsh很简单，但是安装好假如自行配置会比较麻烦，可以使用oh-my-zsh来简化这一流程。

安装的命令。

```bash
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

大部分情况使用默认即可，更详细的配置可以查阅<https://github.com/ohmyzsh/ohmyzsh>。

#### ssh

#### 安装配置

ubuntu需要安装，而manjaro不需要。

ubuntu安装命令。

```bash
sudo apt-get install openssh-server
```

通过下面的命令开启sshd

```bash
systemctl enable sshd.service  #开机启动
systemctl start sshd.service   #立即启动
systemctl restart sshd.service #立即重启
```

##### 密钥登陆

生成密钥，使用默认参数即可。
```bash
ssh-keygen
```

复制公钥到服务器上。
```bash
ssh-copy-id -i .ssh/id_rsa.pub  USR_NAME@SERVER_IP
```

>未完待续
