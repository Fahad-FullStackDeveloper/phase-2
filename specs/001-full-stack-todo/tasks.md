---

description: "Task list template for feature implementation"
---

# Tasks: Full-Stack Todo Web Application

**Input**: Design documents from `/specs/001-full-stack-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan with backend/ and frontend/ directories
- [ ] T002 [P] Initialize Next.js project with TypeScript and Tailwind CSS in frontend/
- [ ] T003 [P] Initialize FastAPI project with SQLModel and database dependencies in backend/
- [ ] T004 [P] Configure linting and formatting tools for both frontend and backend
- [ ] T005 [P] Set up environment configuration management with proper secret handling

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [ ] T006 Setup Neon PostgreSQL database schema and migrations framework
- [ ] T007 [P] Implement Better Auth with JWT configuration for secure communication
- [ ] T008 [P] Setup API routing and middleware structure in FastAPI backend
- [ ] T009 Create base models/entities that all stories depend on (users, tasks)
- [ ] T010 Configure error handling and logging infrastructure for both frontend and backend
- [ ] T011 [P] Implement authentication middleware to verify JWT and extract user
- [ ] T012 Setup email notification service integration (Resend or similar)
- [ ] T013 Create database connection utilities for Neon PostgreSQL

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - User Registration and Authentication (Priority: P1) 🎯 MVP

**Goal**: Enable new users to register for an account and securely access their personal todo list from any device

**Independent Test**: Can be fully tested by registering a new user account and verifying that they can log in and access a protected area of the application.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T014 [P] [US1] Contract test for POST /api/auth/register in backend/tests/contract/test_auth.py
- [ ] T015 [P] [US1] Contract test for POST /api/auth/login in backend/tests/contract/test_auth.py
- [ ] T016 [P] [US1] Integration test for user registration flow in backend/tests/integration/test_auth.py
- [ ] T017 [P] [US1] Frontend component test for registration form in frontend/tests/components/test_registration.tsx

### Implementation for User Story 1

- [ ] T018 [P] [US1] Create User model in backend/src/models/user.py with SQLModel
- [ ] T019 [P] [US1] Create Session model in backend/src/models/session.py with SQLModel
- [ ] T020 [US1] Implement User service in backend/src/services/user_service.py (depends on T018)
- [ ] T021 [US1] Implement authentication service in backend/src/services/auth_service.py
- [ ] T022 [US1] Implement POST /api/auth/register endpoint in backend/src/routes/auth_routes.py
- [ ] T023 [US1] Implement POST /api/auth/login endpoint in backend/src/routes/auth_routes.py
- [ ] T024 [US1] Create Registration component in frontend/src/components/Registration.tsx
- [ ] T025 [US1] Create Login component in frontend/src/components/Login.tsx
- [ ] T026 [US1] Add API client function for authentication in frontend/src/lib/api.ts
- [ ] T027 [US1] Add validation and error handling for authentication operations
- [ ] T028 [US1] Add logging for user story 1 operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Create and Manage Personal Tasks (Priority: P2)

**Goal**: Enable registered users to create, view, update, and delete their personal tasks to organize daily activities effectively

**Independent Test**: Can be fully tested by creating a task, viewing it in the list, updating its details, marking it as complete, and deleting it.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T029 [P] [US2] Contract test for GET /api/{user_id}/tasks in backend/tests/contract/test_tasks.py
- [ ] T030 [P] [US2] Contract test for POST /api/{user_id}/tasks in backend/tests/contract/test_tasks.py
- [ ] T031 [P] [US2] Integration test for task creation flow in backend/tests/integration/test_tasks.py
- [ ] T032 [P] [US2] Frontend component test for TaskForm in frontend/tests/components/test_task_form.tsx

### Implementation for User Story 2

- [ ] T033 [P] [US2] Create Task model in backend/src/models/task.py with SQLModel
- [ ] T034 [US2] Implement Task service in backend/src/services/task_service.py (depends on T033)
- [ ] T035 [US2] Implement GET /api/{user_id}/tasks endpoint in backend/src/routes/task_routes.py
- [ ] T036 [US2] Implement POST /api/{user_id}/tasks endpoint in backend/src/routes/task_routes.py
- [ ] T037 [US2] Implement GET /api/{user_id}/tasks/{id} endpoint in backend/src/routes/task_routes.py
- [ ] T038 [US2] Implement PUT /api/{user_id}/tasks/{id} endpoint in backend/src/routes/task_routes.py
- [ ] T039 [US2] Implement DELETE /api/{user_id}/tasks/{id} endpoint in backend/src/routes/task_routes.py
- [ ] T040 [US2] Implement PATCH /api/{user_id}/tasks/{id}/complete endpoint in backend/src/routes/task_routes.py
- [ ] T041 [US2] Create TaskList component in frontend/src/components/TaskList.tsx
- [ ] T042 [US2] Create TaskForm component in frontend/src/components/TaskForm.tsx
- [ ] T043 [US2] Create TaskDetail component in frontend/src/components/TaskDetail.tsx
- [ ] T044 [US2] Add API client functions for task operations in frontend/src/lib/api.ts
- [ ] T45 [US2] Add validation and error handling for task operations (1-100 chars for title, up to 1000 chars for description)
- [ ] T046 [US2] Add recurring task functionality (daily, weekly, monthly, yearly) in task model and service

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Secure Data Isolation (Priority: P3)

**Goal**: Ensure that each user's tasks are only visible to them so their personal information remains private and secure

**Independent Test**: Can be fully tested by having multiple users create tasks and verifying that each user only sees their own tasks.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T047 [P] [US3] Integration test for user data isolation in backend/tests/integration/test_isolation.py
- [ ] T048 [P] [US3] Contract test for unauthorized access attempts in backend/tests/contract/test_security.py
- [ ] T049 [P] [US3] Frontend component test for user-specific data display in frontend/tests/components/test_dashboard.tsx

### Implementation for User Story 3

- [ ] T050 [P] [US3] Enhance authentication middleware to verify user ID in URL matches JWT token
- [ ] T051 [US3] Add user ID filtering to all task endpoints to ensure data isolation
- [ ] T052 [US3] Implement authorization checks in task service layer
- [ ] T053 [US3] Add user-specific data validation in frontend API calls
- [ ] T054 [US3] Create Dashboard component in frontend/src/components/Dashboard.tsx
- [ ] T055 [US3] Add email notification functionality for important events (deadline reminders, account alerts)
- [ ] T056 [US3] Implement recurring task generation based on recurrence patterns
- [ ] T057 [US3] Add responsive UI components that work across different device sizes

**Checkpoint**: All user stories should now be independently functional

---

[Add more user story phases as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T058 [P] Documentation updates in docs/
- [ ] T059 Code cleanup and refactoring
- [ ] T060 Performance optimization across all stories
- [ ] T061 [P] Additional unit tests (if requested) in tests/unit/
- [ ] T062 Security hardening (ensure all endpoints require JWT, user isolation enforced)
- [ ] T063 Run quickstart.md validation
- [ ] T064 Constitutional compliance verification

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for POST /api/auth/register in backend/tests/contract/test_auth.py"
Task: "Integration test for user registration flow in backend/tests/integration/test_auth.py"

# Launch all models for User Story 1 together:
Task: "Create User model in backend/src/models/user.py"
Task: "Create Session model in backend/src/models/session.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Constitutional Compliance Verification

- [ ] Full-Stack Integration: Tasks address both frontend and backend components
- [ ] User-Centric Authentication: JWT authentication implemented between layers
- [ ] Test-First: Test tasks defined before implementation tasks
- [ ] API-First Design: API contracts clearly defined and implemented
- [ ] Persistent Data Management: Database operations properly handled
- [ ] Responsive User Experience: UI/UX considerations addressed

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence