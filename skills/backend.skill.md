# Backend Skill

## Purpose
Provide all primitives needed to build and operate a FastAPI-based backend.

This skill is the ONLY place where API execution logic lives.

---

## Core Capabilities

This skill handles:

### 1. Route Generation
- Define HTTP methods
- Attach paths
- Bind controllers
- Inject dependencies

### 2. Request Handling
- Parse JSON
- Validate input
- Extract auth tokens
- Call Auth Agent

### 3. Response Handling
- Format output
- Enforce API schemas
- Return proper status codes
- Handle errors

### 4. Auth Integration
- Validate JWT via Auth Agent
- Extract user identity
- Enforce permissions

### 5. Database Integration
- Call Database Agent
- Execute queries
- Handle transactions
- Return domain objects

---

## Execution Rules

- No route may bypass Auth Agent
- No data may bypass Database Agent
- All inputs must be validated
- All outputs must match API Agent contracts

---

## Output Format

This skill outputs:
- Route handlers
- Controller logic
- Service orchestration

It never outputs:
- Auth rules
- Schema definitions
- UI code
