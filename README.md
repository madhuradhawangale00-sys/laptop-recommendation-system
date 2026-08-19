“Personalized Laptop Recommendation System Using Machine Learning and K-Nearest Neighbors”

              LAPTOP RECOMMENDER
                      │
        ┌─────────────┴─────────────┐
        │                           │
     Frontend                    ML Layer
        │                           │
    Streamlit                  Python
                                    │
                           ┌────────┼────────┐
                           │        │        │
                         Pandas   Scikit   NumPy
                                  Learn
                                    │
                              KNN / Scaling
                                    │
                              laptops.csv


User preferences → preprocessing → feature engineering → weighted/scaled features → KNN → similarity score → Top 5 recommendations → explanation of why each laptop was recommended

                 USER
                   |
                   ↓
        Enter Laptop Requirements
                   |
                   ↓
             Data Preprocessing
                   |
                   ↓
          Feature Transformation
                   |
                   ↓
          StandardScaler / Encoding
                   |
                   ↓
          KNN Recommendation Model
                   |
                   ↓
        Calculate Similarity/Distance
                   |
                   ↓
       Find K Nearest Laptops
                   |
                   ↓
          Rank Recommendations
                   |
                   ↓
        Top 5 Recommended Laptops


Our final Streamlit application will have something like:
╔══════════════════════════════════════╗
║       💻 LAPTOP RECOMMENDER           ║
╠══════════════════════════════════════╣
║                                      ║
║ Budget                               ║
║ ₹ [ 60000              ]             ║
║                                      ║
║ RAM                                  ║
║ [ 16 GB ▼ ]                          ║
║                                      ║
║ Storage                              ║
║ [ 512 GB ▼ ]                         ║
║                                      ║
║ Processor                            ║
║ [ Intel i5 ▼ ]                       ║
║                                      ║
║ GPU                                  ║
║ [ RTX 3050 ▼ ]                       ║
║                                      ║
║ Purpose                              ║
║ [ Gaming ▼ ]                         ║
║                                      ║
║       🔍 RECOMMEND LAPTOPS            ║
╚══════════════════════════════════════╝

Recommended Laptops
─────────────────────────────────────

🥇 ASUS TUF Gaming F15
₹59,990

16 GB RAM | 512 GB SSD
Intel i5 | RTX 3050
Similarity: 94.2%


🥈 Lenovo LOQ
₹62,990

16 GB RAM | 512 GB SSD
Intel i5 | RTX 3050
Similarity: 91.8%




Technology
Python
│
├── Pandas          → Dataset handling
├── NumPy           → Numerical operations
├── Scikit-learn    → KNN + preprocessing
├── Matplotlib      → Visualization
├── Seaborn         → Visualization
└── Streamlit       → Web interface



| Step | What we'll do                |
| ---- | ---------------------------- |
| 1    | Create project               |
| 2    | Get/create dataset           |
| 3    | Understand dataset           |
| 4    | Clean data                   |
| 5    | Feature engineering          |
| 6    | Convert categorical data     |
| 7    | Scale features               |
| 8    | Build KNN                    |
| 9    | Test recommendations         |
| 10   | Calculate similarity score   |
| 11   | Build Streamlit UI           |
| 12   | Improve recommendation logic |
| 13   | Add graphs                   |
| 14   | Test project                 |
| 15   | Prepare PPT/report/viva      |
