import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [review, setReview] = useState('');
  const [calificacion, setCalificacion] = useState('');

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
      <header className="bg-dark text-light p-3">
        <div className="container">
          <h1>Proyecto 1 Etapa 2</h1>
        </div>
      </header>
      <div className="container text-center flex-grow-1 d-flex justify-content-center align-items-center">
        <div className="w-100">
          <h2>Reseñas turísticas</h2>
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
                    className="btn btn-primary btn-lg btn-block"
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
        </div>
      </div>
    </div>
  );
}

export default App;
