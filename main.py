from get_token import get_access_token
from get_playlists import collect_playlists_data

# List of playlist IDs
playlist_ids = [
    '0XViN0HyZ55Uc1GTQPXuos','18CPDY5QPack31L80UTI3l', '2lfbdA64XkpEZjD98IYoAa', '6IijFAKuyjWO5PM1V0DBPD','78TBcuceC80a4tLHgZDDaj' , '1djhe9t67kwT0GPl7noZBr' ,'6423RwGfIBXVrNBfyh2hcz' 
]

# Obtain the access token
access_token = get_access_token()

# Collect data from the playlists and save it to a CSV file
combined_df = collect_playlists_data(playlist_ids, access_token, "playlist_data.csv")

# Display the combined DataFrame
print(combined_df)