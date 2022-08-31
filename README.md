# Backend Component Design - Lyft Virtual Experience
This repository contains a **backend component** built for Lyft's Backend Engineering Virtual Experience Program, where I was given a scenario and an engineering problem to solve as if I were an engineer on Lyft's team.

Let's get to it :))

## Backgroud:
I inherited a backend component project from another engineer, who left for another urgent project. Because of the urgent departure, the backend component is unfinished - meaning it's messy, unreviewed, and untested. To finish up the component, there's also one more functionality that needs to be added.


Problems:
* the code needs cleaning up
* the component needs to be tested
* directly adding the new functionality will make the code base even messier


Tasks to finish the component:
* draft new architecture to incorporate the new functionality cleanly
* refactor messy codebase
* test and debug codebase
* add new functionality using TDD

## The component:
The component is responsible for determining whether cars in Lyft’s new rental fleet should be serviced when they are returned. The fleet has 5 models of cars, each model with a differect engine-battery combination.

Whether or not a car should be serviced depends on two factors at the moment: 
1. what type of engine the car has (3 types of engine currently)
2. what type battery the case has (2 types of battery currently)
Each engine/battery type has it's own evaluation criteria for when it needs to be serviced


Design requirements:

The component must be **extensible** and **easy to modify**:
* the criteria that governs whether an engine or battery needs service will change somewhat frequently in the future
* new car models will be added to the fleet in the future
* new criteria - the system should also take tire wear into account in determining whether a car needs to be serviced

## Navigating the repository:
/doc - documentation including design docs for the new software architecture and the new functionality.


## Credit
This repository is forked from vagabond-systems/forage-lyft-starter-repo, which contained the starting codebase that I inherited.
This is a project under Lyft's Backend Engineering Virtual Experience Program
