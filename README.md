# 🏢 EcoOptimize AI - Intelligent Energy Management

![EcoOptimize AI Header](https://picsum.photos/seed/smartcity/800/300)

**EcoOptimize AI** is a machine-learning-driven platform that integrates seamlessly with Building Management Systems (BMS) to dynamically adjust HVAC and lighting based on real-time occupancy and weather data, reducing commercial building energy waste by up to 30%. This project is being built for the **Yuva Yodha Energy Tech Hackathon 2026**.

## 💡 The Problem
Nearly 40% of global energy goes into commercial buildings, and up to 30% of it is wasted due to rigid, static heating and lighting schedules. This puts an enormous pressure on energy grids and drives unnecessary Scope 2 carbon emissions.

## 🚀 The Solution (Edge AI)
Instead of relying on cloud data centers which introduce latency and privacy concerns, EcoOptimize uses **Privacy-First Edge AI** (e.g. Snapdragon NPU architecture). 
By ingesting IoT occupancy sensor streams and hyperlocal weather forecasts, it uses reinforcement learning to intelligently set HVAC temperature targets and dim lighting—all handled instantaneously on-site.

## ⚙️ Features
- **Real-Time Interactive Dashboard**: Built with Streamlit to monitor energy consumption and predicted savings.
- **Localized Inference**: Core ML inference happens on-device.
- **Dynamic Set-Points**: Algorithms automatically replace human-configured rigid BMS schedules.

## 🛠️ Tech Stack
- **Dashboard UI**: Python (Streamlit), Plotly
- **Data Manipulation**: Pandas, NumPy
- **Edge ML Concepts**: TinyML, TensorFlow Lite (Simulated)

## 💻 Running the Prototype Locally

To run the Streamlit dashboard simulation:

```bash
# 1. Clone the repository
git clone https://github.com/Pushyami45/EcoOptimize-AI.git

# 2. Navigate to directory
cd EcoOptimize-AI

# 3. Install requirements
pip install -r requirements.txt

# 4. Run the Streamlit Dashboard
streamlit run app.py
```

## 📈 Impact
- Flattened energy demand curves for grid operators.
- 20-30% HVAC energy cost reduction for building managers.
- Accelerated decarbonization of commercial real estate.

---
*Developed by Pushyami Reddy for the 2026 Yuva Yodha Hackathon.*
