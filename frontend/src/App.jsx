import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [image, setImage] = useState(null);
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);

  const handleImageChange = (e) => {
    setImage(e.target.files[0]);
  };

  const handleQuestionChange = (e) => {
    setQuestion(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!image || !question) {
      alert('Please select an image and enter a question.');
      return;
    }
    setLoading(true);
    const formData = new FormData();
    formData.append('image', image);
    formData.append('question', question);

    try {
      const response = await axios.post('http://127.0.0.1:8000/vqa/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setAnswer(response.data.answer);
    } catch (error) {
      setAnswer('Error: ' + (error.response?.data?.error || error.message));
    }
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 500, margin: 'auto', padding: 20 }}>
      <h2>Visual Question Answering</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleImageChange} />
        <br /><br />
        <input
          type="text"
          placeholder="Enter your question about the image"
          value={question}
          onChange={handleQuestionChange}
          style={{ width: '100%', padding: 8 }}
        />
        <br /><br />
        <button type="submit" disabled={loading}>
          {loading ? 'Processing...' : 'Ask'}
        </button>
      </form>
      {answer && (
        <div style={{ marginTop: 20 }}>
          <strong>Answer:</strong> {answer}
        </div>
      )}
    </div>
  );
}

export default App;
