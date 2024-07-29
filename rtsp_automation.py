def generate_rtsp_file(base_rtsp_url, company_name, num_channels):
    # Extract the base part of the URL before the channel number
    base_url_part, channel_part = base_rtsp_url.rsplit('/', 1)
    base_channel = int(channel_part[-4:-2])
    
    # Content of the Python file
    file_content = "import cv2\n\n# Generated RTSP URLs for different channels\n"
    file_content += f'rtsp_url = "{base_rtsp_url}"\n'
    
    for i in range(1, num_channels + 1):
        new_channel = str(base_channel + i).zfill(2)
        new_rtsp_url = f"{base_url_part}/{channel_part[:-4]}{new_channel}01"
        file_content += f'rtsp_url = "{new_rtsp_url}"\n'
    
    # Append the video capture code
    video_capture_code = """
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
"""
    file_content += video_capture_code
    
    # Write the content to a new Python file
    file_name = f"{company_name}_rtsp_channels.py"
    with open(file_name, 'w') as file:
        file.write(file_content)
    print(f"Created {file_name}")

# Example usage
base_rtsp_url = "rtsp://user:password@ip:rtsp_port/Streaming/Channels/0101"
company_name = "sheepshead"
num_channels = 16

generate_rtsp_file(base_rtsp_url, company_name, num_channels)
