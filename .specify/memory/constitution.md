<!-- SYNC IMPACT REPORT
Version change: 1.0.0 → 1.1.0
Modified principles: None (new constitution)
Added sections: All sections (new constitution)
Removed sections: None
Templates requiring updates:
  - ✅ .specify/templates/plan-template.md - Updated to reflect new principles
  - ✅ .specify/templates/spec-template.md - Updated to reflect new requirements
  - ✅ .specify/templates/tasks-template.md - Updated to reflect new task types
  - ⚠️  README.md - Review needed for updated principles
Follow-up TODOs: None
-->

# Todo Full-Stack Web Application Constitution

## Core Principles

### I. Full-Stack Integration
The application consists of a Next.js 16+ frontend with a Python FastAPI backend, connected via RESTful API endpoints. All features must be implemented with consideration for both frontend and backend components, ensuring seamless integration between layers. Components must be designed to work cohesively across the entire stack.

### II. User-Centric Authentication
Authentication must be implemented using Better Auth with JWT tokens for secure communication between frontend and backend. Every API request must be authenticated and authorized, with user data properly isolated so each user only accesses their own tasks. Security is paramount in all user interactions.

### III. Test-First (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced. Both frontend and backend components must have comprehensive test coverage before deployment.

### IV. API-First Design
All backend functionality must be exposed through well-defined RESTful API endpoints following the specified contract. APIs must be consistent, predictable, and follow standard HTTP methods and status codes. Documentation must be maintained alongside implementation.

### V. Persistent Data Management
Data must be stored in Neon Serverless PostgreSQL database using SQLModel ORM for type-safe database operations. All data operations must be reliable, efficient, and maintain data integrity across application states.

### VI. Responsive User Experience
The frontend interface must be responsive and accessible across different devices and screen sizes. User interactions should be intuitive and provide immediate feedback. Performance considerations must be taken into account for all UI components.

## Additional Constraints

### Technology Stack Requirements
- Frontend: Next.js 16.1.6 with App Router, TypeScript, Tailwind CSS
- Backend: Python FastAPI with SQLModel ORM
- Database: Neon Serverless PostgreSQL
- Authentication: Better Auth with JWT integration
- Spec-Driven Development: Claude Code + Spec-Kit Plus

### Security Standards
- All API endpoints must require valid JWT tokens
- Requests without tokens receive 401 Unauthorized responses
- Each user only sees/modify their own tasks
- Task ownership is enforced on every operation
- Shared secret (BETTER_AUTH_SECRET) must be consistent between frontend and backend

### Performance Standards
- API endpoints should respond within 500ms for typical operations
- Database queries must be optimized with appropriate indexing
- Frontend should load initial content quickly with progressive enhancement
- Efficient data fetching strategies should be implemented

## Development Workflow

### Feature Implementation Process
1. Write/update feature specifications in the specs/ directory
2. Generate architectural plan based on specifications
3. Break features into testable tasks
4. Implement via Claude Code following Agentic Dev Stack workflow
5. Test and validate both frontend and backend components
6. Iterate based on testing and validation results

### Code Review Requirements
- All pull requests must verify compliance with constitutional principles
- Cross-stack impact must be considered (frontend and backend)
- Security implications must be validated
- API contract compliance must be confirmed
- Test coverage must meet minimum thresholds

### Quality Gates
- All automated tests must pass
- API endpoints must conform to documented contracts
- Database migrations must be properly handled
- Authentication and authorization must be correctly implemented
- Performance benchmarks must be met

## Governance

This constitution governs all development activities for the Todo Full-Stack Web Application. All code reviews, architectural decisions, and feature implementations must comply with these principles. Amendments to this constitution require documentation of the change, approval from project stakeholders, and a migration plan for existing code.

All pull requests and code reviews must verify constitutional compliance. Complexity must be justified with clear benefits to the overall system. Use this constitution as the primary guidance document for development decisions.

**Version**: 1.1.0 | **Ratified**: 2026-02-07 | **Last Amended**: 2026-02-07