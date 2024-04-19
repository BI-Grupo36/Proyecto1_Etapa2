import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './style.css';

function App() {
  const [review, setReview] = useState('');
  const [calificacion, setCalificacion] = useState('');
  const [historialResenas, setHistorialResenas] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchHistorialResenas();
  }, []);

  const fetchHistorialResenas = async () => {
    try {
      const response = await fetch('http://localhost:8000/reviews/');
      const data = await response.json();
      setHistorialResenas(data);
    } catch (error) {
      console.error('Error al obtener el historial de reseñas:', error);
    }
  };

  const handleReviewChange = (event) => {
    setReview(event.target.value);
  };

  const handleReviewSubmit = async () => {
    try {
      if (!review) {
        return;
      }
  
      const response = await fetch('http://localhost:8000/reviews', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: review,
        }),
      });
      const data = await response.json();
  
      if (response.ok) {
        if (data.score !== undefined) {
          setCalificacion(data.score);
        } else {
          setCalificacion('No se pudo clasificar');
        }
      } else {
        console.error('Error al clasificar la reseña:', data.error);
      }

      fetchHistorialResenas();
    } catch (error) {
      console.error('Error al clasificar la reseña:', error);
    }
  };
  
  const handleCSVSubmit = async (event) => {
    try {
      const file = event.target.files[0];
      if (!file) return;
  
      const formData = new FormData();
      formData.append('file', file);
  
      setLoading(true);
      const response = await fetch('http://localhost:8000/reviews/file', {
        method: 'POST',
        body: formData,
      });
  
      if (response.ok) {
        const data = await response.json();
        if (data.reviews && data.reviews.length > 0) {
          setHistorialResenas(data.reviews);
        } else {
          console.log('No se encontraron reseñas en el archivo CSV');
        }
      } else {
        console.error('Error al cargar el archivo CSV:', response.statusText);
      }
  
      setLoading(false);
    } catch (error) {
      console.error('Error al cargar el archivo CSV:', error);
      setLoading(false);
    }
  };

  const clearHistorialResenas = async () => {
    try {
      const response = await fetch('http://localhost:8000/reviews/', {
        method: 'DELETE',
      });
      if (response.ok) {
        setHistorialResenas([]);
      } else {
        console.error('Error al limpiar el historial de reseñas:', response.statusText);
      }
    } catch (error) {
      console.error('Error al limpiar el historial de reseñas:', error);
    }
  };

  return (
    <div className="App d-flex flex-column vh-100">
      <header className="bg-custom p-3">
        <div className="container">
          <h1>Análisis de recomendaciones turísticas</h1>
        </div>
      </header>
      <div className="my-3"></div>
      <div className="container text-center flex-grow-1 d-flex justify-content-center align-items-center">
        <div className="w-100">
          <h2>Nueva reseña turística</h2>
          <div className="row">
            <div className="col-lg-8 mx-auto">
              <div className="card">
                <div className="card-body">
                  <textarea
                    className="form-control mb-3"
                    placeholder="Ingrese su reseña"
                    value={review}
                    onChange={handleReviewChange}
                    rows="5"
                  />
                  <button
                    className="btn btn-warning btn-lg btn-block"
                    onClick={handleReviewSubmit}
                  >
                    Calificar reseña
                  </button>
                </div>
              </div>
              {calificacion && (
                <div className="mt-3">
                  <p>Calificación: {calificacion}</p>
                </div>
              )}
            </div>
          </div>
          <div className="my-5"></div>
          <h2>Calificar archivo CSV</h2>
          <div className="row">
            <div className="col-lg-8 mx-auto">
              <div className="input-group mb-3">
                <input
                  type="file"
                  accept=".csv"
                  className="form-control"
                  onChange={handleCSVSubmit}
                />
                <button
                  className="btn btn-warning"
                  type="button"
                  onClick={handleCSVSubmit}
                  disabled={loading}
                >
                  {loading ? 'Cargando...' : 'Calificar CSV'}
                </button>
              </div>
            </div>
          </div>
          <div className="my-5"></div>
          <h2>Historial de reseñas</h2>
          <div className="row">
            <div className="col-lg-8 mx-auto">
              <div>
                <button
                  className="btn btn-danger mb-3"
                  onClick={clearHistorialResenas}
                >
                  Limpiar historial de reseñas
                </button>
              </div>
              <ul className="list-group">
                {historialResenas.map((resena) => (
                  <li key={resena.id} className="list-group-item">
                    {resena.text} - Calificación: {resena.score}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
