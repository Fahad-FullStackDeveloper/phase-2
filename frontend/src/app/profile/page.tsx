'use client';

import { useState, useEffect } from 'react';

export default function ProfilePage() {
  const [user, setUser] = useState<any>(null);

  useEffect(() => {
    // In a real app, you would fetch user details from the API
    // For now, we'll use the user info from localStorage or a dummy object
    const token = localStorage.getItem('authToken');
    if (token) {
      // Decode token or fetch user info from API
      setUser({ id: '1', name: 'John Doe', email: 'john@example.com' });
    }
  }, []);

  if (!user) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="max-w-md w-full bg-white p-8 rounded-lg shadow-md">
          <p className="text-center text-gray-600">Please log in to view your profile.</p>
          <div className="mt-4 text-center">
            <a 
              href="/login" 
              className="inline-block bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700"
            >
              Login
            </a>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-8">
        <div className="max-w-2xl mx-auto bg-white rounded-lg shadow-md p-6">
          <h1 className="text-2xl font-bold text-gray-800 mb-6">Profile</h1>
          
          <div className="space-y-4">
            <div>
              <h2 className="text-lg font-medium text-gray-700">Name</h2>
              <p className="text-gray-900">{user.name}</p>
            </div>
            
            <div>
              <h2 className="text-lg font-medium text-gray-700">Email</h2>
              <p className="text-gray-900">{user.email}</p>
            </div>
            
            <div>
              <h2 className="text-lg font-medium text-gray-700">Account ID</h2>
              <p className="text-gray-900">{user.id}</p>
            </div>
            
            <div className="pt-4">
              <h2 className="text-lg font-medium text-gray-700 mb-2">Account Actions</h2>
              <div className="flex space-x-4">
                <button className="bg-red-100 text-red-800 px-4 py-2 rounded hover:bg-red-200">
                  Change Password
                </button>
                <button className="bg-gray-100 text-gray-800 px-4 py-2 rounded hover:bg-gray-200">
                  Update Profile
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}