// frontend/src/components/Dashboard.tsx
import React from 'react';
import { TaskList } from './TaskList';
import { TaskForm } from './TaskForm';

export const Dashboard: React.FC = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <header className="mb-8">
        <h1 className="text-3xl font-bold text-gray-800">Todo Dashboard</h1>
        <p className="text-gray-600">Manage your tasks efficiently</p>
      </header>
      
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div>
          <h2 className="text-xl font-semibold mb-4">Create New Task</h2>
          <TaskForm />
        </div>
        
        <div>
          <h2 className="text-xl font-semibold mb-4">Your Tasks</h2>
          <TaskList />
        </div>
      </div>
    </div>
  );
};