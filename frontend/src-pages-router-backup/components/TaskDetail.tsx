// frontend/src/components/TaskDetail.tsx
import React from 'react';

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

interface TaskDetailProps {
  task: Task;
  onEdit?: (task: Task) => void;
  onDelete?: (taskId: string) => void;
  onToggleCompletion?: (taskId: string) => void;
}

export const TaskDetail: React.FC<TaskDetailProps> = ({ 
  task, 
  onEdit, 
  onDelete, 
  onToggleCompletion 
}) => {
  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <div className="flex justify-between items-start">
        <div>
          <h2 className={`text-xl font-bold mb-2 ${task.completed ? 'line-through text-gray-500' : ''}`}>
            {task.title}
          </h2>
          
          {task.description && (
            <p className="text-gray-700 mb-4">{task.description}</p>
          )}
        </div>
        
        <div className="flex space-x-2">
          <button
            onClick={() => onToggleCompletion?.(task.id)}
            className={`px-3 py-1 rounded text-sm ${
              task.completed 
                ? 'bg-yellow-100 text-yellow-800 hover:bg-yellow-200' 
                : 'bg-green-100 text-green-800 hover:bg-green-200'
            }`}
          >
            {task.completed ? 'Mark Incomplete' : 'Mark Complete'}
          </button>
          
          <button
            onClick={() => onEdit?.(task)}
            className="px-3 py-1 bg-blue-100 text-blue-800 rounded text-sm hover:bg-blue-200"
          >
            Edit
          </button>
          
          <button
            onClick={() => onDelete?.(task.id)}
            className="px-3 py-1 bg-red-100 text-red-800 rounded text-sm hover:bg-red-200"
          >
            Delete
          </button>
        </div>
      </div>
      
      <div className="grid grid-cols-2 gap-4 mt-4 text-sm">
        <div>
          <p className="font-medium text-gray-700">Status:</p>
          <p className={task.completed ? 'text-green-600' : 'text-gray-600'}>
            {task.completed ? 'Completed' : 'Pending'}
          </p>
        </div>
        
        <div>
          <p className="font-medium text-gray-700">Created:</p>
          <p>{formatDate(task.created_at)}</p>
        </div>
        
        <div>
          <p className="font-medium text-gray-700">Last Updated:</p>
          <p>{formatDate(task.updated_at)}</p>
        </div>
        
        {task.recurrence_pattern && (
          <div>
            <p className="font-medium text-gray-700">Recurrence:</p>
            <p className="capitalize">{task.recurrence_pattern}</p>
          </div>
        )}
        
        {task.reminder_time && (
          <div>
            <p className="font-medium text-gray-700">Reminder:</p>
            <p>{formatDate(task.reminder_time)}</p>
          </div>
        )}
      </div>
    </div>
  );
};