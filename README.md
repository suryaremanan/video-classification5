# video-classification

## Dataset Collection

data_collection.py will search for videos and add their video IDs to the videos list until it reaches the desired number of results (in this case, 1000). You can then generate the URLs for each video using the following format: https://www.youtube.com/watch?v=VIDEO_ID.

## Usage

The model is deployed using streamlit. You can install it in your local system using : 
``` pip install streamlit ```

then type 

``` python deployment.py ```

NOTE: the model is only 53% accurate so the videos may get misclassified majority of the time.

## Key Takeaways

- Due to tha large number of videos in the dataset, my local system kept crashing
- I only used 5 epochs while training which should have been 50 instead
- hence the low accuracy
- the frames per video should have been less which i realized later
- even preprocessing of the frames kept crashing my system
- the whole process of iteration took many times with not much fruitful results
- even google colab kept crashing due to the huge number of frames

## Conclusion

The overall project was a great learning experience for me. I made a lot of mistakes in the beginning which I know now I should have avoided. I hope that in future, I'll prepare my mind for a better model training experience.
