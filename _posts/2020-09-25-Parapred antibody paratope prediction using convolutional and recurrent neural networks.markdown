---
layout:     post
title:      "Parapred antibody paratope prediction using convolutional and recurrent neural networks"
subtitle:   ""
date:       2020-09-25 20:23:30
author:     "gcrth"
header-img: "img/post-bg-2015.jpg"
catalog: true
---

## Background

It is vital to predict antibody paratope.

## Solution

This moedel takes the amino acid sequence of a CDR and four adjacent residues as input and predicts the paratope.

### Data

The extended CDR sequence is from SAbDab, which contains 277 bound complexes. These sequence need to be preprocessed.

* Each sequence is encoded as a row and a batch of sequences forms a three dimensions tensor after padding.
* Each element in the row is a feature vector which has two parts.
  * One-hot encoding of the type of the residue. (21D)
  * Seven features.

There are 1662 (277*6) sequences in the dataset in total.

### Model

The problem can be formalized as binary classification problem of each element in the sequence.

The main structure of the model is as follow.

![model structure](../img/in-post/2020-09-25-Parapred%20antibody%20paratope%20prediction%20using%20convolutional%20and%20recurrent%20neural%20networks/Screenshot%202020-09-26%20192211.jpg)

There are several key points.

* The `conv` in the picture is actually 1-D convolution layer. There is a zero padding on each side of the sequence.
* Bidirectional RNN is a RNN introduces a second pass going in the opposite direction.The details is showed in the picture below.
* The activation function used in this model is ELU.
* The loss is binary cross-entropy loss.
* Adam optimizer.

![Bidirectional RNN](../img/in-post/2020-09-25-Parapred%20antibody%20paratope%20prediction%20using%20convolutional%20and%20recurrent%20neural%20networks/Screenshot%202020-09-26%20192232.jpg)

## Experiment

The experiment is done with 10-fold cross-validation. The result is showed as follow.

![result](../img/in-post/2020-09-25-Parapred%20antibody%20paratope%20prediction%20using%20convolutional%20and%20recurrent%20neural%20networks/Screenshot%202020-09-26%20192250.jpg)

## Future Work

### According to the Paper

Add 3-D structure infromation.

### other

The model would be more useful if it could output whether residues is the paratope related to the input antigen.
