# This database contains Matlab and Python program codes for the Final Year Project (FYP) on Sky/Cloud Analysis: Cloud Imaging with Day- and Night-time Images.

In the *Day Images* folder, the first step is to familiarize with image analysis by generating the histogram of (unnormalized) images. Secondly, normalization is carried out to obtain accurate results. Next, Otsu thresholding is implemented and the percentage error is calculated.

In the *Night Images* folder, the first step is to undistort the raw images that are taken with a fisheye lens. Secondly, SLIC segmentation is carried out to generate the ground truth images. Next, Otsu thresholding is implemented and the percentage error is calculated.

The color spaces and ratios involved are C1:R, C2:G, C3:B, C4:H, C5:S, C6:V, C7:Y, C8:I, C9:Q, C10:L, C11:a, C12:b, C13:R/B, C14:R/G, C15:G/B, C16:R-B, C17:(B-R)/(B+R), C18:C.
