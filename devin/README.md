# Devin Agent Integration

## Overview

This directory contains templates and integration files for the Devin Agent, which implements the Working Backwards methodology within the Auto-coder-agent_Cursor_Roo_code repository's Log-Driven Development (LDD) system.

## Contents

- `devin_agent_template.mdc`: Main template for Devin Agent with Working Backwards methodology
- `ldd_integration.mdc`: Integration between Devin Agent and LDD System
- `README.md`: This file

## Working Backwards Methodology

The Devin Agent implements the Working Backwards methodology, which:

1. Starts with the desired end result (Goal State)
2. Uses step-back questioning to identify prerequisites
3. Creates a chain of prerequisites back to the initial state
4. Reorders steps to create a forward execution plan
5. Executes the plan with continuous feedback

For detailed documentation, see `/docs/devin/working_backwards.md`.

## Integration with LDD

The Devin Agent integrates with the existing LDD system through:

1. Extended logging templates
2. Memory Bank enhancements
3. SpecStory integration
4. Cursor Rules compatibility

## Usage

To use the Devin Agent template:

1. Reference the template in your agent implementation
2. Follow the Working Backwards methodology
3. Use the standard visual format with ◤◢◤◢ border markers
4. Integrate with the LDD system for logging and tracking

## Visual Format

All content blocks should use the standardized format:

```
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
Content goes here
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
```
