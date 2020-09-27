---
layout:     post
title:      "Analyzing Learned Molecular Representations for Property Prediction"
subtitle:   ""
date:       2020-09-27 15:43:43
author:     "gcrth"
header-img: "img/post-bg-2015.jpg"
catalog: true
---

## Background

There are many model predict the property of molecular, and they either use expert-crafted descriptors or graph convolutions. This paper evaluates the performance of these model carefully and proposes a new model.

Splitting the dataset according to scaffold is better than splitting randomly. Expert-crafted descriptor model can outperform learned representations on small datasets. Hyperparameter selection is vital, and Bayesian optimization is a good solution.

The model combining both expert-crafted descriptors and graph convolutions like the one proposed in this paper has the best performance. (To be confirmed)

## Methods

There are two key points about this model.

* It combines expert-crafted descriptors and graph convolutions. (a little weird, the paper says that they do not use descriptors at the end)
* The convolutions in this model perform on bonds instead of atoms.

The main structure of this model is called Directed MPNN. The main difference between it and MPNN is that it uses messages associated with bonds instead of atoms to prevent totters. Most vital calculation in the model is showed below.

![calculation1](../img/in-post/2020-09-27-Analyzing%20Learned%20Molecular%20Representations%20for%20Property%20Prediction/Screenshot%202020-09-27%20180356.jpg)

![calculation2](../img/in-post/2020-09-27-Analyzing%20Learned%20Molecular%20Representations%20for%20Property%20Prediction/Screenshot%202020-09-27%20180432.jpg)

The initial features can be calcualted with the following tables.

![feature tables](../img/in-post/2020-09-27-Analyzing%20Learned%20Molecular%20Representations%20for%20Property%20Prediction/Screenshot%202020-09-27%20180447.jpg)

To enhance the performance, the model can incorporates 200 global molecular features that can be computed rapidly with RDKit. The incorporation is done as follow.

![incorporation](../img/in-post/2020-09-27-Analyzing%20Learned%20Molecular%20Representations%20for%20Property%20Prediction/Screenshot%202020-09-27%20180504.jpg)

The hyperparameter is optimized with Hyperopt. By training multiple model seperately and use the average of the output as actual ouput, we could improve the performance.

## Experiment

This paper does a lot of experiment and shows that its model has state-of-art performance.

The experiment also shows that the dataset split by scaffold is more challenging.

## Future Work

### In the Paper

* Add 3-D infromation
* pretain model
* resolve extreme imbalance classification problem

## Something Unsure

The description in the paper does not seem to be matched.

The first one.

![description1](../img/in-post/2020-09-27-Analyzing%20Learned%20Molecular%20Representations%20for%20Property%20Prediction/Screenshot%202020-09-27%20220141.jpg)

The second one.

![description2-1](../img/in-post/2020-09-27-Analyzing%20Learned%20Molecular%20Representations%20for%20Property%20Prediction/Screenshot%202020-09-27%20220058.jpg)

![description2-2](../img/in-post/2020-09-27-Analyzing%20Learned%20Molecular%20Representations%20for%20Property%20Prediction/Screenshot%202020-09-27%20220114.jpg)

## Code

Implemented with pytorch, the code is avaliable on <https://github.com/chemprop/chemprop>.
