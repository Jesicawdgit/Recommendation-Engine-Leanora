# How to Find Your Auth0 Domain

The error "Unknown host" means your Auth0 domain is not set correctly. Follow these steps:

## Step 1: Log into Auth0 Dashboard

1. Go to https://manage.auth0.com/
2. Log in with your Auth0 account

## Step 2: Find Your Domain

1. In the left sidebar, click on **Applications**
2. Click on your application (or create one if you haven't)
3. In the application settings, look for the **Domain** field
   - It will look something like: `dev-xxxxx.us.auth0.com` or `your-tenant.eu.auth0.com`
   - **This is your Auth0 domain**

## Step 3: Update Your .env File

1. Open `frontend/.env` file
2. Replace `your_domain.auth0.com` with your actual domain from Step 2
3. Example:
   ```env
   REACT_APP_AUTH0_DOMAIN=dev-xxxxx.us.auth0.com
   REACT_APP_AUTH0_CLIENT_ID=xcBX1MN78Qf8CZ6qnNPVSM4yokvmIFZ7
   ```

## Step 4: Restart Your Development Server

After updating the .env file:
1. Stop your React app (Ctrl+C)
2. Restart it: `npm start`

## Step 5: Enable Social Connections

1. In Auth0 Dashboard, go to **Authentication** > **Social**
2. Enable **Google** connection
3. Enable **GitHub** connection
4. Configure them with your OAuth credentials

## Common Domain Formats

- US: `your-tenant.us.auth0.com`
- EU: `your-tenant.eu.auth0.com`
- AU: `your-tenant.au.auth0.com`

Your domain is unique to your Auth0 tenant and cannot be guessed - you must get it from your Auth0 dashboard.

