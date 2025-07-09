# Finntelligence Engine: A Personalized Loan Offer API

This project is an end-to-end MLOps implementation of a multi-model system that provides personalized, profit-optimized loan offers.

## MLOps Workflow Demonstrated

This project was built to showcase a robust MLOps workflow. The key practices implemented are:

*   **1. Experiment Tracking:** All model training runs were logged to an **MLflow Tracking Server**. This captured parameters, metrics, and model artifacts for every experiment, ensuring full traceability and comparability.

*   **2. Data & Model Versioning:** Large data files and models were versioned using **DVC (Data Version Control)**. This allows us to tie specific model versions back to the exact data they were trained on, ensuring perfect reproducibility without committing large files to Git.

*   **3. Model Registry:** The best-performing models from our experiments were promoted to a formal **MLflow Model Registry**. This centralized, versioned artifact store manages the model lifecycle from "Staging" to "Production."

*   **4. Code Refactoring & Modularity:** Initial exploration was done in Jupyter Notebooks, but all final logic (data processing, model training, API serving) was refactored into modular Python scripts within the `src/` directory.

*   **5. Model Serving as a Service:** The final engine, which integrates both the Risk and Acceptance models, is served via a **FastAPI** REST endpoint. This decouples the model logic from any single application and makes it available as a callable service.

*   **6. Dependency and Environment Management:** The project environment is managed by `uv` and all dependencies are pinned in a `requirements.txt` file, ensuring a consistent and reproducible setup.

## System Architecture

The Finntelligence Engine consists of two complementary models:

- **Risk Assessment Model**: Predicts the probability of loan default based on customer characteristics
- **Acceptance Prediction Model**: Estimates the likelihood of loan offer acceptance based on terms and customer profile

These models work together to optimize loan offers by balancing risk exposure with acceptance probability.

## Project Structure

```
finnt/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── .gitignore                  # Git ignore rules
├── data/                       # Data management
│   ├── raw/                    # Original datasets (DVC tracked)
│   ├── processed/              # Processed data (DVC tracked)
│   └── external/               # External data sources (if any)
├── notebooks/                  # Jupyter notebooks for exploration
│   ├── 01-EDA-and-Data-Cleaning.ipynb
│   ├── 02-Feature-Engineering.ipynb
│   ├── 03-Risk-Model-Training.ipynb
│   ├── 04-Model-Registration-and-Explainability.ipynb
│   └── 05-Acceptance-Model-Training.ipynb
├── src/                        # Production code
│   ├── main_api.py             # FastAPI application
│   ├── schemas.py              # Pydantic models
│   ├── train_risk_model.py     # Risk model training
│   └── finntelligence/         # Core package
├── models/                     # Local model artifacts
├── mlruns/                     # MLflow experiment tracking
├── scripts/                    # Utility scripts
```

## API Endpoints

The FastAPI server provides the following endpoints:

- `GET /`: Health check and system status
- `POST /predict`: Generate optimized loan offers
- `GET /docs`: Interactive API documentation (Swagger UI)

## MLOps Features Implemented

### Experiment Tracking
- **MLflow Tracking**: All training runs logged with parameters, metrics, and artifacts
- **Reproducible Experiments**: Consistent random seeds and environment management
- **Comparative Analysis**: Easy comparison of different model configurations

### Model Management
- **MLflow Model Registry**: Centralized model versioning and lifecycle management
- **Staging Workflow**: Models promoted from development to staging to production
- **Model Lineage**: Full traceability from data to deployed model

### Data Management
- **DVC Integration**: Large files tracked without bloating Git repository
- **Data Versioning**: Reproducible data pipelines with version control
- **Automated Processing**: Scripted data transformation and feature engineering

### Deployment & Serving
- **FastAPI Framework**: REST API with automatic documentation
- **Model Loading**: Dynamic model loading from MLflow registry
- **Error Handling**: Robust error handling and validation

## Development Workflow

1. **Data Exploration**: Initial analysis in Jupyter notebooks
2. **Feature Engineering**: Systematic feature development and selection
3. **Model Training**: Iterative model development with MLflow tracking
4. **Model Registration**: Promotion of best models to registry
5. **Code Refactoring**: Production-ready code in modular structure
6. **API Development**: FastAPI service for model serving
7. **Testing & Validation**: Comprehensive testing of all components

## Key Technologies

- **Machine Learning**: XGBoost, Scikit-learn, SHAP
- **MLOps**: MLflow, DVC
- **API Framework**: FastAPI, Uvicorn
- **Data Processing**: Pandas, NumPy
- **Environment Management**: uv, pip
- **Visualization**: Matplotlib, Seaborn

## License

This project is licensed under the MIT License - see the LICENSE file for details.