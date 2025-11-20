# 🚀 AI-Powered Resume & Job Description Skill Matcher

A full-stack AI-powered system that extracts skills from resumes and job descriptions, compares them using a **role-aware LLM-generated skill database**, and outputs:

- **Match Score (%)**
- **Matched Skills**
- **Missing Skills**
- **Extra Skills in Resume**
- **Role Skills (from LLM)**
- **JD Explicit Skills**

Built with:

- 🧠 **FastAPI** (backend)
- ⚛️ **React + Vite** (frontend)
- 🤖 **OpenAI GPT-4o / GPT-4o-mini** (skill generation)
- 📂 **skills_db.json** (local skill database)

---

## ✨ Features

- 🔍 Extracts skills from **PDF/TXT Resumes**
- 📄 Extracts skills from **Job Descriptions**
- 🤖 Automatically generates **role-based skillsets using LLMs**
- 🔄 Stores skills in a dynamic **skills_db.json** file
- 🔥 Matches **Resume Skills** against **Role + JD requirements**
- 🎯 Returns structured JSON scoring output
- 🌐 Full UI to upload resume, paste JD & select role
- 🛠 Works for **ANY job role** (not just software)

---

## 📁 Project Structure

```
resume-matcher/
├── backend/
│   ├── app/
│   │   ├── main.py               # FastAPI backend (APIs)
│   │   ├── nlp.py                # Skill extraction + scoring
│   │   ├── skill_builder.py      # LLM-powered skill generator
│   │   ├── skill_store.py        # Reads/writes skills_db.json
│   │   ├── utils.py              # PDF/TXT text extraction
│   ├── skills_db.json            # Auto-filled skill DB (initially {})
│   ├── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── App.jsx               # Main UI
    │   └── main.jsx
    ├── package.json
    ├── vite.config.js
```

---

# 🛠 Backend Installation (FastAPI)

### 1️⃣ Navigate to backend

```bash
cd backend
```

### 2️⃣ Create a virtual environment (recommended)

```bash
python3 -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
# .\venv\Scripts\activate
```

### 3️⃣ Install Python dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables (IMPORTANT)

Create:

```
backend/.env
```

Add:

```
OPENAI_API_KEY=your-openai-api-key-here
```

Or set via shell:

```bash
export OPENAI_API_KEY="your-openai-api-key-here"
```

---

# ▶️ Run the Backend

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend available at:

- http://localhost:8000  
- http://localhost:8000/docs (Swagger UI)

---

# 🧠 REQUIRED: Generate Skills for a Role

Before matching resumes, you **must generate skills** for the chosen job role.

### Steps:

1. Open: http://localhost:8000/docs  
2. Go to:

```
POST /api/generate-skills
```

3. Click **Try it out**  
4. Enter a role (example):

```
Software Engineer
```

5. Execute → The LLM generates 40–60 skills and stores them in:

```
backend/skills_db.json
```

---

# 🎨 Frontend Installation (React + Vite)

### 1️⃣ Navigate to frontend

```bash
cd frontend
```

### 2️⃣ Install dependencies

```bash
npm install
```

### 3️⃣ Start frontend dev server

```bash
npm run dev
```

Frontend runs at:

👉 http://localhost:5173

---

# 🔁 Connect Frontend to Backend

Create:

```
frontend/.env
```

Add:

```
VITE_API_BASE=http://localhost:8000
```

---

# 🧪 How to Use

### 1️⃣ Start backend  
### 2️⃣ Start frontend  
### 3️⃣ Go to frontend UI:

- Upload your **resume (PDF/TXT)**
- Paste the **job description**
- Select a **job role**
- Click **Analyze Match**

### 4️⃣ View results:

- Match Score (%)
- Matched Skills
- Missing Skills
- Extra resume skills
- Role skillset (LLM)
- JD explicit skills

---

# 🐛 Troubleshooting

### ❌ 422 Unprocessable Entity  
Frontend didn’t send all required fields (`resume`, `job_description`, `role`).

### ❌ Internal Server Error on `/api/generate-skills`  
Set your API key:

```
OPENAI_API_KEY=your-key
```

### ❌ skills_db.json is empty  
Run `/api/generate-skills` for your role.

