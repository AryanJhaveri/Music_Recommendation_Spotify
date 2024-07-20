
# Song Recommendation System

This project collects data from Spotify playlists and builds a music recommendation system. The recommendation system suggests songs based on the input song name using cosine similarity.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
  - [Data Collection](#data-collection)
  - [Running the Recommendation System](#running-the-recommendation-system)
  - [Running the Web Application](#running-the-web-application)
- [Project Files Explanation](#project-files-explanation)
  - [`get_token.py`](#get_tokenpy)
  - [`spotify_data.py`](#spotify_datapy)
  - [`get_playlist.py`](#get_playlistpy)
  - [`main.py`](#mainpy)
  - [`app.py`](#apppy)
  - [`recommendation_system.ipynb`](#recommendation_systemipynb)

## Project Structure

- `app.py`: Flask web application to provide a simple user interface for the recommendation system.
- `get_playlist.py`: Script to collect data from multiple Spotify playlists.
- `get_token.py`: Script to obtain an access token from the Spotify API.
- `main.py`: Main script to orchestrate the data collection and save it to a CSV file.
- `spotify_data.py`: Script to fetch and process playlist data from Spotify.
- `recommendation_system.ipynb`: Jupyter Notebook to build and evaluate the recommendation system.
- `templates/`: Directory containing HTML templates for the web interface.

## Installation and Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/spotify-recommendation-system.git
   cd spotify-recommendation-system
   
2. Install the required Python packages:

   ```sh
   pip install pandas spotipy flask

4. Obtain Spotify API credentials by creating an application in the Spotify Developer Dashboard.

5. Update the get_token.py file with your Spotify API CLIENT_ID and CLIENT_SECRET.


## Usage

### Data Collection

1. Open the `main.py` file and update the list of `playlist_ids` with the Spotify playlist IDs you want to collect data from.

2. Run the `main.py` script to collect data from the specified playlists and save it to `playlist_data.csv`:

   ```sh
   python main.py

### Running the Recommendation System

1. Open the recommendation_system.ipynb notebook.

2. Load the data and run through the cells to build and evaluate the recommendation system.

### Running the Web Application

1. Run the Flask app to start the web server:

   ```sh
   python app.py

2. Open your web browser and go to http://127.0.0.1:5000/.

3. Enter the name of a song in the input field and click the "Recommend" button to get song recommendations.

## Project Files Explanation

### `get_token.py`
This script obtains an access token from the Spotify API. The token is required to make authenticated requests to the Spotify Web API.

### `spotify_data.py`
This script fetches data from a Spotify playlist, including track details, album information, and audio features. It uses the Spotipy library to interact with the Spotify API.

### `get_playlist.py`
This script collects data from multiple Spotify playlists by calling the `get_trending_playlist_data` function from `spotify_data.py`. It combines the data into a single DataFrame and saves it to a CSV file.

### `main.py`
This is the main script that orchestrates the data collection process. It uses `get_token.py` to get an access token and `get_playlist.py` to collect data from specified playlists.

### `app.py`
This is the Flask web application that provides a simple user interface for the recommendation system. It allows users to input a song name and get recommendations.

### `recommendation_system.ipynb`
This Jupyter Notebook contains the code to build and evaluate the music recommendation system. It uses cosine similarity to recommend songs based on the input song name.
