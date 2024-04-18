import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './style.css';

function App() {
  const [review, setReview] = useState('');
  const [calificacion, setCalificacion] = useState('');
  const [historialResenas, setHistorialResenas] = useState([]);

  useEffect(() => {
    // Simulando una solicitud a la API para obtener el historial de reseñas
    fetch('URL_DE_TU_API')
      .then(response => response.json())
      .then(data => {
        // Actualizar el estado con los datos recibidos del API
        setHistorialResenas(data);
      })
      .catch(error => console.error('Error al obtener el historial de reseñas:', error));
  }, []); // La dependencia vacía asegura que esta solicitud solo se realice una vez al cargar el componente

  const handleReviewChange = (event) => {
    setReview(event.target.value);
  };

  const handleReviewSubmit = () => {
    // Posteriormente aquí va la conexión con el API para calcular la calificación
    console.log('Reseña:', review);
    // Finalmente aquí se muestra la calificación de la reseña abajo en una caja aparte y grande la calificación que salió
  };

  return (
    <div className="App d-flex flex-column vh-100">
      <header className="bg-custom p-3">
        <div className="container">
          <h1>Análisis de recomendaciones turísticas</h1>
        </div>
      </header>
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
                    className="btn btn-warning btn-lg btn-block" // Cambio de color a amarillo
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
          <h2>Historial de reseñas</h2>
          <div className="row">
            <div className="col-lg-8 mx-auto">
              {historialResenas.length > 0 ? (
                <ul className="list-group">
                  {historialResenas.map((resena, index) => (
                    <li key={index} className="list-group-item">
                      {resena.reseña} - Calificación: {resena.calificación}
                    </li>
                  ))}
                </ul>
              ) : (
                <p>No hay reseñas disponibles.</p>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;