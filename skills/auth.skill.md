# Auth Skill

## Purpose
Provide all authentication and authorization primitives for the system.

This skill is the ONLY place where authentication logic is defined.

---

## Core Capabilities

This skill handles:

### 1. Signup
- Validate email
- Validate password strength
- Hash password
- Prepare user identity payload
- Return safe user object (never password)

### 2. Sign In
- Verify email exists
- Compare hashed password
- Generate JWT access token
- Generate refresh token
- Return session payload

### 3. Password Security
- Use industry-standard hashing (bcrypt or argon2)
- Never store plain text passwords
- Enforce minimum complexity

### 4. JWT Tokens
- Create access tokens
- Verify tokens
- Handle expiration
- Attach user identity
- Enforce revocation logic

### 5. Better Auth Integration
- Map Better Auth users to internal user model
- Validate Better Auth tokens
- Sync identity
- Handle SSO and OAuth logins

---

## Security Rules

- Passwords are always hashed
- Tokens must be signed
- Tokens must expire
- Refresh tokens must be rotatable
- Invalid tokens are always rejected

---

## Output Format

This skill outputs:
- Auth payloads
- Token structures
- Validation results
- Auth errors

It never outputs:
- SQL
- UI
- API routes

