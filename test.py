# import logging
# import hercules.lib.util.hercules_logging as l
# from hercules.lib.util import sso as sso
import opencv2 as cv2
import urllib
import numpy as np

# log = l.setup_logging(__name__)

def main(args=None):
    # username, passowrd = sso.get_login_credentials("WATCHER")
    # Open a sample video available in sample-videos
    vcap = cv2.VideoCapture('https://www.sample-videos.com/video/mp4/720/big_buck_bunny_720p_2mb.mp4')
    #if not vcap.isOpened():
    #    print "File Cannot be Opened"

    while(True):
        # Capture frame-by-frame
        ret, frame = vcap.read()
        #print cap.isOpened(), ret
        if frame is not None:
            # Display the resulting frame
            cv2.imshow('frame',frame)
            # Press q to close the video windows before it ends if you want
            if cv2.waitKey(22) & 0xFF == ord('q'):
                break
        else:
            print("Frame is None")
            break

    # When everything done, release the capture
    vcap.release()
    cv2.destroyAllWindows()
    print("Video stop")



if __name__ == "__main__":
    main()
