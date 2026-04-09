import { useEffect, useState } from "react";

// Dev: Vite proxies /api -> backend (same origin, no CORS). Override with VITE_API_URL if needed.
const API_BASE =
  import.meta.env.VITE_API_URL ??
  (import.meta.env.DEV ? "/api" : "http://127.0.0.1:8000");

function App() {
  const [workers, setWorkers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    setError(null);
    fetch(`${API_BASE}/workers`)
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then((data) => {
        setWorkers(Array.isArray(data) ? data : []);
      })
      .catch((err) => {
        console.error("Failed to load workers:", err);
        setError(err.message || "Request failed");
      })
      .finally(() => setLoading(false));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Construction Payroll</h1>

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
            KES {worker.daily_rate}
          </div>
        ))
      ) : null}
    </div>
  );
}

export default App;