# Finntelligence Engine

**Personalized Loan Offer Engine with Profitability Optimization**

A sophisticated fintech ML system that optimizes loan offers by predicting default probability and customer acceptance rates to maximize profitability.

## Project Status
✅ **Phase 0: Complete** - Environment and project structure established  
✅ **Phase 1: Complete** - Data acquisition and exploratory analysis  
✅ **Phase 2: Complete** - Feature engineering and preprocessing  
✅ **Phase 3: Complete** - Risk model training and MLflow setup  
✅ **Phase 4: Complete** - Model registration and explainability  
🚀 **Current**: Migration to GitHub Codespaces  

## Quick Start

### 🚀 GitHub Codespaces (Recommended)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/huseyincavusbi/t)

1. Click the Codespaces badge above or create a new Codespace from your repository
2. Wait for the environment to set up automatically (2-3 minutes)
3. Run the quick setup: `./setup.sh`
4. Start exploring: `make notebook`

### 🖥️ Local Development
```bash
# Clone the repository
git clone https://github.com/huseyincaavusbi/t.git
cd t

# Set up environment
make setup

# Quick start
./setup.sh
```

### 📊 MLflow & Jupyter Access
```bash
make notebook    # Start Jupyter Lab (Port 8888)
make mlflow      # Start MLflow UI (Port 5000)
make help        # Show all available commands
```

## Architecture Overview

This system combines three key components:
1. **Default Risk Model**: Predicts P(Default) for loan applications
2. **Acceptance Model**: Predicts P(Acceptance) given interest rates
3. **Optimization Engine**: Maximizes expected profit per customer

## Project Structure
```
finntelligence-engine/
├── .devcontainer/          # GitHub Codespaces configuration
├── .github/workflows/      # CI/CD pipelines
├── src/                    # Core ML modules
│   ├── finntelligence/     # Main package
│   └── train_risk_model.py # Production training script
├── notebooks/              # Exploratory data analysis
├── data/                   # Data storage (versioned with DVC)
├── tests/                  # Unit and integration tests
├── models/                 # Trained model artifacts
├── configs/                # Configuration files
├── api/                    # FastAPI service endpoints
├── mlruns/                 # MLflow experiment tracking
├── Makefile               # Development commands
└── requirements.txt       # Python dependencies
```

## Development Workflow

### 🔄 Complete ML Pipeline
```bash
make full-pipeline    # Download data → Process → Train models
```

### 🧪 Individual Steps
```bash
make download-data    # Download Kaggle dataset
make process-data     # Feature engineering
make train-lr         # Train Logistic Regression
make train-xgb        # Train XGBoost
make test            # Run test suite
make lint            # Code quality checks
```

### 📈 Model Tracking & Visualization
- **MLflow UI**: Track experiments, compare models, register artifacts
- **SHAP Explanations**: Understand model decisions and feature importance
- **DVC**: Version control for data and model artifacts

## Data Setup

### Kaggle API Configuration
1. Get your API key from [Kaggle Account Settings](https://www.kaggle.com/account)
2. Create `~/.kaggle/kaggle.json`:
```json
{"username":"your_username","key":"your_api_key"}
```
3. Download data: `make download-data`

### DVC Remote Storage (Optional)
```bash
# Set up cloud storage for data versioning
dvc remote add -d storage s3://your-bucket/path
dvc push  # Upload data to remote
```

## Progress Status

✅ **Phase 0**: Project Setup & Environment  
✅ **Phase 1**: Data Acquisition & EDA  
✅ **Phase 2**: Feature Engineering & Preprocessing  
✅ **Phase 3**: Risk Model Training & MLflow Setup  
✅ **Phase 4**: Model Registration & Explainability  
🚀 **Phase 5**: GitHub Codespaces Migration (Current)  
🔄 **Phase 6**: Acceptance Probability Model (Next)  
📋 **Phase 7**: Profit Optimization Engine  
🌐 **Phase 8**: FastAPI Deployment  
🔧 **Phase 9**: CI/CD & Production Monitoring  

## 🛠️ MLOps Features

- ✅ **Experiment Tracking**: MLflow for model versioning and metrics
- ✅ **Data Versioning**: DVC for reproducible data pipelines  
- ✅ **Model Explainability**: SHAP for interpretable AI
- ✅ **Automated Testing**: pytest for code quality
- ✅ **CI/CD Pipeline**: GitHub Actions for automated deployment
- ✅ **Containerization**: Codespaces for consistent environments
- 🔄 **Model Registry**: Production model management
- 📋 **API Deployment**: FastAPI for model serving
- 📋 **Monitoring**: Performance and drift detection

## 📚 Documentation

- [Setup Guide](docs/setup.md) - Detailed environment setup
- [Data Guide](docs/data.md) - Dataset documentation  
- [Model Guide](docs/models.md) - Model architecture and training
- [API Guide](docs/api.md) - REST API documentation
- [Deployment Guide](docs/deployment.md) - Production deployment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make changes and test: `make test`
4. Commit changes: `git commit -m 'Add amazing feature'`
5. Push to branch: `git push origin feature/amazing-feature`
6. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
🔄 **Phase 5**: Profit Optimization Engine  
🔄 **Phase 6**: SHAP Explanations  
🔄 **Phase 7**: FastAPI Service & Deployment  

### Current Capabilities

**Risk Model (Default Prediction)**
- Models: Logistic Regression (baseline), XGBoost (performance)
- Metrics: ROC-AUC, Precision, Recall, F1-Score
- MLflow Integration: Full experiment tracking & model versioning
- Business Analysis: Risk threshold optimization

## Development Principles
- **Reproducibility**: Git + DVC + requirements.txt
- **Modularity**: Clean separation of concerns
- **Explainability**: SHAP integration for model interpretability
- **MLOps Ready**: CI/CD pipeline compatible design

## Quick Start

```bash
# 1. Activate environment
source finnt/bin/activate  # or your activation command

# 2. View MLflow experiments
mlflow ui
# Then open: http://localhost:5000

# 3. Run notebooks in sequence
jupyter notebook notebooks/
```

---
*Generated by Finnt AI Assistant - July 8, 2025*
