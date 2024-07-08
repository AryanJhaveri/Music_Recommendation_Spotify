# This Is A Bollywood Song Recommendation System

# Spotify Playlist Data Collector and Recommendation System

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
- [License](#license)

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
