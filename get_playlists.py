import pandas as pd
from spotify_data import get_trending_playlist_data

def collect_playlists_data(playlist_ids, access_token, output_csv="playlist_data.csv"):
    all_music_data = []
    
    for playlist_id in playlist_ids:
        print(f"Collecting data for playlist: {playlist_id}")
        playlist_data = get_trending_playlist_data(playlist_id, access_token)
        all_music_data.append(playlist_data)
    
    # Combine all data into a single DataFrame
    combined_df = pd.concat(all_music_data, ignore_index=True)
    
    # to a csv file
    combined_df.to_csv(output_csv, index=False)
    print(f"Data saved to {output_csv}")

    return combined_df

