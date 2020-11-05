---
layout:     post
title:      "Question about R"
subtitle:   ""
date:       2020-10-16 12:07:38
author:     "gcrth"
header-img: "img/post-bg-2015.jpg"
catalog: true
---

## Four Different Way to Get The Type

I found there are four differnt ways to get the type of an object, and combined them into a function as follow.

```R
get_type <- function(obj) {
  cat('class: ', class(obj), '\n')
  cat('typeof: ', typeof(obj), '\n')
  cat('mode: ', mode(obj), '\n')
  cat('storage.mode: ', storage.mode(obj), '\n')
}
```

### Question

I wonder what it is the difference between all these four different way. I could not get much information from the document.

### Answer

The type system in R is not good designed, and the diffference between these is not that clear. Generally the class is a tag given by the user, and mode is how the system treat this data.

## Class of Vector

The class of vector, ie `class(1:6)`, behaves a little different from the class of other objects including matrix, array, list, data.frame. The class of vector would be the type of the element inside, but the class of other compound objects (container) would be the type of the container. We could found this with the following code.

```R
a = 1:6
get_type(a)

dim(a)=6
get_type(a)

dim(a)=c(2,3)
get_type(a)

dim(a)=c(1,2,3)
get_type(a)

a = list(a = 1, b = 2)
get_type(a)

nms <- c("joe", "fred", "harry")
a <- c(24, 19, 30)
ht <- c(1.7, 1.8, 1.75)
s <- c(TRUE, FALSE, TRUE)


d <- data.frame(
  name = nms,
  age = a,
  height = ht,
  student = s
)

get_type(d)
```

Result

```R
> a = 1:6
> get_type(a)
class:  integer 
typeof:  integer 
mode:  numeric 
storage.mode:  integer 
> 
> dim(a)=6
> get_type(a)
class:  array 
typeof:  integer 
mode:  numeric 
storage.mode:  integer 
> 
> dim(a)=c(2,3)
> get_type(a)
class:  matrix array 
typeof:  integer 
mode:  numeric 
storage.mode:  integer 
> 
> dim(a)=c(1,2,3)
> get_type(a)
class:  array 
typeof:  integer 
mode:  numeric 
storage.mode:  integer 
> 
> a = list(a = 1, b = 2)
> get_type(a)
class:  list 
typeof:  list 
mode:  list 
storage.mode:  list 
> 
> nms <- c("joe", "fred", "harry")
> a <- c(24, 19, 30)
> ht <- c(1.7, 1.8, 1.75)
> s <- c(TRUE, FALSE, TRUE)
> 
> 
> d <- data.frame(
+   name = nms,
+   age = a,
+   height = ht,
+   student = s
+ )
> 
> get_type(d)
class:  data.frame 
typeof:  list 
mode:  list 
storage.mode:  list 
```

### Question

I wonder why the vector behaves so differently, and is there a way to identity a vector without using `is.vector()`?

### Answer

It is because it is not well designed. `is.vector()` is the only way to do so.

## Why a list is a vector

If you test whether a list is a vector with following code, you would find something suprising.

```R
a = list(a = 1, b = 2)
is.list(a)
is.vector(a)
```

Result

```R
> a = list(a = 1, b = 2)
> is.list(a)
[1] TRUE
> is.vector(a)
[1] TRUE
```

### Question

Why is a list also a vector?

### Answer

Unclear yet.

### Build a Vector and Get a List

I could use the follwing code to build a vector `b`, and what I got is a list.

```R
a = list(a = 1, b = 2)
b = vector(mode = 'list', 3)
b[1]=a # abnormal
b[[1]] = a
print(b)

is.list(b)
is.vector(b)

get_type(b)
```

Result

```R
> a = list(a = 1, b = 2)
> b = vector(mode = 'list', 3)
> b[1]=a # abnormal
Warning message:
In b[1] = a : 被替换的项目不是替换值长度的倍数
> b[[1]] = a
> print(b)
[[1]]
[[1]]$a
[1] 1

[[1]]$b
[1] 2


[[2]]
NULL

[[3]]
NULL

> 
> is.list(b)
[1] TRUE
> is.vector(b)
[1] TRUE
> 
> get_type(b)
class:  list 
typeof:  list 
mode:  list 
storage.mode:  list 
```

### Question

