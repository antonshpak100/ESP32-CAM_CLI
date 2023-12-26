# --- launch_stream.py --- #
# Launch the stream from the stream URL on the ESP32's web server in a new window.

# We use cv2 to read the video from the URL and display the stream.
import cv2


# launchStream: read the video from the URL and display the stream until the user presses S.
def launchStream(URL):

    video = cv2.VideoCapture(URL + ":81/stream")
    if video.isOpened() == False:
        print("Error reading video file")

    # Read frames until the user presses 'S' to stop the stream.
    while True:
        ret, frame = video.read()
        if ret == True:  # ret is true if the frame is read without errors
            cv2.imshow('Stream [Press S to end stream]', frame)

            # If user presses 'S', break the loop to end the stream.
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        else:
            break
    video.release()
    cv2.destroyAllWindows()
    # Release the video capture and close all frames.
