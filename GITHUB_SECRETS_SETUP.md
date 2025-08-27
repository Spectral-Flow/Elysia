# GitHub Secrets Setup for Elysia

This document explains how to configure GitHub secrets for the Elysia AI Concierge application to enable proper CI/CD functionality.

## Required GitHub Secrets

The following secrets need to be configured in your GitHub repository settings:

### Essential Secrets (Required)

| Secret Name | Description | Example Value |
|-------------|-------------|---------------|
| `OPENAI_API_KEY` | OpenAI API key for AI functionality | `sk-...` |
| `JWT_SECRET_KEY` | Secret key for JWT token generation | `your-jwt-secret-key-here` |
| `SECRET_KEY` | General application secret key | `your-app-secret-key-here` |

### Docker Hub Secrets (For Docker deployment)

| Secret Name | Description |
|-------------|-------------|
| `DOCKERHUB_USERNAME` | Your Docker Hub username |
| `DOCKERHUB_TOKEN` | Your Docker Hub access token |

### Optional Secrets (Have defaults)

| Secret Name | Description | Default Value |
|-------------|-------------|---------------|
| `BUILDING_NAME` | Name of your building | `Elysia Apartments` |
| `BUILDING_ADDRESS` | Building address | `123 Main Street` |
| `BUILDING_CONTACT` | Contact information | `manager@elysiaapartments.com` |
| `SMART_HOME_API_URL` | Smart home integration API URL | _(none)_ |
| `SMART_HOME_API_KEY` | Smart home integration API key | _(none)_ |

## How to Set Up GitHub Secrets

1. Go to your GitHub repository
2. Click on **Settings** tab
3. In the left sidebar, click **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Add each secret with its name and value
6. Click **Add secret**

## Getting Required Values

### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key and add it as `OPENAI_API_KEY` secret

### JWT and Application Secret Keys
Generate secure random strings for:
- `JWT_SECRET_KEY`: Used for JWT token signing
- `SECRET_KEY`: Used for general application security

You can generate these using:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### Docker Hub Token
1. Log in to Docker Hub
2. Go to Account Settings → Security
3. Create a new access token
4. Use your username as `DOCKERHUB_USERNAME`
5. Use the token as `DOCKERHUB_TOKEN`

## Environment Variables in CI/CD

The GitHub workflow now automatically uses these secrets as environment variables during:

- **Testing phase**: All secrets are available as environment variables
- **Build phase**: Secrets are passed to Docker build as build arguments
- **Deployment phase**: Environment variables are set in the container

## Vercel Deployment

If deploying to Vercel, set these environment variables in your Vercel dashboard:
- `OPENAI_API_KEY`
- `JWT_SECRET_KEY`
- `SECRET_KEY`
- `BUILDING_NAME` (optional)
- `BUILDING_ADDRESS` (optional)
- `BUILDING_CONTACT` (optional)

## Security Notes

- Never commit secrets to your repository
- Use strong, randomly generated values for secret keys
- Rotate secrets regularly
- Limit access to secrets to necessary team members only
- The application works in demo mode without an OpenAI API key, but AI responses will be limited

## Troubleshooting

- If tests fail with authentication errors, check that `JWT_SECRET_KEY` is set
- If AI responses are limited, verify `OPENAI_API_KEY` is correctly configured
- If Docker build fails, ensure all required secrets are set in GitHub
- For Vercel deployment issues, check environment variables in Vercel dashboard