The object `b` I built work entirely as a list not a vector, but I built it with a `vector()` method. I am confusing why this would happened and what structure of `b` is.

### Answer

Function `vector` could be used to create a list in this situation, and other mode options work just normally.

## Understanding of the class in R

I found that the class in R is different from the class in Java. 

The class in R seems to have no method included in it and just have some data fields inside (I am not sure). Could I difine a class like what I do in Java?

Moreover, the main purpose of using class in R seems to be matching the generic function instead of OOD, isn't it?

### Answer

The basic class in R is very weak and can not include any method in its class. Use s4 or r6 could extend the system.

<https://adv-r.hadley.nz/s4.html><https://adv-r.hadley.nz/r6.html>

## About the graphics

Some function would create a figure (plot, curve, symbols), but other would need to be added to an existed figure (points lines).

Could I use the function that would create a figure to change a existing figure by some way?

What is the most elegant way to create a bank canvas? I use the following function.

```R
plot(c(0, 1),
     c(0, 1),
     type = "n",
     xlab = "",
     ylab = "",
     bty='n',
     axes = F)
```

The figure saved in pdf format would have a better quality when zooming, but how can I embed it into another document?

How could I reset all the par settings? I do this by restarting the current session.

### Answer

There is no way to change the bahavior of these function.

That is the best way to create the canvas.

Latex code `\includegraphics` could include pdfs as figures.

`op <- par()` could save the original par setting and could use `par(op)` to recover it.

`asp` is a good option to control the picture x/y percentage.

## Can I use the code in the hint directly?

## About the unpack

Some function would need to have a parameter list, such as (paste). It could not deal with vector correctly, so we need to unpack the vector.

```R
paste(c('a','b'))
```

In python, we could do the following things.

```python
a=[1,2,3]
some_function_need_parameter_list(*a)
```

Could I do similiar things in R?

### Answer

`do.call("paste", list("a", "b"))` could work around.

## How could I index the string?

If I want to get the i element, I could not do `some_sting[n]`. I could only use `substr` to do so.

No. `substr` is the best way.

## Could I index the element from reverse way

I could do this by `some_list[-i]` in python.

No.

## Why I could not use as.vector to turn a list to a vector?

I need to use unlist to do so.

No. Poor design.

## Could I have a vector with multiple vector inside?

I did not find a way to do so.

No.

## Best Practice of Changing string in data.frame to factor

If I got a data.frame from the function I could not change, in which the string is actually string not factor, I could not change these string to factor directly by using `d = data.frame(d, stringsAsFactors = TRUE)` again. What I could do is to change it to a list and change it back again with `d = data.frame(d, stringsAsFactors = TRUE)`. However, this is obvious not the best practice.

```R
nms <- c("joe", "fred", "harry")
a <- c(24, 19, 30)
ht <- c(1.7, 1.8, 1.75)
s <- c(TRUE, FALSE, TRUE)


d <- data.frame(
  name = nms,
  age = a,
  height = ht,
  student = s
)

get_type(d)

d = as.list(d)
d = data.frame(d, stringsAsFactors = TRUE)
d[[1]]
# work

d[[1]] = nms
d = data.frame(d, stringsAsFactors = TRUE)
d[[1]]
# not work best practice?
```

Result

```R
> nms <- c("joe", "fred", "harry")
> a <- c(24, 19, 30)
> ht <- c(1.7, 1.8, 1.75)
> s <- c(TRUE, FALSE, TRUE)
> 
> 
> d <- data.frame(
+   name = nms,
+   age = a,
+   height = ht,
+   student = s
+ )
> 
> get_type(d)
class:  data.frame 
typeof:  list 
mode:  list 
storage.mode:  list 
> 
> d = as.list(d)
> d = data.frame(d, stringsAsFactors = TRUE)
> d[[1]]
[1] joe   fred  harry
Levels: fred harry joe
> # work
> 
> d[[1]] = nms
> d = data.frame(d, stringsAsFactors = TRUE)
> d[[1]]
[1] "joe"   "fred"  "harry"
> # not work best practice?
```

No better way.

### Question

Is there a better way to do this?

## Is there reference or pointer in R?

## What is x in the following code.

```R
curve(x^2)
```

It is an expression. The `x` in that expression has special meaning.

## Tips

* If you expect the result in the `heatmap` to be shown symmetrically, you need to care about the `symm` option.
