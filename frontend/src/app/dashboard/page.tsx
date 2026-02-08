// frontend/src/app/dashboard/page.tsx
'use client';

import { useState, useEffect } from 'react';
import { TaskList } from '@/components/TaskList';
import { TaskForm } from '@/components/TaskForm';

export default function DashboardPage() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [user, setUser] = useState<any>(null);

  useEffect(() => {
    // Check if user is logged in by checking for token in localStorage
    const token = localStorage.getItem('authToken');
    if (token) {
      setIsLoggedIn(true);
      // In a real app, you might decode the token or fetch user info
      // For now, we'll just set a dummy user
      setUser({ id: '1', name: 'User' });
    }
  }, []);

  if (!isLoggedIn) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="max-w-md mx-auto bg-white rounded-lg shadow-md p-6">
          <h1 className="text-2xl font-bold text-center text-gray-800 mb-6">Todo App</h1>
          <p className="text-center text-gray-600 mb-6">Please log in to access your tasks</p>
          
          <div className="space-y-4">
            <a 
              href="/login" 
              className="block w-full bg-blue-600 text-white py-2 px-4 rounded-md text-center hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
            >
              Login
            </a>
            
            <a 
              href="/register" 
              className="block w-full bg-gray-200 text-gray-800 py-2 px-4 rounded-md text-center hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2"
            >
              Register
            </a>
          </div>
        </div>
      </div>
    );
  }

  return (
    <main className="container mx-auto px-4 py-8">
      <div className="text-center mb-8">
        <h1 className="text-3xl font-bold text-gray-800">Todo Dashboard</h1>
        <p className="text-gray-600">Manage your tasks efficiently</p>
      </div>
      
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
    </main>
  );
}