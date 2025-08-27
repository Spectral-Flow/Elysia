# Deploying Elysia to Vercel

This guide explains how to deploy the Elysia AI Concierge to Vercel.

## Prerequisites

1. A Vercel account
2. Vercel CLI installed: `npm i -g vercel`
3. OpenAI API key

## Environment Variables

Set these environment variables in your Vercel dashboard:

- `OPENAI_API_KEY`: Your OpenAI API key
- `JWT_SECRET_KEY`: A secret key for JWT token generation
- `SECRET_KEY`: A general secret key for the application
- `BUILDING_NAME`: Name of your building (optional, defaults to "Elysia Apartments")
- `BUILDING_ADDRESS`: Building address (optional)
- `BUILDING_CONTACT`: Contact information (optional)

## Deployment Steps

### Option 1: Deploy via Vercel CLI

1. Clone the repository
2. Navigate to the project directory
3. Run `vercel` and follow the prompts
4. Set environment variables when prompted

### Option 2: Deploy via Git Integration

1. Push the code to GitHub
2. Connect your repository to Vercel
3. Set environment variables in the Vercel dashboard
4. Deploy

## Project Structure for Vercel

```
/
├── api/                    # Serverless API functions
│   ├── chat.py            # Chat endpoint
│   ├── login.py           # Authentication
│   ├── maintenance.py     # Maintenance requests
│   ├── events.py          # Events listing
│   ├── building-info.py   # Building information
│   ├── health.py          # Health check
│   ├── shared.py          # Shared utilities
│   └── requirements.txt   # Python dependencies
├── frontend/              # React frontend
│   ├── src/               # React source code
│   ├── public/           # Static assets
│   ├── package.json      # Frontend dependencies
│   └── build/            # Built frontend (generated)
├── vercel.json           # Vercel configuration
└── package.json          # Root package.json for build commands
```

## API Endpoints

After deployment, your API endpoints will be available at:

- `https://your-app.vercel.app/api/chat` - Chat with AI
- `https://your-app.vercel.app/api/login` - User authentication
- `https://your-app.vercel.app/api/maintenance` - Submit maintenance requests
- `https://your-app.vercel.app/api/events` - Get events
- `https://your-app.vercel.app/api/building-info` - Building information
- `https://your-app.vercel.app/api/health` - Health check

## Frontend

The React frontend will be served from the root domain:
`https://your-app.vercel.app`

## Troubleshooting

1. **Build failures**: Check that all dependencies are properly listed in package.json files
2. **API errors**: Verify environment variables are set correctly
3. **CORS issues**: API functions include CORS headers for cross-origin requests
4. **Memory limits**: Vercel serverless functions have memory limits; optimize if needed

## Local Development

To test locally before deploying:

1. Install Vercel CLI: `npm i -g vercel`
2. Run `vercel dev` in the project directory
3. This will simulate the Vercel environment locally

## Production Considerations

1. **Database**: This setup uses in-memory storage. For production, integrate with a database like MongoDB, PostgreSQL, or Vercel's KV store.
2. **Authentication**: Implement proper user authentication system.
3. **Rate limiting**: Add rate limiting to API endpoints.
4. **Monitoring**: Set up monitoring and logging for production use.