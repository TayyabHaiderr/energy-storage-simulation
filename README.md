# Energy Storage Performance Simulation

This project implements a simplified, reproducible energy storage performance model
based on an independent research study comparing energy storage technologies.

## What the model does
The simulation calculates year-by-year:
- Round-trip efficiency decline using a linear degradation assumption
- Annual energy delivered based on system capacity and cycling behavior

The model directly translates analytical equations and pseudo-code from the research
into executable Python logic.

## Why this matters
Small assumptions about degradation and system lifetime can significantly change
long-term performance outcomes. By implementing the model in code, these effects
can be tested, reproduced, and validated computationally.

## How to run
```bash
python model.py
