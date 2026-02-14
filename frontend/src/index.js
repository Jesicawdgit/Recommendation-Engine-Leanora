import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Auth0Provider } from '@auth0/auth0-react';
import Login from './Login';
import Signup from './Signup';
import ProtectedRoute from './ProtectedRoute';

const domain = process.env.REACT_APP_AUTH0_DOMAIN;
const clientId = process.env.REACT_APP_AUTH0_CLIENT_ID || 'xcBX1MN78Qf8CZ6qnNPVSM4yokvmIFZ7';

if (!domain || domain === 'your_domain.auth0.com') {
  console.error('⚠️ REACT_APP_AUTH0_DOMAIN is not set correctly!');
  console.error('Please:');
  console.error('1. Go to https://manage.auth0.com/');
  console.error('2. Navigate to Applications > Your App');
  console.error('3. Find your "Domain" (e.g., dev-xxxxx.us.auth0.com)');
  console.error('4. Update .env file with: REACT_APP_AUTH0_DOMAIN=your_actual_domain');
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Auth0Provider
      domain={domain}
      clientId={clientId}
      authorizationParams={{
        redirect_uri: window.location.origin
      }}
      useRefreshTokens={true}
      cacheLocation="localstorage"
      onRedirectCallback={(appState) => {
        // After Auth0 redirects back, navigate to the app
        // The ProtectedRoute will handle authentication check
      }}
    >
      <BrowserRouter>
        <Routes>
          <Route 
            path="/" 
            element={
              <ProtectedRoute>
                <App />
              </ProtectedRoute>
            } 
          />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="*" element={<Navigate to="/login" replace />} />
        </Routes>
      </BrowserRouter>
    </Auth0Provider>
  </React.StrictMode>
);
