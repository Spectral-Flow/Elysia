#!/bin/bash

# Elysia Vercel Deployment Test Script

echo "🚀 Testing Elysia Vercel deployment setup..."

# Check if we're in the right directory
if [ ! -f "vercel.json" ]; then
    echo "❌ Error: vercel.json not found. Please run this script from the project root."
    exit 1
fi

# Test frontend build
echo "📦 Building React frontend..."
cd frontend
npm ci
npm run build

if [ $? -eq 0 ]; then
    echo "✅ Frontend build successful"
else
    echo "❌ Frontend build failed"
    exit 1
fi

cd ..

# Test API functions
echo "🔧 Testing API functions..."
source venv/bin/activate 2>/dev/null || python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt > /dev/null

python test_api_functions.py

if [ $? -eq 0 ]; then
    echo "✅ API functions test passed"
else
    echo "❌ API functions test failed"
    exit 1
fi

# Test original Flask tests
echo "🧪 Running original test suite..."
python -m pytest tests/ -v

if [ $? -eq 0 ]; then
    echo "✅ All tests passed"
else
    echo "❌ Some tests failed"
    exit 1
fi

echo ""
echo "🎉 All tests passed! Your Elysia project is ready for Vercel deployment."
echo ""
echo "Next steps:"
echo "1. Install Vercel CLI: npm i -g vercel"
echo "2. Deploy to Vercel: vercel"
echo "3. Set environment variables in Vercel dashboard"
echo "4. Visit your deployed app!"
echo ""
echo "For detailed instructions, see VERCEL_DEPLOYMENT.md"