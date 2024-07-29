import cv2

# Generated RTSP URLs for different channels
rtsp_url = "rtsp://user:password@ip:rtsp_port/Streaming/Channels/0101"
rtsp_url = "rtsp://user:password@ip:rtsp_port/Streaming/Channels/0201"
rtsp_url = "rtsp://user:password@ip:rtsp_port/Streaming/Channels/0301"
rtsp_url = "rtsp://user:password@ip:rtsp_port/Streaming/Channels/0401"
rtsp_url = "rtsp://user:password@ip:rtsp_port/Streaming/Channels/0501"
rtsp_url = "rtsp://user:password@ip:rtsp_port/Streaming/Channels/0601"
rtsp_url = "rtsp://user:password@ip:rtsp_port/Streaming/Channels/0701"
rtsp_url = "rtsp://user:password@ip:rtsp_port/Streaming/Channels/0801"
rtsp_url = "rtsp://user:password@ip:rtsp_port/Streaming/Channels/0901"
rtsp_url = "rtsp://user:password@ip:rtsp_port/Streaming/Channels/1001"
rtsp_url = "rtsp://user:password@ip:rtsp_port/Streaming/Channels/1101"
rtsp_url = "rtsp://user:password@ip:rtsp_port/Streaming/Channels/1201"
rtsp_url = "rtsp://user:password@ip:rtsp_port/Streaming/Channels/1301"
rtsp_url = "rtsp://user:password@ip:rtsp_port/Streaming/Channels/1401"
rtsp_url = "rtsp://user:password@ip:rtsp_port/Streaming/Channels/1501"
rtsp_url = "rtsp://user:password@ip:rtsp_port/Streaming/Channels/1601"

# Create a VideoCapture object
cap = cv2.VideoCapture(rtsp_url)
fps = cap.get(cv2.CAP_PROP_FPS)
counter = 0

# Check if the stream is opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream")
    exit()

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if frame is not None:
            print(frame.shape, fps)
        # If frame is read correctly, ret is True
        if not ret:
            print("Error: Can't receive frame (stream end?). Exiting ...")
            break

        cv2.imshow("show", frame)
        # Press 'q' on the keyboard to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    print("Stream stopped by user")

# When everything done, release the VideoCapture object
cap.release()
# Close all the frames
cv2.destroyAllWindows()
