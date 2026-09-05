# Deployment Guide: Student Management System

This project is configured with **Vercel** (`vercel.json`), **Gunicorn**, **WhiteNoise**, and production-ready Django settings for one-click deployment.

---

## ⚡ Option 1: Deploy on Vercel (Fast & Global)

### Step 1: Push project to GitHub
```bash
git init
git add .
git commit -m "Configure Vercel and production deployment"
git branch -M main
git remote add origin https://github.com/<your-username>/student-management-system.git
git push -u origin main
```

### Step 2: Import to Vercel
1. Go to [https://vercel.com/dashboard](https://vercel.com/dashboard) and click **Add New...** ➔ **Project**.
2. Select your `student-management-system` GitHub repository.
3. Framework Preset: Leave as **Other**.
4. In **Environment Variables**, add:
   - `DEBUG` = `False`
   - `SECRET_KEY` = `<your-random-secret-key>`
5. Click **Deploy**.
   - Vercel will build the serverless functions via [`vercel.json`](file:///d:/seeluu/vercel.json) and provide you with an instant live URL (`https://your-project.vercel.app`)!

---

## 🚀 Option 2: Deploy on Render.com (Recommended for SQLite persistence)

### Step 1: Push project to GitHub
```bash
git push -u origin main
```

### Step 2: Create Web Service on Render
1. Go to [https://dashboard.render.com/](https://dashboard.render.com/) and click **New +** -> **Web Service**.
2. Connect your GitHub repository.
3. Settings:
   - **Name:** `student-management-system`
   - **Environment:** `Python 3`
   - **Branch:** `main`
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn student_management.wsgi --log-file -`
   - **Plan:** `Free`
4. In **Environment Variables**:
   - `DEBUG` = `False`
   - `ALLOWED_HOSTS` = `.onrender.com,localhost,127.0.0.1`
5. Click **Create Web Service**.

---

## 🐍 Option 3: Deploy on PythonAnywhere

1. Create a free account at [https://www.pythonanywhere.com/](https://www.pythonanywhere.com/).
2. Open a **Bash Console** and clone your repository:
   ```bash
   git clone https://github.com/<your-username>/student-management-system.git
   cd student-management-system
   virtualenv --python=python3.10 venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py seed_students
   python manage.py collectstatic
   ```
3. Go to the **Web** tab, configure the WSGI file, set static files mapping to `staticfiles`, and reload.

---

## 🚂 Option 4: Deploy on Railway.app

1. Go to [https://railway.app/](https://railway.app/).
2. Click **New Project** -> **Deploy from GitHub repo**.
3. Select your repository. Railway automatically runs your `Procfile`.
