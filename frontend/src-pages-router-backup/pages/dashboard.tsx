// frontend/src/pages/dashboard.tsx
import React from 'react';
import { Dashboard } from '../components/Dashboard';

const TaskDashboard: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      <Dashboard />
    </div>
  );
};

export default TaskDashboard;