# Robot-Perception
This repository is intended to use matrix and python to make computers to know how the world is like. 
By using provided lidar file and matrix, we can rearrange the points and finally project those points to make them in 3D.
Here is a simple flow that illustate of how a set of data can be turned into 3D graph in computer's vision.

Below the text shows how the recoding machine is like and from the graph we can see the camera and laser scanner are in distinct places.
![Example file](https://user-images.githubusercontent.com/79177828/184293239-f3266f0c-6ec1-4953-b39c-68e8135b6f43.png)
Since they are in different places we cannot use the data together without handling them, as a result we need the help of matrix and python.
We need to turn one of data into other coordinate frame so that we can form the diagram, otherwise it might show wrongly, so we need both rotation matrix and translation matrix to adjust its position. Camera intrinsic matrix is also needed in turning points recoreded by camera.
As soon as we adjust those points, we can use open3d to show the model that we make:

<img width="401" alt="PointCloud_Diagram" src="https://user-images.githubusercontent.com/79177828/178813104-d93f41b5-c4e9-43e2-acd4-20cd8cd54e5c.png">
