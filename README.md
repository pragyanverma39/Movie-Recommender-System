# 🎬 Movie Recommendation System

A **content-based movie recommendation system** built with **Python and Streamlit** that recommends movies similar to a user's selected movie. The system uses preprocessed movie metadata and cosine similarity to generate recommendations, while the **TMDB API** dynamically provides movie posters for a more visual experience.

## 🚀 Features

* 🎥 Select a movie from an interactive dropdown
* 🤖 Content-based movie recommendations
* 🔍 Get the **top 5 similar movies**
* 🖼️ Fetch movie posters dynamically using the TMDB API
* ⚡ Interactive Streamlit interface
* 💾 Precomputed similarity matrix for fast recommendations
* 🔐 Secure API key management using Streamlit secrets

## 🧠 How It Works

The system uses a **content-based filtering** approach.

```text
Movie Dataset
     ↓
Preprocessed Movie Tags
     ↓
CountVectorizer
     ↓
Feature Vectors
     ↓
Cosine Similarity
     ↓
Similarity Matrix
     ↓
User Selects Movie
     ↓
Find Similar Movies
     ↓
Top 5 Recommendations
     ↓
TMDB API → Movie Posters
```

The application loads the processed movie data and precomputed similarity matrix. When a user selects a movie, the system identifies its position in the dataset, ranks other movies according to their similarity scores, and returns the five most similar movies.

## 🛠️ Tech Stack

| Technology    | Purpose                                     |
| ------------- | ------------------------------------------- |
| Python        | Core programming language                   |
| Streamlit     | Web application interface                   |
| Pandas        | Movie data processing                       |
| NumPy         | Numerical operations                        |
| Scikit-learn  | Feature vectorization and cosine similarity |
| Requests      | TMDB API requests                           |
| Pickle        | Storing and loading processed data          |
| TMDB API      | Movie poster information                    |
| Git & Git LFS | Version control and large model storage     |

## 📂 Project Structure

```text
Movie-Recommender-System/
│
├── .streamlit/
│   └── secrets.toml          
├── app.py                    # Main Streamlit application
├── movies.pkl                # Processed movie dataset
├── movies_dict.pkl           # Movie data used by the application
├── similarity.pkl            # Precomputed similarity matrix
├── requirements.txt          # Python dependencies
├── .gitignore                # Ignored files and secrets
└── .gitattributes            # Git LFS configuration
```

> **Note:** `.streamlit/secrets.toml` is a local configuration file and is intentionally excluded from GitHub to protect the TMDB API key.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/pragyanverma39/Movie-Recommender-System.git
cd Movie-Recommender-System
```

### 2. Install Git LFS

The `similarity.pkl` model file is large and is managed using Git LFS.

Install Git LFS if it is not already installed, then run:

```bash
git lfs install
git lfs pull
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 TMDB API Configuration

The application uses the **TMDB API** to retrieve movie poster information.

Create a `.streamlit` directory in the project root:

```text
.streamlit/
```

Inside the directory, create:

```text
secrets.toml
```

Add your own TMDB API key:

```toml
TMDB_API_KEY = "YOUR_TMDB_API_KEY"
```

The application reads the API key using Streamlit secrets.

**Never commit `secrets.toml` to GitHub.**

The file is already excluded through `.gitignore`.

## ▶️ Run the Application

After activating the virtual environment and configuring your TMDB API key, run:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## 🎯 Recommendation Method

The system uses **content-based filtering**.

Each movie contains preprocessed textual tags representing information such as:

* Plot and description
* Genres
* Keywords
* Cast
* Other movie-related metadata

These tags are converted into numerical feature vectors using **CountVectorizer**. The system then calculates **cosine similarity** between movie vectors.

When a user selects a movie:

1. The selected movie is located in the dataset.
2. Its similarity scores are retrieved from the precomputed similarity matrix.
3. Movies are ranked by similarity.
4. The top 5 similar movies are selected.
5. Their posters are retrieved using the TMDB API.

## 🖼️ Movie Posters

Movie posters are retrieved dynamically from the **TMDB API** using each movie's TMDB movie ID.

If a poster is unavailable, the application displays a fallback placeholder image.

## 💾 Large Model File

The `similarity.pkl` file contains the precomputed movie similarity matrix and is approximately **185 MB** in the repository's Git LFS storage.

Because the file exceeds GitHub's standard 100 MB Git file limit, it is managed using **Git Large File Storage (Git LFS)**.

If you clone the repository, make sure Git LFS is installed and run:

```bash
git lfs install
git lfs pull
```

## 🔮 Future Improvements

Potential improvements include:

* ⭐ Movie ratings and reviews
* 🎭 Genre-based filtering
* 🔎 Movie search functionality
* 📊 Recommendation explanations
* 👤 Personalized recommendations
* 🎬 Movie details and trailers
* 🌐 Online deployment
* 📱 Improved responsive UI
* 🧠 More advanced recommendation algorithms
* 📈 Hybrid recommendation using content-based and collaborative filtering

## 📌 Project Status

**Status: Completed — Initial Working Version**

The current version provides:

* Interactive movie selection
* Content-based movie recommendations
* Top 5 similar movie results
* Dynamically retrieved movie posters
* TMDB API integration
* Precomputed similarity matrix
* Streamlit-based user interface

## 👨‍💻 Author

**Pragyan Verma**

Movie Recommender System:
https://movie-recommender-system39.streamlit.app/

GitHub:
https://github.com/pragyanverma39

---

⭐ If you find this project useful, consider giving the repository a star!
