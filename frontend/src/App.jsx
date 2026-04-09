import { useEffect, useState } from "react";

// Dev: Vite proxies /api -> backend (same origin, no CORS).
const API_BASE =
  import.meta.env.VITE_API_URL ??
  (import.meta.env.DEV ? "/api" : "http://127.0.0.1:8000");

function App() {
  const [workers, setWorkers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [form, setForm] = useState({
    name: "",
    phone: "",
    skill: "",
    daily_rate: "",
  });

  const loadWorkers = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(`${API_BASE}/workers`);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      setWorkers(Array.isArray(data) ? data : []);
    } catch (err) {
      console.error("Failed to load workers:", err);
      setError(err.message || "Request failed");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadWorkers();
  }, []);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const addWorker = async () => {
    try {
      const res = await fetch(`${API_BASE}/workers`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          ...form,
          daily_rate: parseFloat(form.daily_rate),
        }),
      });

      if (!res.ok) throw new Error("Failed to add worker");

      setForm({
        name: "",
        phone: "",
        skill: "",
        daily_rate: "",
      });

      await loadWorkers();
    } catch (err) {
      console.error(err);
      setError("Failed to add worker");
    }
  };

  const markAttendance = async (worker_id) => {
    try {
      await fetch(`${API_BASE}/attendance`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          worker_id: worker_id,
          date: new Date().toISOString().split("T")[0],
          status: "present"
        })
      });
  
      alert("Attendance marked!");
  
    } catch (err) {
      console.error(err);
      setError("Failed to mark attendance");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Construction Payroll</h1>

      <h2>Add Worker</h2>
      <input
        name="name"
        placeholder="Name"
        value={form.name}
        onChange={handleChange}
      />
      <input
        name="phone"
        placeholder="Phone"
        value={form.phone}
        onChange={handleChange}
      />
      <input
        name="skill"
        placeholder="Skill"
        value={form.skill}
        onChange={handleChange}
      />
      <input
        name="daily_rate"
        placeholder="Daily Rate"
        value={form.daily_rate}
        onChange={handleChange}
      />
      <button onClick={addWorker} style={{ marginTop: "10px" }}>
        Add Worker
      </button>

      <h2>Workers</h2>

      {loading && <p>Loading…</p>}
      {error && (
        <p style={{ color: "crimson" }}>
          Could not load workers ({error}). Is the API running on port 8000?
        </p>
      )}
      {!loading && !error && workers.length === 0 ? (
        <p>No workers found</p>
      ) : !loading && !error ? (
        workers.map((worker) => (
          <div key={worker.id} style={{
            background: "#f2f2f2",
            padding: "10px",
            margin: "10px 0",
            borderRadius: "8px"
          }}>
            <b>{worker.name}</b><br />
            {worker.skill}<br />
            KES {worker.daily_rate}<br /><br />
        
            <button onClick={() => markAttendance(worker.id)}>
              Mark Present
            </button>
          </div>
        ))
      ) : null}
    </div>
  );
}

export default App;