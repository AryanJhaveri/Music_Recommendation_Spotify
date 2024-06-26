from get_token import get_access_token
from get_playlists import collect_playlists_data

# List of playlist IDs
playlist_ids = [
    '2U5naKBJ5DN3oOPbuRiTem'
]
#'7sTkp2X5Aq84v9w9UtfkaF','1Ax6quImLr6Ek6bpLO8qK4',
# Obtain the access token
access_token = get_access_token()

# Collect data from the playlists and save it to a CSV file
combined_df = collect_playlists_data(playlist_ids, access_token, "playlist_data1.csv")

# Display the combined DataFrame
print(combined_df)    