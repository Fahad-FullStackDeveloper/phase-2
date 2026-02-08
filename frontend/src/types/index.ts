// frontend/src/types/index.ts

export interface Task {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  created_at: string;
  updated_at: string;
  recurrence_pattern?: string;
  recurrence_end_date?: string;
  reminder_time?: string;
}

export interface User {
  id: string;
  email: string;
  name: string;
  created_at: string;
  updated_at: string;
}