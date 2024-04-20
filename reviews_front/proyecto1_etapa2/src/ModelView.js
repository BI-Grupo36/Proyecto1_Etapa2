import React from 'react';
import { Link } from 'react-router-dom';
import modeloImg from './modelo.jpg';

function ModelView() {
  return (
    <div className="App d-flex flex-column vh-100">
      <header className="bg-custom p-3">
        <div className="container">
          <h1>Modelo Seleccionado</h1>
        </div>
      </header>
      <div className="my-3"></div>
      <div className="container text-center flex-grow-1 d-flex justify-content-center align-items-center">
        <div className="w-100">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Modelo de Support Vector Machine (SVM)</h5>
              <p className="card-text">
                El SVM (Support Vector Machine) con kernel lineal es un algoritmo de aprendizaje supervisado utilizado principalmente para la clasificación de datos. Su característica distintiva radica en su capacidad para separar de manera óptima conjuntos de datos linealmente no separables en un espacio dimensional superior. Esto se logra mediante la transformación de los datos a un espacio de características de mayor dimensión donde sí puedan ser separados linealmente.
                <br />
                <a href="https://github.com/BI-Grupo36/Proyecto1_Etapa1/blob/main/Proyecto1_Etapa1.ipynb" target="_blank" rel="noopener noreferrer">Más información sobre el modelo en GitHub</a>
              </p>
              <div className="row">
                <div className="col-md-6">
                  <img src={modeloImg} className="img-fluid" alt="Foto del modelo" />
                </div>
                <div className="col-md-6">
                  <h6 className="card-subtitle mb-2 text-muted">Métricas del modelo:</h6>
                  <ul className="list-group">
                    <li className="list-group-item">Accuracy: 0.5077</li>
                    <li className="list-group-item">Precision: 0.4987</li>
                    <li className="list-group-item">Recall: 0.5077</li>
                    <li className="list-group-item">F1-Score: 0.4966</li>
                  </ul>
                </div>
              </div>
              <Link to="/" className="btn btn-warning mt-3">Volver a Reseñas</Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ModelView;
