# Database Skill

## Purpose
Provide all primitives for designing and maintaining PostgreSQL schemas in Neon Serverless.

This skill is the ONLY place where data structure rules live.

---

## Core Capabilities

This skill handles:

### 1. Schema Design
- Tables
- Columns
- Data types
- Primary keys
- Foreign keys
- Relations

### 2. Constraints
- NOT NULL
- UNIQUE
- CHECK
- Referential integrity
- Cascading rules

### 3. Indexing
- Performance indexes
- Uniqueness indexes
- Lookup optimization

### 4. Migrations
- Forward migrations
- Backward (rollback) migrations
- Safe evolution of schema
- Zero-data-loss upgrades

### 5. Neon Serverless Compatibility
- Connection-safe designs
- Stateless migration safety
- Serverless-friendly patterns

---

## Data Safety Rules

- No breaking change without a migration
- No destructive migration without rollback
- No nullable fields for required data
- No orphaned records allowed

---

## Output Format

This skill outputs:
- Schema definitions
- Migration plans
- Table structures
- Relation maps

It never outputs:
- API code
- Auth logic
- UI
