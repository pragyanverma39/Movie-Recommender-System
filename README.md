# \# 🎬 Movie Recommendation System

# 

# A content-based movie recommendation system built with \*\*Python and Streamlit\*\* that recommends movies similar to a user's selected movie. The system uses preprocessed movie metadata and similarity scores to generate recommendations, while the \*\*TMDB API\*\* provides movie posters for a more visual experience.

# 

# \## 🚀 Features

# 

# \* 🎥 Select a movie from an interactive dropdown

# \* 🤖 Content-based movie recommendations

# \* 🔍 Finds the \*\*top 5 similar movies\*\*

# \* 🖼️ Fetches movie posters dynamically using the TMDB API

# \* ⚡ Interactive Streamlit interface

# \* 💾 Uses precomputed similarity data for fast recommendations

# \* 🔐 API key stored securely using Streamlit secrets

# 

# \## 🧠 How It Works

# 

# The recommendation system follows a content-based filtering approach.

# 

# ```text

# Movie Dataset

# &#x20;    ↓

# Preprocessed Movie Tags

# &#x20;    ↓

# Feature Representation

# &#x20;    ↓

# Cosine Similarity

# &#x20;    ↓

# Similarity Matrix

# &#x20;    ↓

# User Selects Movie

# &#x20;    ↓

# Find Similar Movies

# &#x20;    ↓

# Top 5 Recommendations

# &#x20;    ↓

# TMDB API → Movie Posters

# ```

# 

# The application loads the processed movie data and similarity matrix, identifies the selected movie, ranks other movies according to their similarity scores, and returns the five highest-ranked recommendations.

# 

# \## 🛠️ Tech Stack

# 

# | Technology    | Purpose                                       |

# | ------------- | --------------------------------------------- |

# | Python        | Core programming language                     |

# | Streamlit     | Web application interface                     |

# | Pandas        | Movie data processing                         |

# | NumPy         | Numerical operations                          |

# | Scikit-learn  | Feature processing and similarity calculation |

# | Requests      | TMDB API requests                             |

# | Pickle        | Storing and loading processed data            |

# | TMDB API      | Movie poster information                      |

# | Git \& Git LFS | Version control and large model storage       |

# 

# \## 📂 Project Structure

# 

# ```text

# Movie-Recommender-System/

# │

# ├── .streamlit/

# │   └── secrets.toml         

# ├── app.py                    # Main Streamlit application

# ├── movies.pkl                # Processed movie dataset

# ├── movies\_dict.pkl           # Movie data used by the application

# ├── similarity.pkl            # Precomputed similarity matrix

# ├── requirements.txt          # Python dependencies

# ├── .gitignore                # Ignored files and secrets

# └── .gitattributes            # Git LFS configuration

# ```

# 

# \## ⚙️ Installation

# 

# \### 1. Clone the repository

# 

# ```bash

# git clone https://github.com/pragyanverma39/Movie-Recommender-System.git

# cd Movie-Recommender-System

# ```

# 

# \### 2. Create a virtual environment

# 

# ```bash

# python -m venv .venv

# ```

# 

# Activate it on Windows:

# 

# ```bash

# .venv\\Scripts\\activate

# ```

# 

# \### 3. Install dependencies

# 

# ```bash

# pip install -r requirements.txt

# ```

# 

# \## 🔑 TMDB API Configuration

# 

# The application uses the TMDB API to retrieve movie poster information.

# 

# Create the following directory:

# 

# ```text

# .streamlit/

# ```

# 

# Inside it, create:

# 

# ```text

# secrets.toml

# ```

# 

# Add your own TMDB API key:

# 

# ```toml

# TMDB\_API\_KEY = "YOUR\_TMDB\_API\_KEY"

# ```

# 

# \*\*Never commit `secrets.toml` to GitHub.\*\*

# 

# The file is already excluded through `.gitignore`.

# 

# \## ▶️ Run the Application

# 

# After activating your virtual environment and configuring your TMDB API key:

# 

# ```bash

# streamlit run app.py

# ```

# 

# The application will be available at:

# 

# ```text

# http://localhost:8501

# ```

# 

# \## 🎯 Recommendation Method

# 

# The system uses a \*\*content-based filtering\*\* approach.

# 

# Movie information is represented through preprocessed tags containing information such as:

# 

# \* Plot/description

# \* Genres

# \* Keywords

# \* Cast

# \* Other movie-related metadata

# 

# The processed tags are transformed into numerical feature vectors, and \*\*cosine similarity\*\* is used to measure the similarity between movies.

# 

# For a selected movie, the system ranks similarity scores and returns the five most similar movies.

# 

# \## 🖼️ Movie Posters

# 

# Movie posters are retrieved dynamically from the \*\*TMDB API\*\* using each movie's TMDB movie ID.

# 

# If a poster is unavailable, the application displays a fallback placeholder.

# 

# \## 💾 Large Model File

# 

# The `similarity.pkl` file is a large precomputed similarity matrix and is therefore managed using \*\*Git LFS\*\*.

# 

# If you clone the repository and Git LFS is not installed, install it before working with the model file.

# 

# ```bash

# git lfs install

# git lfs pull

# ```

# 

# \## 🔮 Future Improvements

# 

# Potential improvements include:

# 

# \* ⭐ Movie ratings and reviews

# \* 🎭 Genre-based filtering

# \* 🔎 Search functionality

# \* 📊 Recommendation explanations

# \* 👤 Personalized recommendations

# \* 🎬 Movie details and trailers

# \* 🌐 Online deployment

# \* 📱 Improved responsive UI

# \* 🧠 More advanced recommendation algorithms

# \* 📈 Hybrid recommendation combining content-based and collaborative filtering

# 

# \## 📌 Project Status

# 

# \*\*Status:\*\* Completed — initial working version

# 

# The current version provides movie selection, content-based recommendations, and dynamically retrieved movie posters through TMDB.

# 

# \## 👨‍💻 Author

# 

# \*\*Pragyan Verma\*\*

# 

# GitHub:

# https://github.com/pragyanverma39

# 

# \---

# 

# ⭐ If you find this project useful, consider giving the repository a star!

