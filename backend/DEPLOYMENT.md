# Backend Deployment to Render

## 🚀 Quick Deploy to Render

### Option 1: Deploy from GitHub (Recommended)

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Prepare backend for Render deployment"
   git push origin main
   ```

2. **Connect to Render**:
   - Go to [render.com](https://render.com)
   - Click "New+" → "Web Service"
   - Connect your GitHub repository
   - Select the `backend` folder as the root directory

3. **Configure Service**:
   - **Name**: `ada-converter-api`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app.main:create_app() --bind 0.0.0.0:$PORT`

4. **Set Environment Variables**:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   DEBUG=False
   API_HOST=0.0.0.0
   ```

### Option 2: Use render.yaml (Infrastructure as Code)

1. The `render.yaml` file is already configured
2. Push to GitHub and Render will auto-detect the configuration
3. Set the `OPENAI_API_KEY` environment variable in the dashboard

## 📋 **Deployment Files Created**

- ✅ `requirements.txt` - Python dependencies
- ✅ `render.yaml` - Render configuration
- ✅ `start.sh` - Production startup script
- ✅ Updated CORS for production
- ✅ Port configuration for Render

## 🔧 **Production Configuration**

### Environment Variables
- `OPENAI_API_KEY` - Required: Your OpenAI API key
- `DEBUG` - Set to "False" for production
- `PORT` - Automatically set by Render
- `API_HOST` - Set to "0.0.0.0" for Render

### CORS Configuration
- Local development: `http://localhost:5173`
- Netlify deployments: `https://*.netlify.app`
- Production: Add your domain to `cors_origins` in `app/main.py`

## 🔗 **After Deployment**

1. Note your Render URL (e.g., `https://ada-converter-api.onrender.com`)
2. Update frontend API URL to point to this backend
3. Test the `/api/v1/convert` endpoint

## 📝 **Deployment Checklist**

- [ ] Repository pushed to GitHub
- [ ] Render service created and connected
- [ ] `OPENAI_API_KEY` environment variable set
- [ ] Service deployed successfully
- [ ] API endpoint accessible
- [ ] Frontend updated with backend URL
- [ ] End-to-end testing completed

## 🐛 **Troubleshooting**

### Common Issues:
1. **Build fails**: Check `requirements.txt` dependencies
2. **Import errors**: Ensure Python path is correct
3. **API key missing**: Verify environment variable is set
4. **CORS errors**: Update `cors_origins` with your frontend URL

### Logs:
- View logs in Render dashboard under "Logs" tab
- Check for startup errors and environment variable issues