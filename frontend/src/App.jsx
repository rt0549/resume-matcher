import { useState } from "react";

const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

function App() {
  const [resumeFile, setResumeFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [role, setRole] = useState("");  // NEW
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setResult(null);

    if (!resumeFile || !jobDescription.trim() || !role) {
      setError("Please upload a resume, paste the JD, and select a role.");
      return;
    }

    const formData = new FormData();
    formData.append("resume", resumeFile);
    formData.append("job_description", jobDescription);
    formData.append("role", role);  // NEW

    try {
      setLoading(true);
      const res = await fetch(`${API_BASE}/api/match`, {
        method: "POST",
        body: formData,
      });

      if (!res.ok) {
        throw new Error("Server error");
      }

      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.log(err);
      setError("Something went wrong. Check backend logs.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px", maxWidth: "800px", margin: "auto" }}>
      <h1>Resume vs Job Description Matcher</h1>

      <form onSubmit={handleSubmit} style={{ marginTop: "20px" }}>

        {/* ROLE DROPDOWN */}
        <label><strong>Select Job Role:</strong></label>
        <select 
          value={role} 
          onChange={(e) => setRole(e.target.value)} 
          style={{ width: "100%", padding: "8px", marginTop: "8px" }}
        >
          <option value="">-- Select a role --</option>
          <option value="Software Engineer">Software Engineer</option>
          <option value="Backend Engineer">Backend Engineer</option>
          <option value="Data Engineer">Data Engineer</option>
          <option value="Database Administrator">Database Administrator</option>
          <option value="DevOps Engineer">DevOps Engineer</option>
          <option value="Cloud Engineer">Cloud Engineer</option>
          <option value="Machine Learning Engineer">Machine Learning Engineer</option>
          <option value="Site Reliability Engineer">Site Reliability Engineer</option>
        </select>

        <br /><br />

        <label><strong>Upload Resume (PDF/TXT):</strong></label>
        <input
          type="file"
          onChange={(e) => setResumeFile(e.target.files[0])}
        />

        <br /><br />

        <label><strong>Paste Job Description:</strong></label><br />
        <textarea
          rows="8"
          style={{ width: "100%" }}
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
        ></textarea>

        <br /><br />

        <button type="submit" style={{ padding: "10px 20px" }}>
          {loading ? "Analyzing…" : "Analyze Match"}
        </button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {/* RESULTS */}
      {result && (
        <div style={{ marginTop: "30px" }}>
          <h2>Match Score: {result.match_score}%</h2>

          <h3>Matched Skills:</h3>
          <p>{result.matched_keywords.join(", ")}</p>

          <h3>Missing Skills:</h3>
          <p>{result.missing_keywords.join(", ")}</p>

          <h3>Extra Skills from Resume:</h3>
          <p>{result.extra_keywords_in_resume.join(", ")}</p>

          <h3>Role Skills (from LLM DB):</h3>
          <p>{result.role_skills.join(", ")}</p>

          <h3>JD Explicit Skills:</h3>
          <p>{result.jd_explicit_skills.join(", ")}</p>
        </div>
      )}
    </div>
  );
}

export default App;
