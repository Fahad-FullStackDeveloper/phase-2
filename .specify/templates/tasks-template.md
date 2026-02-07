---

description: "Task list template for feature implementation"
---

# Tasks: [FEATURE NAME]

**Input**: Design documents from `/specs/[###-feature-name]/`
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
- [ ] T002 Initialize Next.js project with TypeScript and Tailwind CSS in frontend/
- [ ] T003 Initialize FastAPI project with SQLModel and database dependencies in backend/
- [ ] T004 [P] Configure linting and formatting tools for both frontend and backend

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [ ] T005 Setup Neon PostgreSQL database schema and migrations framework
- [ ] T006 [P] Implement Better Auth with JWT configuration for secure communication
- [ ] T007 [P] Setup API routing and middleware structure in FastAPI backend
- [ ] T008 Create base models/entities that all stories depend on (users, tasks)
- [ ] T009 Configure error handling and logging infrastructure for both frontend and backend
- [ ] T010 Setup environment configuration management with proper secret handling
- [ ] T011 [P] Implement authentication middleware to verify JWT and extract user

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - [Title] (Priority: P1) 🎯 MVP

**Goal**: [Brief description of what this story delivers]

**Independent Test**: [How to verify this story works on its own]

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T012 [P] [US1] Contract test for [endpoint] in backend/tests/contract/test_[name].py
- [ ] T013 [P] [US1] Integration test for [user journey] in backend/tests/integration/test_[name].py
- [ ] T014 [P] [US1] Frontend component test for [UI element] in frontend/tests/components/test_[name].tsx

### Implementation for User Story 1

- [ ] T015 [P] [US1] Create Task model in backend/src/models/task.py with SQLModel
- [ ] T016 [P] [US1] Create User model in backend/src/models/user.py (managed by Better Auth)
- [ ] T017 [US1] Implement Task service in backend/src/services/task_service.py (depends on T015)
- [ ] T018 [US1] Implement GET /api/{user_id}/tasks endpoint in backend/src/routes/task_routes.py
- [ ] T019 [US1] Implement POST /api/{user_id}/tasks endpoint in backend/src/routes/task_routes.py
- [ ] T020 [US1] Create TaskList component in frontend/src/components/TaskList.tsx
- [ ] T021 [US1] Create TaskForm component in frontend/src/components/TaskForm.tsx
- [ ] T022 [US1] Add API client function for task operations in frontend/src/lib/api.ts
- [ ] T023 [US1] Add validation and error handling for task operations
- [ ] T024 [US1] Add logging for user story 1 operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - [Title] (Priority: P2)

**Goal**: [Brief description of what this story delivers]

**Independent Test**: [How to verify this story works on its own]

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T025 [P] [US2] Contract test for [endpoint] in backend/tests/contract/test_[name].py
- [ ] T026 [P] [US2] Integration test for [user journey] in backend/tests/integration/test_[name].py
- [ ] T027 [P] [US2] Frontend component test for [UI element] in frontend/tests/components/test_[name].tsx

### Implementation for User Story 2

- [ ] T028 [P] [US2] Create additional models if needed in backend/src/models/
- [ ] T029 [US2] Implement GET /api/{user_id}/tasks/{id} endpoint in backend/src/routes/task_routes.py
- [ ] T030 [US2] Implement PUT /api/{user_id}/tasks/{id} endpoint in backend/src/routes/task_routes.py
- [ ] T031 [US2] Implement DELETE /api/{user_id}/tasks/{id} endpoint in backend/src/routes/task_routes.py
- [ ] T032 [US2] Create TaskDetail component in frontend/src/components/TaskDetail.tsx
- [ ] T033 [US2] Create TaskEdit component in frontend/src/components/TaskEdit.tsx
- [ ] T034 [US2] Add API client functions for detailed task operations in frontend/src/lib/api.ts
- [ ] T035 [US2] Integrate with User Story 1 components (if needed)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - [Title] (Priority: P3)

**Goal**: [Brief description of what this story delivers]

**Independent Test**: [How to verify this story works on its own]

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T036 [P] [US3] Contract test for [endpoint] in backend/tests/contract/test_[name].py
- [ ] T037 [P] [US3] Integration test for [user journey] in backend/tests/integration/test_[name].py
- [ ] T038 [P] [US3] Frontend component test for [UI element] in frontend/tests/components/test_[name].tsx

### Implementation for User Story 3

- [ ] T039 [P] [US3] Create additional models if needed in backend/src/models/
- [ ] T040 [US3] Implement PATCH /api/{user_id}/tasks/{id}/complete endpoint in backend/src/routes/task_routes.py
- [ ] T041 [US3] Create TaskCompletion component in frontend/src/components/TaskCompletion.tsx
- [ ] T042 [US3] Add API client functions for task completion in frontend/src/lib/api.ts
- [ ] T043 [US3] Add user authentication checks to all frontend API calls
- [ ] T044 [US3] Add responsive design enhancements to task components

**Checkpoint**: All user stories should now be independently functional

---

[Add more user story phases as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] TXXX [P] Documentation updates in docs/
- [ ] TXXX Code cleanup and refactoring
- [ ] TXXX Performance optimization across all stories
- [ ] TXXX [P] Additional unit tests (if requested) in tests/unit/
- [ ] TXXX Security hardening (ensure all endpoints require JWT, user isolation enforced)
- [ ] TXXX Run quickstart.md validation
- [ ] TXXX Constitutional compliance verification

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
Task: "Contract test for [endpoint] in backend/tests/contract/test_[name].py"
Task: "Integration test for [user journey] in backend/tests/integration/test_[name].py"

# Launch all models for User Story 1 together:
Task: "Create Task model in backend/src/models/task.py"
Task: "Create User model in backend/src/models/user.py"
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
