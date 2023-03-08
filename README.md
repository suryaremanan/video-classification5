# video-classification

## Dataset Collection

data_collection.py will search for music videos and add their video IDs to the videos list until it reaches the desired number of results (in this case, 1000). You can then generate the URLs for each video using the following format: https://www.youtube.com/watch?v=VIDEO_ID.

## Deployment of the model

The model is deployed using streamlit. You can install it in your local system using : 
``` pip install streamlit ```

then type 

``` python deployment.py ```

NOTE: the model is only 53% accurate so the videos may get misclassified majority of the time.

## Key Takeaways

- 
