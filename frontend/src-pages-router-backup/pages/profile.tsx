// frontend/src/pages/profile.tsx
import React, { useState, useEffect } from 'react';
import { apiClient } from '../lib/api';

interface UserProfile {
  id: string;
  email: string;
  name: string;
  created_at: string;
}

const ProfilePage: React.FC = () => {
  const [profile, setProfile] = useState<UserProfile | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchProfile();
  }, []);

  const fetchProfile = async () => {
    try {
      setLoading(true);
      // In a real app, we would get the user profile from the API
      // For now, we'll simulate with a placeholder
      const token = localStorage.getItem('authToken');
      if (!token) {
        setError('No authentication token found');
        return;
      }
      
      // Placeholder implementation - in real app, this would be an API call
      setProfile({
        id: '123e4567-e89b-12d3-a456-426614174000',
        email: 'user@example.com',
        name: 'John Doe',
        created_at: new Date().toISOString(),
      });
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch profile');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center min-h-screen">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
          {error}
        </div>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-6">User Profile</h1>
      
      {profile && (
        <div className="bg-white rounded-lg shadow-md p-6 max-w-2xl">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h2 className="text-xl font-semibold mb-4">Personal Information</h2>
              
              <div className="space-y-4">
                <div>
                  <label className="block text-gray-600 text-sm font-medium mb-1">Name</label>
                  <p className="bg-gray-50 p-3 rounded border">{profile.name}</p>
                </div>
                
                <div>
                  <label className="block text-gray-600 text-sm font-medium mb-1">Email</label>
                  <p className="bg-gray-50 p-3 rounded border">{profile.email}</p>
                </div>
                
                <div>
                  <label className="block text-gray-600 text-sm font-medium mb-1">Account Created</label>
                  <p className="bg-gray-50 p-3 rounded border">
                    {new Date(profile.created_at).toLocaleDateString()}
                  </p>
                </div>
              </div>
            </div>
            
            <div>
              <h2 className="text-xl font-semibold mb-4">Account Settings</h2>
              
              <div className="space-y-4">
                <button className="w-full bg-blue-100 text-blue-800 py-2 px-4 rounded hover:bg-blue-200 transition-colors">
                  Change Password
                </button>
                
                <button className="w-full bg-gray-100 text-gray-800 py-2 px-4 rounded hover:bg-gray-200 transition-colors">
                  Update Profile
                </button>
                
                <button className="w-full bg-red-100 text-red-800 py-2 px-4 rounded hover:bg-red-200 transition-colors">
                  Delete Account
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ProfilePage;