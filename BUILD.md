# Build Instructions

## Overview

This project uses Vercel for deployment with a React frontend and Python API backend.

## Frontend Build

The frontend is a React application that must be built before deployment.

### Local Development
```bash
cd frontend
npm ci
npm start
```

### Production Build
```bash
cd frontend
npm ci
npm run build
```

## Deployment

### Vercel Configuration

The `vercel.json` file is configured to:
1. Build the frontend automatically: `"buildCommand": "cd frontend && npm ci && npm run build"`
2. Serve static files from: `"outputDirectory": "frontend/build"`
3. Handle API routes with Python functions in the `api/` directory

### Important Notes

- The `frontend/build/` directory is ignored by git (in `.gitignore`) but **must not** be ignored by Vercel
- The `.vercelignore` file should NOT include `frontend/build/` to ensure built files are deployed
- API functions in the `api/` directory are deployed as serverless functions

## Troubleshooting

### 404 NOT_FOUND Error

If you encounter a 404 error when accessing the application:

1. **Check if frontend is built**: Ensure `frontend/build/index.html` exists
2. **Verify .vercelignore**: Make sure `frontend/build/` is not listed in `.vercelignore`
3. **Check build command**: Verify the build command in `vercel.json` completes successfully
4. **Review Vercel logs**: Check deployment logs for build failures

### Common Issues

- **Missing dependencies**: Run `npm ci` in the frontend directory
- **Build failures**: Check for syntax errors in React components
- **API not working**: Verify Python dependencies are installed and API functions are properly formatted

## Testing

Run the test suite to ensure everything works:

```bash
# Install Python dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/ -v

# Test API functions
python test_api_functions.py
```