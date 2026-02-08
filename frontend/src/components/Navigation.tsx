// frontend/src/components/Navigation.tsx
'use client';

import { useState, useEffect } from 'react';

export default function Navigation() {
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

  const handleLogout = () => {
    localStorage.removeItem('authToken');
    setIsLoggedIn(false);
    setUser(null);
    // Redirect to home page
    window.location.href = '/';
  };

  return (
    <nav className="bg-white shadow-md">
      <div className="container mx-auto px-4 py-3">
        <div className="flex justify-between items-center">
          <div className="flex items-center">
            <a href="/" className="text-xl font-bold text-blue-600">Todo App</a>
            <div className="hidden md:block ml-10">
              <a href="/" className="text-gray-700 hover:text-blue-600 px-3 py-2">Home</a>
              {isLoggedIn && (
                <>
                  <a href="/profile" className="text-gray-700 hover:text-blue-600 px-3 py-2">Profile</a>
                </>
              )}
            </div>
          </div>

          <div className="flex items-center space-x-4">
            {isLoggedIn ? (
              <>
                <span className="text-gray-600">Welcome, {user?.name}</span>
                <button 
                  onClick={handleLogout}
                  className="text-sm bg-red-100 text-red-800 px-3 py-1 rounded hover:bg-red-200"
                >
                  Logout
                </button>
              </>
            ) : (
              <>
                <a 
                  href="/login" 
                  className="text-sm bg-gray-200 text-gray-800 px-3 py-1 rounded hover:bg-gray-300"
                >
                  Login
                </a>
                <a 
                  href="/register" 
                  className="text-sm bg-blue-600 text-white px-3 py-1 rounded hover:bg-blue-700"
                >
                  Register
                </a>
              </>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
}