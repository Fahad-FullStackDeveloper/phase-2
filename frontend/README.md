# Frontend for Todo Application

This is the frontend for the Todo Full-Stack Web Application, built with Next.js and TypeScript.

## Features

- User registration and login
- Task management (create, read, update, delete)
- Dashboard for task overview
- Responsive UI with Tailwind CSS
- JWT-based authentication

## Tech Stack

- Next.js 16.1.6
- TypeScript
- Tailwind CSS
- React Hooks
- Better Auth for authentication

## Setup

1. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env.local
   # Edit .env.local with your API endpoint and auth configuration
   ```

3. Run the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

## Components

- Registration: User registration form
- Login: User login form
- TaskList: List of user tasks
- TaskForm: Form to create new tasks
- TaskDetail: Detailed view of a single task
- Dashboard: Main dashboard with task management

## Testing

Run the tests using Jest:

```bash
npm test
# or
yarn test
```