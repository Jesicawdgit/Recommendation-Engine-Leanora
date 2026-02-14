# OAuth Setup Guide

To enable Google and GitHub OAuth login, you need to set up OAuth credentials and configure them in your `.env` file.

## Step 1: Create a `.env` file

Create a file named `.env` in the `backend` directory with the following content:

```env
# Google OAuth
GOOGLE_CLIENT_ID=your_google_client_id_here
GOOGLE_CLIENT_SECRET=your_google_client_secret_here
GOOGLE_REDIRECT_URI=http://localhost:3000/auth/google/callback

# GitHub OAuth
GITHUB_CLIENT_ID=your_github_client_id_here
GITHUB_CLIENT_SECRET=your_github_client_secret_here
GITHUB_REDIRECT_URI=http://localhost:3000/auth/github/callback
```

## Step 2: Set up Google OAuth

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Navigate to **APIs & Services** > **Credentials**
4. Click **Create Credentials** > **OAuth client ID**
5. Configure the OAuth consent screen if prompted
6. Choose **Web application** as the application type
7. Add authorized redirect URIs:
   - `http://localhost:3000/auth/google/callback`
   - `http://localhost:5000/api/auth/google/callback`
8. Copy the **Client ID** and **Client Secret**
9. Add them to your `.env` file

## Step 3: Set up GitHub OAuth

1. Go to [GitHub Developer Settings](https://github.com/settings/developers)
2. Click **New OAuth App**
3. Fill in the application details:
   - **Application name**: Learnora
   - **Homepage URL**: `http://localhost:3000`
   - **Authorization callback URL**: `http://localhost:3000/auth/github/callback`
4. Click **Register application**
5. Copy the **Client ID** and generate a **Client Secret**
6. Add them to your `.env` file

## Step 4: Restart the backend server

After creating the `.env` file with your credentials, restart your Flask backend server:

```bash
cd backend
python app.py
```

## Note

- The `.env` file should be in the `backend` directory
- Never commit your `.env` file to version control (it's already in `.gitignore`)
- For production, use environment variables or a secure secrets management system

