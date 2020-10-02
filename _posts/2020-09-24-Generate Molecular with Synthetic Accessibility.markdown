---
layout:     post
title:      "Generate Molecular with Synthetic Accessibility"
subtitle:   ""
date:       2020-09-24 12:11:28
author:     "gcrth"
header-img: "img/post-bg-2015.jpg"
catalog: true
---

## Background

When generating molecular, we need to consider if it is able to be synthesized. Policy Gradient for Forward Synthesis (PGFS) is designed to solve this problem.

## Solution / Method

The RL model could give the synthesis routes of the proposed small molecules to ensure they could be synthesized.

The base RL algorithm used in this model is TD3. However, there are several difference between each other.

* The actor module includes two learnable networks.
* A k-NN network will be used as a part of the environment.

It is important for this model to reduce the action space.

* At each step, the model will first select a reaction template and then select a reactant. A reaction template is represented as SMARTS, and these templates limit the reactants having reaction to have particular substructure. 
* The reactants are also constrained to have the substructure once. 
* If the outcome have multiple possibilities, one of them will be selected randomly.

The whole structure is showed in the picture. 

![model structure](/img/in-post/2020-09-24-Generate%20Molecular%20with%20Synthetic%20Accessibility/Screenshot%202020-09-25%20121825.jpg)

The actor (blue area) takes the first reactant, the product from the previous step, as input and outputs the action which will be the prototype of the second reactant. The critic (red area) outputs the Q value according to the action and state. The environment chooses k reactants most related to the prototype to be the candidates and output the reactant with the highest reward.

The main structure of training is showed below. In fact any policy gradient algorithm for continuous action spaces will do the similar thing.

![training steps](/img/in-post/2020-09-24-Generate%20Molecular%20with%20Synthetic%20Accessibility/Screenshot%202020-09-25%20124751.jpg)

To enable the model to train faster, there are several ticks.

* smooth the target policy
* use double Q-learning strategy
* delay updates
* add cross entropy for network f

## Experiments

### Compared Metrics

The performance of this model is compared through both traditional metrics and performance against HIV targets.

* QED
* clogP
* pIC50 predicted by QSAR model towards three targets __(this seems to be more reasonable than other two)__
  * CCR5
  * HIV integrace (INT)
  * HIV-RT 

### Result

The performance of this model is compared with other similar models, and the result is as follow.

![result](/img/in-post/2020-09-24-Generate%20Molecular%20with%20Synthetic%20Accessibility/Screenshot%202020-09-25%20170221.jpg)

## Future Work

### In this Paper

* use another policy gradient to update the f network 
* use more advance RL network

### Possible Shortcomming (to be confirmed)

* The reaction templates represented by SMARTS may limited the final product.
* The usage of k-NN is kind of weird and the Pi network should learn to produce valid action instead of fixing it with K-NN.
* The result of QSAR model would have differnce with the truth, and it may have some negetive impact. Actually othe two metrics have similar problem.

## code

No training code. Data, trained models and test code <https://github.com/99andBeyond/Apollo1060>.