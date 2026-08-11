songs = [
    "Song A",
    "Song B",
    "Song C",
    "Song D",
    "Song E",
    "Song F",
    "Song G",
    "Song H"
]
c=songs[::]
f=songs[:3]
l=songs[len(songs)-3:]
s=songs[2:6]
al=songs[::2]
r=songs[::-1]
fl=songs[1:len(songs)-1]
print(f"Complete Playlist: {c}")
print(f"First 3 Songs: {f}")
print(f"Last 3 Songs: {l}")
print(f"Songs from  3 to 6: {s}")
print(f"Alternative Songs: {al}")
print(f"Reversed Songs: {r}")
print(f"Songs without first and last song : {fl}")