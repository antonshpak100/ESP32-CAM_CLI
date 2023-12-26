# --- save_video --- #
# Records video from the stream URL on the webserver to the specified output folder and filename, correcting FPS.

# We use cv2 to read and write the video from the specified URL.
# We use time to record the true length of the video to correct the framerate.
# We use tempfile to create a temporary video file to which we record the stream with a placeholder framerate, from
# which we read the video to adjust the framerate.
import cv2
import time
import tempfile


# saveVideo: records video from the stream URL on the webserver to the specified output folder and filename,
# and corrects FPS.
def saveVideo(URL, outputFolder, filename):

    # If no filename is specified, use default 'output_file.avi'.
    if filename is None:
        filename = "output_file"

    # Read the video from the webserver stream URL.
    video = cv2.VideoCapture(URL+":81/stream")

    # Check if camera is opened previously
    if video.isOpened() == False:
        print("Error reading video file")

    # Check resolution and set resolution of video to match stream.
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))
    size = (frame_width, frame_height)

    # Create a temporary file to store the recorded video with a placeholder framerate.
    with tempfile.NamedTemporaryFile() as tmp:
        tmpName = tmp.name+".avi"
        result = cv2.VideoWriter(tmpName, cv2.VideoWriter_fourcc(*'MJPG'), 10, size)
        # 10 FPS is not the true framerate, we correct this later.

        # Initialize start time and count frames so we card record the true average framerate
        startTime = time.time()
        nFrames = 0

        # Read frames until the user presses 'S' to stop the recording.
        while True:
            ret, frame = video.read()
            nFrames += 1  # iterate frame count
            if ret is True:  # ret is true if the frame is read without errors
                # Write the frame into the temporary file.
                result.write(frame)

                # Display the frames recorded in a new window.
                cv2.imshow('Video  [Press S to stop recording]', frame)

                # If user presses 'S', break the loop to stop the recording.
                if cv2.waitKey(1) & 0xFF == ord('s'):
                    break
            else:
                break

            # Release the video capture and file, calculate the true average framerate, close all the frames.
        video.release()
        result.release()
        totalTime = time.time()-startTime
        frameRate = nFrames/totalTime
        cv2.destroyAllWindows()

        # The FPS of the recorded video is not accurate to real time. To correct this, we find the number of frames and
        # divide by the time elapsed. Then, we read the original video and rewrite it in the "true" FPS.

        # Through the same process as above, we read the video from the temporary file.
        video = cv2.VideoCapture(tmpName)
        if video.isOpened() == False:
            print("Error reading video file")

        # Writing the video again, this time with the corrected true average framerate.
        # Writing the video to the specified output folder and filename.
        result = cv2.VideoWriter(outputFolder+"/"+filename+".avi", cv2.VideoWriter_fourcc(*'MJPG'), frameRate, size)
        while True:
            ret, frame = video.read()
            if ret == True:
                result.write(frame)
            else:
                break  # Break loop when there are no frames left to read (ret returns False).
    video.release()
    result.release()
    cv2.destroyAllWindows()
    # Release the video capture and file, calculate the true average framerate, close all the frames.
