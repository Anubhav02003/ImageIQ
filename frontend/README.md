# ImageIQ: Visual Question Answering Web App

ImageIQ is a full-stack web application that lets users upload an image, ask a question about it, and get an AI-generated answer.  
The backend uses FastAPI and the BLIP VQA model; the frontend is built with React (Vite).

---

## Features

- Upload any image and ask a question about it
- AI answers questions using Salesforce BLIP VQA model
- FastAPI backend with easy REST API
- Modern React frontend
- Easy local development

---

## Project Structure

ImageIQ/
├── backend/
│   └── app/
│       ├── main.py
│       ├── model.py
│       └── __init__.py
└── frontend/
    ├── package.json
    └── src/
        └── App.jsx

---

## Prerequisites

- **Python 3.8+**
- **Node.js & npm** (https://nodejs.org/)
- **Git** (optional, for version control)

---

## 1. Backend Setup (FastAPI + BLIP)

### a. Create and activate a Python virtual environment

cd backend
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

### b. Install dependencies

pip install fastapi uvicorn transformers torch pillow

### c. File structure

- main.py — FastAPI app (API endpoints, CORS)
- model.py — VQA model code

### d. Run the backend

uvicorn app.main:app --reload

- The API will be available at http://127.0.0.1:8000
- Test the API docs at http://127.0.0.1:8000/docs

---

## 2. Frontend Setup (React + Vite)

### a. Install dependencies

cd ../frontend
npm install

### b. Start the frontend dev server

npm run dev

- The app will be available at http://localhost:5173

---

## 3. Usage

1. Make sure both backend and frontend servers are running.
2. Open http://localhost:5173 in your browser.
3. Upload an image, enter your question, and click **Ask**.
4. The answer will appear below the form.

---

## 4. Troubleshooting

- **CORS Error:**  
  Make sure your FastAPI backend includes the following in main.py:

  from fastapi.middleware.cors import CORSMiddleware

  app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],  # Or ["http://localhost:5173"]
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
  )

  Restart the backend after editing.

- **Network Error:**  
  - Confirm both servers are running.
  - Check that the backend URL in your frontend code matches the backend server address and port.

- **Model Download Slow:**  
  The BLIP model will download the first time you run the backend. Be patient!

---

## 5. Customization

- To use a different VQA model, update the model loading code in model.py.
- To improve the UI, edit frontend/src/App.jsx and add your own styles or components.

---

## 6. License

This project is for educational and research purposes.

---

## 7. Credits

- FastAPI (https://fastapi.tiangolo.com/)
- React (https://react.dev/)
- Salesforce BLIP VQA Model (https://huggingface.co/Salesforce/blip-vqa-base)
- Vite (https://vitejs.dev/)

---

## 8. Author

Developed by Anubhav Pratap Singh

---
