// src/Login.jsx
import React, { useState } from 'react';
import { createClient } from '@supabase/supabase-js';

// Read env variables
const supabaseUrl = process.env.REACT_APP_SUPABASE_URL;
const supabaseKey = process.env.REACT_APP_SUPABASE_ANON_KEY;

// Debug logging (remove in production)
console.log("Supabase URL:", supabaseUrl);
console.log("Supabase Key exists:", !!supabaseKey);

// Initialize Supabase client
const supabase = createClient(supabaseUrl, supabaseKey);

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [token, setToken] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');
    setToken('');

    try {
      const { data, error } = await supabase.auth.signInWithPassword({
        email,
        password,
      });

      if (error) {
        setError(error.message);
      } else if (data?.session?.access_token) {
        setToken(data.session.access_token);
      } else {
        setError("Login failed. No session returned.");
      }
    } catch (err) {
      console.error("Unexpected error:", err);
      setError("Something went wrong during login.");
    }
  };

  return (
    <div className="max-w-md mx-auto mt-10 p-6 border rounded shadow-md">
      <h2 className="text-xl font-bold mb-4">Supabase Login</h2>
      <form onSubmit={handleLogin}>
        <input
          type="email"
          placeholder="Email"
          className="w-full mb-2 p-2 border rounded"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          className="w-full mb-4 p-2 border rounded"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
        >
          Log In
        </button>
      </form>

      {error && <p className="text-red-500 mt-4">{error}</p>}

      {token && (
        <div className="mt-6">
          <p className="font-bold mb-2">✅ Access Token:</p>
          <textarea
            readOnly
            className="w-full h-32 p-2 border rounded"
            value={token}
          />
          <button
            className="mt-2 bg-green-600 text-white py-1 px-3 rounded"
            onClick={() => navigator.clipboard.writeText(token)}
          >
            Copy Token
          </button>
        </div>
      )}
    </div>
  );
}
