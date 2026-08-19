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