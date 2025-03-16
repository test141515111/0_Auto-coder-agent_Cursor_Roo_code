# Working Backwards Methodology for Devin Agent

## Overview

The Working Backwards methodology is a problem-solving approach that starts with the desired end result and works backward to identify the steps needed to achieve it. This document explains how this methodology is implemented in the Devin Agent template.

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## Core Principles

1. **Define the Goal State**: Clearly articulate what success looks like
2. **Step-Back Questioning**: Ask what must be true immediately before achieving the goal
3. **Recursive Analysis**: Continue working backwards until reaching initial actions
4. **Forward Execution Planning**: Reorder steps for execution (A→B→C→...→Z)
5. **Continuous Feedback**: Evaluate and adjust the plan during execution
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

## Implementation in Devin Agent

### 1. Goal State Definition

The goal state is defined based on the user's intent analysis:

```
[Input] → [User Intent] → [Intent]
[Input] → [User Intent] → [Want or Need Intent]
```

This is then formalized as:

```
[Fixed User Want Intent] = Defined Goal State
```

### 2. Step-Back Questioning

For each goal or subgoal, Devin asks:
- What must be true immediately before this can happen?
- What resources, tools, or conditions are required?
- What dependencies exist?

### 3. Prerequisites Chain

The answers to step-back questions create a chain of prerequisites:
- Z (Goal) requires Y
- Y requires X
- X requires W
- ...and so on until reaching A (Initial State)

### 4. Forward Execution Plan

The prerequisites chain is reversed to create an actionable plan:
1. A → B → C → ... → Z

Each step includes:
- Clear success criteria
- Required tools and resources
- Verification methods

### 5. Task Execution with Feedback

During execution, Devin:
- Monitors progress against the plan
- Collects feedback after each step
- Adjusts subsequent steps as needed
- Documents outcomes in the LDD system

## Integration with LDD System

The Working Backwards methodology integrates with the Log-Driven Development system:

1. **Planning Phase**: Goal definition and backward analysis are logged
2. **Execution Phase**: Each step execution is logged with outcomes
3. **Feedback Phase**: Adjustments and learnings are captured
4. **Optimization Phase**: The entire process is analyzed for improvement

## Template Usage

The Devin agent template implements this methodology through structured sections:

- **Goal State**: Clearly defined end result
- **Step-Back Questions**: Key questions to identify prerequisites
- **Prerequisites Chain**: Backward-traced dependencies
- **Forward Execution Plan**: Reordered steps for implementation
- **Task Breakdown**: Detailed tasks derived from the plan
- **Agent Execution Stack**: Assignment of tasks to specific agents

## Visual Format

All sections use the standardized visual format with border markers:

```
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
Content goes here
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
```
