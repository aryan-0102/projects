from pytube import YouTube, exceptions

# Get the video URL from the user
vid_link = input('Enter video link: ')

try:
    # Create a YouTube object
    vid = YouTube(vid_link)

    # Print the video title
    video_title = vid.title
    print(f"Title: {video_title}")

    # Ask the user whether to show adaptive or non-adaptive streams
    adaptive = input("Do you want to show adaptive streams? (y/n) ").lower() == "y"

    # Get the available video streams
    streams = vid.streams.filter(adaptive=adaptive)

    # List the available resolutions
    print("Available resolutions:")
    for i, stream in enumerate(streams):
        print(f"{i + 1}. Resolution: {stream.resolution}, Type: {stream.mime_type}")

    # Ask the user to select a resolution
    while True:
        try:
            selection = int(input("Enter the number of the resolution you want to download: "))
            stream = streams[selection - 1]
            break
        except (IndexError, ValueError):
            print("Invalid selection. Please enter a valid number.")

    # Download the video
    stream.download()
    print("Download complete.")

except (exceptions.RegexMatchError, exceptions.VideoUnavailable) as e:
    print(f"Error: {str(e)}")
